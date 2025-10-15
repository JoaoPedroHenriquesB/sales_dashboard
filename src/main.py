from typing import Optional

import pandas as pd
import plotly.express as px
import streamlit as st


def calculate_kpis(df: pd.DataFrame) -> tuple:
    try:
        sales_by_product = df.groupby("Product")["Quantity"].sum().reset_index()
        sales_product_sorted = sales_by_product.sort_values(
            by="Quantity", ascending=False
        )

        total_revenue = df["Total ($)"].sum()
        total_units = df["Quantity"].sum()
        best_seller_name = sales_product_sorted.iloc[0]["Product"]

        return total_revenue, total_units, best_seller_name, sales_product_sorted
    except (KeyError, IndexError) as e:
        st.error(
            f"Error calculating KPIs. The CSV is missing an expected column or is empty: `{e}`. Please check your file."
        )
        return None, None, None, None


def display_charts(df: pd.DataFrame, sales_product_sorted: pd.DataFrame):
    try:
        # Best Selling Product Chart
        sales_product_chart = px.bar(
            sales_product_sorted,
            x="Product",
            y="Quantity",
            title="Best Selling Products",
            labels={"Product": "Products", "Quantity": "Total Sales"},
            template="plotly_dark",
        )
        sales_product_chart.update_xaxes(
            tickangle=45, tickfont=dict(size=14, color="white")
        )

        # Payment Method Chart
        payments_df = df["Payment Method"].value_counts().reset_index()
        payments_df.columns = ["method", "payments"]

        total_payments_chart = px.pie(
            payments_df,
            hole=0.1,
            names="method",
            values="payments",
            title="Most Used Payment Methods",
            labels={"method": "Methods", "payments": "Count"},
            template="plotly_dark",
        )
        total_payments_chart.update_traces(
            hovertemplate="Method: %{label}<br>Count: %{value}<br>Percentage: %{percent}<extra></extra>"
        )

        # City Sales Chart
        city_sales = df.groupby("City")["Quantity"].sum().reset_index()
        city_sales_sorted = city_sales.sort_values(by="Quantity", ascending=False)

        city_sales_chart = px.line(
            city_sales_sorted,
            markers=True,
            x="City",
            y="Quantity",
            title="Sales by City",
            labels={"City": "Cities", "Quantity": "Total Sales"},
            template="plotly_dark",
        )
        city_sales_chart.update_xaxes(
            tickangle=45, tickfont=dict(size=14, color="white")
        )

        # Sales Over Time Chart
        df["Sale Date"] = pd.to_datetime(
            df["Sale Date"],
            errors="coerce",
            dayfirst=True,
        )
        date_sales = df.groupby("Sale Date")["Quantity"].sum().reset_index()
        date_sales_sorted = date_sales.dropna(subset=["Sale Date"]).sort_values(
            by="Sale Date"
        )

        date_sales_chart = px.bar(
            date_sales_sorted,
            x="Sale Date",
            y="Quantity",
            title="Sales Over Time",
            labels={"Sale Date": "Date", "Quantity": "Total Sales"},
            template="plotly_dark",
        )

        date_sales_chart.update_xaxes(
            tickangle=45, tickfont=dict(size=14, color="white")
        )

        # Display charts
        st.plotly_chart(sales_product_chart, use_container_width=True)
        st.plotly_chart(city_sales_chart, use_container_width=True)
        st.plotly_chart(date_sales_chart, use_container_width=True)
        st.plotly_chart(total_payments_chart, use_container_width=True)

    except KeyError as e:
        st.error(
            f"Error creating charts. The CSV is missing an expected column: `{e}`. Please check your file."
        )


def main_page(uploaded_file: Optional[st.runtime.uploaded_file_manager.UploadedFile]):
    if uploaded_file is None:
        st.info("Please upload a CSV file through the sidebar to get started.")
        return

    st.title(f"Analysis for: {uploaded_file.name}")

    try:
        df = pd.read_csv(uploaded_file, sep=";")
        df.columns = df.columns.str.strip()
        if "Sale Date" in df.columns:
            df["Sale Date"] = pd.to_datetime(
                df["Sale Date"], errors="coerce", dayfirst=True
            )
    except Exception as e:
        st.error(
            f"Failed to read the CSV file. Please ensure it is a valid, semicolon-separated file. Error: {e}"
        )
        return

    total_revenue, total_units, best_seller_name, sales_product_sorted = calculate_kpis(
        df
    )

    if total_revenue is not None:
        # --- KPI Section ---
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Total Revenue", f"${total_revenue:,.2f}")
        with col2:
            st.metric("Total Units Sold", f"{total_units:,}")
        with col3:
            st.metric("Best Seller", best_seller_name)
        with col4:
            st.metric("Best City", df["City"].mode()[0])
        with col5:
            st.metric("Most Used Payment Method", df["Payment Method"].mode()[0])

        # if pd.api.types.is_datetime64_any_dtype(df["Sale Date"]):
        #     best_month = int(df["Sale Date"].dt.month.mode()[0])
        #     st.metric("Best Month", best_month)
        # else:
        #     st.metric("Best Month", "Invalid Dates")

        st.markdown("---")
        display_charts(df, sales_product_sorted)


if __name__ == "__main__":
    st.set_page_config(page_title="Intelligent Dashboard", layout="wide")

    # --- Sidebar ---
    with st.sidebar:
        st.title("Welcome")
        uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    # --- Main Page ---
    main_page(uploaded_file)
