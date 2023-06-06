# Microsoft Defender

## Event Logs

|Filename|Provider|Channel|EventID|Note
|-|-|-|-|-
|Microsoft-Windows-Windows Defender*.evtx|?|?|1006|Malware detected
|Microsoft-Windows-Windows Defender*.evtx|?|?|1007|Malware detected (action taken)
|Microsoft-Windows-Windows Defender*.evtx|?|?|1008|Malware detected (action failed)
|Microsoft-Windows-Windows Defender*.evtx|?|?|1009|Quarantine restore
|Microsoft-Windows-Windows Defender*.evtx|?|?|1011|Quarantine delete
|Microsoft-Windows-Windows Defender*.evtx|?|?|1015|Behavior detected



## Application specific files

* `C:\ProgramData\Microsoft\Windows Defender\Support\`
* `C:\Windows\Temp\MpCmdRun.log`
* `...?\detections.log`


# Configuration settings/Registry data

- HKLM\SOFTWARE\Microsoft\Windows Defender\*

# Quarantine

`C:\ProgramData\Microsoft\Windows Defender\Quarantine`

# References:
[^1]: [Why Are Windows Defender AV Logs So Important And How To Monitor Them With Azure Sentinel?](https://m365internals.com/2021/07/05/why-are-windows-defender-av-logs-so-important-and-how-to-monitor-them-with-azure-sentinel/)
[^2]: [Review event logs and error codes to troubleshoot issues with Microsoft Defender Antivirus](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/troubleshoot-windows-defender-antivirus)
[^3]: [DetectionHistory Parser v1.0.1](https://github.com/jklepsercyber/defender-detectionhistory-parser)
[^4]: [Mind the MPLog: Leveraging Microsoft Protection Logging for Forensic Investigations](https://www.crowdstrike.com/blog/how-to-use-microsoft-protection-logging-for-forensic-investigations/)
[^5]: https://www.sans.org/blog/uncovering-windows-defender-real-time-protection-history-with-dhparser

[^6]: [](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-microsoft-defender-antivirus?view=o365-worldwide)