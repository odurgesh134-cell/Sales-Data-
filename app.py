pip  install seaborn pandas matplotlib
import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

st.set_page_config(page_title="Diwali Sales Dashboard", layout="wide")
st.title("🪔 Diwali Sales Data Analysis Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')
    df.drop(['Status', 'unnamed1'], axis=1, errors='ignore', inplace=True)
    df.dropna(inplace=True)
    df['Amount'] = df['Amount'].astype(int)
    return df

df = load_data()

with st.expander("🔍 Preview Dataset"):
    st.dataframe(df)

st.subheader("👫 Gender-based Analysis")
col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    ax1 = sns.countplot(x='Gender', data=df)
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

# Age Group Analysis
st.subheader("🎂 Age Group-wise Analysis")
fig3, ax3 = plt.subplots()
ax3 = sns.countplot(data=df, x='Age Group', hue='Gender')
for container in ax3.containers:
    ax3.bar_label(container)
ax3.set_title("Gender Distribution by Age Group")
st.pyplot(fig3)

sales_age = df.groupby('Age Group', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
fig4, ax4 = plt.subplots()
sns.barplot(x='Age Group', y='Amount', data=sales_age, ax=ax4)
ax4.set_title("Sales by Age Group")
st.pyplot(fig4)

st.subheader("📍 Top 10 States by Orders & Sales")
sales_state_orders = df.groupby('State', as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
fig5, ax5 = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_state_orders, x='State', y='Orders', ax=ax5)
ax5.set_title("Top 10 States by Orders")
st.pyplot(fig5)

sales_state_amount = df.groupby('State', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
fig6, ax6 = plt.subplots(figsize=(15, 5))
sns.barplot(data=sales_state_amount, x='State', y='Amount', ax=ax6)
ax6.set_title("Top 10 States by Sales")
st.pyplot(fig6)

st.subheader("💍 Sales by Marital Status and Gender")
fig7, ax7 = plt.subplots(figsize=(6, 5))
sns.barplot(data=df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum(), 
            x='Marital_Status', y='Amount', hue='Gender', ax=ax7)
ax7.set_title("Sales by Marital Status")
st.pyplot(fig7)

st.subheader("💼 Occupation-based Sales Analysis")
fig8, ax8 = plt.subplots(figsize=(20, 5))
ax8 = sns.countplot(data=df, x='Occupation')
for container in ax8.containers:
    ax8.bar_label(container)
ax8.set_title("Number of Orders by Occupation")
st.pyplot(fig8)

sales_occ = df.groupby('Occupation', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
fig9, ax9 = plt.subplots(figsize=(20, 5))
sns.barplot(data=sales_occ, x='Occupation', y='Amount', ax=ax9)
ax9.set_title("Sales by Occupation")
st.pyplot(fig9)

st.subheader("📦 Product Category Sales Analysis")
fig10, ax10 = plt.subplots(figsize=(20, 5))
ax10 = sns.countplot(data=df, x='Product_Category')
for container in ax10.containers:
    ax10.bar_label(container)
ax10.set_title("Orders by Product Category")
st.pyplot(fig10)

sales_prod = df.groupby('Product_Category', as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
fig11, ax11 = plt.subplots(figsize=(20, 5))
sns.barplot(data=sales_prod, x='Product_Category', y='Amount', ax=ax11)
ax11.set_title("Top 10 Product Categories by Sales")
st.pyplot(fig11)

st.subheader("🏆 Top 10 Selling Products by Orders")
fig12, ax12 = plt.subplots(figsize=(12, 6))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).plot(kind='bar', ax=ax12)
ax12.set_title("Top 10 Products by Orders")
st.pyplot(fig12)

st.markdown("---")
st.markdown("📊 Built with Streamlit | 📁 Data Source: Diwali Sales CSV")
