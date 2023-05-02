# Symantec

Notes: Taken from an email, haven't verified

## Event logs

Symantec Endpoint Protection Client.evtx
Application.evtx

## Quarantine 

Name: Symantec Endpoint Protection Quarantine (XP)
Path: C:\Documents and Settings\All Users\Application Data\Symantec\Symantec Endpoint Protection\Quarantine\
-
Name: Symantec Endpoint Protection Quarantine
Path: C:\ProgramData\Symantec\Symantec Endpoint Protection\*\Data\Quarantine\

* Path: C:\ProgramData\Symantec\Symantec Endpoint Protection\%SEP Version%\Data\Quarantine\  
The .VBN file can be decompress with -- http://hexacorn.com/d/DeXRAY.pl 
Brian Maloneys stuff may be better: https://github.com/Beercow/SEPparser/blob/master/VBN_File_Format.html

## Application specific files

* C:\ProgramData\Symantec\Symantec Endpoint Protection\%SEP Version%\Data\AV\Logs\  

The log file is generally readable with these macros available from the SEP support team -- https://knowledge.broadcom.com/external/article/151245/interpreting-endpoint-protection-av-log.html




|-> AV
MMDDYYYY.log

Detection:
32040517030D,46,1,16,COMPUTERNAME,USERNAME,SONAR.SuspLaunch!g97,c:\windows\system32\wbem\wmic.exe,4,4,20,224,0,"",0,,0,,0,0,0,0,0,,,0,,0,0,0,0,,{GUID1},,,,,,,,,,,,,,,,,,,,,,0,,GUID2,0,,502	Microsoft Corporation	391680	2	d368bcb7934db0c53d1e7277dcb47af2b709253cbf0eee9869ee7e17ed226ea3	10.0.17134.1	1	0		0	0	2	Microsoft® Windows® Operating System	0	0,501,,,0,0,0,0,0,,,0,4,127,,,,0,32040517030D,0,,0,,0,Microsoft Windows,Microsoft Windows Production PCA 

AVManLogs
    
    - Name: Symantec Endpoint Protection Logs (XP)
        - Path: C:\Documents and Settings\All Users\Application Data\Symantec\Symantec Endpoint Protection\Logs\AV\
    - Name: Symantec Endpoint Protection Logs
        - Path: C:\ProgramData\Symantec\Symantec Endpoint Protection\*\Data\Logs\
    - Name: Symantec Endpoint Protection User Logs
        - Path: C:\Users\%user%\AppData\Local\Symantec\Symantec Endpoint Protection\Logs\
    - Name: ccSubSDK Database
        - Path: C:\ProgramData\Symantec\Symantec Endpoint Protection\*\Data\CmnClnt\ccSubSDK\
    - Name: registrationInfo.xml
        - Path: C:\ProgramData\Symantec\Symantec Endpoint Protection\*\Data\registrationInfo.xml

# References

"Contains SEPM entries, documented here: https://support.symantec.com/us/en/article.tech196455.html"
