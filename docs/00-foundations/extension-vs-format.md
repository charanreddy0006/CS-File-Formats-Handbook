# Extension vs Format vs MIME Type

These terms are often confused.

| Concept | Example | Meaning |
|---|---|---|
| Filename | `sales.parquet` | Complete file name |
| Extension | `.parquet` | Conventional suffix |
| Format | Apache Parquet | Internal data organization |
| MIME type | `application/vnd.apache.parquet` | Type identifier used by systems |
| Magic bytes | Format-specific bytes | Binary signature used for identification |
| Encoding | UTF-8 | Representation of text characters |

## Why extensions cannot be trusted blindly

A file can be renamed:

```text
secret.txt → secret.jpg
```

Renaming does not transform its contents.

Applications may therefore inspect:

- magic bytes
- MIME metadata
- internal headers
- parsers
- container signatures

## Engineering lesson

When validating uploaded files, do not rely only on the extension.

Use layered validation:

```text
extension
   +
declared MIME type
   +
content signature
   +
parser validation
   +
size limits
```
