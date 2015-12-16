# CM-8
## Addressed by:
 - AWS Config
 - Amazon Elastic Compute Cloud
 - VisualOps
 - AlienVault
 - S3


## CM-8 a
- AWS Config provides a detailed inventory of all 18F AWS resources and their current configuration, and continuously records configuration changes (e.g., the value of tags on Amazon EC2 instances, ingress/egress rules of security groups, and Network ACL rules for VPCs).
- Using AWS Config, 18F can export a complete inventory of AWS resources with all configuration details, determine how a resource was configured at any point in time, and get notified via Amazon SNS when the configuration of a resource changes.
- AWS Config can provide configuration snapshots, which is a point-in-time capture of all 18F resources and their configurations. Configuration snapshots are generated on demand via the AWS CLI, or API, and delivered to an Amazon S3 bucket that is specified





## CM-8 a
- AWS Config provides a detailed inventory of all 18F AWS resources and their current configuration, and continuously records configuration changes (e.g., the value of tags on Amazon EC2 instances, ingress/egress rules of security groups, and Network ACL rules for VPCs).





## CM-8 a
- The VisualOps Cloud management tool is used to provide a visual, real-time and automated representation of the AWS infrastructure and applications within the environment.





AlienVault USM is currently deployed and used by 18F to facilitate asset management, along with other operations activities, on a real-time ongoing basis.




## CM-8 a
AWS Config can provide configuration snapshots, which is a point-in-time capture of all 18F resources and their configurations. Configuration snapshots are generated on demand via the AWS CLI, or API, and delivered to an Amazon S3 bucket that is specified



