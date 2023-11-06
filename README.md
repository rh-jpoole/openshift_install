# Openshift install collection
This collection includes roles to help users setup openshift with user provisined infrastructure.
This collection contains multiple roles which help to setup infrastructure for the Openshift like
DNS and load balancers on external platforms. We currently support Infoblox and F5.

Role support following platforms:
  - baremetel
  - vpshere
  - none

## Requirements:
 - Python 3.8
 - Ansible 2.13

## Dependencies:
 - python3-aiohttp (vmware)
 - infoblox-client (infoblox)
 - nmstate (openshift-install agent)
 - oc (openshift-install)
 - openshift-install


## Getting started:

### Install role

To install the role please run following command

```
ansible-galaxy collection install machacekondra.openshift_install
```

### Configure variables

To run the configure playbook execute following command:

```
ansible-playbook -i ocp_prod machacekondra.openshift_install.configure
```

