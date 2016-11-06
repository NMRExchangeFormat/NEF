Nmr Exchange Format (NEF) proposal
==================================

###Organization of this document

The first sections present general issues that are not linked to a specific part
of the example files. Section 2 lists comments to the companion documents,
organised by data category (saveframe).

### General issues

  1. Requirements for NEF compatibility

    The NEF format tries to support as many kinds of data as possible in a
    simple file format. But we can clearly not require any program to
    read and understand data that it does not normally support, be it complex or
    crosslinked sequences, non-standard residues or residue variants, OR/AND
    restraint logic, anonymous atom assignments, particular restraint types,
    etc. If a program does support a certain type of data,
    it is required to read and write such data correctly to/from NEF. If it
    does not, it is free to skip such data, or convert them to something it can
    deal with if this can be done appropriately.
    There is a core set of data that programs must be able to
    read, interpret, and convert to a form it can deal with: this is the case
    for simple linear sequences with linking 'start' 'middle', 'end' and
    'single', the standard 20 protein, DNA, and RNA
    with their variants, atoms, and atom wildcard expressions, and disulfide
    bonds. In other cases programs should refuse to read data they cannot
    handle, rather than misinterpret the information.

  2. Residue and Atom names

    Residues are identified by three strings ('chain_code' (e.g. 'A'), 'sequence_code'
    (e.g. ('127'), 'residue_name' (e.g. 'ALA')) that always are used together.
    Atoms are identified by a residue identifier plus the atom name (e.g. 'HA')
    as a fourth string.

    1. The identifying strings are case sensitive, and the same object must have the same
    name (including casing) throughout the file - except for the use of wildcard names
    for atoms, as described below. Residue and atom names of the molecule are taken from
    the RCSB-curated chemical compound desciptions. Atom names and
    standard 3-letter-type residue names must match the molecule names also
    in casing in order to count as assignments to the molecule. Currently
    this means that they must be ALL-UPPER-CASE, but if in the future mmCif
    introduces mixed-case residue names (e.g. for carbohydrates), the nef
    names must match the case used by mmCif. For chain codes and insertion codes
    upper case is strongly recommended, but lower case is allowed if necessary
    to match e.g. lower-case chain codes used by the mmCif.

      Examples:

      'ALA' and 'CYS' are recognised residue names. 'Ala' and 'cys' are
      not recognised as residue names, but only as anonymous annotation
      strings, and converting them to upper case (tempting as it may be)
      is to modify the data.

      Similarly, 'HA' and 'CA' are recognised atom names. The latter could be alpha
      carbon or calcium depending on conventions for specifying isotopes (which
      will be described below). 'ha', 'Ca', and 'ca' are not recognised as atom
      names that match the molecule, but only as anonymous identifier strings.

    2. 'sequence_code' is a string, not an integer. It is recommended to use
    consecutive numbers along a chain, or, failing that, to put any alt_codes
    as suffixes (as in '127B'). It is encouraged to use the same chain code only
    for groups of residues that are bound to each other.

    3. 'sequence_code's, too, must be consistently used throughout the file. It
    follows that any program-specific numberings must be given and used in the
    program-specific namespace, and that renaming and renumbering after
    deposition must preserve the original names (possibly using a
    deposition-specific namespace for the new names).

    4. Structures must be given in mmCIf format. In this format the author naming
    tags are used for the names in the NEF file, whereas IUPAC names are given as
    the main identifiers. This gives a IUPAC-NEF mapping for each individual
    model in an ensemble. The mapping reflects two different phenomena:
    1) The renumbering of the sequence, renaming of residues or atoms that arises
    from regularisation or changes in standard names when going from author to mmCif
    namespace. 2) The different mapping of 'x' and 'y' nonstereospecifically assigned
    atom groups. In the latter case the mapping may be different for different models
    in the same ensemble. Note that wildcards (except for 'x' and 'y') should *not*
    appear in the coordinate file - the author names for e.g. ALA methyl protons
    should be HB1, HB2, and HB3, even if the group is called HB% throughout the NEF file.

    5. For the common standard residues (20 amino acids, 4 DNA and 4 RNA
    nucleotides) the NEF standard will adopt the IUPAC nomenclature for
    residue names, as well as IUPAC atom names. 

    6. 'residue_name' refers to the residue identified by the matching mmCif
    chemical compound code. The atom naming and topology can therefore be
    taken from the mmCif chemical compound definitions. The same residue_name is used
    for all variants and protonation states - these are specified in the residue_linking  
    and residue_variant columns. If there is no matching 
    mmCif residue, the type is unknown and must be specified outside the NEF system
    in some way. If a new residue type is introduced  to match a previously unknown 
    compound it is recommended to use a name that could not match either current or 
    future mmCif codes - a name with at least four characters containing lower case
    characters would be a good choice. 

    7. A residue is uniquely identified by the 'chain_code' and 'sequence_code',
    so that the same 'residue_name' string must be used consistently throughout
    the file. Strictly speaking this makes the 'residue_name' string redundant,
    but it is used in identifiers to avoid ambiguity and to serve as a
    cross-check.

    8. Atoms are identified by their name. The stereo/nonstereo assignment
    status and atom/atomset/pseudoatom distinction follows from the name, so
    that there is no need for ambiguity codes anywhere in the file.
    All atom names start with the one or two letter element name. For
    one-letter element names this lets you derive the element from the name.
    For two-letter element names and for non-standard isotopes the element and
    isotope are given in the chemical shift list.

    9. Atoms that differ only by stereochemistry (prochiral protons or methyl
    groups, NH2 groups, opposite sides of non-rotating aromatic rings) but
    are not stereospecifically assigned, are distinguished using the suffixes
    'x' and 'y' (lower case).  These suffixes work effectively as a wildcard,
    standing for 'one or the other stereochemistry specifier'.
    In most cases 'x' and 'y' stand for one specific digit, but for
    e.g. DNA/RNA H5' and H5'' the two non-stereospecific names are "H5x" and
    "H5y", and so stand for either one or two primes (' or '').
    The choice of 'x' or 'y' for a given resonance is arbitrary, except
    that atoms in a stereochemically separate branch are all given the same
    suffix. For instance, Val CGx is bound to HGx%, and TYR CDx is bound to
    HDx and CEx. The existing upfield/downfield convention (suffixes 'a'
    and 'b') is *not* supported. In NMR-STAR terms x and x suffixes correspond
    to ambiguity codes 2 (geminal atoms) and 3 (symmetrical aromatic rings).
    The example table at the end of the General Issues section should
    illustrate the principle.

      An atom name like e.g.  'HBx' or 'HBy' stands for the same atom throughout the
      file. It is no known whether this maps to HB2 or HB3. Indeed the mapping can
      be different in different models of the same structure ensemble. The point
      is that all the NMR data are consistent, but a structure ensemble is an
      *interpretation* of the NMR data, which can vary from model to model.

      If you observe only one resonance frequency from e.g. a methylene group, you
      should use e.g. HBx to name it. If you know that both atoms resonate at the
      same frequency (and so are indistinguishable) you should a wildcard expression (HB%)
      instead.

    10. Sets of atoms can be represented by using atom names with wildcards.
    There are two kinds of wildcards:

      '%' for 'any sequence of digits', equivalent to the regular expression
      "[0-9]+".

      '\*' for 'any whitespace-free string', including the empty string,
      equivalent to the regular expression "\S\*".

      Wildcard expressions must be as simple as possible. Specifically:

        1.	Where applicable (i.e. to represent a sequence of digits) '%' must
        be used in preference for '\*' . E.g.: The expressions for equivalent
        nuclei in standard amino acid residues contain only '%', not  '\*'

        2.	The expression must contain the smallest possible number of '%' and '\*'.
        E.g.: expressions like '%%' are disallowed.

        3.	The wildcard may only be used to represent letters that differ
        between (some of the) alternative names. E.g. Isoleucine delta protons
        must be represented as 'HD1%' (and NOT as 'HD%').

      In normal current usage '%' wildcard
      expressions will be used for NMR-equivalent atoms, and '\*' expressions must
      only  be used where '%' expressions would not suffice. In practice this
      means that for proteins all common cases of equivalent atoms are expressed with '%'
      (ALA HB%, ASN HB%, ASN HD%, LEU HD1%, LEU HD%, LEU CD%, TYR CD%, TYR HD%,
      LYS HZ%, ...). Notably N-terminal -NH3+ would be 'H%', as would
      N-terminal -NH2.  '\*' would only be
      used where necessary, mainly for 'H\*', 'C\*', '\*',  ... (all protons, all
      carbons,  all atoms, etc.), or for atom names that do not use digits for
      distinguishing stereochemistry (e.g. DNA/RNA H5' and H5'', where the
      two-atom set is designated H5'\*).

    11. IUPAC pseudoatom names (ALA MB, SER QB, etc.) are NOT expanded into
    sets of atoms. They are reserved for the
    original meaning, i.e. a geometric point positioned at the centroid with zero
    van der Waals radius. A restraint to ALA MB would be different from one to
    ALA HB%, and it would be an error to confuse them. Note that a restraint to
    HB% is calculated by r-6 averaging in most programs, whereas a restraint
    to MB is not. The latter therefore needs to modify the given distance limits
    to obtain the same result.

    12. Pseudoatom/wildcard names, stereospecific or non-stereospecific atom
    names can coexist for the same atom in the same file, but the proper name
    must be used with its defined meaning throughout the NEF file. It follows
    that when renaming the atoms to stereospecific entities, e.g. once the
    coordinates are known, the program must also maintain the name previously
    used to preserve continuity.

      The chemical shift list must contain all known relevant shifts, but it is
      not necessary to give the same chemical shift twice. If e.g. a Ser HB%
      shift is given, the HBx, HBy, HB2, and HB3 are known to be the same.
      Similarly HB% or QB can be used without any obligation to give their
      shift explicitly, also if the atoms involved have different shifts.
      Indeed you can have restraints to atoms that have never
      be measured (like oxygens in hydrogen bond restraints) and these need not
      appear in restraint lists.
      In cases where two protons are indistinguishable by NMR it
      is strongly recommended to use the stereospecific atom names (HB2 and HB3)
      in preference to the 'x' and 'y' forms. Since here may be cases where the
      same atoms are stereospecifically assigned under some conditions but not
      others (e.g. at different temperatures), it is not possible to guarantee
      that only one of the two forms will be present.

      The RCSB has agreed to store the NEF atom identifiers in the tags
      '\_atom_site.auth_asym_id', '\_atom_site.auth_seq_id',
      '\_atom_site.auth_comp_id',  '\_atom_site.auth_atom_id' . This preserves
      NEF naming, and gives a mapping for each structure model to the
      equivalent mmCif tags '\_atom_site.label_asym_id',
      '\_atom_site.label_seq_id', '\_atom_site.pdbx_PDB_ins_code',
      '\_atom_site.label_comp_id', '\_atom_site.label_atom_id'. The
      NEF sequence_code is a string, combined from a numerical sequence
      code and an  optional string insertion code, and therefore maps to two
      mmCif tags. Since the 'auth' tags can differ from one model to another
      within the same ensemble, this allows for floating stereospecific
      assignments that can vary between the individual models in the ensemble.

    13. Residues and atoms that match the molecular sequence (including those
    using pseudoatom and non-stereospecific naming conventions) are understood
    as referring to chains/residues/atoms in the molecule. Names that do not
    match the sequence are allowed; they are interpreted as referring to
    observed but (partially) unassigned resonances. They can be ignored where
    they are inapplicable in context (e.g. in restraint lists), but must be
    maintained in the shift list.

      Programs that do not support non-stereospecific assignments, should
      convert these into wildcard expressions (HBx to HB%,
      HDy% to HD%, etc.)

    14. Selection expressions. Wildcards are allowed only for atom names.
    It would in theory be possible to extend their use to 'chain_code',
    'sequence_code' and 'residue_name' at a later date, if there is a use case
    for this. More complex selection expressions, such as residue ranges, are
    surely too complicated for this kind of format. Note that these can be
    expressed as ambiguous peak assignments or restraints. For the specific
    case of residue ranges we should notice that 'sequence_code' is a string,
    not an integer, which renders the concept of ranges rather unwieldy.
    The supported wildcard expressions for standard residues are given
    in the Residue_Variants.txt file.

    15. Elements and isotopes are deduced from the first letter of the atom name; i.e.
    anything stareting with H is hydrogen, C is carbon, etc. The relevant isotope is
    deduced from context where necessary, e.g. NMR chemical shifts refer to 13C.
    Isotope labeling patterns are not supported in this version of NEF.
    For elements with two-letter abbreviations (e.g. Ca, Cd) the element must be specified
    in the \_nef_chemical_shift.element column. Similarly, non-default isotopes must be
    specified in the \_nef_chemical_shift.isotope_number column (e.g. 2H, 111Cd, 113Cd, ...).
    Note that it is not possible to specify separate shifts for different isotopes of the
    same atom in a single shiftlist. In the unlikely case that this is necessary, the two
    shifts must be given in separate shiftlists.

  3. Identifiers
    1. NEF data block IDs (the string that follows 'data\_') *must* start with
    'nef\_'.

    2. 'sf\_category' values all start with 'nef\_'; for
    program-specific categories they start with the program namespace tag.

    3. 'sf_framecode' *must* start with the relevant category name. If there
    can be more than one saveframe in the category, the category name must
    be followed by an underscore, and then by the unique part of the framecode.

    4. All loops in the format have one or more mandatory columns defined as
    keys, that uniquely identify each row.

    5. Spectrum dimensions, peaks, restraints etc. are numbered starting at
    1 (and *not* at zero). Peaks and restraints are represented by more than one
    line in the corresponding loop; an additional column for the line number
    ('index') serves as the unique key for the loop. The index values are *not*
    preserved when reading and re-writing data.

    6. Peak numbers, restraint numbers, and datablock names / saveframe
    framecodes must  be kept unchanged by programs, so that they can be used as
    persistent identifiers

  4. Program-specific namespaces

    We will define and register prefixes for programs to use in program-specific
    data, that other programs may ignore. We would propose simple prefixes like
    'ccpn', 'cyana', 'amber', 'xplor', 'aria', etc.  For saveframes the
    'saveframe_category' would start with the prefix ('cyana_special_frame',
    'ccpn_special_frame' etc.), and would be used for saveframe names
    ('save_cyana_special_frame_1'), and tag prefixes
    ('\_cyana_special_frame.sf_category') . The loop-prefix would be '\_cyana',
    with loop tags like '\_cyana_special_loop.tag1', '\_cyana_special_loop.tag2',
    ... to match with the STAR rule that all tags must start with an
    underscore. For individual tag names, the prefix will be positioned at the
    start of the actual tag, after  the 'saveframeName' or 'loopName' prefix
    (e.g. '\_chemical_shift_list.cyana_specific_tag' or
    '\_chemical_shift.ccpn_specific_column').

  5. Mandatory content

    A valid NEF data block must contain 'nef_nmr_meta_data', and a valid
    'nef_molecular_system' saveframe. It must also contain at least one
    'nef_chemical_shift_list'. A file whose chemical shift list(s) contain no
    data is technically valid, but will not be accepted for deposition.

  6. Single and multiple files

    Each data block is a self-contained project description, and must have a
    unique name, in context. Data will normally be passed with one data block
    per file, and programs will read only the first NEF data block they
    encounter. It is legal to have multiple data blocks in a file, but under
    normal circumstances only one will be read. Non-NEF data blocks may be
    appended to the file to hold non-NEF information.

    The rules call for keeping data always in a single coherent file, but it is
    not possible to prevent users from gathering data from multiple files. The
    format rules will hold for each file (including the rules on mandatory
    molecular system description, etc.), but programs may, at their own risk,
    put in empty molecular descriptions.

    Programs must faithfully read and (re-)export the information they use.
    Information that is not used may be omitted; it is preferable to keep
    and re-export it, but not if this makes the exported file inconsistent or
    the data are incorrectly reproduced.

  7. Field values and data types
    1. Unlike NMR-STAR, the dollar sign ('$') is *not* used as a prefix to
    indicate a saveframe identifier.

    2. Again unlike NMR-STAR, the question mark ('?') is *not* used to indicate
    missing data - all missing data are indicted by a dot ('.'), which may be
    translated as a null value.

  8. NEF Format versions

    We propose to divide format versions in major and minor, with both running
    as consecutive integers (e.g. 1.0, ... 1.8, 1.9, 1.10, 1.11, ... ... 1.314,
    ...). Minor version changes to the format should be incremental and
    non-breaking, so that code that reads version 1.4 automatically reads
    version 1.3 also. This includes not having duplicate storage slots, so
    that the same information would be found in the same place in both
    versions. Each change should cause an increase in the minor version
    of the format, so that the minor format number is expected to increase
    fast over time.

    Program-specific tags are not included in this rule, and can be
    changed freely by the program owner.

    Major format version changes (e.g. from 1.8 to 2.0) may break previous
    readers. We would expect that many programs would support only one major
    version, and that separate upgrade and downgrade routines be produced to
    convert between major versions.

Examples of mapping from 'xy' atom names to IUPAC
-----------------------------------------------

| Residue | 'xy' names |Mapping 1 | Mapping 2 | Mapping 3 | Mapping 4 |
|---------|------------|----------|-----------|-----------|-----------|
| SER |   |   |   |   |   |
|     | HBx | HB2 | HB3 | - | - |
|     | HBx | HB3 | HB2 | - | - |
| GLU |   |   |   |   |   |
|     | HBx | HB2 | HB3 | HB2 | HB3 |
|     | HBy | HB3 | HB2 | HB3 | HB2 |
|     | HGx | HG2 | HG2 | HG3 | HG3 |
|     | HGy | HG3 | HG3 | HG2 | HG2 |
| VAL |   |   |   |   |   |
|     | HGx% | HG1% | HG2% | - | - |
|     | CGx  | CG1  | CG2  | - | - |
|     | HGy% | HG2% | HG1% | - | - |
|     | CGy  | CG2  | CG1  | - | - |
| TYR |   |   |   |   |   |
|     | HDx | HD1 | HD2 | - | - |
|     | CDx | CD1 | CD2 | - | - |
|     | CEx | CE1 | CE2 | - | - |
|     | HEx | HE1 | HE2 | - | - |
|     | HDy | HD2 | HD1 | - | - |
|     | CDy | CD2 | CD1 | - | - |
|     | CEy | CE2 | CE1 | - | - |
|     | HEy | HE2 | HE1 | - | - |

Comments:

* The same mapping is used whether or not all the x/y atom names are observed
  in context.

* SER: HBx and HBy can map to either HB2 or HB3, but if both are present in a
  given context they must map to *different* atoms.

* GLU: Since HB and HG are different branchings of the residue, there is no
  connection between the mapping for HBx/y and for HGx/y

* VAL: The methyl protons and methyl carbons are part of the same branching, so
  the mappings are correlated. HGx% is always bound to CGx, and HGy%
  to CGy.

* TYR: x and y each designate one of the two branches of the side chain, so
  there are only two possible mappings.
  Regardless whether all the atom names are present in the context, you always
  have the following bond patterns: HDx - CDx - CEx - HEx , and HDy - CDy - CEy - HEy

Wildcard atom sets for N-terminal Threonine
---------------------------------------------

| Atom name | Atoms in set |
|-----------|--------------|
| H% | H1, H2, H3 |
| HA% | - |
| HB% | - |
| HG1% | - |
| HG2% | HG21, HG22, HG23 |
| HG% | HG1, HG21, HG22, HG23 |
| H\* | H1, H2, H3, HA, HB, HG1, HG21, HG22, HG23 |
| HA\* | HA |
| HB\* | HB |
| HG1\* | HG1 |
| HG\* | HG1, HG21, HG22, HG23 |
| HG\*1 | HG1, HG21 |
| H\*1 | H1, HG1, HG21 |
| H\*2\* | H2, HG21, HG22, HG23 |

These expressions are for illustrative purposes only. They comprise the simplest
possible expressions that give a meaningful set of atoms, as well as expressions
for HA, HB, and HG1, that would not be meaningful in context, to illustrate the
system. Only the expressions H%, HG2%, and H\* would appear in normal use.
See the specification/Residue_Variants.txt file for supported wildcard
expressions.

### Data Types

  The precise data type specifications are given (as either data types or
  enumerated values) in the mmcif_nef.dic specification files , which is the
  authoritative reference. They are summarized here.

  * Basic string types
    1. ALL string values are limited to printable 7-bit ASCII characters
    (codes 32 to 126 inclusive), plus line breaks for multiline strings.

    2. 'sf\_framecode's are limited to values that can be written in STAR without
    the use of quotes. This means strings that do not contain whitespace,
    single or double quotes ('"), or the hash sign (#), and that do not start
    with any of the following strings : '\_', 'data\_', 'save\_', 'loop\_', 'stop\_'.

  * Enumerated types:

    1. Booleans: 'true', 'false'

    2. Potential types: 'undefined','log-harmonic','parabolic',
    'square-well-parabolic', 'square-well-parabolic-linear',
    'upper-bound-parabolic', 'lower-bound-parabolic',
    'upper-bound-parabolic-linear',  'lower-bound-parabolic-linear'

    3. '\_nef_sequence.linking': 'start', 'end', 'middle', 'cyclic', 'break',
    'single', 'dummy'

    4. '\_nef_spectrum_dimension.folding': 'circular', 'mirror', 'none'

    5. '\_nef_spectrum_dimension_transfer.transfer_type': 'onebond', 'jcoupling',
    'jmultibond', 'relayed', 'relayed-alternate', 'through-space'

  * Open enumerations (suggested values, but other values allowed):

    1. '\_nef_distance_restraint_list.restraint_origin': 'noe', 'hbond',
    'mutation', 'shift_perturbation', ...

    2. '\_nef_dihedral_restraint_list.restraint_origin': 'chemical_shift',
    'jcoupling', ...

    3. '\_nef_dihedral_rdc_list.restraint_origin': 'measured', ...

    4. '\_nef_spectrum_dimension.axis_code' Isotope codes of form '1H,' '13C', ...
    Jcoupling of the form J(HH), J(HC), ... Multi-quantum coherence of the form
    DQ(HH), DQ(CC), etc., 'delay', 'temperature', 'concentration'

    5. '\_nef_spectrum_dimension.axis_unit': 'hz', 'ppm', 'point', 'K', 's',
    'M', ...

    6. '\_nef_nmr_spectrum.experiment_classification': The CCPN experiment
    classification includes several hundred names. CCPN will provide a table of
    systematic names, associated common names, and a brief description, at a
    later date.

    7. '\_nef_nmr_spectrum.experiment_type': This field should contain a common
    name for the experiment and can be freely chosen. If anyone can propose a
    standard list of such names we could consider proposing those as a standard.


### Specific questions for the NEF draft example files

  * Regarding Section 3. Mandatory: **Molecular system**

    1. There is only one molecular system per project. Different complexes,
    ligands, etc. are handled by using different chain codes.

    2. All programs must support the standard linear polymer residues and
    their default states. Support for non-standard links, residues or residue
    variants is not mandatory, but programs that do support these should read
    and write sequence descriptions accordingly.

    3. Covalent links that are not part of a linear polymer chain are given in
    the 'covalent_links' loop, which shows which atoms are directly bound.
    Which atoms from the original template are missing,will be aparent from the residue 
    variant.

    4. The '\_sequence' loop is a compromise between a full, complex topology
    description and simply assuming linear polymers - see the example files,
    section 3. The '\_nef_sequence.residue_name' is always the
    canonical name (e.g. 'HIS' regardless of protonation state or chain
    position).The '\_nef_sequence.linking' column shows linear connection
    information.

      Linear polymer residues (alpha-amino acids, DNA, and RNA) can have the
      following linking values:
        - 'start': the N-terminal or 5' end of a linear polymer
        - 'end': the C-terminal or 3' end of a linear polymer
        - 'middle': non-terminal residue in a linear polymer
        - 'single': Linking 'single' is a 'free, single molecule' form.
          It is used for any residue that does not participate in a regular linear
          polymer link, e.g. for free amino acids or for any residue that is
          not an alpha amino acid or nucleotide..
        - 'cyclic': first and last residue of a cyclic linear polymer; the
          second 'cyclic' residue precedes the first cyclic residue in the
          sequence
        - 'break': A residue of linking type 'middle' that does not form a standard
        sequential link to the following residue in the table,
        - 'dummy': Linking 'dummy' is used for dummy residues. By definition
        these do not contain atoms or participate in links. By convention, dummy
        residues used to represent tensor values have the residue name 'TNSR'

        Linkings 'middle', 'cyclic', or 'break' all signify a linear polymer
        residue with links in both directions

      Sequential links are specified as follows:

        - A normal sequence is given as a 'start' residue, followed by a series of 'middle'
          residues and terminated with an 'end' residue.

        - If the 'start' ,'end' or both are omitted, or replaced by a form that does not
          allow links, the residue(s) at the end(s) of the sequence are NOT converted to
          terminal form, but remain in 'middle' form, with dangling ends.

        - A series of 'middle' residues with a 'cyclic' residue at either end defines a cyclic
          stretch of linear polymer. 'cyclic' residues must appear in pairs, and all intervening
          residues must be of type 'middle'.

        - 'single' residues do not partake in implicit sequential links, but may be linked
          through explicitly specified covalent bonds.

        - The 'break' linking is used only to specify gaps in the sequence and has a very specific
          meaning: It signifies a residue of 'middle' form, that does NOT form a link to the
          successive residue. It s necessary only if  the successive residue is of type 'middle',
         'end', or 'break', and is likely to be very rarely used.

      By default variants of standard residues are assumed to be the pH 7 forms,
      as specified in the Residue_Variants.txt file. Programs
      are required to support (in the sense of being able to read and
      sensibly interpret) the standard 20 amino acids, 4 DNA and 4 RNA
      nucleotides, together with their standard variants and wildcard atoms.
      These are all defined in the specification/Residue_Variants.txt file.
      The mmCIf_NEF_variant_mapping.txt file further gives the NEF representation of
      all existing mmCif variant codes.
      Non-standard residues are assumed to be in the form given by the corresponding
      mmCif chemical compound.

    5. Cis peptide bonds are indicated by the (Boolean) nef_sequence.cis_peptide column. 
    The default value is 'false'.

    6. The index column is a line number with consecutive integers starting
    at 1. It is not preserved on import and re-export. The purpose it to
    preserve the order of the lines (which is significant for specifying the
    sequence) for implementations like (deposition) databases that do not use
    ordered containers for the data.


  * Regarding Section 5. Optional: **Distance restraint lists(s)**

    1. The index column is a series of consecutive integers that serve to
    make each line unique. The index values are *not* preserved when reading and
    re-writing data.

    2. All types of restraints need persistent identifier numbers (see separate
    discussion above).

    3. Potential types ('parabolic', 'log-normal', ...)  are given for the
    entire list, as these determine the number and kind of parameters. This
    means that restraints using different potential types must be given in
    separate lists.

    4. The 'restraint_origin' field gives the source of the restraints, e.g.
    'noe', 'hbond', 'mutation', 'shift_perturbation' for a distance restraint
    list, or 'talos', 'jcoupling', ... for a dihedral restraint list.

    5. We have column names for the parameters used by most common
    potential types, specifically 'target_value', 'target_value_uncertainty',
    'lower_limit', 'upper_limit', lower_linear_limit', and 'upper_linear_limit'.
    All are optional, depending on the potential type, but 'target_value' and
    'target_value_uncertainty' should be given whenever a meaningful value is
    defined, even if this value is not used in the calculation.

    6. Each line (sub-restraint) of the table has its own independent
    parameters ('weight', 'target_value', 'upper_limit', etc.), although in most
    common cases the values will be identical on lines that belong to the same
    restraint. It is up to each program to deal with the data as they are.

    7. In the most common case, sub-restraints within the same restraint are
    treated as ambiguous, and can be OR'ed or summed as the program may prefer.

      The hbond restraint list shows an example where it is necessary to combine
      sub-restraints with AND logic. Each hydrogen bond is defined by two
      distance restraints. For a simple restraints these can be given
      separately, as for restraints 1,2 or in a single restraint (as for
      restraint 3). For an ambiguous hydrogen bond (restraint 4) it is
      necessary to combine the contributions as (a AND b) OR (c AND d)

      The 'restraint_combination_id' is a positive integer used to signify an AND
      statement, so that all sub-restraints with the same combination_id are
      AND'ed. Only sub-restraints with the same 'restraint_id' can be AND'ed, but
      the 'restraint_combination_id' is valid across the entire table, so that you
      can select a single AND'ed group by looking only in the 'combination_id'
      column. Where it is not needed, the 'restraint_combination_id' is left
      empty. Whereas the normal ambiguous restraint can be described as
      [a OR b OR c], the 'restraint_combination_id' allows you to describe
      restraints as [(a AND b) OR (c AND d) OR e] etc.

      For another  discussion of more complex restraint logic, using the
      'restraint_combination_id', see section 6.

    8. Note that the weight of a restraint contribution may be 0.0, in which
    case this contribution should not be used for restraining in calculations

    9. The current draft supports the potential types

      - 'undefined'

      - 'log-harmonic'

         *Parameters*: 'target_value', 'target_value_error'

      - 'parabolic'

         *Parameters*: 'target_value', 'target_value_error'

         *Formula*: E = k(r-target_value)\*\*2

      - 'square-well-parabolic'

         *Parameters*: 'upper_limit', 'lower_limit'
          (optionally: 'target_value', 'target_value_error')

         *Formula*:

         E = k(r-upper_limit)\*\*2 for r > upper_limit

         E = k(r-lower_limit)\*\*2 for r < lower_limit

      - 'square-well-parabolic-linear'

         *Parameters*: 'upper_limit', 'lower_limit', 'upper_linear_limit',
          'lower_linear_limit', (optional: 'target_value', 'target_value_error')

         *Formula*:

          If upper_limit = u, upper_linear_limit = u2,
            lower_limit = l, lower_linear_limit = l2:

          E = 2k(u2-u)(r - (u2+u)/2) for r > u2

          E = k(r-u)\*\*2 for u < r < u2

          E = k(r-l)\*\*2 for l > r > l2

          E = 2k(l2-l)(r - (l2+l)/2) for r < l2

      - 'upper-bound-parabolic'

      - 'lower-bound-parabolic'

      - 'upper-bound-parabolic-linear'

      - 'lower-bound-parabolic-linear'

      The formulae and parameters for the last four follow obviously from the
      preceding definitions.

  * Regarding Section 6. Optional: **Dihedral restraint lists(s)**

    1. The 'restraint_origin' describes the origin or source of the restraints.
    We recommend using one of the values given below, but if these do
    not fit, others may be added. Values: 'chemical_shift', 'jcoupling'.

    2. The index column is a series of consecutive integers that serve to
    make each line unique. The index values are *not* preserved when reading and
    re-writing data.

    3. In the most common case, sub-restraints within the same 'restraint_id'
    are treated as ambiguous. This amounts to combining them with an OR
    statement.  There are cases where it is necessary to combine sub-restraints
    with an AND, e.g. for dihedral restraints where the molecule must be
    constrained within either of two disjoint regions of the Ramachandran plot.
    The 'restraint_combination_id' is a positive integer used to signify an AND
    statement, so that all sub-restraints with the same combination_id are
    AND'ed. Only sub-restraints with the same 'restraint_id' can be AND'ed, but
    the 'restraint_combination_id' is valid across the entire table, so that you
    can select a single AND'ed group by looking only in the 'combination_id'
    column. Where it is not needed, the 'restraint_combination_id' is left
    empty. Whereas the normal ambiguous restraint can be described as
    [a OR b OR c], the 'restraint_combination_id' allows you to describe
    restraints as [(a AND b) OR (c AND d) OR e] etc.

    4. The '\_nef_dihedral_restraint.name' column gives the standard name of the
    corresponding dihedral ('PHI', 'PSI', 'OMEGA', 'CHI1', 'CHI2', ...).
    This column is an information field, that supplements but does *not* replace
    or override the atom designations.

    5. Note that the weight of a restraint contribution may be 0.0, in which
    case this contribution should not be used for restraining in calculations

  * Regarding Section 7. Optional: **RDC restraint lists(s)**

    1. The orientation tensor is indicated by giving the 'chain_code',
    'sequence_code', and 'residue_name' for the residue used to give the
    orientation tensor in coordinate files. The 'residue_name' should be TNSR.
    Tensor values are given as magnitude and rhombicity.

    2. The RDC restraint list can also be used to give non-reduced dipolar
    couplings.

    3. The 'restraint_origin' describes the origin or source of the restraints.
    We recommend using one of the values given below, but if these do
    not fit, others may be added. The value 'measured' should typically be
    sufficient.

    4. The index column is a series of consecutive integers that serve to
    make each line unique. The index values are *not* preserved when reading and
    re-writing data.

    5. RDC's should be given unscaled (i.e. the values actually measured), and
    with proper signs (i.e. NH RDC's should list a positive value for decreasing
    splitting whereas CH RDC's should list a positive value for increasing
    splitting). The scale column gives a scaling constant that is multiplied with
    the measured value to give a set of values that can be compared, as used by
    the program.

    6. The 'distance_dependent' column shows whether the measurement depends on
    a variable interatom distance.

    7. Note that the weight of a restraint contribution may be 0.0, in which
    case this contribution should not be used for restraining in calculations

  * Regarding Section 8. Optional: **Peak lists(s)**

    1. Each 'nmr_spectrum' block can contain only one 'peak_list'. If you want
    to give different peak lists for the same experiment, you must duplicate the
    entire block, including the spectrum description.

    2. Each spectrum must be associated with a shift list, to allow for data
    from different temperatures, isotope labellings etc. Multiple peak lists can
    share a shift list. The '\_nmr_spectrum.chemical_shift_list' tag gives the
    framecode for the relevant shift list.

    3. There are both a free-form and an officially controlled version of
    experiment classification. Both are optional, but strongly recommended.
    The latter uses the CCPN nomenclature, which is designed to capture only
    those experimental differences that reflect in different assignment
    possibilities for the peaks. See
    [the CCPN wiki](https://sites.google.com/site/ccpnwiki/Home/documentation/ccpnmr-analysis/core-concepts/nme-experiment-nomenclature-v2-2011)
    for a current description and view (an earlier version) of the publication
    [here](http://link.springer.com/article/10.1007%2Fs10858-006-9076-z).

    4. Dimension numbering runs from 1 to n for a n-dimensional spectrum.

    5. Magnetisation transfer between dimensions is given as an explicit table
    of dimension pairs and their transfer types - which ought to be the most
    robust system. Transfer types follow the CCPN system, which reflects only
    differences that are important for assignment possibilities. The permitted
    values are:

      * 'onebond': atoms directly bound, whatever the transfer mechanism
      * 'Jcoupling': J coupling over one or more bonds
        (also used for standard proton-proton coupling)
      * 'Jmultibond': J coupling over more than one bond
      * 'relayed': relayed through multiple J couplings (multistep transfer,
        TOCSY, ...)
      * 'relayed-alternate': a solid state TOCSY transfer type with alternating
         peak sign
      * 'through-space': Through-space transfer (NOESY, ROESY,.. but also
        J coupling across H-bonds)

    6. There is only one kind of \_peak loop, so we use the same tags for 2D
    peaks, 3D peaks etc. For e.g. a 3D peak list, tags for dimensions 4 and
    higher are simply omitted. The maximum possible dimension is 15.

    7. The index column is a series of consecutive integers that serve to
    make each line unique. The index values are *not* preserved when reading and
    re-writing data.

    8. Peak lists can choose to give height, volume or both to represent
    intensity. If a peak table gives both values, it is up to the program and
    the restraint list section to indicate which value was used for restraint
    generation (if so desired).

    9. The current draft does not allow for storing different transitions
    (multiplet components) within a single peak (multiplet). If this were to be
    desired at some point, the format could be extended, most likely with an
    additional '\_peak.component_id' column or '\_peak.peak_group'.

  * Regarding Section 9. Optional: **Linkage table for peaks and restraints** (one per project)

    1. Links between peaks and restraints are given in the 'peak_restraint_link'
    table. The use of an extra table is necessary in order to support links from
    multiple restraints to more than one peak. There is only a single such table in
    each project. The links connect entire peaks and restraints (which
    corresponds to multiple lines in the relevant loops). Each peak can be
    linked to multiple restraints, and vice versa. Links to different types of
    restraint all share a single table.


  * Regarding Section 10. Optional: **Program-specific raw_data saveframe**

    1. Each program-specific namespace should include the '\_programspecific_raw_data'
    saveframe (e.g. '\_cyana_raw_data', '\_csrosetta_raw_data' etc. as a slot to add
    copies of raw input files. The preferred option remains to use structured
    program-specific tags to store program-specific information, but this
    saveframe serves as a quick way to add unstructured data or copies of input
    files for comparison.

    NB, being program-specific this saveframe is not specified in the mmCIf_nef.dic
    specification file, but only shown as an example in the Commented_Example.nef
    file. Suggestions are welcome as to how such a saveframe should be put into the
    general nef specification.
