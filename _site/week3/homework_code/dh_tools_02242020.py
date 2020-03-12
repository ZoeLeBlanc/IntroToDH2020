#make a way to quickly make a new dictionary with the right properties
def tool_dict(line):
    return {"name":line[0],"2015":line[1],"2016":line[2],"2017":line[3],"2018":line[4],"2019":line[5],"total":sum(line[1:])}
#open file
file=open("tools_dh_proceedings.csv")
print("Opened tools_dh_proceedings.csv")
#throw away title line
file.readline()
#get the rest of the lines
lines=file.readlines()
file.close()
print("File has been read.")
dh_tools=[]
for line in lines:
    line=line.split(',')
    for i in range(1,len(line)):
        line[i]=int(line[i])
    dh_tools.append(tool_dict(line))
print("List of tools successfully created.")
#enter a loop where you can choose between printing the info of a tool or all stats for a year
x=""
while x!="EXIT":
    x=input("Type... \nNAME to display info of a tool by name, \nTOTALS to see a list of **all** tool totals, \nYEAR to input a year to see its top 10 tools, or \nEXIT to exit this loop.\n")
    if "TOTALS" in x:
        for tool in dh_tools:
            print(tool["name"]+": "+str(tool["total"]))
        print("Printed all tool names.")
    elif "YEAR" in x:
        z=input("What year?\n")
        if z in ["2015","2016","2017","2018","2019"]:
            print("Top tools for "+z+":")
            dh_tools.sort(key=lambda tool: tool[z],reverse=True)
            for tool in dh_tools[0:10]:
                print(tool["name"]+": "+str(tool[z]))
        else:
            print("Sorry, we don't have data for that year.")
    elif "NAME" in x:
        z=input("What name?\n")
        found=False
        for tool in dh_tools:
            if z==tool["name"]:
                print(z)
                for key, value in tool.items():
                    print(key+": "+str(value))
                found=True
        if( not found):
            print("Sorry, couldn't find data for that tool.")
    elif "EXIT" not in x:
        print("Please match the commands exactly.")
print("Quit loop successfully.")


        
    


