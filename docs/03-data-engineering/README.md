# 📊 Data Engineering Formats

## Row-oriented text

### CSV

Good for:

- interoperability
- simple exports
- human inspection
- small/medium tabular datasets

Weaknesses:

- ambiguous types
- escaping complexity
- weak schema semantics
- inefficient analytics at scale

### JSONL / NDJSON

One JSON object per line:

```json
{"id":1,"name":"A"}
{"id":2,"name":"B"}
```

Excellent for logs, streaming pipelines, and ML datasets.

## Columnar formats

### Parquet

Designed for analytical workloads.

Key concepts:

- columnar storage
- schema
- compression
- predicate pushdown support
- column pruning
- statistics

Common ecosystem:

```text
Spark
DuckDB
Snowflake
BigQuery
Athena
Pandas
Polars
PyArrow
```

### ORC

Another columnar format strongly associated with Hadoop/Hive ecosystems.

## Serialization / interchange

### Avro

Schema-oriented serialization commonly used in distributed systems and event/data platforms.

### Apache Arrow

A columnar in-memory representation rather than simply a traditional file format. Arrow also has IPC and Feather-related storage.

## Format selection

```text
Human interchange → CSV / JSON
Event records → JSONL / Avro / Protobuf
Analytics → Parquet / ORC
In-memory analytics → Arrow
```
