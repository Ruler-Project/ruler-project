# Atera 

Splashtop may be seen in conjunction with Atera RMM usage which is embeddded, but also integrates with other remote desktop applications.

## Event logs

* EID 11707 for MsiInstaller for MSI installation
* EID 7045 in System for Service installation event
* EID 4688 Process tracking may show file transfers (B64 encoded data)

Atera may also log in Application event logs under AlphaAgent or AteraAgent

## Log files

|Log Path|Notes|Timestamp
|-|-|-|
|AgentPackageRunCommandInteractive\log.txt|Logs remote interactive commands|DD/MM/YYYY HH:MM:SS
|AgentPackageInternalPooler\log.txt|Interanl events and nothing interesting[2]|DD/MM/YYYY HH:MM:SS

## Install files

* AteraSetupLog.txt
* InstallUtil.logs
* C:\Program Files\Atera Networks 
* C:\Program Files (x86)\Atera Networks

## Registry

Registry key updated on install

* \HKEY_LOCAL_MACHINE\SOFTWARE\ATERA Networks\AlphaAgent\**

## References

* https://github.com/Velocidex/velociraptor-docs/blob/master/content/exchange/artifacts/AteraNetworks.yaml
* https://www.synacktiv.com/en/publications/legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects.html