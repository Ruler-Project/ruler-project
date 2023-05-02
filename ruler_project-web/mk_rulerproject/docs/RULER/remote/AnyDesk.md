# AnyDesk

Remote desktop application that can be installed or run as a portable application.

## Application specific files

File paths:
* Windows
    * %LOCALAPPDATA%\AnyDesk\Logs\
    * C:\ProgramData\AnyDesk\Logs\
    * C:\Windows\system32\config\systemprofile
* Mac
    * ~/Library/Application Support/AnyDesk/Logs/
* Linux
    * ~/.config/AnyDesk/Logs/

Files:
|Filename|Information|
|-|-|
|ad.trace|history, errors, system notifications. Incoming and outgoing connections|
|ad_svc.trace Log|history, errors, system notifications. Incoming and outgoing connections with IP addresses|
|connection_trace.txt|Incoming connections - Date/Time, status, alias and ID of AnyDesk|
|user.conf||
|chat log|Conversation history named after the AnyDesk ID|

ad_svc.trace is only available in installed versions of AnyDesk.[1]
AnyDesk ID is related to the installation - so it's not that useful for tracking.[1]

## Analysis tips
Remote connection - "anynet.relay_conn" or "logged in from" - the IP may be the connected computer. 
File transfer - "app.prepare_task"

Bulk grep:
"anynet\.relay_conn|anynet\.any_socket|app\.local_file_transfer|app\.prepare_task|app\.local_file_transfer|app\.ctrl_clip_comp|app\.backend_session|app\.ft_src_session|app\.ctrl_clip_comp"

### Resources

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