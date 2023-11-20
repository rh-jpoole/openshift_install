# Setup role

This role prepare the environment for the run of the `openshift-install` agent.

This role install following dependencies:
 - openshift-install
 - oc

It downloads `oc` binary from official Openshift website. Then based on the input parameters
it either download `openshift-install` binary or extract it from the registry.

Install dependencies for the agent based installation:
 - nmstate

Dependencies for the dependent collections:
 - python3-infoblox (infoblox)
 - python3-aiohttp (vmware)
