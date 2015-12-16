# CM-2
## Addressed by:
 - Manifests
 - Amazon Elastic Compute Cloud
 - AWS Service Catalog
 - AlienVault
 - Cloud Formation
 - Amazon Machine Images
 - Amazon Elastic Block Store


Configure UAA clients and users using a standard BOSH manifest for cloud Foundry Deployment, Limit and manage these clients and users as you would any other kind of privileged account.




DevOps maintain baseline configurations for VPC, EBS, EC2 instances and AMIs. AWS Cloud Formation templates help 18F maintain a strict configuration management scheme of the cloud infrastructure. If an error or misconfiguration of the infrastructure or associated security mechanism (security groups, NACLs) is detected, the administrators can analyze the current infrastructure templates; compare with previous versions, and redeploy the configurations to a known and approved state.




AWS Service Catalog allows 18F to centrally manage commonly deployed IT services, and helps achieve consistent governance and meet compliance requirements, while enabling users to quickly deploy only the approved IT services they need.




AlienVault USM for AWS is provided by the vendor as a secure hardened AMI image that is deployed using a cloudformation template.




- DevOps maintain baseline configurations for VPC, EBS, EC2 instances and AMIs. AWS Cloud Formation templates help 18F maintain a strict configuration management scheme of the cloud infrastructure. If an error or misconfiguration of the infrastructure or associated security mechanism (security groups, NACLs) is detected, the administrators can analyze the current infrastructure templates; compare with previous versions, and redeploy the configurations to a known and approved state.
- AWS Cloud Formation templates are the approved baseline for all changes to the infrastructure and simplify provisioning and management on AWS. They provide an automated method to assess the status of an operational infrastructure against an approved baseline.





- Linux instances are based on the standard AWS AMI images with configuration to GSA requirements based on secure configurations documented in CM-6.
- AlienVault USM for AWS is provided by the vendor as a secure hardened AMI image that is deployed using a cloudformation template.
- NIST guidance, best practices, CIS benchmarks along with standard and hardened Operating System AMIs have been utilized.
- DevOps maintain copies of the latest Production Software Baseline, which includes the following elements: Manufacturer, Type, Version number, Software, Databases, and Stats.





DevOps maintain baseline configurations for VPC, EBS, EC2 instances and AMIs. AWS Cloud Formation templates help 18F maintain a strict configuration management scheme of the cloud infrastructure. If an error or misconfiguration of the infrastructure or associated security mechanism (security groups, NACLs) is detected, the administrators can analyze the current infrastructure templates; compare with previous versions, and redeploy the configurations to a known and approved state.



