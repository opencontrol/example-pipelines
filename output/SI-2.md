# SI-2
## Addressed by:
 - Nessus
 - OWASP Zap
 - BOSH Stemcells


## SI-2 a
- Flaw identification is accomplished via Nessus, AlienVault USM, OWASP Zap, and Code Climate static code analysis.  Nessus is a vulnerability, configuration, and compliance scanner.





## SI-2 a
OWASP Zap (Web Application scanner and penetration test tool) for monthly scanning of all web applications that reside within Cloud Foundry. Upon implementation of the application, authenticated (Web Application) scans will be run on Test instances of the code every major release and minor releases when the release contains a change with a potential security impact.  OWASP Zap reports are reviewed after each scan and appropriate actions taken on discovery of vulnerabilities.





Cloud Foundry manages software vulnerability using releases and BOSH stemcells. New Cloud Foundry releases located at https:/github.com/cloudfoundry/cf-release, are created with updates to address code issues, while new stemcells are created with patches for the latest security fixes to address any underlying operating system issues.



