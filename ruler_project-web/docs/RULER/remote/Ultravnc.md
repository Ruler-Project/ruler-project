# UltraVNC

## Event logs

|Event Log file| Event ID | Description | Notes
|-|-|-|-|
|Application|1|Client connected|Source is UltraVNC. Includes IP address|
|Application|3|Client disconnected|Source is UltraVNC|

## Application specific log files

`%ProgramData%\uvnc bvba\mslogon.log`

Timestamp format: DD/M/YYYY HH:MM
Local time of the target

!!! info "Useful grep"

    `Connection received|Client.*disconnected`

## References

1. [Remote Access Software - Forensics](https://vikas-singh.notion.site/vikas-singh/Remote-Access-Software-Forensics-3e38d9a66ca0414ca9c882ad67f4f71b)
