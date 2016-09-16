Change log
==========


**Proposal change_sequence_linking**

* Changed rules for 'break' linking type, making it simper t0 specify sequences with breaks

* Removed 'nonlinear' linking type - now using 'single' for all residue types instead.



**Proposal new_residue_variants**

* Change variant specification from RCSB codes to form tha lista added and subtracted atoms

* Add _nef_sequence.cis_peptide column to specify peptide obnd cis/trans state.

* Add specifications/Residue_Variants.txt listing all supported standard residue variants

* Add example of non-stadard modified residue


**Proposal add_nef_sequence_ordinal**

* Add ordinal column to nef_sequence loop to recflect the (significant) line order.

**Proposal multiple changes**

* Add program_specific_raw_data saveframe
* Change nonsereospecific wildcards from X/Y (upper case) to x/y (lower case)
* Tighten allowed wildcards
* Improve consistency of COmmented_Example

**Proposal remove_chemical_shift_units**

* Remove  _nef_chemical_shift_list.atom_chemical_shift_units tag

**Proposal ordinal_to_index_id**

* change 'ordinal' to 'index_id' 
(preserving _nef_run_history.run_ordinal, which *does* signify an ordering)

**Proposal residue_type_to_name**

* change 'residue_type' to 'residue_name' in all occurrences and tags

**Version 0.2**

* Version 0.2 (unfortunately named) is the final, cleaned-up version before
proposing the changes that will define the first release version, 1.0.

* Version 0.2 has a proper specifications file mmcif_nef.dic.

* A wide range of test data have been added.

* The Commented_Example file has been reorganised, expanded with additional
examples, and cleaned of errors and inconsistencies.

* The overview document has been modified to clarify confusion on a number of
points.

**Version 0.8**

* Updated charter to reflect the discussion at the Rutgers 7/11-9/1 2015 meeting.

* Basic format rules
	* Datablock name must now start with 'nef_'
	* All sf_framecode must now start with the name of the corresponding
		sf_category
	* '?' is no longer supported to mean 'not set' - all unset parameters must
		now be given as '.', which translates as null (None)
	* mandatory and optional tags and key columns for loops defined and given in
		Commented_Example.nef
	* The convention of starting references to saveframes with a '$' is NOT
		supported any longer.
	* added ordinal column to peak and restraint lists to provide unique
		identifier for each line


* Added new tags
	* Added restraint_origin tag to _nef_dihedral_restraint_list, _nef_distance_restraint_list, _nef_rdc_restraint_list
	* Added _nef_rdc_restraint.distance_dependent and _nef_rdc_restraint.scale
	* Explicitly expanded _nef_peak loop to support up to 15D peaks
	* _nef_nmr_meta_data.uuid, uniquely identifying the specific version of the data


* Further changes
	* Changed atomset wildcard from '#' (e.g. ALA HB#) to '%' (e.g. ALA HB%)
	* Changed specification of sequence and amino acid variants.

**Version 0.7**

1. **Global nef name space**. All tags now start with '_nef_'.

2. **RCSB Amino acid variant codes**

  The RCSB variant codes consist of three parts, connected by underscores:

  - The amino acid three-letter code

  - the backbone linking, with twelve alternatives:
    * 'LL' : L-amino acid, middle position
    * 'LSN3' : L-amino acid, N-terminal -NH3+
    * 'LEO2' : L-amino acid, C-terminal COO-
    * 'LEO2H' : L-amino acid, C-terminal  COOH
    * 'LFZW' : L-amino acid, free zwitterion
    * 'LFOH' : L-amino acid, free COOH,NH2 form

    And six equivalent forms starting with 'D' for D-amino acids.

  - The side chain protonation state.

   The default is the fully protonated form (no third field).

   A missing proton is indicated by DHxy, where Hxy is the proton name.

      For NEF the standard forms are with charged Glutamate, Aspartate, Lysine,
      and Arginine side chains and charged N and C termini. These need not be
      indicated. The cases you might want to indicate (enclosed in '\*\* in the table)
      are protonated Aspartate, di-sulfide or deprotonated Cysteine, protonated
      Glutamate, double protonated Histidine, neutral HE-protonated Histidine,
      neutral Lysine, and O-linked (or deprotonated) Serine, Threonine, or
      Tyrosine.  These are the codes that programs should consider using.
      You would also want to indicate cis-Proline, but there are no RCSB codes
      for that situation (as far as we could tell), so we invented them (John
      Westbrook!?).

      The more common variant codes are given in the table below. I have omitted
      free amino acid forms and side chain deprotonated ARG and TRP.
      Non-standard variant codes that should be used where relevant, are enclosed in '\*\*'.
      In all other cases, the short three-letter residue-type will suffice.

      ```
      **Table 1:** *PDB amino-acids variant codes (sorted)*
    Description               Residue-type    Middle      N-terminal-NH3+   C-terminal COO-   C-terminal COOH
    Alanine                     ALA           ALA_LL        ALA_LSN3          ALA_LEO2              ALA_LEO2H
    protonated Arginine         ARG           ARG_LL        ARG_LSN3          ARG_LEO2          ARG_LEO2H
    Asparagine                  ASN           ASN_LL        ASN_LSN3          ASN_LEO2          ASN_LEO2H
    de-protonated Aspartate     ASP           ASP_LL_DHD2   ASP_LSN3_DHD2     ASP_LEO2_DHD2     ASP_LEO2H_DHD2
    protonated Aspartate        ASP          *ASP_LL*      *ASP_LSN3*        *ASP_LEO2*         ASP_LEO2H
    Free cysteine               CYS           CYS_LL        CYS_LSN3          CYS_LEO2          CYS_LEO2H
    S_S or S- cysteine          CYS          *CYS_LL_DHG*  *CYS_LSN3_DHG*    *CYS_LEO2_DHG*     CYS_LEO2H_DHG
    Glutamine                   GLN           GLN_LL        GLN_LSN3          GLN_LEO2          GLN_LEO2H
    protonated Glutamate        GLU          *GLU_LL*      *GLU_LSN3*        *GLU_LEO2*         GLU_LEO2H
    de-protonated Glutamate     GLU           GLU_LL_DHE2   GLU_LSN3_DHE2     GLU_LEO2_DHE2     GLU_LEO2H_DHE2
    Glycine                     GLY           GLY_LL        GLY_LSN3          GLY_LEO2          GLY_LEO2H
    HD-protonated Histidine     HIS           HIS_LL_DHE2   HIS_LSN3_DHE2     HIS_LEO2_DHE2     HIS_LEO2H_DHE2
    HD,HE protonated Histidine  HIS          *HIS_LL*      *HIS_LSN3*        *HIS_LEO2*         HIS_LEO2H
    HE-protonated Histidine     HIS          *HIS_LL_DHD1* *HIS_LSN3_DHD1*   *HIS_LEO2_DHD*     HIS_LEOH2_DHD1
    Isoleucine                  ILE           ILE_LL        ILE_LSN3          ILE_LEO2          ILE_LEO2H
    Leucine                     LEU           LEU_LL        LEU_LSN3          LEU_LEO2          LEU_LEO2H
    protonated Lysine           LYS           LYS_LL        LYS_LSN3          LYS_LEO2          LYS_LEO2H
    neutral Lysine              LYS          *LYS_LL_DHZ3* *LYS_LSN3_DHZ3*   *LYS_LEO2_DHZ3*    LYS_LEO2H_DHZ3
    Methionine                  MET           MET_LL        MET_LSN3          MET_LEO2          MET_LEO2H
    Phenylalanine               PHE           PHE_LL        PHE_LSN3          PHE_LEO2          PHE_LEO2H
    Proline                     PRO           PRO_LL        PRO_LSN3          PRO_LEO2          PRO_LEO2H
    cis Proline                 PRO          *PRO_LL_CIS*  *PRO_LSN3_CIS*    *PRO_LEO2_CIS*     PRO_LEO2H_CIS
    Serine                      SER           SER_LL        SER_LSN3          SER_LEO2          SER_LEO2H
    O-linked-Serine             SER          *SER_LL_DHG*  *SER_LSN3_DHG*    *SER_LEO2_DHG*     SER_LEO2H_DHG
    Threonine                   THR           THR_LL        THR_LSN3          THR_LEO2          THR_LEO2H
    O-linked Threonine          THR          *THR_LL_DHG1* *THR_LSN3_DHG1*   *THR_LEO2_DHG1*    THR_LEO2H_DHG1
    Tryptophan                  TRP           TRP_LL        TRP_LSN3          TRP_LEO2          TRP_LEO2H
    Tyrosine                    TYR           TYR_LL        TYR_LSN3          TYR_LEO2          TYR_LEO2H
    O-linked or O- Tyrosine     TYR          *TYR_LL_DHH*  *TYR_LSN3_DHH*    *TYR_LEO2_DHH      TYR_LEO2H_DHH
    Valine                      VAL           VAL_LL        VAL_LSN3          VAL_LEO2          VAL_LEO2H
    ```

3. Indirect magnetisation transfer

      We have added a new tag to the spectrum_dimension_transfer loop, so that it becomes e.g.

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

    The is_indirect tag would be used for transfers that are relayed through other nuclei. The relevant cases are
    the ChhC NOESY (used in solid state NMR) or 3D CCH HSQC-NOESY-HSQC, where the transfer being measured is a
    proton-proton NOESY, but the nucleus observed is actually carbon.

4. We have added a proposal for representing tensors (for use in e.g. RDC restraint lists), including a format for the tensor value, and a system of dummy residues to hold the tensor orientation. Please see the Questions document for details
