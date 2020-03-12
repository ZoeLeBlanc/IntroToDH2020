# Input a tool name and output it's information


def make_tool_dict(name, value_2015 , value_2016, value_2017,value_2018, value_2019):
    tool = {
        "2015":value_2015,
        "2016":value_2016,
        "2017":value_2017,
        "2018":value_2018,
        "2019":value_2019,
        "name":name,
        "total":value_2015+value_2016+value_2017+value_2018+value_2019
    }
    return tool


    

dh_tools=[make_tool_dict("Python",9,22,27,32,35),
          make_tool_dict("JavaScript",8,18,12,6,15),
          make_tool_dict("Twitter",10,18,26,16,12),
          make_tool_dict("GitHub",2,6,17,5,10),
          make_tool_dict("Gephi",11,16,14,10,9),
          make_tool_dict("GeoNames",2,4,3,1,8),
          make_tool_dict("Transkribus",0,1,2,1,8),
          make_tool_dict("Excel",5,9,3,6,7),
          make_tool_dict("MySQL",0,6,9,5,7)]


# def get_tool_info(toolname):
#     # print(dh_tools)
#     for tool in dh_tools:
#         if toolname == tool.name:
#             print(tool)
#         else:
#             print("Not a DH tool")
# user_toolname = input("Enter a DH Tool...")
# get_tool_info(user_toolname)

a_tool = dh_tools[0]
print(a_tool.keys())

# print("\nPrinting tools...\n")
# for tool in dh_tools:
#     print(tool)
#     for prop in ["name","2015","2019","total"]:
#         print(tool[prop])
#         # print(prop+": "+str(tool[prop])+"\n")
#     # print("\n")