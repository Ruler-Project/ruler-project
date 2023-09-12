# Sophos

## Event Logs

* Application.evtx

|Filename|Provider|Channel|EventID|Note
|-|-|-|-|-
|||||

## Application specific logs

* `C:\Documents and Settings\All Users\Application Data\Sophos\Sophos *\Logs\`
* `C:\ProgramData\Sophos\Sophos *\Logs\`

* `C:\ProgramData\Sophos\Sophos Anti-Virus\logs`
    *  sav.txt
        * Log files need to be converted before viewing, `iconv -f UTF-16LE -t UTF-8`
        * Some messages go over a line
        * dates/times are in UTC


``` yaml title="Example"
yyyymmdd hhmmss $message
```

!!! info "Useful Grep"
    "belongs to|

    "User (.*) has stopped on-access scanning for this machine." (exclude "NT AUTHORITY\LOCAL SERVICE")

    "A threat has been blocked and quarantined."

## Registry

details to be added

## References
[^1]: [Sophos Central Endpoint and Sophos Central Server: Information on Windows log files](https://community.sophos.com/kb/en-us/133912)
[^2]: [Sophos Endpoint Security and Control: Information on Windows log files](https://support.sophos.com/support/s/article/KB-000033591?language=en_US)