##wwPDB NMR restraints validation reports
####Author : Kumaran Baskaran, BMRB
This folder contains preliminary version of validation reports for the restraints deposited in NMR-STAR/NEF format. 
NMR-STAR is the archival format for NMR data at wwPDB. All deposited NMR data will be converted into NMR-STAR 
format and validated against the coordinate data in CIF format. 

The NMR Restraints validation software package is being developed and integrated into wwPDB's OneDep pipeline by BMRB.

###File description in each folder
pdb_id.nef : NEF file from PDBStats_NEW folder
pdb_id.cif : CIF file from PDBStats_NEW folder
pdb_id.str : NMR-STAR file translated from NEF
pdb_id.pdf : wwPDB's validation report in PDF format(long: lists all violations)
pdb_id_summary.pdf : wwPDB's validation report in PDF format(short: lists only top 10)
pdb_id.xml : wwPDB's validation report in XML format

