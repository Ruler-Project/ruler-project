# Level RMM

Remote Management and Montirong application.

## Application specific files

|Platform|File paths|
|-|-|
|Windows|C:\Windows\Temp\level-windows-amd64.exe
|Windows|C:\Windows\Temp\level-windows-amd32.exe
|Windows|C:\Program Files\Level\level.exe

|Filename|Notes|Timestamp format|Timezone
|-|-|-|-|
|level.log|history, errors, system notifications. Incoming and outgoing connections. Found at C:\Program Files *\Level\ |YYYY-MM-DD HH:MM:SS.SSS|UTC

## Log analysis

|Search term|Description|
|-|-|
|"Action":"terminal/start"| Remote terminal sessions established|
| "agent_id":| Client ID based on install.|
|"Capturing whole desktop" | logged in level.log when desktop remote screen viewing occurs.|
 
## Analyst notes

 Level uses OSQuery for recurring recon of system information. Hunting for osqueryi.exe execution where signer is “Level Software” and parent process is level.exe
 Level also uses winpty-agent.exe when invoking the remote termal sessions capability.

## Resources
[^1]: [RMM – Level.io: Forensic Artifacts and Evidence](https://dfirtnt.wordpress.com/2023/09/05/rmm-level-io-forensic-artifacts-and-evidence/)