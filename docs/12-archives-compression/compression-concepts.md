# Compression Concepts

## Lossless

Original information can be reconstructed exactly.

```text
original → compress → decompress → original
```

Examples include:

- GZIP
- ZIP compression
- FLAC
- PNG compression

## Lossy

Some information is intentionally removed.

```text
original → encode → smaller representation
```

Examples:

- JPEG
- MP3
- many video codecs

## Compression ratio

Conceptually:

```text
compression ratio =
original size / compressed size
```

Higher ratio is not automatically better; CPU cost, decode speed, quality, and workload matter.
