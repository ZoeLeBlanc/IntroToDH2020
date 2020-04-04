# tools = ["Abbot", 1,0,0,0,0, "ABBYY FineReader",0,0,1,0,1,"Academia.edu",0,0,0,1,0, "Adobe After Effects" ,0,1,0,0,0, "Adobe Flash",0,0,0,0,1, "Adobe Illustrator",0,0,0,0,1, "Adobe InDesign" ,1,0,0,0,0, "Advene",0,0,0,0,1, "Alpheios",1,0,0,0,0, "Alveo",1,0,0,0,0]



# def converter(data):
#     output = {}
#     vals = []
#     name = ""
#     for i in range(0,len(data)):
#         print(i, i % 6)
#         if i % 6 == 0: 
#             name = data[i]
#             vals = []
#         elif i % 6 == 5: 
#             vals.append(data[i])
#             print(vals) 
#             total = sum(vals)
#             print(total)
#             vals.append(total)
#             output[name] = vals
#             name = ""
#         else:
#             vals.append(data[i])
#     return output

# def output (name, dict):
#     for key in dict.keys():
#         if key == name:
#             print(dict[key])

# tools1 = converter(tools)
# print(tools1)
# output("Abbot",tools1)

dhtools = {
    "python": {
        "2015": 9,
        "2016": "22",
        "2017": "27",
        "2018": "32",
        "2019": "35",
        "sum" : "125"
    },
    "javascript": {
        "2015":"8",
        "2016": "18",
        "2017": "12",
        "2018": "6",
        "2019": "15",
        "sum" : "59"
    },
    "twitter": {
        "2015":"10",
        "2016": "18",
        "2017": "26",
        "2018": "16",
        "2019": "12",
        "sum" : "82"
    },
    "github": {
        "2015":"2",
        "2016": "6",
        "2017": "17",
        "2018": "5",
        "2019": "10",
        "sum" : "40"
    },
    "gephi": {
        "2015":"11",
        "2016": "16",
        "2017": "14",
        "2018": "10",
        "2019": "9",
        "sum" : "60"
    },
    "geonames": {
        "2015":"2",
        "2016": "4",
        "2017": "3",
        "2018": "1",
        "2019": "8",
        "sum" : "18"
    },
    "transkribus": {
        "2015":"0",
        "2016": "1",
        "2017": "2",
        "2018": "1",
        "2019": "8",
        "sum" : "12"
    },
    "excel": {
        "2015":"5",
        "2016": "9",
        "2017": "3",
        "2018": "6",
        "2019": "7",
        "sum" : "30"
    },
    "mysql": {
        "2015":"0",
        "2016": "6",
        "2017": "9",
        "2018": "5",
        "2019": "7",
        "sum" : "27"
    }
}
# print(dhtools.items())
for tool,value in dhtools.items():
    tool_values = []
    for year, pop in value.items():
        value[year] = int(pop)
        tool_values.append(int(pop))
    print(sum(tool_values), tool_values)
print(dhtools)
