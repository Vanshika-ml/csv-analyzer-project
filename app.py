import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 CSV Analyzer")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("CSV Loaded Successfully ✅")

    st.subheader("First 5 Rows")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.subheader("Column Names")
    st.write(df.columns.tolist())

    st.subheader("Missing Values")
    st.dataframe(df.isnull().sum())

    st.subheader("Statistics")
    st.dataframe(df.describe())

    if st.button("Remove Missing Values"):
        df = df.dropna()
        st.success("Missing Values Removed ✅")

    numeric_df = df.select_dtypes(include=['number'])

    if not numeric_df.empty:

        st.subheader("Correlation Heatmap")

        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        st.subheader("Histograms")

        fig2 = plt.figure(figsize=(10, 6))
        numeric_df.hist(figsize=(10, 6))
        st.pyplot(fig2)

    csv = df.to_csv(index=False)

    st.download_button(
        "Download Cleaned CSV",
        csv,
        "cleaned_data.csv",
        "text/csv"
    )