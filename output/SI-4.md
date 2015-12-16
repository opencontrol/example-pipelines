# SI-4
## Addressed by:
 - AlienVault
 - Amazon Machine Images
 - Amazon Elastic Compute Cloud
 - HM9000


Alienvault USM for AWS monitors for attacks and indicators of potential attacks,  unauthorized local, network, and remote connections using  built-in, essential security controls and threat intelligence




## SI-4 a
- All Cloud Foundry EC2 instances will be monitored for attacks and unauthorized connections through Alienvault USM
- AlienVault USM collects and aggregates various audit logs and alerts based on abnormal activity or attacks.





## SI-4 a
- All Cloud Foundry EC2 instances will be monitored for attacks and unauthorized connections through Alienvault USM


## SI-4 b
- All Cloud Foundry EC2 instances will be monitored for attacks and unauthorized connections through Alienvault USM





## SI-4 c
- HM9000 is essential to ensuring that apps running on Cloud Foundry remain available. HM9000 restarts applications whenever the DEA running an app shuts down for any reason, when Warden kills the app because it violated a quota, or when the application process exits with a non-zero exit code
- Cloud Foundry application monitoring component HM9000 (Health Manager) has four core responsibilities:
- Monitor applications to determine their state (e.g. running, stopped, crashed, etc.), version, and number of instances. HM9000 updates the actual state of an application based on heartbeats and droplet.exited messages issued by the DEA running the application.
- Determine applications’ expected state, version, and number of instances. HM9000 obtains the desired state of an application from a dump of the Cloud Controller database.
- Reconcile the actual state of applications with their expected state. For instance, if fewer than expected instances are running, HM9000 will instruct the Cloud Controller to start the appropriate number of instances.
- Direct Cloud Controller to take action to correct any discrepancies in the state of applications.




