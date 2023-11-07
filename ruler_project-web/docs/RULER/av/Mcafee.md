# McAfee

## Event logs

## Application specific files

* `ProgramData\McAfee\DesktopProtection` or `ProgramData\McAfee\Endpoint Security\Logs`
    * AccessProtectionLog.txt
    * EmailOnDeliveryLog.txt
    * EmailOnDemandLog.txt
    * FullScanLog.txt
    * MemoryScanLog.txt
    * OnAccessScanLog.txt
    * OnDemandScanLog.txt
    * UpdateLog.txt
    * FirewallEventMonitor.log
    * Firewall_Activity.log
    * Firewall_Debug.log

Logs can also have .bak files.

### OnAccessScanLog.txt
Timestamps appear to be in local.

Detections/scan information.

``` yaml title="Example"
M/DD/YYYY       H:MM:SS AM      Script execution blocked        DOMAIN\USER C:\Program Files (x86)\Internet Explorer\IEXPLORE.EXE   Script executed by IEXPLORE.EXE Exploit-CVE2018-8174 (Trojan)
```

!!! info "Useful Grep"
    `CVE|blocked`

### OnAccessScan_Activity.log

``` yaml title="Example"
2021-10-12 01:10:34.822Z    |Activity|oasbl               |mfetp                    |      4716|      8700|OAS                 |oasbl.cpp(2428)                         | DOMAIN\User ran PROCESS, which attempted to access FILE. The Trojan named TROJANNAME was detected and deleted.
```

### AdaptiveThreatProtection_Activity.log

``` yaml title="Example"
DATE UTC    |Activity|Orchestrator        |mfeatp                   |      6336|     11956|Action              |post_scan_actions.cpp(3511)             | Action Details::  File: regsvr32.exe , Mode: Enforce , Scanner: On-Execute Scan , Detection Name: ATP/Suspect!6e5498e81964 , Reputation: 15  [Most Likely Malicious] , ActionTaken: Would Block  Rule id: 309 , Content Version: Not Available
DATE UTC    |Activity|Orchestrator        |mfeatp                   |      6336|      8152|Action              |jcm_native.cpp(1537)                    | File C:\Datop\test.test sent successfully to ATD (Advanced Threat Defense) server.
```

!!! info "Useful Grep"
    `Detection Name: `

### FirewallEventMonitor.log

Appears to be in local time

!!! info "Python conversion"

    ```
    print ("Time,Event,IP Address,Description,Path,Message,Matched Rule")
    f  = open("FirewallEventMonitor.log", "r") 
    contents = f.read()
    contents = contents.replace("\n", "\",\"")
    contents = contents.replace(",\"\",\"", "\n")
    contents = contents.replace("Time:\t ", "")
    contents = contents.replace("Event:  ", "")
    contents = contents.replace("IP Address:  ", "")
    contents = contents.replace("Description:  ", "")
    contents = contents.replace("Path:  ", "")
    contents = contents.replace("Message:      ", "")
    contents = contents.replace("Matched Rule:  ", "")
    print (contents)
    f.close()
    ```

## Registry

## Quarantine

## References

[^1]: [https://techadminblog.com/mcafee-log-file-locations-cheat-sheet-windows/](MCAFEE LOG FILE LOCATIONS CHEAT SHEET – WINDOWS)