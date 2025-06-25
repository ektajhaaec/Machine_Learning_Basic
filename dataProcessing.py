import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder, OneHotEncoder


# data = {
#     'age': [25, 30, 45, 35, 50],
#     'income': [50000, 60000, 80000, 70000, 90000],
#     'gender': ['Male', 'Female', 'Female', 'Male', 'Female'],
#     'education': ['Bachelor', 'Master', 'PhD', 'PhD', 'Bachelor']
# }

# df = pd.DataFrame(data)
# print(df['education'].str.lower().str.capitalize()) #Capitalize

# print(df['gender'].value_counts())

# min_max_scaler = MinMaxScaler()
# df['income_scaled'] = min_max_scaler.fit_transform(df[['income']])
# print(df[['income','income_scaled']])

# standard_scaler = StandardScaler()
# df['age_scaled'] = standard_scaler.fit_transform(df[['age']])
# print(df[['age','age_scaled']])

# bins = [0,30, 40, 60]
# labels =['Young', 'Middle-aged','Senior']
# df['age_group'] = pd.cut(df['age'],bins =bins, labels =labels)
# print(df[['age','age_group']])

# labelEncoder = LabelEncoder()
# df['gender_encoded'] = labelEncoder.fit_transform(df[['gender']])

# print(df[['gender' , 'gender_encoded']])

# df_encoded = pd.get_dummies(df, columns =['education'], prefix = 'edu')
# print(df_encoded)

data ={
"Student": ["A", "B", "C", "D", "E", "F", "G"],
"Math_Score": [85, 78, 90, 85, 95, 78, 88],
"Study_Hours": [10, 8, 12, 6, 15, 2, 11],
"Study_Group": ["Intermediate", "Beginner", "Advanced", "Beginner", "Advanced", "Beginner", "Intermediate"],
}

df = pd.DataFrame(data)
mean = df['Math_Score'].mean()
median = df['Math_Score'].median()
mode = df['Math_Score'].mode()
print(mode)

min_max_Scaler = MinMaxScaler()
df['normailzed_study_hour'] = min_max_Scaler.fit_transform(df[['Study_Hours']])
print(df["normailzed_study_hour"])

bins = [0, 6, 11, 15]
labels = ['Low', 'Medium', 'High']
df['binned_study_hours'] = pd.cut(df['Study_Hours'], bins = bins, labels =labels)
print(df[['Study_Hours','binned_study_hours']])

# label_Encoder = LabelEncoder()
# df['label_encoded_study_group'] = label_Encoder.fit_transform(df[['Study_Group']])

# print(df[['label_encoded_study_group','Study_Group']])
custom_mapping ={'Beginner':0 ,
                 'Intermediate':1 ,
                 'Advanced':2}
df['label_encoded_study_group'] = df['Study_Group'].map(custom_mapping)
print(df[['Study_Group','label_encoded_study_group']])