import json
import math

f = open('Json/data.json',)
data = json.load(f)
print("hi")
count = 0
store_list = []
newls = []
for item in data:
    store_details = {"latlng":None, "name":None,"population":None}
    store_details['latlng'] = item['latlng']
    store_details['name'] = item['name']
    store_details['population'] = item['population']
    if item['population'] >= 847000 and count <20:
        count=count +1
        dif=847000-item['population'] 
        print(count,item['name'],item['population'],dif,item['latlng'])
        newls.append(store_details['latlng'])
    store_list.append(store_details)
#print(store_list)
print(newls)
print(newls[0][0])

def dis(i,j):
    lat1,lon1=newls[i]
    lat2,lon2=newls[j]
    radius = 6371
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
            math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
            math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d
print("strt")
s=0.00
for i in range(0,20):
    for j in range(i,20):
        if i != j:
            d= round(dis(i,j),2)
            s=s+round(d,2)
            
print(round(s,2))
f.close()

#1619949.7200000002
#1619950.4000000001
#1619949.8039999995
#1619949.8109