# LogMeIn

## Application specific log files

`C:\ProgramData\LogMeIn`

* The active log file is named LogMeIn.log
* Older logs are stored with the naming convention LMIYYYYMMDD.log (example: the log file for January 10, 2009, would be LMI20090110.log)
* Log files may contain public IP of the remote user, and information about file transfers
* Datetime format "YYYY-MM-DD HH:MM:SS.SSS", timezone UNKNOWN
* "Received file sharing ticket" - generating a download link.
    * Link is also reflected in `HKLM\Software\LogMeIn\V5\WebSvc\Shared\<random>`

!!! info "Useful grep"

    `File transfer|file sharing ticket`

## Event logs


|Event Log | Event ID | Provider | Message
|-|-|-|-
|Application.evtx|102|`LogMeIn`| XXXX has successfully logged on from IP addres X.X.X.X
|Application.evtx|202|`LogMeIn`| Remote control session started .* from IP address X.X.X.X
|Application.evtx|205|`LogMeIn`| .* ended a Remote Control Session



## References

1. [An exploration of artefacts of remote desktop applications on Windows ](https://ro.ecu.edu.au/cgi/viewcontent.cgi?article=1166&context=adf)
1. https://support.logmeininc.com/pro/help/how-to-view-logmein-event-log-files-logmein-t-host-preferences-log
1. https://jsac.jpcert.or.jp/archive/2023/pdf/JSAC2023_1_1_yamashige-nakatani-tanaka_en.pdf