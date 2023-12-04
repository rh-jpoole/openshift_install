# DNS role

This role setup the DNS[1] for Openshift.

Supported DNS systems:

 - Infoblox

This role follow following [guide](https://docs.openshift.com/container-platform/4.14/installing/installing_vsphere/installing-vsphere.html#installation-dns-user-infra_installing-vsphere) to configure all relevant DNS records:

## Variables documentation

#### dns_nodes
List of dictionaries describing Openshift nodes based on which DNS records are created.

```yaml
openshift_install_nodes
  name[required] - Name of the node. DNS A record is created based on this name.
  ipaddr - If specified static IP configuration will be used for the node.
}
```

#### dns_dhcp_enabled
Default is `false`.

#### dns_network
Network to be used to create the DNS records in.
Required.

### Infoblox
#### dns_primary_grid
Specify the primary grid for the DNS zone.

#### dns_network_view
Specify network view of the DNS records.
Default is `default`.

#### dns_provider
Dictionary that define a credentials to connect to the Infoblox system.
If not define we look for the credentials in the hashi vault system.

```yaml
host - hostname of the Infoblox systme
username - Username of the user to use Infoblox system
password - Password of the user speficied in username
```
