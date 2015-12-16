# IA-2
## Addressed by:
 - User Account and Authentication (UAA) Server
 - S3
 - Amazon Elastic Compute Cloud
 - Identity and Access Management


- The UAA is the identity management service for Cloud Foundry. Its primary role is as an OAuth2 provider, issuing tokens for client applications to use when they act on behalf of Cloud Foundry users. In collaboration with the login server, it authenticates users with their Cloud Foundry credentials, and act as a Single Sign-On (SSO) service using those credentials (or others). It has endpoints for managing user accounts and for registering OAuth2 clients, as well as various other management functions.
- All users have individually unique identifiers to access and authenticates  to the environment
- Shared or group authenticators are not utilized, with the exception of a root administrative account. There are only two authorized users from the DevOps team who has access to the root administrative account. 




## IA-2 a
Additional temporary permission are delegated with the IAM roles usually for applications that run on EC2 Instanc.es in order to access AWS resources (i.e. Amazon S3 buckets, DynamoDB data)




- Additional temporary permission are delegated with the IAM roles usually for applications that run on EC2 Instanc.es in order to access AWS resources (i.e. Amazon S3 buckets, DynamoDB data)





- All users have individually unique identifiers to access and authenticate to the AWS environment through the AWS management console.
- 18F AWS IAM users are placed into IAM roles based on their assigned roles and permissions
- Additional temporary permission are delegated with the IAM roles usually for applications that run on EC2 Instanc.es in order to access AWS resources (i.e. Amazon S3 buckets, DynamoDB data)
- All user accounts for 18F staff are maintained within the 18F AWS Environment.
- Shared or group authenticators are not utilized; Service accounts are implemented as Managed Services Accounts within AWS.




