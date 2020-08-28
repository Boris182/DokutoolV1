import fdb

con = fdb.connect(dsn='localhost:c:\sirio.gdb', user='sysdba', password='masterkey')
cur = con.cursor()

cur.execute("select ALARM.ALARM_NAME, AL_AB_IN.ALARM_ID_1, AL_AB_IN.MADDR "
            "from ALARM "
            "inner join AL_AB_IN on ALARM.ALARM_ID = AL_AB_IN.ALARM_ID_0")
data = cur.fetchall()

for i in range(len(data)):
    print(data[i])


# ALARM_ID