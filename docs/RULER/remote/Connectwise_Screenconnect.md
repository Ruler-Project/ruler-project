# Connectwise/Screenconnect

Currently named Connectwise, but old Screenconnect name still persists

## Event logs

|Event Log | Event ID | Provider | Message
|-|-|-|-
|Application.evtx|100|`ScreenConnect Client (<random>)`* or `Screenconnect`| Cloud account administrator connected
|Application.evtx|101|`ScreenConnect Client (<random>)`* or `Screenconnect`| Cloud account administrator disconnected
|Application.evtx|201|`ScreenConnect Client (<random>)`* or `Screenconnect`| Transferred files with action 'Transfer'
|Application.evtx|200|`ScreenConnect Client (<random>)`* or `Screenconnect`| "Executed command of length" (but no command is provided)

* There is also a Service install (EID: 7045, System evtx) on screenconnect install.
* No Evtxecmd map can cover this due to engineering decisions. The result will be in the Payload column.
* Previous versions had all of the above events in EventID == 1. However, more recent testing showed 100, 101, and 201. The 4th row may still be Event ID == 1. Additional testing needed.

## Application files

* User config - `C:\Windows\SysWOW64\config\systemprofile\AppData\Local\ScreenConnect Client (<random>)\user.config`
* `%PROGRAMDATA%\ScreenConnect Client (<random>)\`
* `%PROGRAMFILES(x86)%\ScreenConnect Client (<random>)\`
* `%SYSTEMROOT%\temp\screenconnect\[version]\`
* `%USERPROFILE%\Documents\ConnectWiseControl\captures\`
* File execution - `%USERPROFILE%\Documents\ConnectWiseControl\Temp\malware.exe`
* File Transfers - `%USERPROFILE%\Documents\ConnectWiseControl\Files\`
* Scripts - `%SYSTEMROOT%\temp`

## Useful notes

If you see https://<subdomain>.screenconnect.com, this is the username of the account.^[4]^ ^[5]^

## References
[^1]: [Remote Access Software - Forensics](https://vikas-singh.notion.site/vikas-singh/Remote-Access-Software-Forensics-3e38d9a66ca0414ca9c882ad67f4f71b)
[^2]: [Establishing Connections: Illuminating Remote Access Artifacts in Windows](https://youtu.be/0qSWfbti4yM?list=PLfouvuAjspToNFRwt0ssrvaSMI11RcSgp)
[^3]: [Analysis on legit tools abused in human operated ransomware](https://jsac.jpcert.or.jp/archive/2023/pdf/JSAC2023_1_1_yamashige-nakatani-tanaka_en.pdf)
[^4]: [RMM – ScreenConnect: Client-Side Evidence](https://dfirtnt.wordpress.com/2023/07/14/rmm-screenconnect-client-side-evidence/)
[^5]: [Configure ConnectWise Control for Single Sign-On](https://docs.citrix.com/en-us/citrix-secure-private-access/downloads/connect-wise-control.pdf)
