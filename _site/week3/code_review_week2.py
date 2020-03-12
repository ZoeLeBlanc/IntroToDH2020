# Example 1
firstnames = ["Sara", "Kevin", "Shiva", "Anna", "Meher", "Maia"]
print(firstnames[-1])
print(firstnames[int(len(firstnames)/2)])
print(firstnames[0] + " " + firstnames[1])

randNumbers = [10, 76, 30, 12, 66, 98, 2, 74, 21, 50]
sum1 = sum(randNumbers)
print(str(sum1/len(randNumbers)))

tools = {"Python":{"2015":9, "2016":22, "2017":27, "2018":32, "2019":35}, "Javascript":{"2015":8, "2016":18, "2017":12, "2018":6, "2019":15}, "Twitter":{"2015":10, "2016":18, "2017":26, "2018":16, "2019":12}, "Github":{"2015":2, "2016":6, "2017":17, "2018":5, "2019":10}, "Gephi":{"2015":11, "2016":16, "2017":14, "2018":10, "2019":9}, "Geonames":{"2015":2, "2016":4, "2017":3, "2018":1, "2019":8}, "Transkribus":{"2015":0, "2016":1, "2017":2, "2018":1, "2019":8}, "Excel":{"2015":5, "2016":9, "2017":3, "2018":6, "2019":7}, "MySQL":{"2015":0, "2016":6, "2017":9, "2018":5, "2019":7}}

tools["Python"]["cumulative"] = sum(tools["Python"].values())
print("Python: 2015: " + str(tools["Python"]["2015"]) + " 2019: " + str(tools["Python"]["2019"]) + " Cumulative: " + str(tools["Python"]["cumulative"]))

tools["Javascript"]["cumulative"] = sum(tools["Javascript"].values())
print("Javascript: 2015: " + str(tools["Javascript"]["2015"]) + " 2019: " + str(tools["Javascript"]["2019"]) + " Cumulative: " + str(tools["Javascript"]["cumulative"]))

tools["Twitter"]["cumulative"] = sum(tools["Twitter"].values())
print("Twitter: 2015: " + str(tools["Twitter"]["2015"]) + " 2019: " + str(tools["Twitter"]["2019"]) + " Cumulative: " + str(tools["Twitter"]["cumulative"]))

tools["Github"]["cumulative"] = sum(tools["Github"].values())
print("Github: 2015: " + str(tools["Github"]["2015"]) + " 2019: " + str(tools["Github"]["2019"]) + " Cumulative: " + str(tools["Github"]["cumulative"]))

tools["Gephi"]["cumulative"] = sum(tools["Gephi"].values())
print("Gephi: 2015: " + str(tools["Gephi"]["2015"]) + " 2019: " + str(tools["Gephi"]["2019"]) + " Cumulative: " + str(tools["Gephi"]["cumulative"]))

tools["Geonames"]["cumulative"] = sum(tools["Geonames"].values())
print("Geonames: 2015: " + str(tools["Geonames"]["2015"]) + " 2019: " + str(tools["Geonames"]["2019"]) + " Cumulative: " + str(tools["Geonames"]["cumulative"]))

tools["Transkribus"]["cumulative"] = sum(tools["Transkribus"].values())
print("Transkribus: 2015: " + str(tools["Transkribus"]["2015"]) + " 2019: " + str(tools["Transkribus"]["2019"]) + " Cumulative: " + str(tools["Transkribus"]["cumulative"]))

tools["Excel"]["cumulative"] = sum(tools["Excel"].values())
print("Excel: 2015: " + str(tools["Excel"]["2015"]) + " 2019: " + str(tools["Excel"]["2019"]) + " Cumulative: " + str(tools["Excel"]["cumulative"]))

tools["MySQL"]["cumulative"] = sum(tools["MySQL"].values())
print("MySQL: 2015: " + str(tools["MySQL"]["2015"]) + " 2019: " + str(tools["MySQL"]["2019"]) + " Cumulative: " + str(tools["MySQL"]["cumulative"]))

#Example 2
names = ["Sara","Kevin","Shiva","Anna","Meher","Maia","Zoe"]
print("First name is " + names[0])
names.reverse()
print("New first name is " + names[0])
print("New last name is " + names[-1])
print("New middle name is " + names[4])
print("New first two names are " + names[0] + " " + names[1])
rngdata = [45,60,72,7,83,86,5,16,90,55]
total = sum(rngdata)
print(total/len(rngdata))
Python = {2015: 9,2016: 22,2017:27,2018:32,2019:35}
JavaScript = {2015:8,2016:18,2017:12,2018:6,2019:15}
Twitter = {2015:10,2016:18,2017:26,2018:16,2019:12}
GitHub = {2015:2,2016:6,2017:17,2018:5,2019:10}
Gephi = {2015:11,2016:16,2017:14,2018:10,2019:9}
GeoNames = {2015:2,2016:4,2017:3,2018:1,2019:8}
Transkribus = {2015:0,2016:1,2017:2,2018:1,2019:8}
Excel = {2015:5,2016:9,2017:3,2018:6,2019:7}
MySQL = {2015:0,2016:6,2017:9,2018:5,2019:7}

Python.update({'total': sum(Python.values())})
JavaScript.update({'total': sum(JavaScript.values())})
Twitter.update({'total': sum(Twitter.values())})
GitHub.update({'total': sum(GitHub.values())})
Gephi.update({'total': sum(Gephi.values())})
GeoNames.update({'total': sum(GeoNames.values())})
Transkribus.update({'total': sum(Transkribus.values())})
Excel.update({'total': sum(Excel.values())})
MySQL.update({'total': sum(MySQL.values())})
print("Python 2015, 2019, and overall values are: " + str(Python[2015]) + " " + str(Python[2019]) + " " + str(Python['total']))
print("JavaScript 2015, 2019, and overall values are: " + str(JavaScript[2015]) + " " + str(JavaScript[2019]) + " " + str(JavaScript['total']))
print("Twitter 2015, 2019, and overall values are: " + str(Twitter[2015]) + " " + str(Twitter[2019]) + " " + str(Twitter['total']))
print("GitHub 2015, 2019, and overall values are: " + str(GitHub[2015]) + " " + str(GitHub[2019]) + " " + str(GitHub['total']))
print("Gephi 2015, 2019, and overall values are: " + str(Gephi[2015]) + " " + str(Gephi[2019]) + " " + str(Gephi['total']))
print("GeoNames 2015, 2019, and overall values are: " + str(GeoNames[2015]) + " " + str(GeoNames[2019]) + " " + str(GeoNames['total']))
print("Transkribus 2015, 2019, and overall values are: " + str(Transkribus[2015]) + " " + str(Transkribus[2019]) + " " + str(Transkribus['total']))
print("Excel 2015, 2019, and overall values are: " + str(Excel[2015]) + " " + str(Excel[2019]) + " " + str(Excel['total']))
print("MySQL 2015, 2019, and overall values are: " + str(MySQL[2015]) + " " + str(MySQL[2019]) + " " + str(MySQL['total']))

# Example 3
names=["Sara", "Kevin", "Shiva", "Anna", "Meher", "Maia"]
names.append("Zoe")
print("First: "+names[0])
names.insert(1,names.pop())
print("Order changed!")
print("First: "+names[0]+", "+names[1])
print("Middle: "+names[int(len(names)/2)])
print("Last: "+names[len(names)-1])
nums_from_google=[14, 73, 76, 85, 72, 82, 25, 4, 41, 83]
total=0
for item in nums_from_google:
    total+=item
result=total/len(nums_from_google)
print("Random number average: "+str(result))
def tool_dict(name,a,b,c,d,e):
    return {"2015":a,"2016":b,"2017":c,"2018":d,"2019":e,"name":name,"total":a+b+c+d+e}

dh_tools=[tool_dict("Python",9,22,27,32,35),
          tool_dict("JavaScript",8,18,12,6,15),
          tool_dict("Twitter",10,18,26,16,12),
          tool_dict("GitHub",2,6,17,5,10),
          tool_dict("Gephi",11,16,14,10,9),
          tool_dict("GeoNames",2,4,3,1,8),
          tool_dict("Transkribus",0,1,2,1,8),
          tool_dict("Excel",5,9,3,6,7),
          tool_dict("MySQL",0,6,9,5,7)]
print("\nPrinting tools...\n")
for tool in dh_tools:
    for prop in ["name","2015","2019","total"]:
        print(prop+": "+str(tool[prop]))
    print("")

# Example 4
# QUESTION 1
names = ['Sara', 'Kevin', 'Shiva', 'Anna', 'Meher', 'Maia']
names.extend([True, 'Zoe'])
print(names[0])

def invertList(names): 
   names.reverse()
   return names
   
# Unit test 1
#names = ['Sara', 'Kevin', 'Shiva', 'Anna', 'Meher', 'Maia']
#print("names[id={}] items: {}".format(id(names), names))

names = invertList(names)
#print("Output list[id={}] items: {}".format(id(names), names))
print(names[0])
print(names[6])
print(names[3])
print(names[0:1])

# QUESTION 2 
rng10 = [69, 38, 75, 96, 14, 69, 89, 30, 90, 16]
avg_rng = sum(rng10)/10
print(avg_rng)

# QUESTION 3 
dhtools = {
    'python': {
        '2015':'9',
        '2016': '22', 
        '2017': '27', 
        '2018': '32', 
        '2019': '35',
        'sum' : '125'
    },
    'javascript': {
        '2015':'8',
        '2016': '18', 
        '2017': '12', 
        '2018': '6', 
        '2019': '15',
        'sum' : '59'
    },
    'twitter': {
        '2015':'10',
        '2016': '18', 
        '2017': '26', 
        '2018': '16', 
        '2019': '12',
        'sum' : '82'
    },
    'github': {
        '2015':'2',
        '2016': '6', 
        '2017': '17', 
        '2018': '5', 
        '2019': '10',
        'sum' : '40'
    },
    'gephi': {
        '2015':'11',
        '2016': '16', 
        '2017': '14', 
        '2018': '10', 
        '2019': '9',
        'sum' : '60'
    },
    'geonames': {
        '2015':'2',
        '2016': '4', 
        '2017': '3', 
        '2018': '1', 
        '2019': '8',
        'sum' : '18'
    },
    'transkribus': {
        '2015':'0',
        '2016': '1', 
        '2017': '2', 
        '2018': '1', 
        '2019': '8',
        'sum' : '12'
    },
    'excel': {
        '2015':'5',
        '2016': '9', 
        '2017': '3', 
        '2018': '6', 
        '2019': '7',
        'sum' : '30'
    },
    'mysql': {
        '2015':'0',
        '2016': '6', 
        '2017': '9', 
        '2018': '5', 
        '2019': '7',
        'sum' : '27'
    }
}
   
print(dhtools['python']['2015']) 
print(dhtools['python']['2019']) 
print(dhtools['python']['sum']) 
print(dhtools['javascript']['2015']) 
print(dhtools['javascript']['2019']) 
print(dhtools['javascript']['sum']) 
print(dhtools['twitter']['2015']) 
print(dhtools['twitter']['2019']) 
print(dhtools['twitter']['sum'])
print(dhtools['github']['2015']) 
print(dhtools['github']['2019']) 
print(dhtools['github']['sum'])
print(dhtools['gephi']['2015']) 
print(dhtools['gephi']['2019']) 
print(dhtools['gephi']['sum'])
print(dhtools['geonames']['2015']) 
print(dhtools['geonames']['2019']) 
print(dhtools['geonames']['sum'])
print(dhtools['transkribus']['2015']) 
print(dhtools['transkribus']['2019']) 
print(dhtools['transkribus']['sum'])
print(dhtools['excel']['2015']) 
print(dhtools['excel']['2019']) 
print(dhtools['excel']['sum'])
print(dhtools['mysql']['2015']) 
print(dhtools['mysql']['2019']) 
print(dhtools['mysql']['sum'])






