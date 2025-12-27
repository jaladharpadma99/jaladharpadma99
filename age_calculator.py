import streamlit as st
import datetime
import pandas as pd
col1,col2=st.columns(2)
start_date=pd.to_datetime("1992-01-01")
def age_calculation(day):
    result=" "
    if day>=365:
        years=day//365
        leper=(years//4 if years>3 else 0)
        day=day-(years*365)-leper
        result+=str(years)+" "+"YEARS"+" "
    if day>=30:
        month=day//30
        day=day-(month*30)
        result+=str(month)+" "+"MONTHS"+" "
    if day>0:
        result+=str(day)+" "+"DAYS"
    return result
with col1:
  dob=st.date_input("ENTER YOUR DOB : ",min_value=start_date)
  today=datetime.date.today()
  day=(today-dob).days 
  if st.button("calculate"):
    if dob:
       st.success(f"NOW YOUR AGE : {age_calculation(day)}")
    else:
        st.warning("ENTER YOUR AGE ")