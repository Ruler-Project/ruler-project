# Connectwise/Screenconnect

Currently named Connectwise, but old Screenconnect name still persists

## Event logs

|Event Log | Event ID | Provider | Message
|-|-|-|-
|Application.evtx|100|`ScreenConnect Client (<random>)`* or `Screenconnect`| Cloud account administrator connected
|Application.evtx|101|`ScreenConnect Client (<random>)`* or `Screenconnect`| Cloud account administrator disconnected
|Application.evtx|201|`ScreenConnect Client (<random>)`* or `Screenconnect`| Transferred files with action 'Transfer'
|Application.evtx|?|`ScreenConnect Client (<random>)`* or `Screenconnect`| "Executed command of length" (but no command)

* No Evtxecmd map can cover this due to engineering decisions. The result will be in the Payload column.

## References
[^1]: [Remote Access Software - Forensics](https://vikas-singh.notion.site/vikas-singh/Remote-Access-Software-Forensics-3e38d9a66ca0414ca9c882ad67f4f71b)
[^2]: [Establishing Connections: Illuminating Remote Access Artifacts in Windows](https://youtu.be/0qSWfbti4yM?list=PLfouvuAjspToNFRwt0ssrvaSMI11RcSgp)
[^3]: [Analysis on legit tools abused in human operated ransomware](https://jsac.jpcert.or.jp/archive/2023/pdf/JSAC2023_1_1_yamashige-nakatani-tanaka_en.pdf)
[^4]: [RMM – ScreenConnect: Client-Side Evidence](https://dfirtnt.wordpress.com/2023/07/14/rmm-screenconnect-client-side-evidence/)