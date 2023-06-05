# Sophos

## Event Logs

* Application.evtx

## Application specific logs

* `C:\Documents and Settings\All Users\Application Data\Sophos\Sophos *\Logs\`
* `C:\ProgramData\Sophos\Sophos *\Logs\`

C:\ProgramData\Sophos\Sophos Anti-Virus\logs
- sav.txt
yyyymmdd hhmmss $message

Log files need to be converted before viewing, `iconv -f UTF-16LE -t UTF-8`

Notes: Some messages go over a line
dates/times are in UTC

Useful grep searches
"belongs to"
"User (.*) has stopped on-access scanning for this machine."
    - where use is not "NT AUTHORITY\LOCAL SERVICE"
"A threat has been blocked and quarantined."

## Registry

details to be added

## References
[^1]: [](https://community.sophos.com/kb/en-us/133912)
[^2]: [](https://support.sophos.com/support/s/article/KB-000033591?language=en_US)