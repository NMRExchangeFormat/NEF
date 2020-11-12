Directory for wwPDB NMR Restraint Validation Project data.

Prof A. Liwo group - Faculty of Chemistry, University of Gdańsk
UNRES package
submiter - E.A. Lubecka - Faculty of Electronics, Telecommunications and Informatics,
Gdańsk University of Technology

The *_UNRES.pdb and *_UNRES.cif files contain the best structure obtained with the UNRES force filed for protein.
The *_UNRES.nef - is a file with restraints write back out in NEF format with “zero cycles” of structure calculations.
The *_UNRESused.nef - is a file with restraints used to structures calcultions.

Methods:
The structure was predicted using our ab-initio hierarchical approach described in ref. 1, in which an extensive conformational search is carried out in a united-residue approximation by means of multiplexing replica exchage molecular dynamics (MREMD), followed by selection of the most probable clusters of geometrically similar conformations and the conversion of the alpha-carbon trace of the most probable structure of each cluster to a full-atom chain by using the PULCHRA [2] and SCWRL [3] algorithms. The new version of UNRES force field with torsional and correlation potentials derived rigorously in our recent work [4], which depend on both virtual-bond and virtual-bond-dihedral angles (consistent with the statistics derived from the PDB), which was calibrated by using the new maximum-likelihood optimization procedure developed in our laboratory [4] was used.
The last column of each ATOM record contains the average deviation of the respective backbone or sidechhain atoms of the conformations of the cluster of which the model is a representative conformation; this is an estimate of the accuracy of the predition of the poosition of this atom.
NMR data provided with the target were used. The phi and psi angles were converted to backbone virtual-bond-dihedral angles and the interproton distance were estimated based on the Calpha and sidechain-center positions, by using our recently developed procedure (E.A. Lubecka, A. Liwo, in preparation).
The last column of each ATOM record contains the average deviation of the respective backbone or sidechhain atoms of the conformations of the cluster of which the model is a representative conformation; this is an estimate of the accuracy of the predition of the poosition of this atom.
1. P. Krupa et al., Bioinformatics, 2016, 32, 3270-3278.
2. P. Rotkiewicz and J. Skolnick. J. Comput. Chem., 2008, 29, 1460-1465.
3. Q. Wang et al., Nat Protoc. 2008, 3, 1832-1847.
4. A.K. Sieradzan et al., Chem. Phys., 2017, 146, 124106.
5. P. Krupa et al., J. Chem. Inf. Model. 2017, 57, 2364-2377.

