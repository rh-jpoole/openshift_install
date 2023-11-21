# Setup role

This role prepare the environment for the run of the `openshift-install` agent.

This role download and install following dependencies:
 - openshift-install
 - oc

It downloads `oc` binary from official Openshift website. Then based on the input parameters
it either download `openshift-install` binary or extract it from the container `registry`.

This role also uses pip and system package manager to install following packages:

System dependencies:
 - nmstate
 - podman
 - python3-hvac (hashi)
 - python3-passlib (httpasswd)

Pip dependencies:
 - infoblox-client (infoblox)
 - aiohttp (vmware)


## Variables documentation

URL which is used to download client tools - `oc` and `openshift-install`.
Default URL used is https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp
```yaml
setup_clients_url
```

Required variable which define the name of the Openshift cluster.
```yaml
setup_cluster_name
```

Define a directory where downloaded binaries will be added.
```yaml
setup_binaries_dir: {{ ansible_env.HOME }}/.{{ configure_cluster_name }}
```

Define of the `setup_binaries_dir` directory should be cleaned before the run of the role.
```yaml
setup_binaries_clean
```

Version of the Openshift tools to be downloaded from the `setup_clients_url`.
Could be `latest`/`stable` or specific release.
```yaml
setup_cluster_version
```

If true the `openshift-install` binary won't be downloaded from `setup_clients_url`.
It should be extracted from restricted registry, which is done in `registry` role.
Default is `false`.
```yaml
setup_install_registry
```
