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
 - python3-hvac (hashi vault)
 - hvac
 - infoblox-client (infoblox)
 - nmstate (openshift-install agent)
 - openshift-install
 - oc


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


## Flow

## Variables

### Custom
`Define a openshift-install binary on a target machine, if set we won't download openshift-install binary based on `openshift_install_version` variable`
openshift_install_binary

### Base config
``
openshift_install_base_domain
``
openshift_install_cluster_name: omachace-vsphere-day2

### Vsphere
openshift_install_datacenter: DC-Practice-Lab
openshift_install_cluster: Practice-Lab-Cluster
openshift_install_datastore: pool0-ceph-storage
openshift_install_folder: "/DC-Practice-Lab/vm/omachace"
openshift_install_network_name: "vlan-314 - DPortGroup"

### LB
openshift_install_api_vip: 10.1.192.242
openshift_install_ingress_vip: 10.1.192.243

### Hashi Vault
openshift_install_vault_secret_dns: flightpath/data/dns
openshift_install_vault_secret_lb: flightpath/data/lb
openshift_install_vault_secret_vsphere: flightpath/data/vsphere
openshift_install_vault_url: https://10.1.196.198:8200/

### Nodes
openshift_install_network: "10.1.198.224/28"
openshift_install_dhcp: true
openshift_install_nodes:
  - {name: 'vm0'}
  - {name: 'vm1'}
  - {name: 'vm2'}
