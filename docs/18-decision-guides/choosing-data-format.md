# Choosing a Data Format

## Start with the workload

| Requirement | Consider |
|---|---|
| Human-readable export | CSV / JSON |
| API payload | JSON |
| Line-by-line streaming | JSONL / NDJSON |
| Analytical warehouse files | Parquet / ORC |
| Event serialization with schema | Avro / Protobuf |
| In-memory columnar processing | Arrow |

## Practical pipeline

```text
API
 ↓
JSON
 ↓
Validation
 ↓
Transformation
 ↓
Parquet
 ↓
Object storage
 ↓
Warehouse / query engine
```

The format should match the boundary where it is used.
