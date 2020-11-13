(opts,args) = xplor.parseArguments(["quick",
                                    "nef:1",
                                    "cif:1"]) # check for command-line typos

quick=False
nefFile=None
cifFile=None
for opt in opts:
    if opt[0]=="quick":  #specify -quick to just test that the script runs
        quick=True
        pass
    if opt[0]=="nef":  #specify -quick to just test that the script runs
        nefFile=opt[1]
        pass
    if opt[0]=="cif":  #specify -quick to just test that the script runs
        cifFile=opt[1]
        pass
    pass

from os.path import splitext
id=splitext(nefFile)[0]

# protocol module has many high-level helper functions.
#
import protocol
protocol.initRandomSeed(3421)   #explicitly set random seed


protocol.initParams("protein")
from glob import glob
for topFile in glob('*.top'):
    protocol.initTopology(topFile)
    pass
for parFile in glob('*.par'):
    protocol.initParams(parFile)
    pass
import psfGen
psfGen.addResidueName("ACD","metal")

# generate PSF data from sequence and initialize the correct parameters.
#
#from psfGen import seqToPSF
#seqToPSF('protG.seq')
#protocol.initStruct("g_new.psf") # - or from file


# or read an existing model
#
from nefTools import readNEF
nefData = readNEF(nefFile)

from iupacNaming import toIUPAC, fromIUPAC
toIUPAC()
protocol.initCoords(cifFile)

protocol.addUnknownAtoms()

protocol.fixupCovalentGeom(maxIters=100,useVDW=1)

from selectTools import getSegsResidues
segsResidues=getSegsResidues()
isDimer=False
if len(segsResidues)==2:
    idNames= list(segsResidues.values())
    if idNames[0]==idNames[1]:
        isDimer=True
        print("found a homo dimer")
        pass
    pass

#
# a PotList contains a list of potential terms. This is used to specify which
# terms are active during refinement.
#
from potList import PotList
potList = PotList()

# parameters to ramp up during the simulated annealing protocol
#
from simulationTools import MultRamp, StaticRamp, InitialParams

rampedParams=[]
highTempParams=[]

# compare atomic Cartesian rmsd with a reference structure
#  backbone and heavy atom RMSDs will be printed in the output
#  structure files
#
from posDiffPotTools import create_PosDiffPot
refRMSD = create_PosDiffPot("refRMSD","name CA C N O",
                            selection2="initial")



from noePotTools import create_NOEPot, readNEF
noe=create_NOEPot("noe",nef=nefData)
noe.setAllowOverlap(False)
noe.setShowAllRestraints(True)
potList.append(noe)
rampedParams.append( MultRamp(2,30, "noe.setScale( VALUE )") )

import nefTools
from potList import PotList
rdcs = PotList('rdcs')
try:
    rdcNames=nefTools.getBlockNames(nefData,'rdc')
except:
    rdcNames=[]
    pass
        
tensors=[]
for name in rdcNames:
    print(f"reading RDC block {name}")
    block = nefTools.getBlock(nefData,'rdc',name)
    from rdcPotTools import readNEF
    tensors.append( readNEF(rdcs,block) )
    pass
if len(rdcs): potList.append(rdcs)
rampedParams.append( MultRamp(0.05,5.0, "rdcs.setScale( VALUE )") )
# calc. initial tensor orientation
# and setup tensor calculation during simulated annealing
#
from varTensorTools import calcTensorOrientation, calcTensor
for i,tensor in enumerate(tensors):
    calcTensor(tensor)
    rampedParams.append( StaticRamp(f"calcTensor(tensors[{i}])") )
    pass

#for all calculations, allow the full alignment tensor to float
for m in tensors:
#    m.setFreedom("fixDa, fixRh")        #fix tensor Rh, Da, vary orientation
    m.setFreedom("varyDa, varyRh")      #vary tensor Rh, Da, vary orientation


from xplorPot import XplorPot
from torsionPotTools import Xplor_readNEF
try:
    Xplor_readNEF(nefData)
except Exception as e:
    if not e.args[0].startswith('getBlock: could find no saveset'):
        print("Warning: no dihedral table read")
        raise
    pass

pot=XplorPot('CDIH')
pot.setThreshold(5)
potList.append( XplorPot('CDIH') )
highTempParams.append( StaticRamp("potList['CDIH'].setScale(10)") )
rampedParams.append( StaticRamp("potList['CDIH'].setScale(200)") )

if isDimer:
    # this assumes the two subunits have segids A and B:

    from distSymmTools import create_DistSymmPot, genDimerRestraints
    from selectTools import minResid, maxResid

    minResid=minResid("segid A")
    maxResid=maxResid("segid A")

    dSymm = create_DistSymmPot('dSymm',
                               genDimerRestraints(segids=['A','B'],
                                                  resids=range(minResid,
                                                               maxResid,5)))
    potList.append(dSymm)
    

    # ``NCS'' term - keep dimer subunits identical
    from posDiffPotTools import create_PosDiffPot
    ncs = create_PosDiffPot("ncs","segid A","segid B")
    ncs.setScale(10)
    potList.append(ncs)
    
    pass

fromIUPAC()



# gyration volume term 
#
# gyration volume term 
#
#from gyrPotTools import create_GyrPot
#gyr = create_GyrPot("Vgyr",
#                    "resid 1:56") # selection should exclude disordered tails
#potList.append(gyr)
#rampedParams.append( MultRamp(.002,1,"gyr.setScale(VALUE)") )

# HBPot - knowledge-based hydrogen bond term
#
from hbPotTools import create_HBPot
hb = create_HBPot('hb')
hb.setScale(2.5)
potList.append( hb )

#New torsion angle database potential
#
from torsionDBPotTools import create_TorsionDBPot
torsionDB = create_TorsionDBPot('torsionDB', system='protein')
potList.append( torsionDB )
rampedParams.append( MultRamp(.002,2,"torsionDB.setScale(VALUE)") )

#
# setup parameters for atom-atom repulsive term. (van der Waals-like term)
#
from repelPotTools import create_RepelPot,initRepel
repel = create_RepelPot('repel')
potList.append(repel)
rampedParams.append( StaticRamp("initRepel(repel,use14=False)") )
rampedParams.append( MultRamp(.004,4,  "repel.setScale( VALUE)") )
# nonbonded interaction only between CA atoms
highTempParams.append( StaticRamp("""initRepel(repel,
                                               use14=True,
                                               scale=0.004,
                                               repel=1.2,
                                               moveTol=45,
                                               interactingAtoms='name CA'
                                               )""") )

# Selected 1-4 interactions.
import torsionDBPotTools
repel14 = torsionDBPotTools.create_Terminal14Pot('repel14')
repel14.addSelectionPair( "resname ACD","resid ACD" )
potList.append(repel14)
highTempParams.append(StaticRamp("repel14.setScale(0)"))
rampedParams.append(MultRamp(0.004, 4, "repel14.setScale(VALUE)"))


potList.append( XplorPot("BOND") )
potList.append( XplorPot("ANGL") )
potList['ANGL'].setThreshold( 5 )
rampedParams.append( MultRamp(0.4,1,"potList['ANGL'].setScale(VALUE)") )
potList.append( XplorPot("IMPR") )
potList['IMPR'].setThreshold( 5 )
rampedParams.append( MultRamp(0.1,1,"potList['IMPR'].setScale(VALUE)") )
      


# Give atoms uniform weights, except for the anisotropy axis
#
protocol.massSetup()


# IVM setup
#   the IVM is used for performing dynamics and minimization in torsion-angle
#   space, and in Cartesian space.
#
from ivm import IVM
dyn = IVM()

# reset ivm topology for torsion-angle dynamics
#
dyn.reset()

protocol.torsionTopology(dyn)

# minc used for final cartesian minimization
#
minc = IVM()
protocol.initMinimize(minc)

protocol.cartesianTopology(minc)



# object which performs simulated annealing
#
from simulationTools import AnnealIVM
init_t  = 3000.     # Need high temp and slow annealing to converge
cool = AnnealIVM(initTemp =init_t,
                 finalTemp=25,
                 tempStep =12.5,
                 ivm=dyn,
                 rampedParams = rampedParams)

def accept(potList):
    """
    return True if current structure meets acceptance criteria
    """
    if potList['noe'].violations()>0:
        return False
    if potList['CDIH'].violations()>0:
        return False
    if potList['BOND'].violations()>0:
        return False
    if potList['ANGL'].violations()>0:
        return False
    if potList['IMPR'].violations()>1:
        return False
    
    return True

def calcOneStructure(loopInfo):
    """ this function calculates a single structure, performs analysis on the
    structure, and then writes out a pdb file, with remarks.
    """

    # initialize parameters for high temp dynamics.
    InitialParams( rampedParams )
    # high-temp dynamics setup - only need to specify parameters which
    #   differfrom initial values in rampedParams
    InitialParams( highTempParams )

    # high temp dynamics
    #
    protocol.initDynamics(dyn,
                          potList=potList, # potential terms to use
                          bathTemp=init_t,
                          initVelocities=1,
                          finalTime=10,    # stops at 10ps or 5000 steps
                          numSteps=5000,   # whichever comes first
                          printInterval=100)

    dyn.setETolerance( init_t/100 )  #used to det. stepsize. default: t/1000 
    dyn.run()

    # initialize parameters for cooling loop
    InitialParams( rampedParams )


    # initialize integrator for simulated annealing
    #
    protocol.initDynamics(dyn,
                          potList=potList,
                          numSteps=100,       #at each temp: 100 steps or
                          finalTime=.2 ,       # .2ps, whichever is less
                          printInterval=100)

    # perform simulated annealing
    #
    cool.run()
              
              
    # final torsion angle minimization
    #
    protocol.initMinimize(dyn,
                          printInterval=50)
    dyn.run()

    # final all- atom minimization
    #
    protocol.initMinimize(minc,
                          potList=potList,
                          dEPred=10)
    minc.run()

    #do analysis and write structure when this function returns
    toIUPAC()
    from simulationTools import analyze
    protocol.writeCIF( loopInfo.filename()+".cif",
                       remarks=analyze(potList))
    fromIUPAC()
    
    pass



from simulationTools import StructureLoop, FinalParams
StructureLoop(numStructures=100,
              structLoopAction=calcOneStructure,
              pdbTemplate="SCRIPT_STRUCTURE.sa",
#              calcMissingStructs=True, #calculate only missing structures
              doWriteStructures=True,  #analyze and write coords after calc
              genViolationStats=True,
              averagePotList=potList,
              averageCrossTerms=refRMSD,
              averageTopFraction=0.2, #report only on best 20% of structs
#              averageAccept=accept,   #only use structures which pass accept()
              averageContext=FinalParams(rampedParams),
              averageFilename="SCRIPT_ave.pdb",    #generate regularized ave structure
              averageFitSel="ordered and name CA",
              averageCompSel="not resname ANI and not name H*"     ).run()

