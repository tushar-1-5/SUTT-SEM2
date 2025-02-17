import pandas
import json
xl = "Mess Menu Sample.xlsx"  #accessing the mess menu

dict1 = {}                    #initialising lists and dictionaries
dict2 = {}                    
blist = []
llist = []
dlist = []

df = pandas.read_excel(xl)          #reading the excel file(loading its content into the code)
var = df.to_dict()                  #converting the loaded content into ditionary form,into variable var, for easier understanding and accessing the data
ch = var.keys()
for i in ch:                        #loop to access the elements of dictionary var
    date = str(var[i][0].date())    #accesing date from datetime object and converting it into string such that it can be used as a key for dict2
    b = var[i]                      #accessing each dictionary in var
    
    for n in range(2,11):           #accesing the food items of breakfast
        if type(b[n]) != float:         #eliminating the case of empty cell in the excel file
            if str(b[n])[0] != "*":     #eliminating the case of a cell containing ***********
                blist.append(b[n])
        
    dict1["BREAKFAST"]  =blist
    blist = []                          #emptying the list in order to eliminate repitative data

    for n in range(13,21):
        if type(b[n]) != float:         #eliminating the case of empty cell in the excel file
            if str(b[n])[0] != "*":     #eliminating the case of a cell containing ***********
                llist.append(b[n])
    dict1["LUNCH"]  =llist
    llist = []                          #emptying the list in order to eliminate repitative data

    for n in range(23,30):
        if type(b[n]) != float:         #eliminating the case of empty cell in the excel file
            if str(b[n])[0] != "*":     #eliminating the case of a cell containing ***********
                dlist.append(b[n])
    dict1["DINNER"]  =dlist
    dlist = []                          #emptying the list in order to eliminate repitative data
    
    dict2[date]  =dict1            #appending the final dictionary
    dict1 = {}                          #emptying the initial dictinary, in order to eliminate repitative data


with open("task.json","w") as file:     #creating/opening the json file in write mode
    json.dump(dict2,file,indent=2)      #json serialization
