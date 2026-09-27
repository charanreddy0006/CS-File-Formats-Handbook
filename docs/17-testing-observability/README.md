# 🧪 Testing and Observability Artifacts

Testing and production systems create many machine-readable files.

## Test reports

```text
JUnit XML
coverage.xml
coverage.json
```

## Logs

```text
.log
.jsonl
.ndjson
```

Structured logs are easier to search and process automatically.

Example:

```json
{"timestamp":"2026-09-27T10:00:00Z","level":"INFO","event":"request_completed","status":200}
```

## Metrics

Metrics are often exported through protocols or text formats rather than a universal filename extension.

## Traces

Distributed tracing systems commonly exchange structured trace data through formats/protocols such as OTLP and related encodings.

## Engineering principle

Observability artifacts should be:

- machine-readable
- timestamped
- structured
- safe to retain
- free of accidental secrets
