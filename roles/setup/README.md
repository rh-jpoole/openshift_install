# Setup role

This role prepare the environment for the run of the openshift-install agent installation.

This role install following dependencies:
 - openshift-install
 - oc

as binary files from official Openshift URLs.

Install dependencies for the agent based installation:
 - nmstate

Dependencies for the dependent collections:
 - python3-infoblox (infoblox)
 - python3-aiohttp (vmware)
