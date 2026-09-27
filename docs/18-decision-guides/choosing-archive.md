# Choosing an Archive / Compression Format

## ZIP

Good for:

- broad compatibility
- desktop distribution
- application packages
- simple archives

## TAR

Good for:

- Unix/Linux packaging
- preserving filesystem metadata
- combining with compression tools

## 7z

Good when strong compression and its ecosystem are appropriate.

## gzip / bzip2 / xz / zstd

These are compression technologies rather than general-purpose multi-file archive formats.

```text
many files
   ↓
TAR
   ↓
compression
   ↓
.tar.gz / .tar.xz / .tar.zst
```
