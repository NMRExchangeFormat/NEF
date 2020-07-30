# Comments from the first round of wwPDB NEF initiative.

1. Validation of the NMR restraints involving non-degenerate, but non-stereospecifically assigned atoms. 

2. Conversion of the existing available data, chemical shifts and restraints into NEF files.
This formating involved, not only, converting a number of files into a single file, but also uses information stored in ambiguity codes to represent the data in a form as close to the original data as possible. Importantly, this was a process which effectively worked in ‘reverse’ order, generating NEF files from existing files in other formats. The aim of the NEF format, of course, is to have these generated as primary source by the various programmes.

3. Expanding mmCIF dictionary to include NEF atom names. 
This allows NEF atoms (which can be identified with x/y nomenclature) to be mapped onto the atoms in a mmCIF coordinate file on a per model basis. It is essential for solving the NMR non-stereospecific assignment problem.

4. Use of residue variants 
Additional or missing atoms for each residue can be indicated with the use of a simple label in non-mandatory _nef_sequence.residue_variant tag. We are in the process of converting the current Residue_Variants.txt and mmCIF_NEF_variant_mapping.txt, that are part of NEF specifications, into computer readable forms. 

5. Addition of tag in restraints saveframe indicating whether a particular restraint list has been used in calculations. This change would enable the preservation of the data that has not been used in biomolecular structure calculations, such as restraints (and associated peaks) which were deemed problematic by the calculation program, or restraints that were predicted. This would involve consultation with the wider NEF Working Group. 
(INITIAL SUGGESTION: _nef_distance_restraint_list.calculation_use  True/False)

6. Possible extension of current NEF format to include non-mandatory saveframes carrying ligand topology information. This would also require consultation with biomolecular structure calculation software developers to ensure their needs are met.



# Observation from the first (read in - write out) round of deposited NEF files.

1. Mandatory tags.
A valid NEF file suitable for OneDep system must contain 'nef_nmr_meta_data', 'nef_molecular_system' and 'nef_chemical_shift_list' saveframes. Each NEF saveframe has a number of mandatory tags (listed in Commented_Example.nef and mmcif_nef.dic). The NEF file  must also list all mandatory tags from present saveframes. For instance, _nef_distance_restraint is a non mandatory saveframe, however if it is listed in a NEF file then it must contain all the mandatory tags for this saveframe.

2. Non-mandatory tags.
Although it would be desirable if all tags read into a program were also, either processed by the software or left unchanged, outputted in the new NEF file, it is not essential to list non- mandatory tags. 
As an example the optional tag '_nef_distance_restraint.restraint_origin' can currently be dropped from a generated NEF file. However, the current round indicates the need for a future discussion on some elements of the NEF standard, to enhance, clarify and remedy some issues. 

3. Tag names.
It is critical that all NEF tags have the correct names when a new NEF file is outputted in order for other software to use the information correctly.

4. Addition of new data.
As NEF is an extendable format it offers the possibility to add new data. For instance a score, or comment for each _nef_distance_restraint can be added to pre-existing save_nef_distance_restraint_list saveframe as: 

    _nef_distance_restraint.nmrProgram_comment

    to "_nef_distance_restraint" loop. If the program generates a new set of restraints a new saveframe (for example: save_nef_distance_restraint_list_nmrProgram_new1) can be added to the NEF file. Software should not a use previous saveframe name as this is used as a persistent identifier. 


