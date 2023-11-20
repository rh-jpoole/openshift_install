# Openshift install collection
This collection contains roles to install and configure Openshift and its infrastructure.
There are roles to setup external DNS and LoadBalancer. It's using agent based installation
method.

Collection support following Openshift platforms:
  - vpshere

Collection support following DNS systems:
  - Infoblox

Collection support following LoadBalancer systems:
  - F5

## Requirements:
 - Python 3.8
 - Ansible 2.13

## Dependencies:
Following dependencies will be installed by playbook on the node which is used for installation:

 - python3-aiohttp (vmware)
 - python3-hvac (hashi vault)
 - hvac
 - infoblox-client (infoblox)
 - nmstate (openshift-install agent)
 - oc
 - openshift-install

## Getting started:

### Install role

The role is available on Ansible Galaxy, to install the role please run following command

```
ansible-galaxy collection install machacekondra.openshift_install
```

### Configure variables

There are few mandatory variables which must be specified to configure the infrastructure.
All the variables are documented in specific roles and also [here](doc/vars.md).

## Execution

To run the playbook execute following command:

```
ansible-playbook -i ocp_prod machacekondra.openshift_install.run
```

Where the `ocp_prod` is inventory file, with specified variables for your infrastructure.
The example inventory files are in `examples` directory.

## Registry
Custom container registry can be installed and cofigured on any machine on the network so user can use disconnected envirnoment with their registry.

### Dependencies
Following dependencies will be installed on the target machine.
 - podman
 - python3-passlib (httpasswd)

