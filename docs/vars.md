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
