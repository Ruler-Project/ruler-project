# Remote_Utilities

## Application specific files

|Platform|File paths|
|-|-|
|Windows|C:\Program files\remote utilities\rutserv.exe
|Windows|C:\Program files\remote utilities\rutclient.exe
|Windows|%appdata%\Remote Utilities Agent\70220\A2F2E8D838\rutserv.exe
|Windows|%appdata%\Remote Utilities Agent\70220\A2F2E8D838\rutclient.exe

## Application Logs

Logs showing connection history
C:\ProgramData\Remote Utilities\Logs\rut_log_YYYY-MM.html
C:\ProgramData\Remote Utilities\install.log

|Filename|Notes|Timestamp format|Timezone
|-|-|-|-|
|rut_log_YYYY-MM.html|Connection events, access details, File transfer activity, remote executions events|DD-MM-YYYY HH:MM:SS.SSS|UTC
 
## Registry keys

`HKEY_LOCAL_MACHINE\SOFTWARE\Usoris\Remote Utilities Host\Host\Parameters`

The encrypted Remote Utilities host password and config settings are stored within this key.

## References
[^1]: [Remote access tool or trojan? How to detect misbehaving RATs](https://redcanary.com/blog/misbehaving-rats/)
[^2]: [Remote Utilities Logging Documentation](https://www.remoteutilities.com/support/docs/logging/)