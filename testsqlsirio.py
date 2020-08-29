import fdb

con = fdb.connect(dsn='localhost:c:\SIRIO.GDB', user='sysdba', password='masterkey')
cur = con.cursor()

#cur.execute("SELECT * from ALARM")

querydata = {}

cur.execute("SELECT ALARM.ALARM_NAME, AL_JOB.JOB_NAME, AL_REF_J.PRI "
            "from AL_ESPA "
            "right join ALARM on ALARM.ALARM_ID = AL_ESPA.ALARM_ID "
            "right join AL_REF_A on AL_REF_A.AGROUP_ID = ALARM.AGROUP_ID "
            "full join AL_REF_J on AL_REF_J.JGROUP_ID = AL_REF_A.JGROUP_ID "
            "inner join AL_JOB on AL_JOB.JOB_ID = AL_REF_J.JOB_ID "
            "order by ALARM.ALARM_NAME")

espadata = cur.fetchall()

for i in range(len(espadata)):
    if espadata[i][0] in querydata:
        querydata[espadata[i][0]].append([espadata[i][1], espadata[i][2]])
    else:
        querydata[espadata[i][0]] = [[espadata[i][1], espadata[i][2]]]
    #print(espadata[i][0])

for i in querydata:
    print(i)
    print(querydata[i])

