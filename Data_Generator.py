from random import randint
import json

day =[]
month =[]
year = []

for i in range(10000):
    year.append(randint(2001,2021))
    month.append(randint(1,12))
    if(month[i]!=2):
        day.append(randint(1,31))
    elif(year[i]%4==0):
        day.append(randint(1,29))
    else:
        day.append(randint(1,28))

#Generating License plate
license_num = []
state = ['AN','AP','AR','AS','BR','CH','DN','DD','DL','GA','GJ','HR','HP','JK','KA','KL','LD','MP','MH','MN','ML','MZ','NL','OR','PY','PN','RJ','SK','TN','TR','UP','WB']
num_st = []
for i in range(10000):
    num_st.append(state[randint(0,31)])
    num_st[i] += " "
    num_st[i] += str(randint(0,9))
    num_st[i] += str(randint(0,9))
    num_st[i] += " "
    num_st[i] += chr(randint(65,90))
    if(randint(0,1)==0):
        num_st[i] += chr(randint(65,90))
    num_st[i] += " "
    num_st[i] += str(randint(0,9))
    num_st[i] += str(randint(0,9))
    num_st[i] += str(randint(0,9))
    num_st[i] += str(randint(0,9))

#Generating license plate owner names
name =[]
for i in range(10000):
    name.append('')
    for j in range(5):
        name[i] += chr(randint(65,90))
        
#Generating Insurance Renewal Date
iday =[]
imonth =[]
iyear = []

for i in range(10000):
    iyear.append(randint(2001,2021))
    imonth.append(randint(1,12))
    if(imonth[i]!=2):
        iday.append(randint(1,31))
    elif(iyear[i]%4==0):
        iday.append(randint(1,29))
    else:
        iday.append(randint(1,28))

validity = 20 #years

data = {}
data.update({'Licnum':num_st,'Name':name,'LicPreday':day,'LicPreMon':month,'LicPreYear':year,'LicExpStatus':[" " for x in range(len(year))],
            'InsPreday':iday, 'InsPreMon':imonth, 'InsPreYear':iyear, 'InsExpStatus':[" " for x in range(len(iyear))]})
  
f = open('Data.json','w')        
f.write(json.dumps(data))   
f.close() 