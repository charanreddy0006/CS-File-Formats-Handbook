# Choosing an ML Model Format

## Questions to ask

1. Which framework created the model?
2. Is the artifact weights-only or a complete model?
3. Does the deployment target support the format?
4. Is portability important?
5. Is quantization required?
6. Can the artifact be loaded safely?

## Common mapping

```text
PyTorch ecosystem → .pt / .pth / .safetensors
Cross-framework inference → .onnx
TensorFlow ecosystem → .keras / SavedModel ecosystem
Local LLM inference → .gguf
```

Never treat model serialization as automatically trustworthy. Verify source, provenance, integrity, and loading behavior.
