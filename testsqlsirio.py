import fdb

con = fdb.connect(dsn='localhost:c:\SIRIO.GDB', user='sysdba', password='masterkey')
cur = con.cursor()

#cur.execute("SELECT * from ALARM")

querydata = {}

cur.execute("SELECT AL_ESPA.DESCRIPTION, AL_JOB.JOB_NAME, AL_REF_J.PRI, ALARM.ALARM_NAME "
            "from AL_ESPA "
            "right join ALARM on ALARM.ALARM_ID = AL_ESPA.ALARM_ID "
            "right join AL_REF_A on AL_REF_A.AGROUP_ID = ALARM.AGROUP_ID "
            "full join AL_REF_J on AL_REF_J.JGROUP_ID = AL_REF_A.JGROUP_ID "
            "inner join AL_JOB on AL_JOB.JOB_ID = AL_REF_J.JOB_ID "
            "WHERE ALARM.ALARM_ID = AL_ESPA.ALARM_ID")

esparefdata = cur.fetchall()

cur.execute("select * from ALARM")
dataAlarm = cur.fetchall()

cur.execute("select * from AL_ESPA")
dataEspa = cur.fetchall()

cur.execute("select * from AL_JOB")
dataJob = cur.fetchall()

cur.execute("select * from AL_AB_IN")
dataCont = cur.fetchall()

for i in range(len(esparefdata)):
    if esparefdata[i][0] in querydata:
        querydata[esparefdata[i][0]].append([esparefdata[i][1], esparefdata[i][2]])
    else:
        querydata[esparefdata[i][0]] = [[esparefdata[i][1], esparefdata[i][2]]]

print(querydata)

for i in querydata:
    print(i)
    print(querydata[i])



dataEspa.sort(key=lambda psa:psa[2])

for i in dataEspa:
    print(i)

for i in dataJob:
    print(i)


dataCont.sort(key=lambda cont:cont[1])
dataCont.sort(key=lambda cont:cont[0])


