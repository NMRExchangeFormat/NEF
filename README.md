NEF (NMR Exchange Format)
=========================

### Project Organisation

`specifications` contains the format specifications. Currently this consists of the `Commented_example.nef` example file and the `Overview.md` explanatory comments. More formal specifications will be added to the project later.

The `data` directory contains sample and test data.
 `data/orginal` contains original test data input, while `data/derived` is reserved for I/O tests.  All the files in that directory currently come from the Jan 2015 NEF meeting.

For input/output test we use the naming convention that a program that reads a file prepends its name to the file when output. So if e.g. Cyana reads the file `ARIA-CCPN_CASD155.nef`, the result would be output to `Cyana-ARIA-CCPN_CASD155.nef`.

For the top-level files, `LICENSE` contains the license for the NEF files (we propose GNU LGPL v. 3), `Charter.md` is the (proposed) charter and founding document for the NEF consortium, `Questions.md` contains a list of outstanding problems and topics for discussion, and `Changes.md` is a change log.
`
