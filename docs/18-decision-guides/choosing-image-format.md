# Choosing an Image Format

```text
Is it a photograph?
 ├─ Yes → JPEG / WebP / AVIF
 └─ No
     ↓
Needs transparency?
 ├─ Yes → PNG / WebP / AVIF
 └─ No
     ↓
Is it a logo / icon / vector illustration?
 └─ Yes → SVG
```

For production systems, also consider:

- browser compatibility
- decoding cost
- editing tools
- quality targets
- animation
- color profile
- accessibility and delivery pipeline
