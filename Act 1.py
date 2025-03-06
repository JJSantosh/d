d1={"id1":{"name":"santosh","roll no":32},
    "id2":{"name":"gautam","roll no":3},
    "id3":{"name":"santosh","roll no":32}
}
r={}
for k,v in d1.items():
    if v not in r.values():
        r[k]=v
    
print(r)
