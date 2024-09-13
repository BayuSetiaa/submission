import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mengatur konfigurasi halaman dashboard
st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# Mengimpor dataset
def load_data(uploaded_file):
    if uploaded_file is not None:
        main_data = pd.read_csv(uploaded_file)
        return main_data
    else:
        st.error("Silakan unggah file CSV terlebih dahulu.")
        return None

# Preprocessing data
def preprocess_data(main_data):
    # Convert timestamps to datetime
    main_data['order_purchase_timestamp'] = pd.to_datetime(main_data['order_purchase_timestamp'])
    main_data['order_month_year'] = main_data['order_purchase_timestamp'].dt.to_period('M').astype(str)

    # Calculate repeat customers
    orders_per_customer = main_data.groupby('customer_id')['order_id'].nunique().reset_index()
    orders_per_customer.columns = ['customer_id', 'order_count']
    orders_per_customer['is_repeat_customer'] = orders_per_customer['order_count'] > 1

    # Merge repeat customer info back into main data
    main_data = pd.merge(main_data, orders_per_customer[['customer_id', 'is_repeat_customer']], on='customer_id', how='left')

    # Calculate average review score per customer
    avg_review_score_per_customer = main_data.groupby('customer_id')['review_score'].mean().reset_index()
    avg_review_score_per_customer.columns = ['customer_id', 'avg_review_score']

    # Merge with main data
    main_data = pd.merge(main_data, avg_review_score_per_customer, on='customer_id', how='left')

    return main_data

# Display retention analysis
def display_retention_analysis(main_data):
    st.header("Analisis Retensi Pelanggan")

    repeat_customers = main_data['is_repeat_customer'].value_counts(normalize=True) * 100
    st.write("Persentase Pelanggan Tetap:")
    st.write(repeat_customers)

    corr_factors = main_data[['is_repeat_customer', 'avg_review_score']].corr()
    st.write("Korelasi antara Pelanggan Tetap dan Skor Ulasan Rata-Rata:")
    st.write(corr_factors)

    fig, ax = plt.subplots()
    sns.boxplot(x='is_repeat_customer', y='avg_review_score', data=main_data, palette='Set2', ax=ax)
    ax.set_title('Hubungan antara Pelanggan Tetap dan Skor Ulasan Rata-Rata')
    st.pyplot(fig)

# Display sales trends
def display_sales_trends(main_data):
    st.header("Tren Penjualan Bulanan")

    monthly_order_trends = main_data.groupby('order_month_year')['order_id'].nunique().reset_index().rename(columns={'order_id': 'total_orders'})
    
    fig, ax = plt.subplots()
    sns.lineplot(data=monthly_order_trends, x='order_month_year', y='total_orders', marker='o', color='orange', ax=ax)
    ax.set_title('Tren Penjualan Bulanan')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Display top selling products
def display_top_products(main_data):
    st.header("Kategori Produk Terlaris")

    top_products = main_data['product_category_name'].value_counts().reset_index()
    top_products.columns = ['product_category_name', 'total_sold']

    st.write("10 Kategori Produk Terlaris:")
    st.write(top_products.head(10))

    fig, ax = plt.subplots()
    sns.barplot(data=top_products.head(10), x='total_sold', y='product_category_name', palette='viridis', ax=ax)
    ax.set_title('Kategori Produk Terlaris')
    st.pyplot(fig)

# Main function
def main():
    st.title("E-Commerce Dashboard")
    
    # Upload file
    uploaded_file = st.file_uploader("Unggah file CSV", type="csv")
    
    # Load data
    main_data = load_data(uploaded_file)
    
    if main_data is not None:
        # Preprocess data
        main_data = preprocess_data(main_data)

        # Display analyses
        display_retention_analysis(main_data)
        display_sales_trends(main_data)
        display_top_products(main_data)

if __name__ == "__main__":
    main()
