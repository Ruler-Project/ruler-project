# TeamViewer

## Application logs

Log path: `C:\Program Files\Teamviewer` or `C:\Program Files(x86)\Teamviewer`

|Path|Timestamp format|Notes
|-|-|-
|C:\program files(x64)\teamviewer\connections_incoming.txt|DD-MM-YYYY HH:MM:SS (UTC)|TeamViewer ID, remote computer (display name field), time duration, connection type and unique connection ID.
|C:\program files(x64)\teamviewer\TeamViewer##_Logfile.log|YYYY/HH/DD HH:MM:SS.SSS (timezone included)|complete history of incoming and outgoing connection
|%appdata%\Teamviewer\connections.txt|?|successful outgoing connection details
|%appdata\Teamviewer\TeamViewer##_Logfile.log|YYYY/MM/DD HH:MM:SS.SSS (timezone unknown)|General software information log

Logs are mostly TSV

Teamviewer ID is unique per device.

!!! info "Log format^[5]^"
    
    Outgoing (connections.txt):
        
        <Slave ID> <Start Date> <Start Time> <End Date> <End Time> <Current Windows User> <Connection Type> <Unique Session ID>
    
    Incoming (Connections_incoming.txt):
        
        <Controller ID> <Controller Display Name> <Start Date> <Start Time> <End Date> <End Time> <Current Windows User> <Connection Type> <Unique Session ID>

!!! info "Useful grep"

    To get the public IP look for the following in TeamViewer##_logfile.log:

    `punch received a=`

    Other searches:

    `Send file|Write file|Download from|AddParticipant|ParticipantRemoved|SessionTerminate|RunAutheticationMethod`

## References
[^1]: [TeamViewer Forensics](https://www.systoolsgroup.com/forensics/teamviewer/)
[^2]: [Digital Forensic Artifact of TeamViewer Application](https://medium.com/mii-cybersec/digital-forensic-artifact-of-teamviewer-application-cfd6290dc0a7?source=rss----5aebc5961dd0---4)
[^3]: [Blog #27: IPv6 in TeamViewer(v15) part [^1]: [EN]](https://kyl3song.github.io/artifacts/IPv6-in-TeamViewer(v15)-part-1.-EN/)
[^4]: [Blog #27: IPv6 in TeamViewer(v15) part 2. [EN]](https://kyl3song.github.io/artifacts/IPv6-in-TeamViewer(v15)-part-2.-EN/)
[^5]: [An exploration of artefacts of remote desktop applications on Windows](https://ro.ecu.edu.au/cgi/viewcontent.cgi?article=1166&context=adf)
[^6]: [Remote Access Software - Forensics](https://vikas-singh.notion.site/vikas-singh/Remote-Access-Software-Forensics-3e38d9a66ca0414ca9c882ad67f4f71b)
[^7]: [Remote Desktop Software as a forensic resource](https://www.researchgate.net/publication/359220574_Remote_Desktop_Software_as_a_forensic_resource)
[^8]: [Analysis on legit tools abused in human operated ransomware](https://jsac.jpcert.or.jp/archive/2023/pdf/JSAC2023_1_1_yamashige-nakatani-tanaka_en.pdf)
[^9]: [LEGITIMATE RATS: A COMPREHENSIVE FORENSIC ANALYSIS OF THE USUAL SUSPECTS
](https://www.synacktiv.com/en/publications/legitimate-rats-a-comprehensive-forensic-analysis-of-the-usual-suspects.html)