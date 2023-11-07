# Kaspersky

## Event logs

|Filename|Provider|Channel|EventID|Note
|-|-|-|-|-
|?|avp|Kaspersky Event Log|?|?
|?|OnDemandScan|Kaspersky Security|3203|Threat detected
|?|Real-Time File Protection|Kaspersky Security|3203|Threat detected (Real-time file protection)

### Messages of interest

``` yaml title="Active threat detected"
- Event type:     Active threat detected. Advanced Disinfection should be started
- Application Name:     Kaspersky Endpoint Security 10 for Windows
- Application Path:     C:\\Program Files (x86)\\Kaspersky Lab\\Kaspersky Endpoint Security 10 for Windows SP2
- User:     USERNAME (Active user)
- Component:     Protection
```

``` yaml title="Malicious object detected"
- Event type:     Malicious object detected
- User:     USERNAME (Active user)
- Object:     System Memory
- Object Type:     File
- Object Path:     System Memory
- Object Name:     System Memory
- Result Description:     Detected
- Result Type:     Trojan
- Result Name:     Trojan.Multi.GenAutorunReg.a
- Result Threat level:     High
- Result Precision:     Exactly
- Reason:     Local databases
- Database release date:     21/02/2021 10:21:00 p.m.
```
  
## Application specific files

## Registry

Have not identified anything other than settings related to detections. Further research required.

## Quarantine

Found online: [^1]

Windows XP: %ALLUSERSPROFILE%\Application Data\Kaspersky Lab\AVP\14.0.0\QB
Windows Vista/7/8: %ALLUSERSPROFILE%\Kaspersky Lab\AVP\14.0.0\QB.

## References
[^1]: [Tip Of The Week: Quarantining Suspicious Files](https://www.kaspersky.com.au/blog/tip-of-the-week-quarantining-suspicious-files/3544/)
[^2]: [Kaspersky Anti-virus](https://support.kaspersky.com/KAV/21.3/en-US/87342.htm)
