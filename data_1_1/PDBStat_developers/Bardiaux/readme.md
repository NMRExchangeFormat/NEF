# ARIA results for reading/writing NEF/mmCIF

Input files were taken from the **NEF/data_1_1/PDBStats_NEW/** directory

- coordinates were water refined using cif files as initial coordinates and NEF files as restraints

- Refined coordinates are written back as cif by ARIA (\*\_ARIA\_it1.cif)

- Molecule, Shifts and Restraints (as used by ARIA) are exported back to NEF (\*\_ARIA\_it1.nef)

The corresponding restraints in CNS tbl format are also given (\*\_ARIA\_distances.tbl and \*\_ARIA\_distances.tbl)

NB: the following entries couldn't be processed correclty without manual intervention so we skipped them.

- 2kzn: OXT atoms missing in cif coordinates 
- 2loy: OXT atoms missing in cif coordinates 
- 2luz: MET1 has no H% atoms and HIS114 should have variant -HD1
- 6nbn: CYS should have variant -HG and MET1 has linking "end" (where it should be "start")


 
