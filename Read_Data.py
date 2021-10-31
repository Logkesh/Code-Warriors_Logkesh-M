# Read Dict and DataFrame from JSON file
import json
import pandas as pd
from License_Status_Update import Lic_update
def readdata():    
    jdata = {}
    with open('Data.json' ,'r') as file:
                jdata = json.loads(file.read()) 

    data = pd.read_json('Data.json')

    # Updating the License Expiry status
    jdata,data = Lic_update(jdata,data,'LicExpStatus','LicPreYear','LicPreMon','LicPreday')

    # Updating the Insurance Expiry status
    jdata,data = Lic_update(jdata,data,'InsExpStatus','InsPreYear','InsPreMon','InsPreday')

    # Writing the updated IES and LES in the json file
    f = open('Data.json','w')        
    f.write(json.dumps(jdata))   
    f.close()

    return data,jdata