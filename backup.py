#!/usr/bin/python3
import os
import time
import datetime
import pipes
import configparser


def dbBackup(dbName, backupdir):
    try:
        os.stat(BackupDir)
    except:
        os.makedirs(BackupDir)

    dumpFile = pipes.quote(backupdir) + "/" + dbName + ".sql"
    DumpCmd = "mysqldump " + "--defaults-extra-file=./backup.cnf " + dbName + " > " + dumpFile

    if os.system(DumpCmd) == 0:
        os.system("gzip " + dumpFile)
    else:
        os.unlink(dumpFile)


Config = configparser.ConfigParser()
Config.read('backup.cnf')
dbList = Config.get('config','dbList').split(',')
BackupDir = os.path.join( os.path.abspath(Config.get('config','backupDir')), time.strftime('%Y%m%d-%H%M%S'))

for dbName in dbList:
    dbBackup(dbName, BackupDir)
