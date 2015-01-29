Nmr Exchange Format (NEF) proposal
==================================

###Organization of this document

The first sections present general issues that are not linked to a specific part
of the example files. Section 2 lists comments to the companion documents,
organised by data category (saveframe).

### General issues

  1. Residue and Atom names

    Residues are identified by three strings (chain_code, sequence_code,
    residue_type) that always are used together. Atoms are identified by a
    residue identifier plus the atom name as a fourth string.

    1.  The identifying strings are case sensitive, and all identifiers
    (including casing) must be consistent throughout a file. Atom names and
    standard 3-letter-type residue names should be ALL-UPPER-CASE, and it is
    recommended that this convention is followed throughout. Lower case is
    allowed for chain codes, and future names (e.g. carbohydrate residues) may
    allow lower case.

    2.  sequence_code is a string, not an integer. It is recommended to use
    consecutive numbers along a chain, or, failing that, to put any alt_codes
    as suffixes (as in '127B').

    3.  sequence_codes, too, must be consistently used throughout the file. It
    follows that any program-specific numberings must be given and used in the
    program-specific namespace, and that renaming and renumbering after
    deposition must preserve the original names (possibly using a
    deposition-specific namespace for the new names).

    4.  For the common standard residues (22 amino acids, 4 DNA and 4 RNA nucleotides) the NEF standard will adopt the IUPAC nomenclature for residue types and wwPDB nomenclature for  variants, as well as IUPAC atom names. For the standard residues we will use UPPER-CASE for atom names. For non-standard residues applications can make their own choices, although IUPAC or wwPDB nomenclature is recommended. It has to be decided which variants are formally part of the standard.

    5.  residue_type must be specified as the basic type in all cases (e.g. use
      HIS regardless of protonation state).

    6.  A residue is uniquely identified by the chain_code and sequence_code,
    so that the same residue_type string must be used consistently throughout
    the file. Strictly speaking this makes the residue_type string redundant,
    but it is used in identifiers to avoid ambiguity and to serve as a
    cross-check.

    7.  Atoms are identified by their name. The stereo/nonstereo assignment
    status and atom/atomset/pseudoatom distinction follows from the name, so
    that there is no need for assignment status codes anywhere in the file

    8.  Atoms that differ only by stereochemistry (prochiral protons or methyl
      groups, NH2 groups, opposite sides of non-rotating aromatic rings) but
      are not stereospecifically assigned, are distinguished using the suffixes
      'X' and 'Y'.  These suffixes work effectively as a wildcard, so the 'X'
      and 'Y' stands for one specific digit, and cannot be used for other
      purposes. The choice of suffix for a given resonance is arbitrary, except
      that atoms in a stereochemically separate branch are all given the same
      suffix. For instance, Val CGX is bound to HGX%, and TYR CDX is bound to
      HDX and CEX. The existing upfield/downfield convention (suffixes 'a'
      and 'b') is not supported. In NMR-STAR terms X and Y suffixes correspond
      to ambiguity codes 2 (geminal atoms) and 3 (symmetrical aromatic rings).

    9.  Sets of atoms can be represented by using atom names with wildcards. We propose to support two kinds of wildcards: '#' for 'any sequence of digits', and '\*' for 'any whitespace-free string'. In normal current usage wildcard expressions will be used for NMR-equivalent atoms, and '\*' expressions must only  be used where '#' expressions would not suffice. In practice this means that all common cases of equivalent atoms are expressed with '#' (ALA HB#, ASN HB#, ASN HD#, LEU HD1#, LEU HD#, LEU CD#, TYR CD#, TYR HD#, LYS HZ#, ...). Notably N-terminal -NH3+ would be 'H#'.  '\*' would only be used where necessary, mainly for 'H\*', 'C\*', '\*',  ... (all protons, all carbons,  all atoms, etc.).

    10. IUPAC pseudoatom names (ALA MB, SER QB, etc.) would be reserved for the original meaning, i.e. a separate atom positioned at the centroid with zero van der Waals radius. A restraint to ALA MB would be different from one to ALA HB#, and it would be an error to confuse them. E.g. ALA MB and ALA HB# can both appear in the same shift list, if both are needed e.g. in different restraint lists.

    11. Pseudoatom/wildcard names, stereospecific or non-stereospecific atom names can coexist for the same atom in the same file, but the proper name must be used with its defined meaning throughout the NEF file. It follows that when renaming the atoms to stereospecific entities, e.g. once the coordinates are known, the program must also maintain the name previously used to preserve continuity.

      The RCSB has agreed to store an 'nef_atom_name' alongside the existing
    atom identifier ('_atom_site.label_atom_id' ?)' in separate tags in the
    coordinate file, where nef_atom_name refers to the name used in the NEF
    file. Individual models in the ensemble can thus each have their own unique
    combinations of nef_atom_name and label_atom_id, allowing for floating
    stereospecific assignments that can vary between the individual models in
    the ensemble.  

    12. Residues and atoms that match the molecular sequence (including those
    using pseudoatom and non-stereospecific naming conventions) are understood
    as referring to chains/residues/atoms in the molecule. Names that do not
    match the sequence are allowed; they are interpreted as referring to
    observed but (partially) unassigned resonances. They can be ignored where
    they are inapplicable in context (e.g. in restraint lists), but must be
    maintained in the shift list.

    13. Selection expressions. For the time being wildcards are allowed only
    for atom names. It would be possible to extend their use to chain_code,
    sequence_code and residue_type at a later date, if there is a use case for
    this. More complex selection expressions, such as residue ranges, are
    surely too complicated for this kind of format. Note that these can be
    expressed as ambiguous peak assignments or restraints. For the specific
    case of residue ranges we should notice that sequence_code is a string, not
    an integer, which renders the concept of ranges rather unwieldy.

  2. Identifiers
    1. NEF data block IDs (the string that follows "data\_") *must* start with
    "nef\_".

    2. sf\_category values all start with 'nef\_'; for program-specific
    categories they start with the program namespace tag.

    3. sf_framecodes *must* start with the relevant category name. If there
    can be more than one saveframe in the category, the category name must
    be followed by an underscore, and then by the unique part of the framecode.

    4. All loops in the format have one or more mandatory columns defined as
    keys, that uniquely identify each row.

    5. Spectrum dimensions, peaks, restraints etc. are numbered starting at
    1 (and *not* at zero). Peaks and restraints are represented by more than one
    line in the corresponding loop; an additional column for the line number
    ('ordinal') serves as the unique key for the loop.

    6. Peak numbers, restraint numbers, and datablock names /  saveframe
    framecodes must  be kept unchanged by programs, so that they can be used as
    persistent identifiers

  3. Program-specific namespaces

    We will define and register prefixes for programs to use in program-specific
    data, that other programs may ignore. We would propose simple prefixes  
    like 'ccpn', 'cyana', 'amber', 'xplor', 'aria', etc.  For saveframes the
    saveframe_category would start with the prefix (cyana_special_frame,
    ccpn_special_frame etc.), and would be used for saveframe names
    ('save_cyana_special_frame_1'), and tag prefixes
    ('_cyana_special_frame.sf_category') . The loop-prefix would be '_cyana',
    with loop tags like '_cyana_special_loop.tag1', '_cyana_special_loop.tag2',
    ...  to match with the STAR rule that all tags must start with an
    underscore.  For individual tag names, the prefix will be positioned at the
    start of the actual tag, after  the saveframeName or loopName prefix
    (e.g. "_chemical_shift_list.cyana_specific_tag" or
    _chemical_shift.ccpn_specific_column).

  4. NEF Format versions

    A valid NEF data block must contain nef_nmr_meta_data, and a valid
    nef_molecular_system saveframe. It must also contain at least one 
    nef_chemical_shift_list. A file whose chemical shift list(s) contain no
    data is technically valid, but will not be accepted for deposition.


  5. Single and multiple files

    Each data block is a self-contained project description, and must have a
    unique name, in context. Data will normally be passed with one data block
    per file, and programs will read only the first nef data block they
    encounter. It is legal to have multiple data blocks in a file, but under
    normal circumstances only one will be read.

    The rules call for keeping data always in a single coherent file, but it is
    not possible to prevent users from gathering data from multiple files. The
    format rules will hold for each file (including the rules on mandatory
    molecular system description, etc.), but programs may, at their own risk,
    put in empty molecular descriptions.

    Programs must faithfully read and (re-)export the information they use.
    Information that is not used should be kept and re-exported if possible but
    may be omitted.
    Programs should not re-export incorrect values for information they do not use
    (e.g. truncated residue names, partial sequences, ...)

  6. Field values and data types
    1. Unlike NMR-STAR, the dollar sign ('$') is *not* used as a prefix to
    indicate a saveframe identifier.

    2. Again unlike NMR-STAR, the question mark ('?') is *not* used to indicate
    missing data - all missing data are indicted by a dot ('.'), which may be
    translated as a null value.

  7. Format  versions

    We propose to divide format versions in major and minor, with both running
    as consecutive integers (e.g. 1.0, ... 1.8, 1.9, 1.10, 1.11, ... ... 1.314,
      ...). Minor version changes to the format should be incremental and
      non-breaking, so that code that reads version 1.4 automatically reads
      version 1.3 also. This includes not having duplicate storage slots, so
      that the same information would be found in the same place in both
      versions. Each change should cause an increase in the minor version
      of the format, so that the minor format number is wexpected to increase
      fast over time.

      Program-specific tags are not included in this rule, and can be
      changed freely by the program owner.

      Major format version changes (e.g. from 1.8 to 2.0) may break previous
      readers. We would expect that many programs would support only one major
      version, and that separate upgrade and downgrade routines be produced to
      convert between major versions.



### Specific questions for the NEF draft example files

  1. Regarding Section 3. Mandatory: **Molecular system**

    1.  There is only one molecular system per project. Different complexes,
    ligands, etc. are handled by using different chain codes.

    2.  The _sequence loop is a compromise between a full, complex topology description and simply assuming linear polymers - see the example files, section 3. Of the three information columns the residue_type is always the canonical name, while the residue_variant shows variants, according to the wwPBD system. The linking column shows linear connection information, and can have the following values:

      - 'start' - meaning the N-terminal or 5' end of a linear polymer
      - 'end' - meaning the C-terminal or 3' end of a linear polymer
      - 'single' - meaning not connected to anything,

      The cross_linking column shows cross-linking state and can have two values (for now):

      - 'link' - meaning involved in a link that is not part of a linear polymer.
      - 'disulfide' - meaning specifically forming a disulfide link.

      Other relevant information on the linking state can be found in the residue_variant column and the covalent_links loop below.

    3.  The residue numbers given are author values, and do not have to be consecutive, or even integers. However, a sequence of consecutive residues beginning with a  'start' linking and ending with an 'end' linking form a connected  linear polymer in order. It is discouraged to use the same chain code for residues that are not bound to the others in the chain. Covalently bound residues that do not form part of a regular chain (e.g. side-chain-linked carbohydrates) can be given after the 'end' residue to show they are not part of the chain proper.

  2. Regarding Section 5. Optional: **Distance restraint lists(s)**

    1. The ordinal column is a series of consecutive integers that serve to
    make each line unique. These values are *not* preserved when reading and
    re-writing data.

    1. All types of restraints need persistent identifier numbers (see separate
      discussion above)

    2.  Potential types (parabolic, log-normal, ...)  are given for the entire
    list, as these determine the number and kind of parameters. This means that
    restraints using different potential types must be given in separate lists.

    3. The 'restraint_origin' field gives the source of the restraints, e.g.
    'noe', 'hbond', 'mutation', 'shift_perturbation' for a distance restraint
    list, or 'talos', 'jcoupling', ... for a dihedral restraint list.

    4.  We have column names for the parameters used by most common
    potential types, specifically 'target_value', ' target_value_uncertainty',
    'lower_limit', 'upper_limit', lower_linear_limit', and 'upper_linear_limit'.
    All are optional, depending on the potential type, but target_value and
    target_value_uncertainty should be given whenever a meaningful value is
    defined, even if this value is not used in the calculation.

    5.  Each line (sub-restraint) of the table has its own independent
    parameters (weight, target_value, upper_limit, etc.), although in most
    common cases the values will be identical on lines that belong to the same
    restraint. It is up to each program to deal with the data as they are.

    6.  In the most common case, sub-restraints within the same restraint are
    treated as ambiguous, and can be OR'ed or summed as the program may prefer.
    For a discussion of more complex restraint logic, using the
    restraint_combination_id, see section 6.

    7. The current draft supports the potential types

      - 'undefined'

      - 'log-harmonic'

         *Parameters*: target_value, target_value_error

      - 'parabolic'

         *Parameters*: target_value, target_value_error

         *Formula*: E = k(r-target_value)**2

      - 'square-well-parabolic'

         *Parameters*: upper_limit, lower_limit
                       (optionally: target_value, target_value_error)

         *Formula*:

         E = k(r-upper_limit)\**\2 for r > upper_limit

         E = k(r-lower_limit)\*\*2 for r < lower_limit

      - 'square-well-parabolic-linear'

         *Parameters*: upper_limit, lower_limit, upper_linear_limit,
              lower_linear_limit, (optional: target_value, target_value_error)

         *Formula*:

          If upper_limit = u, upper_linear_limit = u2,
             lower_limit = l, lower_linear_limit = l2:

          E = 2k(u2-u)(r - (u2+u)/2) for r > u2

          E = k(r-u)**2 for u < r < u2

          E = k(r-l)**2 for l > r > l2

          E = 2k(l2-l)(r - (l2+l)/2) for r < l2

      - 'upper-bound-parabolic'

      - 'lower-bound-parabolic'

      - 'upper-bound-parabolic-linear'

      - 'lower-bound-parabolic-linear'

      The formulae and parameters for the last four follow obviously from the
      preceding definitions.


  3. Regarding Section 6. Optional: **Dihedral restraint lists(s)**

    1.The restraint_origin describes the origin or source of the restraints.
      We recommend using one of teh values given below, but if these do
      not fit, others may be added. Values: 'chemical_shift', 'jcoupling'.

    2. The ordinal column is a series of consecutive integers that serve to
     make each line unique. These values are *not* preserved when reading and
     re-writing data.

    3.  In the most common case, sub-restraints within the same restraint_id  
    are treated as ambiguous. This amounts to combining them with an OR
    statement.  There are cases where it is necessary to combine sub-restraints
    with an AND, e.g.  for dihedral restraints where the molecule must be
    constrained within either of two disjoint regions of the Ramachandran plot.
    The restraint_combination_id is a positive integer used to signify an AND
    statement, so that all sub-restraints with the same combination_id are
    AND'ed. Only sub-restraints with the same restraint_id can be AND'ed, but
    the restraint_combination_id is valid across the entire table, so that you
    can select a single AND'ed group by looking only in the combination_id
    column.  Where it is not needed, the restraint_combination_id is left empty.

    Whereas the normal ambiguous restraint can be described as [a OR b OR c],
    the restraint_combination_id allows you to describe restraints as
    [(a AND b) OR (c AND d) OR e] etc.

    4. The  _nef_dihedral_restraint.name column gives the standard name of the
    corresponding dihedral ('PHI', 'PSI', 'OMEGA', 'CHI1', 'CHI2', ...).
    This column is an information field, that sup-lements but does *NOT* replace
    or override the atom designations.

  4. Regarding Section 7. Optional: **RDC restraint lists(s)**

    1.  The orientation tensor is indicated by giving the chain_code,
      sequence_code, and residue_type for the residue used to give the
      orientation tensor in coordinate files. The residue_type should be TNSR.
      Tensor values are given as magnitude and rhombicity.

    2. The RDC estraint list can also be used to give non-reduced dipolar
    couplings.

    3.The restraint_origin describes the origin or source of the restraints.
    We recommend using one of the values given below, but if these do
    not fit, others may be added. The value 'measured' should typically be  
    sufficient.

    4. The ordinal column is a series of consecutive integers that serve to
     make each line unique. These values are *not* preserved when reading and
     re-writing data.

    5.  RDC's should be given unscaled (i.e. the values actually measured), and
    with proper signs (i.e. NH RDC's should list a positive value for decreasing
    splitting whereas CH RDC's should list a positive value for increasing
    splitting). The 'scale' column gives the scaling constant used.

    6.  The distance_dependent column shows whether the mesurement depends on
    a variable ineratom distance.

  5. Regarding Section 8. Optional: **Peak lists(s)**

    1.  Each nmr_spectrum block can contain only one peak_list. If you want to
    give different peak lists for the same experiment, you must duplicate the
    entire block, including the spectrum description.

    2.  Each spectrum must be  associated with a shift list, to allow for data
    from different temperatures, isotope labellings etc. Multiple peak lists can
    share a shift list. The   _nmr_spectrum.chemical_shift_list tag gives the
    framecode for the relevant shift list.

    3.  There are both free-form and an officially controlled version of
    experiment classification. Both are optional, but strongly recommended.
    The latter uses the CCPN nomenclature, which is designed to capture only
    those experiment differences that reflect in different assignment
    possibilities for the peaks. See
    https://sites.google.com/site/ccpnwiki/Home/documentation/ccpnmr-analysis/core-concepts/nme-experiment-nomenclature-v2-2011
    for a current description and  
    http://link.springer.com/article/10.1007%2Fs10858-006-9076-z
    for a publication (reflecting an earlier version).

    4.  Dimension numbering runs from 1 to n for a n-dimensional spectrum.

    5.  Magnetisation transfer between dimensions is given as an explicit table
    of dimension pairs and their transfer types - which ought to be the most robust system. Transfer types follow the CCPN system, which reflects only differences that are important for assignment possibilities. The permitted values are :

      * 'onebond'	: atoms directly bound, whatever the transfer mechanism
      * 'Jcoupling'	: J coupling over one or more bonds
      * 'Jmultibond' : J coupling over more than one bond
      * 'relayed' : relayed through multiple J couplings (multistep transfer,  
        TOCSY, ...)
      * 'relayed-alternate' : a solid state TOCSY transfer type with alternating
         peak sign
      * 'through-space' : Through-space transfer (NOESY, ROESY,.. but also
        J coupling across H-bonds)

    6.  There is only one kind of _peak loop, so we use the same tags for 2D
    peaks, 3D peaks etc. For e.g. a 3D peak list, tags for dimensions 4 and
    higher are simply omitted. The maximum possible dimension is 15.

    1. The ordinal column is a series of consecutive integers that serve to
    make each line unique. These values are *not* preserved when reading and
    re-writing data.

    7.  Peak lists can choose to give height, volume or both to represent
    intensity. If a peak table gives both values, it is up to the program and
    the restraint list section to indicate which value was used for restraint
    generation (if so desired).

    8.  The current draft does not allow for storing  different transitions
    (multiplet components) within a single peak (multiplet). If this is desired
    at some point, the format can be extended, most likely with an additional
    _peak.component_id column or _peak.peak_group.

  6. Regarding Section 9. Optional: **Linkage table for peaks and restraints**
  (one per project)

    1.  Links between peaks and restraints are given in the peak_restraint_link
    table. The use of an extra table is necessary in order to support links from
    one restraint to more than one peak. There is only a single such table in
    each project. The links connect entire peaks and restraints (which
    corresponds to multiple lines in the relevant loops). Each peak can be
    linked to multiple restraints, and vice versa. Links to different types of
    restraint all share a single table.
