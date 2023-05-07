# Splashtop

Commonly seen installed alongside Atera RMM.

## Event logs

|Event Log file| Event ID | Description | Notes
|-|-|-|-|
|Splashtop-Splashtop Streamer-Remote Session%4Operational.evtx|1000| Session connection| SPID and source name which may be a computer name|
|Splashtop-Splashtop Streamer-Remote Session%4Operational.evtx|1001| Session disconnection| provides session duration|
|Splashtop-Splashtop Streamer-Remote Session%4Operational.evtx|???| A file was transferred during the Splashtop remote session| Contains client hostanmhostname and filename transferred|

Service install for "SplashtopRemoteService"

## Application logs

Splashtop website indicates that it has logging available through the web platform, which may not be useful in an intrusion where the threat actor has installed their own version of Splashtop [2]
* Session logs
* File transfer logs
* Chat session logs
* History logs
* Event logs


|Log file|Notes|Timestamp
|-|-|-
|%PROGRAMDATA%\Splashtop\Temp\log\FTCLog.txt|file transfers, user account, IP of the client|YYYY-MM-DD HH:MM:SS|
|C:\Program Files (x86)\Splashtop\Splashtop Remote\Server\log\agent_log.txt| Debug log file of the SplashTop agent||
|C:\Program Files (x86)\Splashtop\Splashtop Remote\Server\log\SPLog.txt| general logs of the agent. Connection start, hostname, user display name, IP address of the client. File transfer events, chat functionality.|mmm d HH:MM:SS (no year)
|C:\Program Files (x86)\Splashtop\Splashtop Remote\Server\log\svcinfo.txt|Internal application events|
|C:\Program Files (x86)\Splashtop\Splashtop Remote\Server\log\sysinfo.txt|Internal application events|
|Chat functionality??|parties involved in the chat|\[HH:MM\]

Splashtop Gateway:

* %programfiles%\Splashtop\Splashtop Remote\Splashtop Gateway\log
* %programfiles(x86)%\Splashtop\Splashtop Remote\Splashtop Gateway\log 

Splashtop Streamer:

|Platform|Log location
|-|-
Windows | C:\Program Files (x86)\Splashtop\Splashtop Remote\Server\SPLog.*
Mac | /Users/Shared/SplashtopStreamer/SPLog.txt
Mac | ~/Library/Logs/SPLog.txt

## Install files:

* SplashtopStreamer.*.exe
* unpack,.log
* PreVer.log

## Registry

`HKLM\SOFTWARE\WOW6432Node\Splashtop Inc.\Splashtop Remote Server\ClientInfo\*`

Possible values of interest:

* Client_DisplayName
* UDID
* DeviceName
* Client_IP

## References

1. https://www.synacktiv.com/en/publications/legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects.html
1. https://support-splashtopbusiness.splashtop.com/hc/en-us/articles/360001692992
1. https://jsac.jpcert.or.jp/archive/2023/pdf/JSAC2023_1_1_yamashige-nakatani-tanaka_en.pdf