# Magic Bytes and MIME Types

## Magic bytes

Some formats begin with recognizable byte signatures.

Conceptually:

```text
file
 ↓
header bytes
 ↓
format identification
 ↓
parser
```

Examples of well-known signatures include PDF and PNG headers.

## MIME type

A MIME type communicates a content type:

```text
text/plain
text/html
application/json
image/png
image/jpeg
application/pdf
audio/mpeg
video/mp4
```

MIME types are widely used by HTTP servers, browsers, APIs, and upload systems.

## Secure upload design

Never trust only:

```text
filename extension
```

Prefer:

```text
extension
+ MIME declaration
+ signature inspection
+ safe parser
+ resource limits
```
