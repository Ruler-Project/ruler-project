# Citrix GoToMyPC

## CommandLines
|EXE Filename | Comments
|-|-
|GoTo.exe | Command line string “GoTo.exe” which also include the words “–type=crashpad-handler”. This is evidence of the Chromium-based GoTo.exe starting to join or host a meeting.
|g2mstart.exe | GoToMeeting Meeting Started by Host if CommandLine strings “g2mstart.exe” or “GoTo.exe” or “g2mcomm.exe” which also include the words “Action” AND “Host”
|g2mcomm.exe | GoToMeeting Meeting Started by Host if CommandLine strings “g2mstart.exe” or “GoTo.exe” or “g2mcomm.exe” which also include the words “Action” AND “Host” 
|GoToScrUtils.exe, g2mui.exe OR G2MScrUtil64.exe | Where CommandLine includes the string “/cr”, this indicates GoTo is being used to share a screen. 


##Log File
|Filename | Comments
|-|-
|C:\Users\AppData\Roaming\GoTo\Logs\goto.log| Search for string "remoteControl" in the log to identify evidence of remote control from a third party.



## Registry

|Registry key|Notes
|-|-
|`HKEY_LOCAL_MACHINE\WOW6432Node\Citrix\GoToMyPc`|Configuration settings including registration email
|`HKEY_LOCAL_MACHINE\WOW6432Node\Citrix\GoToMyPc\GuestInvite`|Guest invites send to connect
|`HKEY_CURRENT_USER\SOFTWARE\Citrix\GoToMyPc\FileTransfer\history`|hostname of the computer making connections and location of transferred files
|`HKEY_USERS\<SID>\SOFTWARE\Citrix\GoToMyPc\FileTransfer\history`|hostname of the computer making connections and location of transferred files

"Citrix GoToMyPc application did not log any access or connection logs on the local computer."^[1]^

## References
[^1]: [An exploration of artefacts of remote desktop applications on Windows](https://dfirtnt.wordpress.com/2023/03/27/gotoforensics/)
[^2]:[GoToForensics](https://dfirtnt.wordpress.com/2023/03/27/gotoforensics/)