import pandas
import json 
list_data = []
inst = []
instructors1 = []
instructors2 = []
instructors3 = []
sec_no = ""
sec_type = ""
room =""
excel = "Timetable Workbook - SUTT Task 1.xlsx"
LST = ["S1","S2","S3","S4","S6"]
dict2 = {}
dict3 = {}
ch =""
for i in LST:
    df = pandas.read_excel(excel,sheet_name=i)
    var = df.to_dict(orient='split')
    code = var["data"][2][1]
    title = var["data"][2][2]
    lecture_ = var["data"][2][3]
    practical_ = var["data"][2][4]
    units_ = var["data"][2][5]

    for v in var["data"]:
        if type(v[6]) != float:
            var1 = v[6][0]
            if var1 == "P":
                sec_type = "Practical"
                sec_no_test = sec_no
                sec_no = str(v[6])
                if sec_no_test != sec_no and sec_no_test != "":
                    instructors1=[]
                    inst.append(dict1)
                dict1 = {}
                room = v[8]
                dict1["section_type"] = sec_type
                dict1["section_number"] = sec_no
                dict1["room"] = room
                instructors1 = [v[7]]
                dict1["Instructors"] = instructors1
                if len(v[9]) ==6:
                    day = v[9][0]
                    t1 = v[9][3]
                    t2 = v[9][5]
                else:
                    day = v[9][0] +v[9][1]
                    t1 = v[9][4]
                    t2 = v[9][6]
                
                dict1["timing"] = [{
                    "day" : day,
                    "slots" : [t1,t2]
                }]
                
                if v[7] == float:
                    pass
                ch = 1
                            
            
            elif var1 == "L":
                sec_type = "Lecture"
                sec_no_test = sec_no
                sec_no = str(v[6])
                
                if sec_no_test[0] == "P":
                    inst.append(dict1)
                
                if sec_no_test != sec_no and sec_no_test!= "":
                    instructors2=[]
                instructors2 = [v[7]] 
                room = v[8]
                dict2["section_type"] = sec_type
                dict2["section_number"] = sec_no
                dict2["room"] = room
                dict2["Instructors"] = instructors2
                
                ch = 2
            elif var1 == "T":
                if len(instructors3) != 0:
                    dict3["Instructors"] = instructors3
                sec_type = "Tutorial"
                sec_no = str(v[6]) 
                instructors3 = [v[7]]
                room = v[8]
                dict3["section_type"] = sec_type
                dict3["section_number"] = sec_no
                dict3["room"] = room
                instructors1 = [v[7]]
                ch=3

        else:
            if ch == 1:
                if type(v[7]) == float:
                    continue
                instructors1.append(v[7])
                
            
            
            elif ch == 2:
                if type(v[7]) == float:
                    pass 
                instructors2.append(v[7])
                
            
            
            elif ch == 3:
                if type(v[7]) == float:
                    continue
            
                instructors3.append(v[7])
        
            
    
    
    
    

    dict = {"course_code" : code,
            "course_title": title,  
            "credits" : {
                "lecture" : lecture_,
                "practical" : practical_,
                "units" : units_
            }
            } 
    
    if dict["course_code"] == "BIO F110":
        dict["sections"]= inst
    list_data.append(dict)


    
with open("TASK16.json","a") as file:
    json.dump(list_data,file,indent=2)








