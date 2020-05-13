#!/usr/bin/python3
import os
import time
import datetime
import pipes
import configparser


def dbBackup(dbName, backupfile):
    dumpFile = pipes.quote(backupfile) + "/" + dbName + ".sql"
    DumpCmd = "mysqldump " + "--defaults-extra-file=./backup.cnf " + dbName + " > " + dumpFile
    # print(DumpCmd)
    if os.system(DumpCmd) == 0:
        os.system("gzip " + dumpFile)
    else:
        os.unlink(dumpFile)


Config = configparser.ConfigParser()
Config.read('backup.cnf')
dbList = Config.get('dblist','list').split(',')

# Getting current DateTime to create backup folders like "2020817-123435".
BackupFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backup', time.strftime('%Y%m%d-%H%M%S'))
BackupDir = os.path.abspath(BackupFile)

try:
    os.stat(BackupDir)
except:
    os.makedirs(BackupDir)

for dbName in dbList:
    dbBackup(dbName, BackupFile)
