# Kaspersky

## Event logs

- Provider: avp
- Channel: Kaspersky Event Log
- Messages of interest
    - {"EventData":{"Data":"Event type:     Active threat detected. Advanced Disinfection should be started\nApplication\\Name:     Kaspersky Endpoint Security 10 for Windows\nApplication\\Path:     C:\\Program Files (x86)\\Kaspersky Lab\\Kaspersky Endpoint Security 10 for Windows SP2\\\nUser:     USERNAME (Active user)\nComponent:     Protection\n","Binary":""}}
    - {"EventData":{"Data":"Event type:     Malicious object detected\nUser:     USERNAME (Active user)\nObject:     System Memory\nObject\\Type:     File\nObject\\Path:     System Memory\nObject\\Name:     System Memory\nResult\\Description:     Detected\nResult\\Type:     Trojan\nResult\\Name:     Trojan.Multi.GenAutorunReg.a\nResult\\Threat level:     High\nResult\\Precision:     Exactly\nReason:     Local databases\nDatabase release date:     21/02/2021 10:21:00 p.m.\n","Binary":""}}

## Windows Registry

  - Have not identified anything other than settings related to detections
  
## On-device logs

  - Have not looked yet

## Quarantine


## References