import json

with open('sample-data.json') as json_file:
    data = json.load(json_file)
print("Interface Status")
print("==============================================================================")
print("""DN                                               Description  Speed    MTU
-----------------------------------------------  ------------ -------- ------   """)

print(data["imdata"][0]["l1PhysIf"]["attributes"]["dn"]+"                    "+ data["imdata"][0]["l1PhysIf"]["attributes"]["speed"]+"   "+data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"])

print(data["imdata"][1]["l1PhysIf"]["attributes"]["dn"]+"                    "+ data["imdata"][1]["l1PhysIf"]["attributes"]["speed"]+"   "+data["imdata"][1]["l1PhysIf"]["attributes"]["mtu"])

print(data["imdata"][2]["l1PhysIf"]["attributes"]["dn"]+"                    "+ data["imdata"][2]["l1PhysIf"]["attributes"]["speed"]+"   "+data["imdata"][2]["l1PhysIf"]["attributes"]["mtu"])