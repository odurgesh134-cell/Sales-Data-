import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# Streamlit page config
st.set_page_config(page_title="Diwali Sales Dashboard", layout="wide")

# Title
st.title("📊 Diwali Sales Data Analysis Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload Diwali Sales CSV", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='unicode_escape')

    # Cleaning data
    if 'Status' in df.columns:
        df.drop(['Status'], axis=1, inplace=True, errors='ignore')
    if 'unnamed1' in df.columns:
        df.drop(['unnamed1'], axis=1, inplace=True, errors='ignore')

    df.dropna(inplace=True)
    df['Amount'] = df['Amount'].astype(int)

    # Show dataset
    st.subheader("📂 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📋 Dataset Info")
    st.write(df.describe())

    # Gender analysis
    st.subheader("👨‍🦰 Gender-wise Count")
    fig, ax = plt.subplots()
    ax = sns.countplot(x='Gender', data=df)
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(fig)

    sales_gen = df.groupby('Gender', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    st.subheader("💰 Total Sales by Gender")
    fig, ax = plt.subplots()
    sns.barplot(x='Gender', y='Amount', data=sales_gen, ax=ax)
    st.pyplot(fig)

    # Age Group analysis
    st.subheader("📊 Sales by Age Group")
    fig, ax = plt.subplots()
    ax = sns.countplot(x='Age Group', hue='Gender', data=df)
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(fig)

    sales_age = df.groupby('Age Group', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    fig, ax = plt.subplots()
    sns.barplot(x='Age Group', y='Amount', data=sales_age, ax=ax)
    st.pyplot(fig)

    # State analysis
    st.subheader("🏙️ Top 10 States by Orders")
    sales_state = df.groupby('State', as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.barplot(data=sales_state, x='State', y='Orders', ax=ax)
    st.pyplot(fig)

    st.subheader("💰 Top 10 States by Sales Amount")
    sales_state = df.groupby('State', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(15, 5))
    sns.barplot(data=sales_state, x='State', y='Amount', ax=ax)
    st.pyplot(fig)

    # Marital Status
    st.subheader("💍 Sales by Marital Status")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax = sns.countplot(data=df, x='Marital_Status')
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(fig)

    sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    fig, ax = plt.subplots(figsize=(6, 5))
    sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender', ax=ax)
    st.pyplot(fig)

    # Occupation
    st.subheader("💼 Sales by Occupation")
    fig, ax = plt.subplots(figsize=(20, 5))
    ax = sns.countplot(data=df, x='Occupation')
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(fig)

    sales_state = df.groupby('Occupation', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    fig, ax = plt.subplots(figsize=(20, 5))
    sns.barplot(data=sales_state, x='Occupation', y='Amount', ax=ax)
    st.pyplot(fig)

    # Product Category
    st.subheader("🛒 Sales by Product Category")
    fig, ax = plt.subplots(figsize=(20, 5))
    ax = sns.countplot(data=df, x='Product_Category')
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(fig)

    sales_state = df.groupby('Product_Category', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(20, 5))
    sns.barplot(data=sales_state, x='Product_Category', y='Amount', ax=ax)
    st.pyplot(fig)

    # Top Products
    st.subheader("🏆 Top 10 Selling Products")
    fig, ax = plt.subplots(figsize=(12, 7))
    df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar', ax=ax)
    st.pyplot(fig)

else:
    st.warning("Please upload a CSV file to continue.")
