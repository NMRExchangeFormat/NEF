# ARIA results for reading/writing NEF/mmCIF round 2

Input files were taken from the **NEF/data_1_1/PDBStats_it2/** directory

- coordinates were water-refined using cif files as initial coordinates and NEF files as restraints

- Refined coordinates are written back as cif by ARIA (\*\_ARIA\_it2.cif)

- Molecule, Shifts and Restraints (as used by ARIA) are exported back to NEF (\*\_ARIA\_it2.nef)

The corresponding restraints in CNS tbl format are also given (\*\_ARIA\_distances.tbl,  \*\_ARIA\_dihedrals.tbl, \*\_ARIA\_rdcs.tbl)

NB: 
- For the 3 entries (2kw5, 2kzn, 2loy) that had RDCs restraints, tensor parameters (magnitude and rhombicity) were first estimated by best-fitting of RDCs to the source coordinates.
- atoms missing in the source CIF file (with regards to NEF molecule definition) were added on the fly during refinement.
