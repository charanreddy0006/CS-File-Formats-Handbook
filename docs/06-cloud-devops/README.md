# ☁️ Cloud, DevOps and Infrastructure Files

Infrastructure is configuration expressed as files.

## Docker

```text
Dockerfile
.dockerignore
compose.yml
docker-compose.yml
```

## Kubernetes

Commonly:

```text
*.yaml
*.yml
```

with resources such as:

```yaml
apiVersion:
kind:
metadata:
spec:
```

## Terraform

```text
.tf
.tfvars
.tfstate
```

Important:

> Terraform state can contain sensitive infrastructure information. Treat it as sensitive data.

## CI/CD

```text
.github/workflows/*.yml
.gitlab-ci.yml
Jenkinsfile
```

## Configuration

```text
.env
.yaml
.yml
.json
.toml
.ini
.conf
```

Never commit real credentials merely because they are stored in a configuration file.
