import streamlit as st
import pandas as pd
from datetime import date
import altair as alt
today = date.today()
global df 


#streamlit config
st.set_page_config(page_title="Explore Data", page_icon="🔬")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """<style>footer {visibility: hidden;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: #8062D6; padding:10px;'> Explore Data 🔬</h1>", unsafe_allow_html=True)
st.write("<hr><br>", unsafe_allow_html=True)

#setup file upload
file_upload = st.file_uploader(label="Upload data. (400MB Max)", type=['csv', 'xlsx',])

#df not defined fix

if file_upload is not None:
   
    print(f"\n{file_upload}")
    print("\n------------File uploaded!------------")
    try:
        df = pd.read_csv(file_upload)
    except Exception as e:
        print(e)
        df = pd.read_excel(file_upload)
try:
    st.markdown("<br><br>",unsafe_allow_html=True)

    

    st.markdown("<h2 style='text-align:center;'>Data Preview</h2>", unsafe_allow_html=True)

    #st.caption("Head")
    st.dataframe(df.head(10))
    st.caption("Tail")
    st.dataframe(df.tail(10))
    #Dataset MetaData
    st.write("<hr><br>", unsafe_allow_html=True)
    st.subheader("Dataset MetaData")
    dataset_meta_data = {'Headers':[len(df.columns)],'Rows':[f'{df.shape[0]:,}'],'Total Data Points':[f'{sum(df.count()):,}'], 'DF Dimensions':[f'{df.ndim:,}'],\
         'Dataset Size (MB)':[f'{file_upload.size/1000000:,}']}
    df_meta_data = pd.DataFrame(data=dataset_meta_data)
    st.table(df_meta_data)
    
    
    #Header display and count
    st.write("<hr><br>", unsafe_allow_html=True)
    st.subheader(f'\nHeaders: {len(df.columns)}\n')
    st.table(df.count())
    
    
    #dypes
    st.write("<hr><br>", unsafe_allow_html=True)
    st.subheader("Header Data Types")
    st.table(df.dtypes.astype(str))


    #data summary
    st.write("<hr><br>", unsafe_allow_html=True)
    st.subheader(f'\nDataset Summary\n')
    st.dataframe(df.describe())

    
    #missing values
    st.write("<hr><br>", unsafe_allow_html=True)
    st.subheader(f'\nMissing Values\n')
    st.table(df.isna().sum())

     #duplicate rows
    st.write("<hr><br>", unsafe_allow_html=True)

    st.subheader(f"Duplicate Rows")
    st.write('click expand icon to see all data headers')
    st.dataframe(df[df.duplicated()])
    st.write(len(df.duplicated))
 
    
    #visualize    
    #control_field = st.multiselect("Select A Field for a summary, values must be numerical", df.columns)
    #st.table(df[control_field].describe())
    #st.bar_chart(df[target_field].value_counts())
    

except Exception as e:
    print(e)
  
  

