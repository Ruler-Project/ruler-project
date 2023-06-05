# TeamViewer

## Application specific log files

Log path: `C:\Program Files\Teamviewer` or `C:\Program Files(x86)\Teamviewer`

|Path|Timestamp format|Notes
|-|-|-
|C:\program files(x64)\teamviewer\connections_incoming.txt|DD-MM-YYYY HH:MM:SS (UTC)|TeamViewer ID, remote computer (display name field), time duration, connection type and unique connection ID.
|C:\program files(x64)\teamviewer\TeamViewer##_Logfile.log|YYYY/HH/DD HH:MM:SS.SSS (timezone included)|complete history of incoming and outgoing connection
|%appdata%\Teamviewer\connections.txt|?|successful outgoing connection details
|%appdata\Teamviewer\TeamViewer##_Logfile.log|YYYY/MM/DD HH:MM:SS.SSS (timezone unknown)|General software information log

Logs are mostly TSV

Teamviewer ID is unique per device.

!!! info "Useful grep"

    To get the public IP look for the following in TeamViewer##_logfile.log:

    `punch received a=`

    End of session:

    `ParticipantRemoved`

## References 

1. [TeamViewer Forensics](https://www.systoolsgroup.com/forensics/teamviewer/)
1. [Digital Forensic Artifact of TeamViewer Application](https://medium.com/mii-cybersec/digital-forensic-artifact-of-teamviewer-application-cfd6290dc0a7?source=rss----5aebc5961dd0---4)
1. [Blog #27: IPv6 in TeamViewer(v15) part 1. [EN]](https://kyl3song.github.io/artifacts/IPv6-in-TeamViewer(v15)-part-1.-EN/)
1. [Blog #27: IPv6 in TeamViewer(v15) part 2. [EN]](https://kyl3song.github.io/artifacts/IPv6-in-TeamViewer(v15)-part-2.-EN/)

1. https://ro.ecu.edu.au/cgi/viewcontent.cgi?article=1166&context=adf
1. [Remote Access Software - Forensics](https://vikas-singh.notion.site/vikas-singh/Remote-Access-Software-Forensics-3e38d9a66ca0414ca9c882ad67f4f71b)
1. https://www.researchgate.net/publication/359220574_Remote_Desktop_Software_as_a_forensic_resource
1. [Analysis on legit tools abused in human operated ransomware](https://jsac.jpcert.or.jp/archive/2023/pdf/JSAC2023_1_1_yamashige-nakatani-tanaka_en.pdf)