# info={
#     "name" : "nargis",
#     "subjects" : ["python","c","javascript"],
#     "topics" : ["dictionary","set"],
#     "age" :  20,
#     "is_adult" : "True",
#     "marks" : 89.0
# }
# print(info["name"])
# print(info["subjects"])
# print(info["topics"])
# info["name"] = "Ankit"
# print(info["name"])
# print(info)

students = {
    "name" : "rahul kumar",
    "score" : {
        "chem" : 98,
        "phy" : 100,
        "maths" : 89
            }
}
# print(students.keys())
# print(list(students.values()))
# print(students.items())
# pairs=list(students.items())
# print(pairs[0])
# print(pairs[1])
# print(students["name2"])
# print(students.get("name2"))
students.update({"city":"delhi"})
print(students)