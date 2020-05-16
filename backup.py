#!/usr/bin/python3
import os
import time
import datetime
import pipes
import configparser


def dbBackup(dbName, backupdir, conff):
    try:
        os.stat(BackupDir)
    except:
        os.makedirs(BackupDir)

    dumpFile = pipes.quote(backupdir) + "/" + dbName + ".sql"
    DumpCmd = "mysqldump " + "--defaults-extra-file="+ conff + ' ' + dbName + " > " + dumpFile

    if os.system(DumpCmd) == 0:
        os.system("gzip " + dumpFile)
    else:
        os.unlink(dumpFile)

scriptFile = os.path.splitext(__file__)[0]
scriptDir = os.path.dirname(__file__)
confFile = scriptFile + '.cnf'

Config = configparser.ConfigParser()
Config.read(confFile)
dbList = Config.get('config','dbList').split(',')

BackupDir = Config.get('config','backupDir')
if(BackupDir[0]=='.'): BackupDir = os.path.join(scriptDir, BackupDir)
BackupDir = os.path.join( BackupDir, time.strftime('%Y%m%d-%H%M%S'))
print(BackupDir)    

for dbn in dbList:
    dbBackup(dbn, BackupDir, confFile)
