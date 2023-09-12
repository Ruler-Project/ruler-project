# N-Able AV Defender

## Event Logs

Unknown

## Application specific files

`\Program Files (x86)\N-able Technologies\Windows Agent\log\AVDefenderSecurityEvents.log`

``` yaml title="Example"
[GeneralEventsDataCollector] 2021-10-28 04:36:24,762 WARN  com.nable.agent.AVDefenderMaintenance.GeneralEventsDataSubmit Event message: <JSON DATA>
```

`<unknown start>\N-Able Technologies\AVDefender\Logs`

`\Program Files (x86)\N-able Technologies\Tools\log\EndPointSDK.log`

## Quarantine

* `\Program Files\N-able Technologies\AVDefender\Quarantine\cache.db\`
    - table: entries
    - fields: Quarid, path, threat, status, size, quartime, acctime, modtime, scanflags, usersid
    - notes: timestamps are unix timestamps

## References

[^1]: [AV Defender - Agent Log files created and their descriptions](https://documentation.n-able.com/N-central/troubleshooting/Content/kb/AV-Defender----Agent-Log-files-created-and-their-descriptions.htm)