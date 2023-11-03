from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import urllib.parse
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import open_session


class FilterModule(object):

    def filters(self):
        'Define filters'
        return {
            'fetch_macaddrs': self.fetch_macaddrs,
            'merge_ips': self.merge_ips,
            'network_cidr': self.network_cidr,
            'worker_nodes_len': self.worker_nodes_len,
            'master_nodes_len': self.master_nodes_len,
        }

    def master_nodes_len(self, nodes):
        return len([node for node in nodes if node.get('role', 'master') == 'master'])

    def worker_nodes_len(self, nodes):
        return len([node for node in nodes if node.get('role') == 'worker'])

    def network_cidr(self, network):
        n = network.split('/')
        if n > 1:
            return n[1]

    def merge_ips(self, openshift_nodes, ips):
        _openshift_nodes = []
        for idx, node in enumerate(openshift_nodes):
            node['ipaddr'] = ips[idx]
            _openshift_nodes.append(node)

        return _openshift_nodes

    def fetch_macaddrs(self, openshift_nodes, cl_name, **kwargs):
        """
        Update openshift_nodes variable with mac addresses fetch from VMware vCenter

        :param openshift_nodes: List of VM names to fetch mac addresses for
        """
        self._openshift_nodes = []
        import asyncio

        current_loop = asyncio.get_event_loop_policy().get_event_loop()
        current_loop.run_until_complete(self._fetch_macs(openshift_nodes, cl_name, **kwargs))

        
        return self._openshift_nodes
    
    async def _fetch_macs(self, openshift_nodes, cl_name, **kwargs):
        for vm in openshift_nodes:
            mac = await self._fetch_mac(cl_name + '-' +vm['name'], **kwargs)
            if mac:
                vm['macaddr'] = mac
            self._openshift_nodes.append(vm)

    async def _fetch_mac(self, vm, **kwargs):
        vcenter_hostname = kwargs.get('vcenter_hostname')
        session = await open_session(
            vcenter_hostname=vcenter_hostname,
            vcenter_username=kwargs.get('vcenter_username'),
            vcenter_password=kwargs.get('vcenter_password'),
            validate_certs=kwargs.get('vcenter_validate_certs', False),
        )

        # Fetch vm id
        vm_encode = '?names=' + urllib.parse.quote(vm)
        async with session.get("https://{}/api/vcenter/vm{}".format(vcenter_hostname, vm_encode)) as resp:
            _json = await resp.json()
            if len(_json) > 0 and 'vm' in _json[0]:
                vm_id = _json[0]['vm']
            else:
                return

        # Fetch nic id
        async with session.get("https://{}/api/vcenter/vm/{}/hardware/ethernet/".format(vcenter_hostname, vm_id)) as resp:
            _json = await resp.json()
            if len(_json) > 0 and 'nic' in _json[0]:
                nic = _json[0]['nic']
            else:
                return

        # Fetch nic mac address
        async with session.get("https://{}/api/vcenter/vm/{}/hardware/ethernet/{}".format(vcenter_hostname, vm_id, nic)) as resp:
            _json = await resp.json()
            return _json['mac_address']

    