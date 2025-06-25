import pandas as pd



data = [
    ("Alice",85 ,"Math", "B"),
    ("Bob", 90, "Science", "A"),
    ("Charlie",78,"History", "C"),
    ("Alice", 88,"Science", "B"),
    ("Bob", 92," Math" ,"A")
]
student_data = pd.DataFrame(data, columns=["Name", "Marks","Subject", "Grade"])
# print(student_data)
# print(student_data['Marks'])
student_data['Bonus_Marks'] =student_data["Marks"] * 0.10
# print(student_data)
group_by_name = student_data.groupby('Name').sum().reset_index()
#print(group_by_name[['Name','Marks','Bonus_Marks']])
group_by_name1 = student_data.groupby('Name').agg({
    'Marks': 'mean',
    'Bonus_Marks':'mean'
}).reset_index()
print(group_by_name1)
score_above_85 = student_data[student_data['Marks'] >85].reset_index()
print(score_above_85)

student_data.set_index('Subject', inplace =True)
print(student_data) 
student_data.reset_index(inplace= True)
print(student_data) 