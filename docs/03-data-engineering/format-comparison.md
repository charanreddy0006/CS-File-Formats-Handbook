# Data Format Comparison

| Property | CSV | JSON | JSONL | Parquet | Avro |
|---|---|---|---|---|---|
| Human-readable | ✅ | ✅ | ✅ | ❌ | Usually ❌ |
| Nested data | ❌/limited | ✅ | ✅ | ✅ | ✅ |
| Strong schema | ❌ | Flexible | Flexible | ✅ | ✅ |
| Columnar | ❌ | ❌ | ❌ | ✅ | ❌ |
| Streaming records | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ |
| Analytics | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| Easy manual editing | ✅ | ✅ | ✅ | ❌ | ❌ |

There is no universal winner. The workload determines the appropriate trade-off.
