# Registry role

This role setup registry for restricted Openshfit installation, which don't have access to the internet.

## Variables documentation

#### registry_cluster_name
A name of the Openshift cluster.
This variable is required.

#### registry_binaries_dir
Directory that contains `oc` binary file. Used to mirror the registry and extract `openshift-install` command.
Default is `{{ ansible_env.HOME }}/.{{ registry_cluster_name }}/bin`.

#### registry_directory
Directory where certs and httpassd files are created for the registry and then mount to container.
Default is `{{ ansible_env.HOME }}/.{{ registry_cluster_name }}/.registry`.

#### registry_username
Define a username for the registry to be used for authentication.
Default is `ansible`.

#### registry_password
Define a password for user specified in `registry_username`.
Default is `ansible`.

#### registry_port
A port of the registry which should be exposed.
Default is `5000`.

#### registry_pull_secret
A pull secret for the registry we want to mirror.
This variable is required.

#### registry_product_repo
Define a repository which should be mirrored.
Default is `openshift-release-dev`.

#### registry_repo
Default is `ocp4/openshift4`.

#### registry_host
Host of the registry. It's the current host the role is running on.
Default is `ansible_hostname`.

#### registry_release
Registry release.
Default is `ocp-release`.

#### registry_ocp_release
The version of the release.
Default is `4.15.0-ec.2-x86_64`.

#### registry_email
The e-mail to be defined the in the pull secret of the created registry.

#### registry_certificate_type
The type of the certificate management system.
Default is `vault`.

### Vault certificate management

#### registry_vault_role_name
Vault role to be used to generate the certificate.

#### registry_vault_url
URL of the vault system.

#### registry_vault_token
A token to authenticate to `vault` system.
