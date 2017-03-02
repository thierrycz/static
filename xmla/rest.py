import json
import requests

### Atlas Environment variables
ATLAS_DOMAIN="slzq0b.sii24.pole-emploi.intra"
ATLAS_DOMAIN="fw1808.dgasi.pole-emploi.intra"

ATLAS_PORT="21000"

### Properties to change
updateProperty="description"
newValue = 'changeMe'
tableFQDN = 'default.sample_aa@Sandbox'


def atlasREST( restAPI ) :
    url = "http://"+ATLAS_DOMAIN+":"+ATLAS_PORT+restAPI
    r= requests.get(url, auth=("admin", "admin"))
    return(json.loads(r.text));


def atlasPOST( restAPI, data) :
    url = "http://" + ATLAS_DOMAIN + ":" + ATLAS_PORT + restAPI
    print (url)
    r = requests.post(url, auth=("admin", "admin"),json=data)
    return (json.loads(r.text));

'''
print("FIND HIVE_TABLE ENTITY FOR MODIFICATION:")
hive_tables=atlasREST("/api/atlas/entities?type=hive_table&property=qualifiedName&value=%s" % (tableFQDN))
print json.dumps(hive_tables, indent=4, sort_keys=True)
'''

print("UPDATE ENTITY DEFINITION:")
#tableGUIid=hive_tables["definition"]['id']['id']
tableGUIid="9e6c4d0d-5fe3-41a9-b9a4-87b7d79f9ef8"

print "   updating: %s = %s" % (updateProperty,newValue)

updatedTable = atlasPOST("/api/atlas/entities/%s?property=%s" % (tableGUIid,updateProperty), newValue)
print("SHOW UPDATED ENTITY DEFINITION")
print json.dumps(updatedTable, indent=4, sort_keys=True)
