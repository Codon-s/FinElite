import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Credit Card Bank Analysis",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Bank Analysis Dashboard")
st.markdown("### Customer Financial & Credit Analysis")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
uploaded_file = st.sidebar.file_uploader(
    "Upload Credit Card Bank Excel File",
    type=["xlsx"]
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.sidebar.success("Dataset Loaded Successfully!")

else:
    st.warning("Please upload the Credit Card Bank Excel file.")
    st.stop()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
st.sidebar.title("📊 Analysis Menu")

option = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Dataset Overview",
        "Distribution Analysis",
        "Boxplot Analysis",
        "Relationship Analysis",
        "Categorical Analysis",
        "Pairplot Analysis",
        "Customer Insights",
        "Regression Analysis"
    ]
)


# ==================================================
# 1. DATASET OVERVIEW
# ==================================================
if option == "Dataset Overview":

    st.header("📋 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())
    col4.metric("Duplicate Rows", df.duplicated().sum())

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)

    st.subheader("Column Names")
    st.write(list(df.columns))

    st.subheader("Data Types")
    st.dataframe(
        pd.DataFrame({
            "Column": df.columns,
            "Data Type": df.dtypes.astype(str).values
        }),
        use_container_width=True
    )

    st.subheader("Statistical Summary")
    st.dataframe(df.describe(), use_container_width=True)

    st.subheader("Missing Values")
    missing = df.isnull().sum()

    missing_df = pd.DataFrame({
        "Column": missing.index,
        "Missing Values": missing.values
    })

    st.dataframe(missing_df, use_container_width=True)


# ==================================================
# 2. DISTRIBUTION ANALYSIS
# ==================================================
elif option == "Distribution Analysis":

    st.header("📈 Distribution Analysis")

    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    # Age
    sb.histplot(
        df["Age"],
        bins=20,
        kde=True,
        color="teal",
        ax=axes[0, 0]
    )
    axes[0, 0].set_title("Age Distribution")

    # Annual Income
    sb.histplot(
        df["Annual_Income"],
        bins=20,
        kde=True,
        color="red",
        ax=axes[0, 1]
    )
    axes[0, 1].set_title("Annual Income")

    # Savings
    sb.histplot(
        df["Savings_Balance"],
        bins=15,
        kde=True,
        color="brown",
        ax=axes[0, 2]
    )
    axes[0, 2].set_title("Savings Balance")

    # Credit History
    sb.histplot(
        df["Credit_History_Years"],
        bins=15,
        kde=True,
        color="green",
        ax=axes[1, 0]
    )
    axes[1, 0].set_title("Credit History Years")

    # Existing Cards
    sb.histplot(
        df["Existing_Credit_Cards"],
        bins=15,
        kde=True,
        color="orange",
        ax=axes[1, 1]
    )
    axes[1, 1].set_title("Existing Credit Cards")

    # Investment
    sb.histplot(
        df["Investment_Value"],
        bins=15,
        kde=True,
        color="plum",
        ax=axes[1, 2]
    )
    axes[1, 2].set_title("Investment Value")

    plt.suptitle(
        "Distribution Analysis of Customer Financial & Demographic Features",
        fontsize=16,
        fontweight="bold"
    )

    plt.tight_layout()

    st.pyplot(fig)


# ==================================================
# 3. BOXPLOT ANALYSIS
# ==================================================
elif option == "Boxplot Analysis":

    st.header("📦 Boxplot Analysis")

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))

    sb.boxplot(
        x=df["Age"],
        color="lightgreen",
        ax=axes[0, 0]
    )
    axes[0, 0].set_title("Age Distribution")

    sb.boxplot(
        x=df["Monthly_Income"],
        color="yellowgreen",
        ax=axes[0, 1]
    )
    axes[0, 1].set_title("Monthly Income Distribution")

    sb.boxplot(
        x=df["Annual_Income"],
        color="turquoise",
        ax=axes[1, 0]
    )
    axes[1, 0].set_title("Annual Income Distribution")

    sb.boxplot(
        x=df["Credit_Limit"],
        color="olive",
        ax=axes[1, 1]
    )
    axes[1, 1].set_title("Credit Limit Distribution")

    plt.suptitle(
        "Financial Feature Distribution",
        fontsize=16,
        fontweight="bold"
    )

    plt.tight_layout()

    st.pyplot(fig)

    # Defaults
    st.subheader("Number of Defaults")

    fig2, ax = plt.subplots(figsize=(8, 4))

    sb.boxplot(
        x=df["Number_of_Defaults"],
        ax=ax
    )

    ax.set_title("Distribution of Number of Defaults")
    ax.set_xlabel("Number of Defaults")

    st.pyplot(fig2)


# ==================================================
# 4. RELATIONSHIP ANALYSIS
# ==================================================
elif option == "Relationship Analysis":

    st.header("🔗 Customer Financial Relationships")

    fig, axes = plt.subplots(3, 3, figsize=(18, 15))

    # 1
    sb.scatterplot(
        x=df["Savings_Balance"],
        y=df["Investment_Value"],
        color="teal",
        ax=axes[0, 0]
    )
    axes[0, 0].set_title("Savings vs Investment")

    # 2
    sb.scatterplot(
        x=df["Monthly_Income"],
        y=df["Credit_Limit"],
        color="khaki",
        ax=axes[0, 1]
    )
    axes[0, 1].set_title("Monthly Income vs Credit Limit")

    # 3
    sb.scatterplot(
        x=df["Debt_To_Income_Ratio"],
        y=df["Credit_Score"],
        color="royalblue",
        ax=axes[0, 2]
    )
    axes[0, 2].set_title("Debt Ratio vs Credit Score")

    # 4
    sb.scatterplot(
        x=df["Annual_Income"],
        y=df["Credit_Limit"],
        color="green",
        ax=axes[1, 0]
    )
    axes[1, 0].set_title("Annual Income vs Credit Limit")

    # 5
    sb.scatterplot(
        x=df["Existing_Credit_Cards"],
        y=df["Credit_Score"],
        color="orchid",
        ax=axes[1, 1]
    )
    axes[1, 1].set_title("Existing Cards vs Credit Score")

    # 6
    sb.scatterplot(
        x=df["Monthly_Income"],
        y=df["Savings_Balance"],
        color="peru",
        ax=axes[1, 2]
    )
    axes[1, 2].set_title("Monthly Income vs Savings")

    # 7
    sb.scatterplot(
        x=df["Credit_History_Years"],
        y=df["Credit_Score"],
        color="red",
        ax=axes[2, 0]
    )
    axes[2, 0].set_title("Credit History vs Credit Score")

    # 8
    sb.scatterplot(
        x=df["Monthly_Income"],
        y=df["Annual_Income"],
        hue=df["Gender"],
        ax=axes[2, 1]
    )
    axes[2, 1].set_title("Monthly Income vs Annual Income")

    # Empty subplot
    axes[2, 2].axis("off")

    plt.suptitle(
        "Customer Financial & Credit Analysis",
        fontsize=18,
        fontweight="bold"
    )

    plt.tight_layout()

    st.pyplot(fig)


# ==================================================
# 5. CATEGORICAL ANALYSIS
# ==================================================
elif option == "Categorical Analysis":

    st.header("📊 Categorical Analysis")

    fig, axes = plt.subplots(3, 3, figsize=(18, 15))

    # Gender
    sb.countplot(
        x=df["Gender"],
        color="skyblue",
        ax=axes[0, 0]
    )
    axes[0, 0].set_title("Gender Distribution")

    # Employment
    sb.countplot(
        x=df["Employment_Type"],
        color="teal",
        ax=axes[0, 1]
    )
    axes[0, 1].set_title("Employment Type")

    # Residential
    sb.countplot(
        x=df["Residential_Status"],
        color="gold",
        ax=axes[0, 2]
    )
    axes[0, 2].set_title("Residential Status")

    # Fraud
    sb.countplot(
        x=df["Fraud_Flag"],
        color="red",
        ax=axes[1, 0]
    )
    axes[1, 0].set_title("Fraud Flag")

    # Loan Count
    sb.countplot(
        x=df["Loan_Count"],
        color="orange",
        ax=axes[1, 1]
    )
    axes[1, 1].set_title("Loan Count")

    # Existing Cards
    sb.countplot(
        x=df["Existing_Credit_Cards"],
        color="green",
        ax=axes[1, 2]
    )
    axes[1, 2].set_title("Existing Credit Cards")

    # Occupation
    sb.countplot(
        x=df["Occupation"],
        color="purple",
        ax=axes[2, 0]
    )

    axes[2, 0].tick_params(axis="x", rotation=90)
    axes[2, 0].set_title("Occupation")

    axes[2, 1].axis("off")
    axes[2, 2].axis("off")

    plt.suptitle(
        "Customer Demographic and Credit Features",
        fontsize=18,
        fontweight="bold"
    )

    plt.tight_layout()

    st.pyplot(fig)


# ==================================================
# 6. PAIRPLOT
# ==================================================
elif option == "Pairplot Analysis":

    st.header("🔍 Pairplot Analysis")

    pair_data = df[
        [
            "Age",
            "Monthly_Income",
            "Credit_Score",
            "Credit_Limit",
            "Credit_Utilization",
            "Debt_To_Income_Ratio"
        ]
    ]

    fig = sb.pairplot(pair_data)

    st.pyplot(fig)


# ==================================================
# 7. CUSTOMER INSIGHTS
# ==================================================
elif option == "Customer Insights":

    st.header("💡 Customer Insights")

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))

    # Gender vs Credit Score
    sb.barplot(
        x=df["Gender"],
        y=df["Credit_Score"],
        color="steelblue",
        ax=axes[0, 0]
    )
    axes[0, 0].set_title("Gender vs Credit Score")

    # Loan Count vs Credit Score
    sb.barplot(
        x=df["Loan_Count"],
        y=df["Credit_Score"],
        color="orange",
        ax=axes[0, 1]
    )
    axes[0, 1].set_title("Loan Count vs Credit Score")

    # Gender vs Monthly Income
    sb.barplot(
        x=df["Gender"],
        y=df["Monthly_Income"],
        color="green",
        ax=axes[0, 2]
    )
    axes[0, 2].set_title("Gender vs Monthly Income")

    # Gender vs Annual Income
    sb.barplot(
        x=df["Gender"],
        y=df["Annual_Income"],
        color="purple",
        ax=axes[1, 0]
    )
    axes[1, 0].set_title("Gender vs Annual Income")

    # Occupation vs Credit Limit
    sb.barplot(
        x=df["Occupation"],
        y=df["Credit_Limit"],
        color="brown",
        ax=axes[1, 1]
    )

    axes[1, 1].tick_params(axis="x", rotation=90)
    axes[1, 1].set_title("Occupation vs Credit Limit")

    # Employment vs Income
    sb.barplot(
        x=df["Employment_Type"],
        y=df["Monthly_Income"],
        color="teal",
        ax=axes[1, 2]
    )
    axes[1, 2].set_title("Employment Type vs Monthly Income")

    plt.suptitle(
        "Customer Insights",
        fontsize=18,
        fontweight="bold"
    )

    plt.tight_layout()

    st.pyplot(fig)


# ==================================================
# 8. REGRESSION ANALYSIS
# ==================================================
elif option == "Regression Analysis":

    st.header("📉 Regression Analysis")

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Monthly Income vs Credit Score
    sb.regplot(
        x=df["Monthly_Income"],
        y=df["Credit_Score"],
        color="slategray",
        ax=axes[0]
    )
    axes[0].set_title("Monthly Income vs Credit Score")

    # Debt Ratio vs Credit Score
    sb.regplot(
        x=df["Debt_To_Income_Ratio"],
        y=df["Credit_Score"],
        color="tan",
        ax=axes[1]
    )
    axes[1].set_title("Debt Ratio vs Credit Score")

    plt.tight_layout()

    st.pyplot(fig)
