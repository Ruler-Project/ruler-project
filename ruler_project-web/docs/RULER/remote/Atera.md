# Atera 

Splashtop may be seen in conjunction with Atera RMM usage which is embeddded, but also integrates with other remote desktop applications.

## Event logs

|Event Log | Event ID | Provider | Notes
|-|-|-|-
|System|11707|MsiInstaller|MSI installation event|
|System|7045||Service installation
|Security|4688|Security|File transfers may be shown as 64 encoded data

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

1. https://github.com/Velocidex/velociraptor-docs/blob/master/content/exchange/artifacts/AteraNetworks.yaml
1. https://www.synacktiv.com/en/publications/legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects.html
1. [Analysis on legit tools abused in human operated ransomware](https://jsac.jpcert.or.jp/archive/2023/pdf/JSAC2023_1_1_yamashige-nakatani-tanaka_en.pdf)