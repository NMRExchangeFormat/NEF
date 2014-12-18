Open questions and proposals
=============================

* Restraint potential types
* Limits on constraint limit values
* Indirect magnetisation transfer
* Linkers and tensor-origin residues
* RDC restraints
* Residue variant codes
* Restraint-peak links
* Changes needed from the RCSB


### Restraint potential types
The current draft supports the potential types
* 'log-harmonic'
  ```
  Parameters: target_value
  ```
* 'parabolic'
  ```
  Parameters: target_value

  Formula: E = k(r-target_value)**2
  ```
* 'square-well-parabolic'
  ```
  Parameters: upper_limit, lower_limit (optionally: target_value)

  Formula:    E = k(r-upper_limit)**2 for r > upper_limit

              E = k(r-lower_limit)**2 for r < lower_limit
  ```
* 'square-well-parabolic-linear'
  ```
  Parameters: upper_limit, lower_limit, upper_linear_limit, lower_linear_limit, (optional: target_value)

  Formula:

    If upper_limit = u, upper_linear_limit = u2, lower_limit = l, lower_linear_limit = l2:

    E = 2k(u2-u)(r - (u2+u)/2) for r > u2

    E = k(r-u)**2 for u < r < u2

    E = k(r-l)**2 for l > r > l2

    E = 2k(l2-l)(r - (l2+l)/2) for r < l2
  ```

We propose to add potential types
* 'upper-bound-parabolic'
* 'lower-bound-parabolic'
* 'upper-bound-parabolic-linear'
* 'lower-bound-parabolic-linear'
with parameters and formulae modified form the full versions (not that target_value is always encouraged).


### Limits on constraint limit values
We propose to enforce that

lower_linear_limit <= lower_limit <= target_value <= upper_limit <= upper_linear_limit

This is particularly relevant to dihedral angles - a restraint of upper_limit: 220.0, lower_limit: 90.0

could be interpreted either as -140.0 - +90.0 or as +90.0 - +220.0

It would be simpler to prohibit it entirely.


### Indirect magnetisation transfer
We propose to add a new tag to the spectrum_dimension_transfer loop, so that it
becomes e.g.
  ```
  loop_
      _nef_spectrum_dimension_transfer.dimension_1
      _nef_spectrum_dimension_transfer.dimension_2
      _nef_spectrum_dimension_transfer.transfer_type
      _nef_spectrum_dimension_transfer.is_indirect

      1 3 through-space  true
      2 3 onebond  false
  stop_
  ```

The is_indirect tag would be used for transfers that are relayed through other
nuclei. The relevant case is the ChhC NOESY (used in solid state NMR) or 3D
CCH HSQC-NOESY-HSQC, where the transfer being measured is a proton-proton NOESY,
but the nucleus observed is actually carbon.


### Linkers and tensor-origin residues
Both types of residue need to be specified to reproduce the calculations that gave
rise to a structure.

Linker residues are essentially program-specific and can be ignored by other programs.
Tensor origin residues, on the other hand, must be understandable by other programs
in order to make sense of the data. I would propose that:

* Linker and origin residues are given the same chain code as the chain they are connected
  to, but are given outside the start-end sequence of the chain.
* A three-letter-code (e.g. 'LNK') be reserved for linker residues. If this is not possible,
  we can specify them as 'UNK' (unknown). Specific linker types (such as Cyana PL, LL2, LL5,
  ...) must be given in a program-specific column.
* A RCSB letter code (such as 'TENSOR')  is reserved for coordinate origin residues. The residue
  contain atoms at positions OO (0.0, 0.0, 0.0), X (1.0, 0.0, 0.0), Y (0.0, 1.0,0.0), and
  Z (0.0, 0.0, 1.0), and the names of these atoms are standardized (I have used ARIA names here,
  but other names could be used). This residue will appear in cooordinate files, so the the name
  has to be official.

  An example is given here:
  ```
  loop_
    _nef_sequence.chain_code
    _nef_sequence.sequence_code
    _nef_sequence.residue_type
    _nef_sequence.residue_variant
    _nef_sequence.linking
    _nef_sequence.cross_linking
    _nef_sequence.cyana_residue_type

    A    1 MET .      start  .         .
    A    2 GLY .      .      .         .
    A    3 LEU .      .      .         .
  [...]
    A   75 SER .      .      .         .
    A   76 LEU .      .      .         .
    A   77 GLU .      .      .         .
    A   78 HIS .      .      .         .
    A   79 HIS .      .      .         .
    A   80 HIS .      .      .         .
    A   81 HIS .      .      .         .
    A   82 HIS .      .      .         .
    A   83 HIS .      end    .         .
    A   84 LNK .      start  .          PL
    A   85 LNK .      .      .         LL2
    A   86 LNK .      .      .         LL2
    A   87 LNK .      .      .         LL2
    A   88 LNK .      .      .         LL2
    A   89 LNK .      .      .         LL2
    A   90 TENSOR .      .      .         ORI
    A   91 LNK .      .      .         LL2
    A   92 LNK .      .      .         LL2
    A   93 LNK .      .      .         LL2
    A   94 LNK .      .      .         LL2
    A   95 LNK .      .      .         LL2
    A   96 TENSOR .      end    .         ORI
  ```

### RDC restraints
RDC restraints must be given with the tensor used.
It would be preferable to have only one tensor per RDC restraint list. Is this acceptable?
* Should the tensor be given as magnitude and rhombicity, or as the axial and rhombic components?
* What should be the specified convention?
* Is it acceptable the tensor origin as a dummy residue? What might be the alternative?

The following proposal has been adapted from Peter Guntert (thanks!):

```
save_rdc_restraint_list_1

  _nef_rdc_restraint_list.sf_category            nef_rdc_restraint_list
  _nef_rdc_restraint_list.sf_framecode             rdc_restraint_list_1

  _nef_rdc_restraint_list.potential_type       parabolic  
  _nef_rdc_restraint_list.tensor_magnitude       11.0000  
  _nef_rdc_restraint_list.tensor_rhombicity    0.0670
  _nef_rdc_restraint_list.tensor_chain_code    A
  _nef_rdc_restraint_list.tensor_sequence_code     90
  _nef_rdc_restraint_list.tensor_residue_type    TENSOR

  loop_
    _nef_rdc_restraint.restraint_id
    _nef_rdc_restraint.restraint_combination_id
    _nef_rdc_restraint.chain_code_1
    _nef_rdc_restraint.sequence_code_1
    _nef_rdc_restraint.residue_type_1
    _nef_rdc_restraint.atom_name_1
    _nef_rdc_restraint.chain_code_2
    _nef_rdc_restraint.sequence_code_2
    _nef_rdc_restraint.residue_type_2
    _nef_rdc_restraint.atom_name_
    _nef_rdc_restraint.weight
    _nef_rdc_restraint.target_value
    _nef_rdc_restraint.target_value_uncertainty
    _nef_rdc_restraint.scale

      1 . A    5 ARG N     A    5 ARG H     1.00      -1.553   3.200    1.198
      2 . A    7 ILE N     A    7 ILE H     1.00      -6.917   3.200    1.200
      3 . A    9 SER N     A    9 SER H     1.00      -8.970   3.200    1.198
      4 . A   10 GLN N     A   10 GLN H     1.00      -9.212   3.200    1.201
[...]
stop_
save_
```

### Residue variant codes
We have proposed a variant code for cis-proline (see change log).
We should discuss variant codes for RNA/DNA and a general system
for non-standard amino acids.

### Restraint-peak links
This is currently handled by a separate savefreame _nef_peak_restraint_links. Incorporating the link
in the restraint tables would simplify the format, but would mean either that each restraint could
have only one peak attached, or that we would need duplicate restraint records.
Do we want to consider any changes here?

### Additional restraint types
Which types should be considered, and who can provide information on how they should be organised?

### Changes needed from the RCSB

  * The main requirement is for the mmCIF format to incorporate a tag for the nef_atom_name, so that the atom name used in the nef file is preserved in the coordinate files

  * We would need an official RCSB code for a TENSOR pseudo-residue to hold tensor descriptions in coordinate files. Failing that, we need to find another way of handling tensor specifications.

  * We are proposing either an official RCSB code for linker residues, or an agreement on using UNK for such residues.

  * There is a need for expanding the set of residue variants. The most urgent need is for cis-proline variants, and for expanding the official variant set to DNA and RNA. If possible it would be useful to make an official specification of the system for making variant codes, so that it was possible to produce such codes de novo for new residues.
