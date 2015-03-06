NEF (NMR Exchange Format)
=========================

### Project Organisation

`specifications` contains the format specifications. Currently this consists of the
`Commented_example.nef` example file and the `Overview.md` explanatory comments. More
formal specifications will be added to the project later.

The `data` directory contains sample and test data.
 `data/original` contains original test data input, while `data/derived` is reserved for  I/O tests.  The data directory is currently empty - more sample files will
 be provided once the current change proposal has been discussed.

For input/output test we use the naming convention that a program that reads a file
prepends its name to the file when output. So if e.g. Cyana reads the file
`ARIA-CCPN_CASD155.nef`, the result would be output to `Cyana-ARIA-CCPN_CASD155.nef`.

For the top-level files,
`LICENSE` contains the license for the NEF files (we propose GNU LGPL v. 3),
`Charter.md` is the (proposed) charter and founding document for the NEF consortium, `
`Changes.md` is a change log.
