# AnyDesk

Remote desktop application that can be installed or run as a portable application.

## Application specific files

File paths:
|File paths||
|-|-|
|Windows|%APPDATA%\AnyDesk\Logs\
||%ProgramData%\AnyDesk\Logs\
||C:\Windows\SysWOW64\config\systemprofile\AppData\Roaming\AnyDesk\
|Mac|~/Library/Application Support/AnyDesk/Logs/
|Linux| ~/.config/AnyDesk/Logs/

|Filename|Information|
|-|-|
|ad.trace|history, errors, system notifications. Incoming and outgoing connections|
|ad_svc.trace Log|AnyDesk service logs - history, errors, system notifications. Incoming and outgoing connections with IP addresses|
|connection_trace.txt|Incoming connections - Date/Time, status, alias and ID of AnyDesk|
|user.conf|may contain attacker username if file transfer has been attempted [5]|
|chat log|Conversation history named after the AnyDesk ID|

ad_svc.trace is only available in installed versions of AnyDesk.[1]
AnyDesk ID is related to the installation - so it's not that useful for tracking.[1]

## Log analysis

Log Timezone: UTC

|||
|-|-|
|New user data. Client-ID:| Client ID based on install.
|Connecting to|Outgoing connection
|Client-ID:|Outgoing connection
|Connection established.|Outgoing connection established
|Accept request from|Incoming connection
|Accepting the connect request.|Incoming connection established
|Session stopped.| End connection
|anynet.relay_conn| Remote connection
|"logged in from" | public IP of incoming connection (attacker computer)
|app.prepare_task|File transfer
|the volatile service has been installed| Unattended access

!!! note "Bulk grep:"

    "anynet\.relay_conn|anynet\.any_socket|app\.local_file_transfer|app\.prepare_task|app\.local_file_transfer|app\.ctrl_clip_comp|app\.backend_session|app\.ft_src_session|app\.ctrl_clip_comp"

## Analyst notes

GCAPI.DLL is the DLL associated with AnyDesk. You may find this.
AnyDesk may be used by admins but it's commonly installed by ransomware operators.

## Resources

1. https://medium.com/mii-cybersec/digital-forensic-artifact-of-anydesk-application-c9b8cfb23ab5
1. https://www.inversecos.com/2021/02/forensic-analysis-of-anydesk-logs.html
1. https://medium.com/@inginformatico/forensic-analysis-to-anydesk-forensic-artifacts-and-log-analysis-eng-3897da98324d
1. https://www.forensafe.com/blogs/anydesk.html
1. https://hatsoffsecurity.com/2022/02/28/anydesk-forensic-analysis-and-artefacts/
1. https://docs.velociraptor.app/exchange/artifacts/pages/windows.applications.anydesk/
1. https://docs.velociraptor.app/exchange/artifacts/pages/windows.applications.anydesk.logparser/
1. https://support.anydesk.com/knowledge/trace-files#trace-file-locations
1. https://support.anydesk.com/knowledge/anydesk-id-and-alias
1. https://vikas-singh.notion.site/vikas-singh/Remote-Access-Software-Forensics-3e38d9a66ca0414ca9c882ad67f4f71b
1. https://www.iblue.team/incident-response-1/anydesk-remote-access