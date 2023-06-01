# RealVNC

# Windows event logs

|Event Log | Event ID | Provider | Notes
|-|-|-|-
Application.evtx| 256|VNC Server|"connections authenticated" and includes email address or IP^[1]^

Application logs are likely going to be the primary investigation source as default text based logs may not be enabled ^[2]^

# Application logs

Debug logs are stored in the following locations:

* `%ProgramData%\RealVBC-Service\**vncserver.log**`
* `%ProgramData%\RealVBC-Service\**vncserver.log.bak**`

Timestamp is in UTC
Timestamp format: YYYY-MM-DDTHH:MM:SS.SSS

!!! info "Useful grep"

    `Connections: authenticated:|Connections: disconnected:`

Unsure whether file transfers are tracked.

# Registry keys

`HKEY_CURRENT_USER\SOFTWARE\RealVNC\vncviewer\MRU` stores history of external IP addresses connected to

`HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\vncserver` stores the encrypted password and config settings of the server

## References

1. [Remote Access Software - Forensics](https://vikas-singh.notion.site/vikas-singh/Remote-Access-Software-Forensics-3e38d9a66ca0414ca9c882ad67f4f71b)
1. [An exploration of artefacts of remote desktop applications on Windows ](https://ro.ecu.edu.au/cgi/viewcontent.cgi?article=1166&context=adf)

