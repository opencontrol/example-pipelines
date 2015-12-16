# AC-2
## Addressed by:
 - Identity and Access Management
 - Amazon Elastic Block Store
 - Amazon Elastic Compute Cloud
 - S3
 - Access Control Policies for 18F
 - Application Security Groups
 - User Account and Authentication (UAA) Server
 - Loggregator


## AC-2 d
AWS user account creation requires approval by the managing 18F project
lead and Cloud Foundry Information System Technical Point of Contact (Operating
Environment). Prior to account creation users must have at least begun the
GSA background investigative process.


## AC-2 a
AWS accounts are managed through AWS Identity and Access Management (IAM). Only users with a need to operate the AWS management console are provided individual AWS user accounts. The following types are used
User – Individual IAM accounts
System – system and application account not used for interactive access
There are no guest/anonymous, groups, or temporary user accounts in the 18F Environment


## AC-2 j
User accounts will be monitored monthly and accounts will be disabled after 90 days of inactivity; this will be a manual review process every 30 days. 18F is in the process of automating this account management process through the use of implementing AWS OSQuery to trigger alerts when user accounts are inactive of a 90 day period.
A manual review of all user accounts will be conducted on an annual basis.


## AC-2 k
18F does not allow shared/group account credentials within the AWS environment. All users have individual accounts to access the AWS environment. 18F has created specific policies that allow individual users to assume a role within the AWS environment listed in Table 9-1. AWS User Roles, Groups and Privileges.


## AC-2 c
Conditions for groups and roles membership in AWS and Cloud Foundry are based on an established need to manage and access the AWS and Cloud Foundry environments.  The user must meet the following the conditions in order for the System Owner/ Project Manager to approve a group membership request:
  - The user’s assigned role is required to access a particular group
  - The user has the requirements and understanding to assume permissions associated with the group
  - The user has completed the security role-based training
  - The user complies with any other group-specific conditions created by the system owner
Once conditions have been met, the system owner /Project manager will request access within GitHub 18F tracking and ticketing system. Once approved, the DevOps group implements the request for group and role memeberships within AWS and Cloud Foundy.


## AC-2 i
User and system access is provided only to those with an established need to access and manage the AWS and Clouf Foundry environments.
System access to local EC2 instance accounts is provided only to those with an established need to manage local services in the AWS environment. User group membership is restricted to the least privilege necessary for the user to accomplish their assigned duties.
All user accounts are issued only to those who have gained approval by 18F DevOps. Once approved, the DevOps team creates the user account and adds it to the appropriate role and organization.
18F and GSA identify authorized users of the information system and specify access rights/privileges. 18F grants access to the information system based on:
  1. a valid need-to-know/need-to-share that is determined by assigned official duties and satisfying all personnel security criteria;
  2.  Intended system usage. 18F and GSA requires proper identification for requests to establish information system accounts and approves all such requests; and
  3. Organizational or mission/business function attributes.


## AC-2 e
AWS/Cloud Foundry  user account creation requires approval by the managing 18F project lead and Information System Technical Point of Contact. Prior to account creation users must have at least begun the GSA background investigative process and complete basic security awareness training.


## AC-2 f
User account establishment, activation, modification, disablement or removal requires approval by the managing 18F project lead and Cloud Foundry Information System Technical Point of Contact (Operating Environment).
Accounts will be created, enabled, modified, disabled, and removed from AWS in accordance with 18F/GSA policies, guidelines, requirements in NIST SP 800-37, and established by the 18F Project Lead and DevOps.





## AC-2 g
- 18F has implemented AWS CloudWatch for its system account monitoring. It allows 18F to monitor AWS resources in near real-time, including Amazon EC2 instances, Amazon EBS volumes, Elastic Load Balancers, and Amazon RDS DB instances. Metrics such as CPU utilization, latency, and request counts are provided automatically for these AWS resources. It allows 18F to supply logs or custom application and system metrics, such as memory usage, transaction volumes, or error rates.


## AC-2 a
- Elastic Block Storage access is managed through the use of IAM Roles which grant IAM permissions to create, access, and manage block level storage using the following interfaces AWS Management Console and the AWS CLI.





## AC-2 i
- System access to local EC2 instance accounts is provided only to those with an established need to manage servers in the Cloud Foundry environment. User group membership is restricted to the least privilege necessary for the user to accomplish their assigned duties


## AC-2 g
- 18F has implemented AWS CloudWatch for basic monitoring of Amazon EC2 instances. Basic Monitoring for Amazon EC2 instances: Seven pre-selected metrics at five-minute frequency and three status check metrics at one-minute frequency.
- 18F has implemented Detailed Monitoring for Amazon EC2 instances: All metrics available to Basic Monitoring at one-minute frequency. Instances with Detailed Monitoring enabled allow data aggregation by Amazon EC2 AMI ID and instance type.
- 18F has implemented the use of Auto Scaling and Elastic Load Balancing where Amazon CloudWatch provides Amazon EC2 instance metrics aggregated by Auto Scaling groups and Elastic Load Balancers.
- Monitoring data is retained for two weeks, even if AWS resources have been terminated. This enables 18F to quickly look back at the metrics preceding an event of interest.
- Metrics are accessed in either the Amazon EC2 tab or the Amazon CloudWatch tab of the AWS Management Console, or by using the Amazon CloudWatch API.


## AC-2 h
- Local system user accounts will be deactivated immediately on receipt of notification of an email from the managing 18F project lead or at a future date as directed.
- User accounts will be monitored monthly and accounts will be disabled after 90 days of inactivity.


## AC-2 f
- Local system user account establishment, activation, modification, disablement or removal requires approval by the managing 18F project lead and Cloud Foundry Information System Technical Point of Contact (Operating Environment).


## AC-2 a
- Access to Amazon EC2 Linux instances are managed by the use of EC2 key pairs and using SSH to access the local instance on the individual Linux, or appliance instance. Account types include individual user and system/application user accounts. Shared or group accounts are not permitted outside of default accounts such as local Administrators or root. There are no guest/anonymous or temporary user accounts.
- Operating System user groups are documented in section 9.1 Types of Users.
- Initial Linux local root access is provided to AWS administrator account users only if they provide the key pair assigned to the Linux EC2 instance and login using SSH.


## AC-2 j
- User accounts will be monitored monthly and accounts will be disabled after 90 days of inactivity.
- Linux accounts will be monitored via scripts which query the last logon date/time of each user account and provide the results in the form of a CSV file which an authorized administrator will use for the basis of disablement.
- Application accounts will be monitored monthly and accounts will be disabled after 90 days of inactivity; this will be a manual review process, but the disablement will be automatic.





## AC-2 a
All Amazon S3 resources including buckets, objects, and related sub-resources (for example, lifecycle configuration and website configuration) are private, only the resource owner, an AWS account that created it, can access the resource through IAM policies granted to it.




## AC-2 d
The 18F/GSA Program Office specifies authorized users of the information system, group and role membership, and access authorizations (i.e., privileges) and other attributes (as required) for each account. Systems Onwers/ Project managers provide the details of what type of access is needed for an authorized authorized user.
All accounts will be documented within their respective information systems, detailing their group and role membership, and access authorizations. This documentation will be exported by DevOps and archived for up to a year from the date of account creation by the managing 18F project lead and Cloud Foundry Information System Technical Point of Contact (Operating Environment) in accordance with best business and security practices.


## AC-2 g
18F Monitors the use of all information system accounts within its environment.


## AC-2 h
18F notifies the DevOps account managers, when accounts are no longer required, users are terminated or transferred, and when individual’s information system usage or need-to-know changes.
For all environments, Account Managers, the 18F Project Manager, and/or  Information System Owner will be notified when accounts are no longer required, accounts are terminated or transferred, and when individual system usage or need to know changes. Notification will be achieved via electronic notification or other official means.


## AC-2 j
18F reviews user and system accounts for compliance with account management requirements at least on an annual basis.  Currently, system and user accounts are being monitored manually on a monthly basis and programmatically on a continuous basis.


## AC-2 k
18F establishes a process for reissuing shared/group account credentials when individuals are removed from the group. 18F utilizes its GitHub tracking and ticketing system for requests to reissue and remove individuals from group memberships within its environment.


## AC-2 c
18F establishes conditions for group and role membership within the Cloud Foundry Platform as a service and AWS environment.


## AC-2 i
18F authorizes access to its information systems based on a valid access authorization from system owners and DevOps, intended system usage within the 18F network environment, and other attributes as required by the organization or associated missions/business functions. This is documented within section 3 of 18F access control policy “Access Management”.


## AC-2 e
18F requires approvals by the 18F project lead and 18F system owners for requests to create information system accounts. All accounts will be documented within the 18F Github Ticketing and Tracking systems with their respective information systems, detailing their group, role membership, and access authorizations.


## AC-2 f
18F creates, enables, modifies, disables, and removes information system accounts in accordance with the 18F access control policy and approvals from 18F DevOps.


## AC-2 b
The 18F DevOps team is the assgiend account managers for all information system accounts. Account managers are assigned for account groups in all environments, determined by the Project Manager and/or the Information System Owner.





## AC-2 a
- Cloud Foundry uses Application security groups (ASGs) to act as virtual firewalls to control outbound traffic from the applications in the deployment. A security group consists of a list of network egress access rules.
- An administrator can assign one or more security groups to a Cloud Foundry deployment or to a specific space in an org within a deployment.
- Cloud Foundry user, organization, and application roles and security groups are documented in section 9.3 Types of Users. 





## AC-2 g
{Missing}


## AC-2 Cloud Foundry user and role accounts are managed and maintained through the UAA Command Line Interface (UAAC). Cloud Foundry uses role-based access control with each role granting permissions in either an organization or an application space. The Following types are used
['Org Manager', 'Org Auditor', 'Space Manager', 'Space Developer', 'Space Auditor']

## AC-2 a


## AC-2 j
User accounts will be monitored monthly and accounts will be disabled after 90 days of inactivity; this will be a manual review process every 30 days, but the disablement will be automatic.
A manual review of all user accounts will be conducted on an annual basis


## AC-2 k
The Cloud Foundry platform utilizes role based access controls (RBAC) for group membership within the platform and does not issue shared/group account credentials.


## AC-2 c
Conditions for groups and roles membership in AWS and Cloud Foundry are based on an established need to manage and access the AWS and Cloud Foundry environments.  The user must meet the following the conditions in order for the System Owner/ Project Manager to approve a group membership request:
  - The user’s assigned role is required to access a particular group
  - The user has the requirements and understanding to assume permissions associated with the group
  - The user has completed the security role-based training
  - The user complies with any other group-specific conditions created by the system owner
Once conditions have been met, the system owner /Project manager will request access within GitHub 18F tracking and ticketing system. Once approved, the DevOps group implements the request for group and role memeberships within AWS and Cloud Foundy.


## AC-2 i
User and system access is provided only to those with an established need to access and manage the AWS and Clouf Foundry environments.
System access to local EC2 instance accounts is provided only to those with an established need to manage local services in the AWS environment. User group membership is restricted to the least privilege necessary for the user to accomplish their assigned duties.
All user accounts are issued only to those who have gained approval by 18F DevOps. Once approved, the DevOps team creates the user account and adds it to the appropriate role and organization.
18F and GSA identify authorized users of the information system and specify access rights/privileges. 18F grants access to the information system based on:
  1. a valid need-to-know/need-to-share that is determined by assigned official duties and satisfying all personnel security criteria;
  2.  Intended system usage. 18F and GSA requires proper identification for requests to establish information system accounts and approves all such requests; and
  3. Organizational or mission/business function attributes.


## AC-2 e
AWS/Cloud Foundry user account creation requires approval by the managing 18F project lead and Information System Technical Point of Contact. Prior to account creation users must have at least begun the GSA background investigative process and complete basic security awareness training.


## AC-2 f
User account establishment, activation, modification, disablement or removal requires approval by the managing 18F project lead and Cloud Foundry Information System Technical Point of Contact (Operating Environment).
Accounts will be created, enabled, modified, disabled, and removed from AWS in accordance with 18F/GSA policies, guidelines, requirements in NIST SP 800-37, and established by the 18F Project Lead and DevOps.





## AC-2 g
- 18F uses Steno for Cloud Foundry account logging. Steno is a shared logging service between the DEA, Cloud Controller and Cloud Foundry components that share a common interface for configuring logs. 
- Loggregator also referred to as Doppler in newer versions of cf, is the Cloud Foundry component responsible for logging, and provides a stream of log output from 18F applications and from Cloud Foundry system components that interact with applications during updates and execution. Loggregator allows users to:
  - Tail their application logs.
  - Dump a recent set of application logs (where recent is a configurable number of log packets).
  - Continually drain their application logs to 3rd party log archive and analysis services (i.e Splunk, Syslog, Alien Vault USM).
  - (Operators and administrators only) Access the firehose, which includes the combined stream of logs from all apps, plus metrics data from CF components
- Syslog and Syslog_aggregator are used for system logging and provide a mechanism to forward system logs via syslog to a syslog server.
- /healthz and /varz are HTTP endpoints provided by Cloud Foundry components used for system monitoring. The endpoints can be polled to obtain information on a job’s health and state. 
  - /healthz is a basic check that returns an ‘ok’ message if the job’s running happily.
  - /varz provides more detailed information about the running job. For example, polling /varz on the uaa server returns data about java memory usage (amongst other things).
- The Collector is used for monitoring and metrics by collecting data from the /health and /var endpoints. It dynamically learns about Cloud Foundry components and polls them for monitoring data and provides options to send monitoring data to AWS CloudWatch, Datadog, graphite and TSDB.
- New components have been added to the most recent version of Cloud Foundry 
  - CF components emit metrics (e.g. the router emits HTTP metrics, such as the time taken to service a request).
  - These metrics are sent to agents running on the VMs called ‘metron’.
  - The metron agents forward these metrics, along with application logs, to ‘doppler’ servers.
  - The doppler servers collect and buffer the data.
  - The loggregator traffic controllers expose a new websocket endpoint ‘/firehose’.
  - When you connect to /firehose, a connection is opened up to all doppler servers.
  - All logs and metrics for all apps and components are then streamed down the connection.




