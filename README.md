NEF (NMR Exchange Format)
=========================

### Project Organisation

`specifications` contains the format specifications. Currently this consists of the
`Commented_example.nef` example file, the `Overview.md` explanatory comments,
and the mmcif_nef.dic speciofications file.

The `data_0_2` directory contains sample and test data up to version 0.20.

For input/output test we use the naming convention that a program that reads a file
prepends its name to the file when output. So if e.g. Cyana reads the file
`ARIA-CCPN_CASD155.nef`, the result would be output to `Cyana-ARIA-CCPN_CASD155.nef`.

For the top-level files,
`LICENSE` contains the license for the NEF files (we propose GNU LGPL v. 3),
`Charter.md` is the (proposed) charter and founding document for the NEF consortium, `
`Changes.md` is a change log.
