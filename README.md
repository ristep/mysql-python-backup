#  mysql-python-backup

#  mysql-python-backup

A simple script for backup MySql databases

- backup.py - main script 
- backup.cnf - is a two-section config file

Examle of backup.cnf
```sh
[client] 
user = pmauser
password = superPassword
host = localhost

[config]
dbList = foodlog,phpmyadmin
backupDir = ./backup
```
