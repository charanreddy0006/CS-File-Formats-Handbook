# Serialization

Serialization converts an in-memory object or structure into a storable/transmittable representation.

```text
Object
  ↓ serialize
Bytes / text
  ↓ store or transmit
File / network
  ↓ deserialize
Object
```

Examples:

| Technology | Common representation |
|---|---|
| JSON | Text |
| YAML | Text |
| XML | Text |
| Pickle | Python binary serialization |
| Protocol Buffers | Binary |
| MessagePack | Binary |
| Avro | Binary/text ecosystem with schemas |
| Parquet | Columnar binary storage |

## Serialization is not the same as compression

Serialization answers:

> How do I represent this object?

Compression answers:

> How do I reduce its representation size?

A serialized object can then be compressed.
