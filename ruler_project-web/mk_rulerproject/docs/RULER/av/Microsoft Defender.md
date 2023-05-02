# Microsoft Defender

## Event Logs

- Microsoft-Windows-Windows Defender*.evtx

## Application specific files

- C:\ProgramData\Microsoft\Windows Defender\Support\
- C:\Windows\Temp\MpCmdRun.log

# Configuration settings/Registry data

- HKLM\SOFTWARE\Microsoft\Windows Defender\*

# Quarantine

C:\ProgramData\Microsoft\Windows Defender\Quarantine

# References:

* https://m365internals.com/2021/08/06/dfir-windows-and-active-directory-attacks-and-persistence/
* https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-antivirus/troubleshoot-windows-defender-antivirus
* https://github.com/jklepsercyber/defender-detectionhistory-parser
* https://www.crowdstrike.com/blog/how-to-use-microsoft-protection-logging-for-forensic-investigations/
* https://www.sans.org/blog/uncovering-windows-defender-real-time-protection-history-with-dhparser