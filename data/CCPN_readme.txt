CCPN test data
==============

CCPN_H1GI_clean.nef and CCPN_Sec5Part3.nef 
------------------------------------------

are both CCPN 'working projects'. They are the export of a complete project as it would accumulate
(minus any CCPN-specific tags), rather than the smaller and more targeted files you would
produce for transfer to a specific program or depositions system. Not all the content will be
relevant for all other programs, but this is the kind of files you may encounter.

CCPN_H1GI_clean.nef is a mature project with assignnments, assigned peaks, restraints, 
peak-restraint links, and the results of violation analysis.

CCPN_Sec5Part3.nef is an early project with the kind of assignments you would expect while
still assigning the spectrum.

For an example that exercises all the tags in the formats, use 
specification/Commented_Example.nef



CCPN_2mqq_docr.nef
------------------

is a protein bound to two non-symmetrical RNA chains.

PDB: 2mqq; BMRB: 25043.

Sequence and restraints were taken from DOCR, chemical
shifts were imported from the corresponding BMRB entry,
and NEF names were set and restraints matched to NEF names
using custom scripts.

The NEF file containss one anonymous atom ('?@1385'), which was present in the DOCR project,
possibly due to a typo or mapping problem.



CCPN_2mtv_docr.nef
------------------

is a protein bound to an RNA chain containing a modified
nucleotide (6MZ).

PDB: 2mtv; BMRB: 25188

Sequence and dihedral restraints were read from DOCR, and chemical
shifts were imported from the corresponding BMRB entry,
and NEF names were set and restraints matched to NEF names
using custom scripts.

Distance restraints were read and adapted from the original deposition (taken from NRG),
using custom scripts, as the original DOCR had had problems converting some restraint atom names.



CCPN_1nk2_docr.nef
------------------

is a protein bound to a DNA duplex.
It includes examples of BMRB ambiguity codes 4, 5, and 9.

PDB: 1nk2; BMRB: 4141

Sequence and dihedral restraints were read from DOCR, and chemical
shifts were imported from the corresponding BMRB entry,
and NEF names were set and restraints matched to NEF names
using custom scripts.

Distance restraints were read and adapted from the original deposition (taken from NRG),
using custom scripts, as the original DOCR had had problems converting some restraint atom names.

The treatment of BMRB ambiguity codes does NOT pretend to be part of the standard.
But ambiguity codes 4, 5, 6, and 9 have to be reflected somehow, since ignoring them
falsely give the impression that the assignments are non-ambiguous. The names given will be treated
as 'assignment anonymous' within the standard.
The procedure to generate them was:
- for intra-residue ambiguities the possible atom names were combined, separated by '|',
  the first atom in the combination being the original atom name.
- For ambiguous-residue and ambiguous-chain, the residue (resp chain) identifier had a '?' appended.
- FOr code 9 ('other') all parts of the atom identifier had a '?' appended.



CCPN_2kko_docr.nef
------------------

is a protein symmetric dimer from teh Montelione NMF/Xray data set.
The file includes unassigned peak lists.

PDB: 2kko; BMRB: 16368

Sequence and restraints were taken from DOCR, chemical
shifts were imported from the corresponding BMRB entry,
and NEF names were set and restraints matched to NEF names
using custom scripts. The chain B chemical shifts weere duplicatged form those of thain A.
