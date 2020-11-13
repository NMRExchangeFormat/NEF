Directory for wwPDB NMR Restraint Validation Project data.

Notes,  09 Nov 2020:

1. This is a partial dump of NEF results from Amber.  More are coming.

2. Amber doesn't modify input restraints, and doesn't write restraint
      files (in any format).  Hence the requests to output .nef files
      were ignored.

3. In place of a full attempt at structure determination, what is
      reported here is just energy minimization (with restraints) from the
      input structures provided.  This offers a partial deonstration
      that the input restraints are being read correctly.

4. The 6nbn restraint list has a number of entries that don't match
      the Amber ambiguity model.  I hand-edit the nef file, and the
      one I actually used is here.  Diffing that with the original
      will show the changes that were made: removing duplicates, and
      assuming that ambiguities arise from chemical shift degeneracy.
      (In Amber, ambiguous restraints are *not* just implemented as OR.)
