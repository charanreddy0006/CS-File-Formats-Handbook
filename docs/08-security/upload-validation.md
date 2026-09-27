# Secure File Upload Validation

A robust upload service should treat every uploaded file as untrusted.

## Weak validation

```text
if filename.endswith(".pdf"):
    accept()
```

An attacker can rename content.

## Stronger validation

```text
1. Limit request size
2. Normalize filename
3. Inspect declared MIME type
4. Inspect content signature
5. Parse with a safe library
6. Enforce resource limits
7. Store outside executable paths
8. Scan where appropriate
9. Generate a safe internal filename
10. Log the decision
```

## Special care

Archives can contain:

- nested archives
- enormous expansion ratios
- path traversal entries
- executable content

Never extract untrusted archives without limits.
