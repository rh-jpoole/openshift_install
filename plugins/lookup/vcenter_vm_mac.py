#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib.parse

from ansible.plugins.lookup import LookupBase
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import open_session

class LookupModule(LookupBase):

    def run(self, vm, variables=None, **kwargs):
        import asyncio

        current_loop = asyncio.get_event_loop_policy().get_event_loop()
        current_loop.run_until_complete(self._run(vm, variables, **kwargs))

        return self._ret

    async def _run(self, vm, variables=None, **kwargs):
        vcenter_hostname = kwargs.get('vcenter_hostname')
        session = await open_session(
            vcenter_hostname=vcenter_hostname,
            vcenter_username=kwargs.get('vcenter_username'),
            vcenter_password=kwargs.get('vcenter_password'),
            validate_certs=kwargs.get('vcenter_validate_certs', False),
        )

        # Fetch vm id
        vm_encode = '?names=' + urllib.parse.quote(vm[0])
        async with session.get("https://{}/api/vcenter/vm{}".format(vcenter_hostname, vm_encode)) as resp:
            _json = await resp.json()
            if len(_json) > 0 and 'vm' in _json[0]:
                vm_id = _json[0]['vm']
            else:
                self.ret = []
                return

        # Fetch nic id
        async with session.get("https://{}/api/vcenter/vm/{}/hardware/ethernet/".format(vcenter_hostname, vm_id)) as resp:
            _json = await resp.json()
            if len(_json) > 0 and 'nic' in _json[0]:
                nic = _json[0]['nic']
            else:
                self.ret = []
                return

        # Fetch nic mac address
        async with session.get("https://{}/api/vcenter/vm/{}/hardware/ethernet/{}".format(vcenter_hostname, vm_id, nic)) as resp:
            _json = await resp.json()
            self._ret = [_json['mac_address']]