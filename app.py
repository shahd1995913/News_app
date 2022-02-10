# Import libraries
from calendar import c
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

# Read the data file 
Economic_df = pd.read_csv('Economic_activity_current_basic_prices_years_2002_2009 _million_dinars.csv')

st.title("الناتج المحلي الإجمالي حسب النشاط الاقتصادي بالأسعار الأساسية الجارية للسنوات 2002-2009 (مليون دينار) مع تعداد السكاني")
st.subheader("تحليل البيانات باستخدام بايثون")


if Economic_df is not None:
    if st.checkbox("إظهار قاعدة البيانات"):
        if st.button("إظهار أول خمس صفوف في قاهدة البيانات"):
            st.write(Economic_df.head())
        if st.button("إظهار آخر خمس صفوف في قاعدة البيانات"):
            st.write(Economic_df.tail())
        




if Economic_df is not None:
    if st.checkbox("نوع البيانات لكل عمود"):
        st.text("نوع البيانات")
        st.write(Economic_df.dtypes)
        


if Economic_df is not None:
    df=st.radio ("ما البعد الذي تريد التحقق منه؟ "  ,   ('الصفوف','الأعمدة'))
    if df=='الصفوف':
        st.text("عدد الصفوف هو ")
        st.write(Economic_df.shape[0])
    if df=='الأعمدة':
        st.text("عدد الأعمدة هو")
        st.write(Economic_df.shape[1])


if st.button("هل هنالك بيانات مفقودة ؟"):
    if Economic_df is not None:
        test=Economic_df.isnull().values.any()
        if test==True:
            if st.checkbox( "توجد قيم مفقودة في قاعدة البيانات"):
                sns.heatmap(Economic_df.isnull())
                st.pyplot()
        else:
            st.success("لا توجد قيم مفقودة")


if st.button("فحص الطول قاعدة البيانات"):
      st.write(len(Economic_df))
        
if st.checkbox("إظهار ملخص عن قاعدة البيانات"):
        st.write(Economic_df.describe(include='all'))


if st.button("عن موقع الويب"):
    st.success("53تم بنائه من مجتمع رقم ")
    st.text("تحدي مجتمعات البرمجة")



def bar_chart1():
    #Creating the dataset
   
    Year = Economic_df["Year"]
    values = Economic_df["number of population"]

    fig = plt.figure(figsize = (10, 5))

    plt.bar(Year, values)
    plt.xlabel("The years from 2000-2009")
    plt.ylabel("population (Million)")
    plt.title("A study of the relationship between population numbers with progress in years in Jordan")
    st.pyplot(fig)


if st.checkbox("إظهار العلاقة ما بين عدد السكان و السنوات"):
    bar_chart1()
def bar_chart2():
    #Creating the dataset
   
    Year = Economic_df["Year"]
    Agriculture = Economic_df["Agriculture, hunting, forestry and fishing"]
    fig = plt.figure(figsize = (10, 5) )
    plt.bar(Year, Agriculture)
    plt.xlabel("The years from 2000-2009")
    plt.ylabel("production rate of  Agriculture, hunting, forestry and fishing")
    plt.title("A study of the relationship between production rate of [Agriculture, hunting, forestry and fishing]  with progress in years in Jordan")
    plt.plot(color="r")
    st.pyplot(fig)




if st.checkbox(" إظهار العلاقة ما بين معدل انتاج الزراعة و الصيد "):
    st.bar_chart(Economic_df)

    bar_chart2()

