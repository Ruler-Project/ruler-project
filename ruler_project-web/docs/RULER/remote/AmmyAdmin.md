# AmmyAdmin


## Application logs

|Log path|Notes|Timestamp|
|-|-|-|
%ProgramData%\AMMYY\access.log|Connection, disconnection, amount of data transferred|YYYYMMDD-HH:MM:SS.SSSSSS*

\* Assumption here about the month and day ordering based on this reference [1]
IP Addresses are for AmmyAdmin

## Log analysis

Log Timezone: Local

|Search term|Description|
|-|-
|Passed authorization remoteId=|Start of session, remote ID generated on Source host
|ENDED  authorized session, bytes recv/send| End of session|

## References

1. https://vikas-singh.notion.site/vikas-singh/Remote-Access-Software-Forensics-3e38d9a66ca0414ca9c882ad67f4f71b