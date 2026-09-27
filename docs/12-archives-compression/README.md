# 📦 Archives and Compression

## Archive

An archive groups files:

```text
ZIP
TAR
7z
```

## Compression

Compression reduces representation size:

```text
GZIP
BZIP2
XZ
Zstandard
```

## Combined workflows

```text
tar + gzip → .tar.gz
tar + xz   → .tar.xz
tar + bzip2 → .tar.bz2
```

TAR itself is primarily an archive format, not a compression algorithm.

## Common commands

```bash
tar -cf archive.tar folder/
tar -czf archive.tar.gz folder/
unzip archive.zip
```

## Security

Be careful with archives from untrusted sources. Path traversal and decompression-bomb style attacks can make extraction dangerous if software does not enforce safe limits.
