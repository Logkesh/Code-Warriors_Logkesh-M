from datetime import datetime

# Updating the License Expiry status
def Lic_update(jdata,data,column,year,mon,day):
    for i in range(len(jdata['Licnum'])):
        jdata[column][i] = 'Valid'

    validity = 20 #year

    dyear = data[data[year]<=int(str(datetime.now())[:4])-validity]
    dmon = dyear[dyear[mon]<=int(str(datetime.now())[5:7])]
    dday = dmon[dmon[day]<=int(str(datetime.now())[8:10])]

    licnum = list(dday['Licnum'])

    for i in licnum:
        if i in jdata['Licnum']:
            jdata[column][jdata['Licnum'].index(i)] = 'Expired'
    return jdata,data