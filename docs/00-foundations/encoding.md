# Character Encoding

Encoding maps characters to bytes.

Common encodings:

- ASCII
- UTF-8
- UTF-16
- UTF-32
- Latin-1 / ISO-8859-1

## UTF-8

UTF-8 is dominant across modern software systems because it preserves ASCII compatibility while supporting Unicode.

Example:

```text
Hello
नमस्ते
こんにちは
```

all can be represented in UTF-8.

## Common failure

A file written as UTF-8 may be decoded incorrectly as another encoding, producing garbled text.

Typical symptoms:

```text
UnicodeDecodeError
mojibake
unexpected symbols
```

## Engineering practice

When a text format does not explicitly define encoding, document the expected encoding in your project.
