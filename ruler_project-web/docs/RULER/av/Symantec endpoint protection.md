# Symantec endpoint protection

Notes: Taken from an email, haven't verified

## Event logs

`Symantec Endpoint Protection Client.evtx`

`Application.evtx`

|Filename|Provider|Channel|EventID|Note
|-|-|-|-|-
|||||

## Quarantine 

* `C:\Documents and Settings\All Users\Application Data\Symantec\Symantec Endpoint Protection\Quarantine\`
* `C:\ProgramData\Symantec\Symantec Endpoint Protection\*\Data\Quarantine\`
* `C:\ProgramData\Symantec\Symantec Endpoint Protection\%SEP Version%\Data\Quarantine\`

The .VBN file can be decompress with -- http://hexacorn.com/d/DeXRAY.pl 
* [VBN File Format Windows](https://github.com/Beercow/SEPparser/wiki/VBN-File-Format-Windows)
* [VBN File Format Linux](https://github.com/Beercow/SEPparser/wiki/VBN-File-Format-Linux)

## Application specific files

* `C:\ProgramData\Symantec\Symantec Endpoint Protection\%SEP Version%\Data\AV\Logs\`

The log file is generally readable with these macros available from the SEP support team -- https://knowledge.broadcom.com/external/article/151245/interpreting-endpoint-protection-av-log.html




|-> AV
MMDDYYYY.log

``` yaml title="Example"
32040517030D,46,1,16,COMPUTERNAME,USERNAME,SONAR.SuspLaunch!g97,c:\windows\system32\wbem\wmic.exe,4,4,20,224,0,"",0,,0,,0,0,0,0,0,,,0,,0,0,0,0,,{GUID1},,,,,,,,,,,,,,,,,,,,,,0,,GUID2,0,,502	Microsoft Corporation	391680	2	d368bcb7934db0c53d1e7277dcb47af2b709253cbf0eee9869ee7e17ed226ea3	10.0.17134.1	1	0		0	0	2	Microsoft® Windows® Operating System	0	0,501,,,0,0,0,0,0,,,0,4,127,,,,0,32040517030D,0,,0,,0,Microsoft Windows,Microsoft Windows Production PCA 
```

* `AVManLogs`
* `C:\Documents and Settings\All Users\Application Data\Symantec\Symantec Endpoint Protection\Logs\AV\`
* `C:\ProgramData\Symantec\Symantec Endpoint Protection\*\Data\Logs\`
* `C:\Users\%user%\AppData\Local\Symantec\Symantec Endpoint Protection\Logs\`
* `C:\ProgramData\Symantec\Symantec Endpoint Protection\*\Data\CmnClnt\ccSubSDK\`
* `C:\ProgramData\Symantec\Symantec Endpoint Protection\*\Data\registrationInfo.xml`

## Tools

* [SEPparser](https://github.com/Beercow/SEPparser)

## References
[^1]: "Contains SEPM entries, documented here: [](https://support.symantec.com/us/en/article.tech196455.html)"
