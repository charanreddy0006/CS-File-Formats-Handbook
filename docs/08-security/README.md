# 🔐 Security and Cryptographic Files

## Certificate ecosystem

```text
.pem
.crt
.cer
.csr
.p12
.pfx
```

### PEM

PEM is a textual encapsulation format commonly used for certificates and keys.

### CSR

A Certificate Signing Request contains information used when requesting a certificate.

### PKCS#12

`.p12` / `.pfx` commonly package certificates and private keys, usually protected by a password.

## Key files

Common SSH files:

```text
id_ed25519
id_ed25519.pub
id_rsa
id_rsa.pub
known_hosts
authorized_keys
config
```

The private key must remain secret.

## Security rule

A file extension does not determine whether a file is safe.

A harmless-looking:

```text
config.json
```

may contain a password.

Treat **content and sensitivity** separately from file type.
