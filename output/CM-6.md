# CM-6
## Addressed by:
 - Amazon Elastic Block Store
 - S3
 - Amazon Machine Images
 - Nessus
 - Manifests
 - BOSH Stemcells


## CM-6 a
- DevOps and Security Engineers maintain the baseline configuration for VPC, EBS and AMIs.  Best practices, FISMA compliant AMIs are utilized as there are no benchmarks available.





## CM-6 a
Updates to new BOSH stemcells are located and stored within Amazon S3 http://boshartifacts.cloudfoundry.org/file_collections?type=stemcells




## CM-6 a
- DevOps and Security Engineers maintain the baseline configuration for VPC, EBS and AMIs.  Best practices, FISMA compliant AMIs, and hardened cloud formation templates are utilized as there are no benchmarks available.
- The organization uses FISMA compliant and hardened AMIs within its AWS infrastructure





## CM-6 d
Nessus and AlienVault USM Joval scans are performed at least on a quarterly basis in the event that no enhancements or upgrades are performed. Both tools meet NIST’s SCAP 1.2 requirements, satisfying OMB Mandate M-08-22 and associated procurement requirements. SCAP scans are performed weekly and monthly to ensure no unauthorized changes, enhancements or upgrades are performed.




Cloud Foundry configuration settings are documented within the deployment manifest on the 18F GitHub and Cloud Foundry sites. DevOps implements manifest templates written in yml to automate deployment of multiple applications at once and the platform within AWS with consistency and reproducibility.




BOSH Stemcells are used for the standard baseline OS images and software vulnerability management updates. Updates to new BOSH stemcells are located and stored within Amazon S3. The specifications of the current release of BOSH stemcells are located on GitHub. DevOps implements Cloud Foundry standard BOSH stemcells for baseline OS configuration.



