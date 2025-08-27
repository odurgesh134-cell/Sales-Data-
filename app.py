import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit page configuration
st.set_page_config(page_title="Diwali Sales Dashboard", layout="wide")
st.title("Diwali Sales Data Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\odurg\Downloads\Python_Diwali_Sales_Analysis-main (2)\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv")
    df.drop(['Status', 'unnamed1'], axis=1, errors='ignore', inplace=True)
    df.dropna(inplace=True)
    df['Amount'] = df['Amount'].astype(int)
    return df

df = load_data()

# Dataset preview
with st.expander(" Preview Dataset"):
    st.dataframe(df)

# Gender-based Analysis
st.subheader(" Gender-based Analysis")
col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    sns.countplot(x='Gender', data=df, ax=ax1)
    ax1.set_title("Count by Gender")
    for container in ax1.containers:
        ax1.bar_label(container)
    st.pyplot(fig1)

with col2:
    sales_gen = df.groupby('Gender', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    fig2, ax2 = plt.subplots()
    sns.barplot(x='Gender', y='Amount', data=sales_gen, ax=ax2)
    ax2.set_title("Sales by Gender")
    st.pyplot(fig2)

# Age Group-wise Analysis
st.subheader("Age Group-wise Analysis")
fig3, ax3 = plt.subplots()
sns.countplot(data=df, x='Age Group', hue='Gender', ax=ax3)
for container in ax3.containers:
    ax3.bar_label(container)
ax3.set_title("Gender Distribution by Age Group")
st.pyplot(fig3)

sales_age = df.groupby('Age Group', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
fig4, ax4 = plt.subplots()
sns.barplot(x='Age Group', y='Amount', data=sales_age, ax=ax4)
ax4.set_title("Sales by Age Group")
st.pyplot(fig4)

# State-wise Analysis
st.subheader("Top 10 States by Orders & Sales")

sales_state_orders = df.groupby('State', as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
fig5, ax5 = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_state_orders, x='State', y='Orders', ax=ax5)
ax5.set_title("Top 10 States by Orders")
plt.xticks(rotation=45)
st.pyplot(fig5)

sales_state_amount = df.groupby('State', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
fig6, ax6 = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_state_amount, x='State', y='Amount', ax=ax6)
ax6.set_title("Top 10 States by Sales")
plt.xticks(rotation=45)
st.pyplot(fig6)

# Marital Status & Gender
st.subheader("Sales by Marital Status and Gender")
sales_marital = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum()
fig7, ax7 = plt.subplots(figsize=(6, 5))
sns.barplot(data=sales_marital, x='Marital_Status', y='Amount', hue='Gender', ax=ax7)
ax7.set_title("Sales by Marital Status")
st.pyplot(fig7)

# Occupation Analysis
st.subheader("Occupation-based Sales Analysis")

fig8, ax8 = plt.subplots(figsize=(20, 5))
sns.countplot(data=df, x='Occupation', ax=ax8)
for container in ax8.containers:
    ax8.bar_label(container)
ax8.set_title("Number of Orders by Occupation")
plt.xticks(rotation=45)
st.pyplot(fig8)

sales_occ = df.groupby('Occupation', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
fig9, ax9 = plt.subplots(figsize=(20, 5))
sns.barplot(data=sales_occ, x='Occupation', y='Amount', ax=ax9)
ax9.set_title("Sales by Occupation")
plt.xticks(rotation=45)
st.pyplot(fig9)

# Product Category Analysis
st.subheader("Product Category Sales Analysis")

fig10, ax10 = plt.subplots(figsize=(20, 5))
sns.countplot(data=df, x='Product_Category', ax=ax10)
for container in ax10.containers:
    ax10.bar_label(container)
ax10.set_title("Orders by Product Category")
plt.xticks(rotation=45)
st.pyplot(fig10)

sales_prod = df.groupby('Product_Category', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
fig11, ax11 = plt.subplots(figsize=(20, 5))
sns.barplot(data=sales_prod, x='Product_Category', y='Amount', ax=ax11)
ax11.set_title("Top 10 Product Categories by Sales")
plt.xticks(rotation=45)
st.pyplot(fig11)

# Product-wise Top Sellers
st.subheader("Top 10 Selling Products by Orders")
top_products = df.groupby('Product_ID')['Orders'].sum().nlargest(10)
fig12, ax12 = plt.subplots(figsize=(12, 6))
top_products.plot(kind='bar', ax=ax12)
ax12.set_title("Top 10 Products by Orders")
ax12.set_xlabel("Product ID")
ax12.set_ylabel("Total Orders")
st.pyplot(fig12)

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | Data Source: Diwali Sales CSV")
