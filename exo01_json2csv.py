import json

with open("mon_fichier1.json") as json_file:
    json_data = json.load(json_file)
    
with open("fichier.csv",'w') as fw:
   for key, value in json_data.items():
        fw.write(str(key)+","+str(value)+"\n")

       

