Generation of output NEF files from the input NEF files was done with the following script (named nef2nef.py).

    import sys
    from org.nmrfx.structure.chemistry.io import NMRNEFReader
    from org.nmrfx.structure.chemistry.io import NMRNEFWriter

    inFileName = sys.argv[1]
    outFileName = sys.argv[2]

    NMRNEFReader.read(inFileName);
    NMRNEFWriter.writeAll(outFileName);

And that was executed,using **1pqx** as an example,  as follows

    nmrfxs nef2nef.py 1pqx.nef 1pqx_NMRFX.nef

The NMRNEFREader parses the NEF file and generates internal objects  (molecules, shifts, restraints etc.). The NMRNEFWriter then generates an output representation as a NEF file.  So this conversion is not a simple copy of the NEF file to  a new file.

Structures were calculated with the following command.

    nmrfxs batch -n 100 -k 5 -p 10 -a -c project.yaml

The arguments to that command specify that 100 structures should be calculated, the best 5 should be kept, 10 jobs should be run simultaneously, the resulting structures should be superimposed, and the output directories cleaned first.

The *project.yaml* file used is like the following.

    nef : input/1pqx.nef

    anneal :
        dynOptions :
            steps : 15000
            highTemp : 5000.0
        param :
            swap : 20
        force :
            irp : 0.05

Single structures can be generated with

    nmrfxs gen -s 1 project.yaml

Or if all defaults are used one can simply specify the NEF file.:

    nmrfxs gen -s 1 1pqx.nef

The **-s** argument specifies a seed.  Different numbers will generate different structures.

Other than changing the nef file name in the *project.yaml* file, no customization of parameters (steps, temperatures, force weights etc.) were done for any of the structures. They were all calculated with the exact same parameters.  Structures of "higher quality" might be obtained with structure specific optimization of the parameters.

The superimposed structures are exported into an mmCIF file (like *1pqx_nmrfx.cif* )

The NEF file **6nbn** contains a ligand not specified within the NEF file.  To generate structures (or do the nef2nef conversion) a .cif file containing the ligand (ACD.cif) should be in the same directory as the NEF file.
