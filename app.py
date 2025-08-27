import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Diwali Sales Analysis", layout="wide")

st.title("🪔 Diwali Sales Data Analysis")

@st.cache_data
def load_data():
    df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
    df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
    df.dropna(inplace=True)
    df['Amount'] = df['Amount'].astype(int)
    return df

df = load_data()

with st.expander("🔍 View Dataset"):
    st.dataframe(df.head())

with st.expander("📊 Dataset Summary"):
    st.write("**Shape of dataset:**", df.shape)
    st.write("**Columns:**", df.columns.tolist())
    st.write("**Data Types:**")
    st.dataframe(df.dtypes)
    st.write("**Statistical Summary:**")
    st.dataframe(df.describe())

# Gender Analysis
st.subheader("🧑‍🤝‍🧑 Gender-wise Count and Sales")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Count Plot**")
    fig, ax = plt.subplots()
    ax = sns.countplot(x='Gender', data=df)
    for bars in ax.containers:
        ax.bar_label(bars)
    st.pyplot(fig)

with col2:
    st.markdown("**Total Sales by Gender**")
    sales_gen = df.groupby('Gender', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    fig2, ax2 = plt.subplots()
    sns.barplot(x='Gender', y='Amount', data=sales_gen, ax=ax2)
    st.pyplot(fig2)

# Age Group Analysis
st.subheader("🎂 Age Group-wise Sales and Distribution")

fig3, ax3 = plt.subplots()
ax3 = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax3.containers:
    ax3.bar_label(bars)
st.pyplot(fig3)

sales_age = df.groupby('Age Group', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
fig4, ax4 = plt.subplots()
sns.barplot(x='Age Group', y='Amount', data=sales_age, ax=ax4)
st.pyplot(fig4)

# State Analysis
st.subheader("📍 Top 10 States by Orders and Sales")

sales_state_orders = df.groupby('State', as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
fig5, ax5 = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_state_orders, x='State', y='Orders', ax=ax5)
st.pyplot(fig5)

sales_state_amount = df.groupby('State', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
fig6, ax6 = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_state_amount, x='State', y='Amount', ax=ax6)
st.pyplot(fig6)

# Marital Status
st.subheader("💍 Sales by Marital Status")

fig7, ax7 = plt.subplots(figsize=(7, 5))
ax7 = sns.countplot(data=df, x='Marital_Status')
for bars in ax7.containers:
    ax7.bar_label(bars)
st.pyplot(fig7)

sales_married = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
fig8, ax8 = plt.subplots(figsize=(6, 5))
sns.barplot(data=sales_married, x='Marital_Status', y='Amount', hue='Gender', ax=ax8)
st.pyplot(fig8)

# Occupation Analysis
st.subheader("👨‍💼 Sales by Occupation")

fig9, ax9 = plt.subplots(figsize=(20, 5))
ax9 = sns.countplot(data=df, x='Occupation')
for bars in ax9.containers:
    ax9.bar_label(bars)
st.pyplot(fig9)

sales_occupation = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
fig10, ax10 = plt.subplots(figsize=(20, 5))
sns.barplot(data=sales_occupation, x='Occupation', y='Amount', ax=ax10)
st.pyplot(fig10)

# Product Category Analysis
st.subheader("📦 Sales by Product Category")

fig11, ax11 = plt.subplots(figsize=(20, 5))
ax11 = sns.countplot(data=df, x='Product_Category')
for bars in ax11.containers:
    ax11.bar_label(bars)
st.pyplot(fig11)

sales_category = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
fig12, ax12 = plt.subplots(figsize=(20, 5))
sns.barplot(data=sales_category, x='Product_Category', y='Amount', ax=ax12)
st.pyplot(fig12)

# Top Selling Products
st.subheader("🏆 Top 10 Products by Number of Orders")

fig13, ax13 = plt.subplots(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar', ax=ax13)
st.pyplot(fig13)

st.markdown("---")
st.markdown("🔚 **End of Diwali Sales Analysis**")
