# Registry role

This role setup registry for restricted Openshfit installation, which don't have access to the internet.

## Variables documentation

A name of the Openshift cluster.
This variable is required.
```yaml
registry_cluster_name
```

Directory that contains `oc` binary file. Used to mirror the registry and extract `openshift-install` command.
Default is `{{ ansible_env.HOME }}/.{{ registry_cluster_name }}/bin`.
```yaml
registry_binaries_dir
```

Directory where certs and httpassd files are created for the registry and then mount to container.
Default is `{{ ansible_env.HOME }}/.{{ registry_cluster_name }}/.registry`.
```yaml
registry_directory
```

Define a username for the registry to be used for authentication.
Default is `ansible`.
```yaml
registry_username
```

Define a password for user specified in `registry_username`.
Default is `ansible`.
```yaml
registry_password
```

A port of the registry which should be exposed.
Default is `5000`.
```yaml
registry_port
```

A pull secret for the registry we want to mirror.
This variable is required.
```yaml
registry_pull_secret
```

Define a repository which should be mirrored.
Default is `openshift-release-dev`.
```yaml
registry_product_repo
```

Default is `ocp4/openshift4`.
```yaml
registry_repo
```

Host of the registry. It's the current host the role is running on.
Default is `ansible_hostname`.
```yaml
registry_host
```

Registry release.
Default is `ocp-release`.
```yaml
registry_release
```

The version of the release.
Default is `4.15.0-ec.2-x86_64`.
```yaml
registry_ocp_release
```

The e-mail to be defined the in the pull secret of the created registry.
```yaml
registry_email
```

The type of the certificate management system.
Default is `vault`.
```yaml
registry_certificate_type
```

### Vault certificate management
Vault role to be used to generate the certificate.
```yaml
registry_vault_role_name
```

URL of the vault system.
```yaml
registry_vault_url
```

A token to authenticate to `vault` system.
```yaml
registry_vault_token
```
