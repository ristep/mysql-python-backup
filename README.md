#  mysql-python-backup

A simple script for backup MySql databases

- backup.py - main script 
- backup.cnf - is a two-section config file

Examle of backup.cnf
```
[client] 
user = pmauser
password = superPassword
host = localhost

[config]
dbList = foodlog,phpmyadmin  
backupDir = ./backup
```
- [client] - section is for connection parameters 
- dbList  - is list of data-bases
- backupDir - folder for backup files

### Using
```sh
python3 backup.py
```
### Requirements

- python
- gzip
- mysqldump

### Operating systems

- Linux
- Windows 10 - not tested yet