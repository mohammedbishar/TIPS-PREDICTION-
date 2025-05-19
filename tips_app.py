import streamlit as st
import pickle 
import numpy as pd
import pandas as pd

with open('model.pkl','rb') as model_file:
   model=pickle.load(model_file)

# streamlit UI for user input
st.title("tip prediction")

# input fields for the user
total_bill=st.number_input("total_bill")
sex=st.selectbox("sex",["Male","Female"])
smoker=st.selectbox("smoker",["No","Yes"])
day=st.selectbox("day",["Thur","Fri","Sat","Sun"])
time=st.selectbox("time",["Lunch","Dinner"])
size=st.number_input("size",min_value=1,max_value=10,value=2)

input_data=pd.DataFrame({
   "total_bill":[total_bill],
   "sex" :[sex],
   "smoker":[smoker],
   "day":[day],
   "time":[time],
   "size":[size]
})

#mapping categrical variable manually

sex_mapping={"Male":0,"Female":1}
smoker_mapping={"No":0,"Yes":1}
day_mapping={"Thur":0,"Fri":1,"Sat":2,"Sun":3}
time_mapping={"Lunch":0,"Dinner":1}

input_data['sex']=input_data['sex'].map(sex_mapping)
input_data['smoker']=input_data['smoker'].map(smoker_mapping)
input_data['day']=input_data['day'].map(day_mapping)
input_data['time']=input_data['time'].map(time_mapping)

# make the prediction
if st.button("predict tip"):
   prediction =model.predict(input_data)
   st.write(f"predicted tip:${round(prediction[0],2)}")