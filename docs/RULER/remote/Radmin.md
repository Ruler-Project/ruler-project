# Radmin 

## Event logs

|Event Log | Event ID | Provider | Notes
|-|-|-|-
|Application|1033|MsiInstaller|Windows Installer installed the product. Product Name: Radmin Server 3.5.2. Product Version: 3.52.1.0000. Product Language: 1033. Manufacturer: Famatech.
|Application|11707|MsiInstaller|Product: Radmin Server 3.5.2 -- Installation operation completed successfully.|
|Application|1042|MsiInstaller|Ending a Windows Installer transaction: C:\Users\username\Downloads\Radmin_3.5.2.1_EN\Radmin_Server_3.5.2.1_EN.msi. Client Process Id: 2016.|
|Application|1040|MsiInstaller|Beginning a Windows Installer transaction: C:\Users\username\Downloads\Radmin_3.5.2.1_EN\Radmin_Server_3.5.2.1_EN.msi. Client Process Id: 2016.|
|System|7045|Service Control Manager|A service was installed in the system. Service Name:  Radmin Server V3|
Microsoft-Windows-Windows Firewall With Advanced Security|2097|Firewall With Advanced Security| A rule has been added to the Windows Defender Firewall exception list. Application Path:	C:\Windows\SysWOW64\rserver30\rserver3.exe
|Application|1034|MsiInstaller|Windows Installer removed the product. Product Name: Radmin Server 3.5.2. Product Version: 3.52.1.0000. Product Language: 1033. Manufacturer: Famatech. Removal success or error status: 0.


## Log files

|Log Path|Notes|Timestamp
|-|-|-|
|C:\Windows\SysWOW64\rserver30\Radm_log.htm|Logs remote access and activity. Is configurable so can be placed and named anywhere. |YYYY.MM.DD HH:MM

Example:


```
<4088> RServer3 2024.01.09 12:50 Radmin Server 3 is started
<4088> RServer3 2024.01.09 12:50 Listening for incoming connections on 4899 port
<8128> RServer3 2024.01.09 12:53 DESKTOP-BVRP8RK.localdomain (x.x.x.x) (username): Password is incorrect or error occurs
<8128> RServer3 2024.01.09 12:53 DESKTOP-BVRP8RK.localdomain (x.x.x.x) connection closed
<7380> RServer3 2024.01.09 12:54 DESKTOP-BVRP8RK.localdomain (x.x.x.x) (DESKTOP-BVRP8RK\username): Password is incorrect or error occurs
<7380> RServer3 2024.01.09 12:54 DESKTOP-BVRP8RK.localdomain (x.x.x.x) connection closed
<4020> RServer3 2024.01.09 12:54 DESKTOP-BVRP8RK.localdomain (x.x.x.x) (DESKTOP-BVRP8RK\username): Password is incorrect or error occurs
<4020> RServer3 2024.01.09 12:54 DESKTOP-BVRP8RK.localdomain (x.x.x.x) connection closed
<3856> RServer3 2024.01.09 12:55 Connection from DESKTOP-BVRP8RK.localdomain (192.168.178.128) (user2): Remote Screen connection
<5472> RServer3 2024.01.09 12:55 DESKTOP-BVRP8RK.localdomain (x.x.x.x) connection closed
<5212> RServer3 2024.01.09 13:19 Connection from DESKTOP-BVRP8RK.localdomain (192.168.178.128) (user2): Remote Screen connection
<7352> RServer3 2024.01.09 13:19 DESKTOP-BVRP8RK.localdomain (x.x.x.x) ( ): Password is incorrect or error occurs
<7352> RServer3 2024.01.09 13:19 DESKTOP-BVRP8RK.localdomain (x.x.x.x) connection closed
```

## Install files

* C:\Windows\SysWOW64\rserver30\

## Network

* Default port: 4899
  * Is configurable

## Registry
* HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Radmin\**

## References
* https://www.radmin.com/
