# Anatomy of a File

A generalized file may contain:

```text
┌───────────────────────────────┐
│ Signature / magic bytes       │
├───────────────────────────────┤
│ Version                       │
├───────────────────────────────┤
│ Header                        │
├───────────────────────────────┤
│ Metadata                      │
├───────────────────────────────┤
│ Schema / indexes              │
├───────────────────────────────┤
│ Payload                       │
├───────────────────────────────┤
│ Checksums / footer            │
└───────────────────────────────┘
```

Not every format has every component.

## Why this matters

Understanding internal structure helps with:

- debugging corrupted files
- efficient parsing
- random access
- compatibility
- security validation
- format conversion
