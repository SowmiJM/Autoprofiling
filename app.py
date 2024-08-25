import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report

def set_page_config():
    st.set_page_config(page_title="AnalyticSowmi", layout="wide")

def display_header():
    st.title("AnalyticSowmi")
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png", width=300)
    st.write("Welcome to AnalyticSowmi - Your Data Profiling Assistant")
    st.write("This app allows you to upload a CSV file and generate a comprehensive data profiling report.")

def upload_file():
    return st.file_uploader("Choose a CSV file", type="csv")

@st.cache_data
def load_csv(uploaded_file):
    return pd.read_csv(uploaded_file)

def display_data_preview(df):
    st.header("Data Preview")
    st.dataframe(df.head())

def generate_profile_report(df):
    st.header("Data Profiling Report")
    profile = ProfileReport(df, title="Profiling Report", explorative=True)
    st_profile_report(profile)

def main():
    set_page_config()
    display_header()
    
    uploaded_file = upload_file()

    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        display_data_preview(df)
        generate_profile_report(df)
    else:
        st.info("Upload a CSV file to get started.")

if __name__ == "__main__":
    main()