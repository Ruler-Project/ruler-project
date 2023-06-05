# TightVNC

# Windows event logs

|Event Log | Event ID | Provider | Notes
|-|-|-|-
Application.evtx|256|VNC Server|Connection/disconnection including IP address ^[2]^

Application logs are likely going to be the primary investigation source as default text based logs may not be enabled.

# Application logs

Logs showing connections and file transfers. By default, logging is not enabled.

* `%ProgramData%\TightVNC\Server\Logs`^[1]^
* `%programdata%\TightVNC\tvnserver.log`^[2]^

There is a slight discrepency in the blog articles on the locations - but they agree that logging isn't enabled by default.

Timestamp format: YYYY-MM-DD HH:MM:SS

!!! info "Useful grep"

    `Incoming.*connection|Client.*connected`

# Registry keys

`HKEY_CURRENT_USER\SOFTWARE\TightVNC\vncviewer\MRU` stores history of external IP addresses connected to

`HKEY_LOCAL_MACHINE\SOFTWARE\TightVNC\vncserver` stores the encrypted password and config settings of the server

## References

1. [An exploration of artefacts of remote desktop applications on Windows](https://ro.ecu.edu.au/cgi/viewcontent.cgi?article=1166&context=adf)
1. [Remote Access Software - Forensics](https://vikas-singh.notion.site/vikas-singh/Remote-Access-Software-Forensics-3e38d9a66ca0414ca9c882ad67f4f71b)
1. [Analysis on legit tools abused in human operated ransomware](https://jsac.jpcert.or.jp/archive/2023/pdf/JSAC2023_1_1_yamashige-nakatani-tanaka_en.pdf)