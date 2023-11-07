# Webroot

## Event logs

Unknown

## Application specific logs

* `C:\ProgramData\WRData`

    - WRLog.log - scan results (inlcuding hashes for detections).
    - timestamps are in local time (DDD dd-mm-yyyy hh:mm:ss.ssss)

## Registry

Data in the registry is stored here[^2]:

* `SOFTWARE --> WOW6432Node\WRData\`
* Contains execution and monitoring times as well as hashes and detection names

## References
[^1]: [WSABLogs User Guide](https://download.webroot.com/WSABLogs_User_Guide.pdf)
[^2]: [webrool.pl](https://github.com/randomaccess3/Regripper-Plugins/blob/main/webroot.pl)