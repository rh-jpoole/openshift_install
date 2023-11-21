## Required variables

The base domain of the cluster. All DNS records will be sub-domains of this base and include the cluster name.
``
openshift_install_base_domain
``

The name of the cluster. Collection will create a subdomain with this name, and all DNS records in this sub-domain.
```
openshift_install_cluster_name
```

List of dictionaries describing Openshift nodes.
```
openshift_install_nodes {
  name[required] - Name of the node. DNS A record is created based on this name.
  ipaddr - If specified static IP configuration will be used for the node.
  macaddr - If specified this MAC address will be configured for the node.
}
```


The name of the datacenter to use in the vCenter instance.
```
openshift_install_datacenter
```

The vCenter cluster to install the OpenShift Container Platform cluster in.
```
openshift_install_cluster
```

The name of the default datastore to use for provisioning volumes.
```
openshift_install_datastore
```

The network that will be created for create Vcenter virtual machine.
```
openshift_install_network_name
```

Network range that will be used to allocate addresses for Openshift nodes and used as Openshift machine network (eg 10.1.198.224/28).
```
openshift_install_network
```

The virtual IP (VIP) address that will be configured for control plane API access.
```
openshift_install_api_vip
```

The virtual IP (VIP) address that will be configured for cluster ingress.
```
openshift_install_ingress_vip
```

DNS primary grid where the DNS zone will be created.
```
openshift_install_dns_primary_grid
```

## Optional

### Vcenter
### Load balancer
#### F5
### DNS
#### Infoblox
### Openshift
