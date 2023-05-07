# Kaseya

Kaseya allows for remote control without necessarily notifying to the user that the session is active.
The events are recorded in the logs for the agents.

Interaction is performed through a webapp (that has an installed application for liveconnect on the host)

# Application specific files

C:\ProgramData\Kaseya\Log\Endpoint\Instance_KSAAS112878653242351\KaseyaEndpoint\KaseyaEndpoint-2020-01-24T04-17-45Z.log

### Connection:
[I 2020-01-24T04:46:16.419139Z +00:00  3160  f18] [AgentRemoteControlSession] Remote Control Session Jwt is valid
[I 2020-01-24T04:46:16.686197Z +00:00  3160  f1c] [RemoteControlApplicationService] Launching remote control host for request 47972bed-33bb-4422-a6f4-6ae0c244a96c with sessionId 92fb5231-0009-44af-bd31-425bf26b8060 ; currently have 0 instances

### Disconnection
[I 2020-01-24T04:47:00.268159Z +00:00  3160  f1c] [AgentRemoteControlSession] Ending remote control session
[I 2020-01-24T04:47:00.268159Z +00:00  3160  f1c] [RemoteControlApplicationService] Shutting down Remote Control Instance #92fb5231-0009-44af-bd31-425bf26b8060

C:\ProgramData\Kaseya\Log\Endpoint\Instance_KSAAS112878653242351\Session_92fb5231-0009-44af-bd31-425bf26b8060

contains 2 folders
KaseyaRemoteControlHost
KaseyaRemoteControlHostDesktop_9976
That contain their own logs of the connection.

## References