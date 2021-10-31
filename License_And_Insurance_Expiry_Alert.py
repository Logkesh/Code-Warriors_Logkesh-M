from Read_Data import readdata



data,jdata = readdata()

# License expiry vehichle's details
print('License expiry vehichle\'s details')
print('Number of Vehichles with Expired License: ',len([x for x in jdata['Licnum'] if(jdata['LicExpStatus'][jdata['Licnum'].index(x)]=='Expired')]))
print(data[data['LicExpStatus']=='Expired'])

# Insurance expiry vehichle's details
print('Insurance expiry vehichle\'s details')
print("Number of Vehichles with Expired Insurance: ",len([x for x in jdata['Licnum'] if(jdata['InsExpStatus'][jdata['Licnum'].index(x)]=='Expired')]))
print(data[data['InsExpStatus']=='Expired'])
