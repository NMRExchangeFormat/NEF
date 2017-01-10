CASD-NMR 2013 test data
=======================

Target (download)	PDB ID 	PDB release date BMRB ID
HR2876C	2M5O 	26/04/2013 19068
HR8254A 2M2E 	12/02/2013 18909
YR313A 	2LTL 	24/07/2012 18487
HR2876B 2LTM 	24/07/2012 18489
StT322 	2LOJ 	20/03/2012 18214
OR135 	2LN3 	09/02/2012 18145
OR36 	2LCI 	24/06/2011 17613
HR5460A 2LAH 	09/05/2011 17524
HR6430A	2LA6 	29/04/2011 17508
HR6470A 2L9R 	19/04/2011 17484  1)

CASD test data can be downloaded from https://www.wenmr.eu/wenmr/casd-nmr-data-sets

BMRB entries can be downloaded from http://www.bmrb.wisc.edu/search/

DOCR projects can be downloaded from http://restraintsgrid.bmrb.wisc.edu/NRG/MRGridServlet

1) This project contains two identical dihedral_restraint_lists. Since the DOCR
entry contains the same error, I have left the files unchanged (and consistent with
the starting point).

NB The files in this directory are simple upgrades of the corresponding files in
data_0_2/CCPN_CASD
They retain any imperfections that may have been present in the preceding files.


NEF file generation:
====================

- Restraint data and sequence were taken from the corresponding DOCR CCPN project.
RDC restraints were then deleted and replaced with RDC restraints read from the
CASD test projects, using a custom script.
The RDC restraints should in principle be the same, but this procedure allows loading 
the RDC tensor values present in the CASD data without introducing an error-prone 
manual editing step.

- Chemical shifts were read from the corresponding BioMagResBank entry file,
using the CCPN STAR format reader and custom scripts.
The names of ambiguous atoms (ambiguity codes 2 and 3) and methyl groups were
converted to the NEF naming system as detailed below.

- Restraints were converted to use the new NEF names by a simple mapping from old to 
new names.

- Spectrum descriptions were loaded by importing the spectra in the CASD
test project (compounds 2loj and 2m2e) or by parsing NMRPIPE input scripts
from the CASD test project using a custom script (all other projects).
Experiment types (NOESY-HSQC) were set manually.

- Unassigned peak lists were read from cyana format peak lists from the
CASD test projects, using custom scripts.


DETAILS
=======

- Triplets of atoms that differ only on the final number suffix (xyz1, xyz2, xyz3)
were mapped to a single atom with the name xyz%.

- Pairs of ambiguous atoms with branch indicators 1 and 2 (e.g. isopropyl methyls,
TYR and PHE aromatic protons, side chain amides) were mapped to branch indicators 
'X' and 'Y' respectively. 
Pairs of ambiguous atoms with branch indicators 2 and 3 (geminal protons) were mapped to
branch indicators 'X' and 'Y' respectively. 
If only one of the pair of ambiguous atoms was present in the list, it was mapped to 'X'
(NB this means that the files in theory cannot be losslessly remapped to the original IUPAC
atom names. But these are correct examples of the kind of input files you would get - where 
the IUPAC mapping is generally not available).

As it happens, 2ME2 and 2LOJ were the only cases that had non-proton atoms with ambiguity
codes different from 1.
In cases where LEU and VAL methyl protons were given as ambiguous, but the equivalent
carbons were given as stereospecific, BOTH protons and carbons were treated as
ambiguous. Strictly speakling this is a modification of the data, but it seems highly 
unlikely that the VAL and LEU methyl carbons should have been stereospecifically 
assigned while the directly bound protons were not.

For these cases (and also PHE and TYR aromatic protons), protons and
carbons with the same branch indication (HD2 and CD2, HG1% and CG1, etc.) were treated 
as belonging to the same branch, so that HD2 and CD2 both mapped to 'Y', HG1% and CG1 
both mapped to 'X' etc.

- The DOCR CCPN projects contained a number of restraints to ambiguous NMR atoms
(the pre-NEF equivalent of atoms with names like HBX). These had been generated
from restraints to wildcard atroms (like 'HB*'), and were converted back to
'HB%', removing duplicate restraint contributions.