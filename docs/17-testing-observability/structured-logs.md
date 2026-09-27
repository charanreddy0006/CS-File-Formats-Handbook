# Structured Log Formats

Plain log:

```text
2026-09-27 INFO request completed status=200 duration=42ms
```

Structured log:

```json
{
  "timestamp": "2026-09-27T10:00:00Z",
  "level": "INFO",
  "event": "request_completed",
  "status": 200,
  "duration_ms": 42
}
```

Structured logs make it easier to:

- query fields
- aggregate events
- create dashboards
- correlate requests
- feed observability systems

Do not log passwords, tokens, private keys, or unnecessary personal information.
