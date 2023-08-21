import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("service_account.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
#db.collection("LoginDetails").document("125_19_1_0038").set({"matric no":"125_19_1_0038","password":"students1234"})
#db.collection("LoginDetails").document("125_19_1_0014").set({"matric no":"125_19_1_0014","password":"students1234"})
#data1 = {"fname": "Muhammed","lname":"TAIRU","tname":"Lolade","programme":"Mathematics","department":"Mathematics and Statitics","faculty":"Natural and Applied Sciences"}
#data1 = {"fname": "Waliyullah","lname":"ADELAKUN","tname":"Adeleye","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data2 = {"fname": "Bukola","lname":"AJAGBE","tname":"Omolola","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data3 = {"fname": "Ridwan","lname":"DAUDA","tname":"Olalekan","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data4 = {"fname": "Segun","lname":"EEBO","tname":"Joseph","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data5 = {"fname": "Hammed","lname":"HASSAN","tname":"Eniola","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data7 = {"fname": "Jamiu","lname":"IBRAHIM","tname":"Ajadi","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data8 = {"fname": "John","lname":"IDOWU","tname":"Damilare","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data9 = {"fname": "Lateef","lname":"LAWAL","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data10 = {"fname": "Pelumi","lname":"MAKINDE","tname":"Akinola","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data11 = {"fname": "Joy","lname":"ODEBUNMI","tname":"Tolulope","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data12= {"fname": "Festus","lname":"OGUNIRAN","tname":"Akinola","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#data114 = {"fname": "Sulaimon","lname":"YISAU","tname":"Akinola","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}

#Pushing Student biodata into database

#db.collection("profile").document("students").collection("125_19_1_0038").document("Biodata").set(data1)
#db.collection("profile").document("students").collection("125_19_1_0014").document("biodata").set(data2)
#db.collection("profile").document("students").collection("125_19_1_0001").document("biodata").set(data1)
#db.collection("profile").document("students").collection("125_19_1_0002").document("biodata").set(data2)
#db.collection("profile").document("students").collection("125_19_1_0003").document("biodata").set(data3)
#db.collection("profile").document("students").collection("125_19_1_0004").document("biodata").set(data4)
#db.collection("profile").document("students").collection("125_19_1_0005").document("biodata").set(data5)
#db.collection("profile").document("students").collection("125_19_1_0007").document("biodata").set(data7)
#db.collection("profile").document("students").collection("125_19_1_0008").document("biodata").set(data8)
#db.collection("profile").document("students").collection("125_19_1_0009").document("biodata").set(data9)
#db.collection("profile").document("students").collection("125_19_1_0010").document("biodata").set(data10)
#db.collection("profile").document("students").collection("125_19_1_0011").document("biodata").set(data11)
#db.collection("profile").document("students").collection("125_19_1_0012").document("biodata").set(data12)
#db.collection("profile").document("students").delete()

#pushing Student login details into database

#db.collection("LoginDetails").document("125_19_1_0001").set({"matric no":"125_19_1_0001","password":"students1234"})
#db.collection("LoginDetails").document("125_19_1_0003").set({"matric no":"125_19_1_0003","password":"students1234"})
#db.collection("LoginDetails").document("125_19_1_0004").set({"matric no":"125_19_1_0004","password":"students1234"})
#db.collection("LoginDetails").document("125_19_1_0005").set({"matric no":"125_19_1_0005","password":"students1234"})
#db.collection("LoginDetails").document("125_19_1_0007").set({"matric no":"125_19_1_0007","password":"students1234"})
#db.collection("LoginDetails").document("125_19_1_0008").set({"matric no":"125_19_1_0008","password":"students1234"})
#db.collection("LoginDetails").document("125_19_1_0009").set({"matric no":"125_19_1_0009","password":"students1234"})
#db.collection("LoginDetails").document("125_19_1_0010").set({"matric no":"125_19_1_0010","password":"students1234"})
#db.collection("LoginDetails").document("125_19_1_0012").set({"matric no":"125_19_1_0012","password":"students1234"})
#db.collection("LoginDetails").document("125_19_2_0002").set({"matric no":"125_19_2_0002","password":"students1234"})
#db.collection("LoginDetails").document("125_19_2_0011").set({"matric no":"125_19_2_0011","password":"students1234"})
course1 = {"title":"Introduction to Computer","units":3,"lecturer":"Prof. Amubieya","status":"C"}
course2 = {"title":"Introduction to Software Engineering","units":3,"lecturer":"Prof. Shuaib","status":"R"}
course3 = {"title":"Introduction to Computer Hardware","units":2,"lecturer":"Prof. Shuaib","status":"E"}
course4 = {"title":" Software Testing","units":2,"lecturer":"Prof. Waliyullah","status":"C"}
course5 = {"title":"Software Economics","units":3,"lecturer":"Prof. Super","status":"R"}
db.collection("CourseRegistration").document("CSC223").set(course1)
db.collection("CourseRegistration").document("CSC232").set(course2)
db.collection("CourseRegistration").document("CSC234").set(course3)
db.collection("CourseRegistration").document("CSC243").set(course4)
db.collection("CourseRegistration").document("CSC224").set(course5)

#Pushing Lecturer Login details into database
#db.collection("LoginDetails").document("12345678SH").set({"matric no":"12345678AB","password":"lecturer1234"})
#db.collection("LoginDetails").document("12345678SU").set({"matric no":"12345678BC","password":"lecturer1234"})
#db.collection("LoginDetails").document("12345678WA").set({"matric no":"12345678CD","password":"lecturer1234"})
#db.collection("LoginDetails").document("12345678AM").set({"matric no":"12345678DE","password":"lecturer1234"})
#db.collection("LoginDetails").document("12345678EF").set({"matric no":"12345678EF","password":"lecturer1234"})

#Pushing Lecturer details into database

#lect1 = {"title":"Prof.","fname":"Amubieya","lname":"Akinola","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#lect2 = {"title":"Prof.","fname":"Shuaib","lname":"Yekeen","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#lect3 = {"title":"Prof.","fname":"Super","lname":"Asimiyu","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}
#lect4 = {"title":"Prof.","fname":"Waliyullah","lname":"Adewuyi","programme":"Computer Science","department":"Computer Science","faculty":"Natural and Applied Sciences"}

#db.collection("profile").document("lecturers").collection("12345678AM").document("biodata").set(lect1)
#db.collection("profile").document("lecturers").collection("12345678SH").document("biodata").set(lect2)
#db.collection("profile").document("lecturers").collection("12345678SU").document("biodata").set(lect3)
#db.collection("profile").document("lecturers").collection("12345678WA").document("biodata").set(lect4)

#results = db.collection("profile").list_documents()
#result = [doc.id for doc in results]
#print(db.collection("LoginDetails").document("125_19_1_0038").get().to_dict())
#print(result)
result1 = {"score":78,"grade":"A","point":15}
result2 = {"score":78,"grade":"A","point":15}
result3 = {"score":78,"grade":"A","point":15}
result4 = {"score":78,"grade":"A","point":15}
result5 = {"score":38,"grade":"F","point":0}
db.collection("Results").document("CSC123").collection("re").document("125_19_1_0014").set(result1)
db.collection("Results").document("CSC132").collection("re").document("125_19_1_0014").set(result2)
db.collection("Results").document("CSC134").collection("re").document("125_19_1_0014").set(result3)
db.collection("Results").document("CSC143").collection("re").document("125_19_1_0014").set(result4)
db.collection("Results").document("CSC124").collection("re").document("125_19_1_0014").set(result5)
#db.collection("profile").document("results").collection("12345678SU").document("biodata").set()
"""details = db.collection("profile").document("students").collection("125_19_1_0038").document("Biodata").get().to_dict()
print(details["lname"])"""