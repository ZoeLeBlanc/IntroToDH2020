tools = ["Abbot", 1,0,0,0,0, "ABBYY FineReader",0,0,1,0,1,"Academia.edu",0,0,0,1,0, "Adobe After Effects" ,0,1,0,0,0,
 "Adobe Flash",0,0,0,0,1, "Adobe Illustrator",0,0,0,0,1, "Adobe InDesign" ,1,0,0,0,0, "Advene",0,0,0,0,1, "Alpheios",1,0,0,0,0, "Alveo",1,0,0,0,0]

def converter (data):
 	output = {}
 	vals = []
 	name = ""
 	for i in range(0,len(data)):
 		if i % 6 == 0: 
 			name = data[i]
 			vals = []
 		elif i % 6 == 5: 
 			vals.append(data[i]) 
 			total = sum(vals)
 			vals.append(total)
 			output[name] = vals
 			name = ""
 		else:
 			vals.append(i)
 	return output

def output (name, dict):
	for key in dict.keys():
		if key == name:
			print(dict[key])

tools1 = converter (tools)
print(tools1)
output("Abbot",tools1)