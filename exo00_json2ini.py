import json

with open("mon_fichier.json") as json_file:
    json_data = json.load(json_file)
    
with open("fichier.ini",'w') as fw:
   for key, value in json_data.items():
        
        fw.write("["+key+"]"+"\n")
        for a,b in value.items():
            fw.write(str(a)+"="+str(b)+"\n")

       

