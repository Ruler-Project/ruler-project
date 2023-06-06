# SupRemo

Credentials are generated on install on the victim machine and are not tied to an account ^[1]^

## Application logs

Log folder: `%ProgramData%\SupremoRemoteDesktop\Log\`
Timestamp format: YYYY-MM-DD HH:MM:SS:SSS

|Log file|Notes
|-|-
|SupremoService.00.Service.log|Software install
|Supremo.00.Client.log|"Connected with ID"
|Supremo.00.Incoming.log|Hostname of the attacker
|Supremo.00.ReportsQueue.log|Start and end of the session
|Supremo.00.FileTransfer.log|Received file or Sent file

Network connections to "nanosystems.it" on 443/5938

!!! info "Useful grep"

    `Connected with ID|\[Incoming\]|Supremo Closed|\[File Transfer\]`

## References
[^1]: [Analysis on legit tools abused in human operated ransomware](https://jsac.jpcert.or.jp/archive/2023/pdf/JSAC2023_1_1_yamashige-nakatani-tanaka_en.pdf)