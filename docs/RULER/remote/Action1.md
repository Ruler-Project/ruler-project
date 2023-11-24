# Action1 RMM

Remote Management and Monitoring application.

## Executables

|Platform|File paths|
|-|-|
|Windows|C:\Windows\Action1\action1_agent.exe
|Windows|C:\Windows\Action1\action1_remote.exe

## Application logs

|Filename|Notes|Timestamp format|Log Timezone
|-|-|-|-|
|C:\Windows\Action1\Action1_log_[date-time].log|history, errors, system notifications. Incoming and outgoing connections.  |YYMMDD HH:MM:SS|UTC

|Search term|Description|
|-|-|
|[REMOTE_SESSION_CONNECT]| Remote session established|
|[Session::Disconnect]| Remote session closed|
|Loaded instance Deploy App:| Action1 used to deploy/install additional software|

 
## Analyst notes
- action1_remote.exe is evidence of remote control
- action1_agent.exe is the basic service binary
  

## Resources
[^1]: [RMM – action1-client-side-evidence](https://dfirtnt.wordpress.com/2023/08/23/rmm-action1-client-side-evidence/)