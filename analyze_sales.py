import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_sales_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # --- Sales Overview ---
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce').fillna(0)
    df.set_index('Date', inplace=True)
    monthly_sales = df['Amount'].resample('M').sum()
    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind='line')
    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Sales Amount')
    plt.grid(True)
    plt.savefig('monthly_sales_trend.png')
    plt.close()
    print("Sales overview analysis complete. monthly_sales_trend.png saved.")

    # --- Product Analysis ---
    plt.figure(figsize=(10, 5))
    top_categories = df['Category'].value_counts().head(10)
    sns.barplot(x=top_categories.index, y=top_categories.values)
    plt.title('Top 10 Product Categories by Orders')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_categories.png')
    plt.close()

    plt.figure(figsize=(10, 5))
    top_sizes = df['Size'].value_counts().head(10)
    sns.barplot(x=top_sizes.index, y=top_sizes.values)
    plt.title('Top 10 Product Sizes Sold')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_sizes.png')
    plt.close()

    plt.figure(figsize=(10, 5))
    top_products = df.groupby('Category')['Qty'].sum().sort_values(ascending=False).head(10)
    sns.barplot(x=top_products.index, y=top_products.values)
    plt.title('Top 10 Product Categories by Quantity Sold')
    plt.ylabel('Total Quantity Sold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_products_by_qty.png')
    plt.close()
    print("Product analysis complete. Plots saved: top_categories.png, top_sizes.png, top_products_by_qty.png.")

    # --- Fulfillment Analysis ---
    plt.figure(figsize=(8, 5))
    fulfillment_counts = df['Fulfilment'].value_counts()
    sns.barplot(x=fulfillment_counts.index, y=fulfillment_counts.values)
    plt.title('Fulfillment Methods Used')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('fulfillment_methods.png')
    plt.close()

    # Delivery effectiveness: % delivered vs cancelled
    delivered = df[df['Status'].str.contains('Delivered', na=False)].shape[0]
    cancelled = df[df['Status'].str.contains('Cancelled', na=False)].shape[0]
    total_orders = df.shape[0]
    print(f"Delivery effectiveness: Delivered: {delivered}, Cancelled: {cancelled}, Total Orders: {total_orders}")

    # --- Customer Segmentation ---
    # By order frequency
    customer_orders = df['Order ID'].value_counts()
    plt.figure(figsize=(8, 5))
    sns.histplot(customer_orders, bins=20, kde=False)
    plt.title('Customer Order Frequency Distribution')
    plt.xlabel('Number of Orders per Customer')
    plt.ylabel('Number of Customers')
    plt.tight_layout()
    plt.savefig('customer_order_frequency.png')
    plt.close()

    # By location (city)
    top_cities = df['ship-city'].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_cities.index, y=top_cities.values)
    plt.title('Top 10 Cities by Orders')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_cities.png')
    plt.close()

    # --- Geographical Analysis ---
    top_states = df['ship-state'].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=top_states.index, y=top_states.values)
    plt.title('Top 10 States by Orders')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('top_states.png')
    plt.close()

    # --- Business Insights ---
    print("\n--- Business Insights & Recommendations ---")
    print(f"1. Sales are highest in these months: {monthly_sales.idxmax().strftime('%B %Y')} with {monthly_sales.max():.2f} in sales.")
    print(f"2. Most popular product categories: {', '.join(top_categories.index[:3])}.")
    print(f"3. Most common fulfillment method: {fulfillment_counts.idxmax()}.")
    print(f"4. Top customer locations: {', '.join(top_cities.index[:3])}.")
    print(f"5. Recommend focusing marketing on top states: {', '.join(top_states.index[:3])}.")
    print("6. Consider strategies to reduce cancellations and improve delivery effectiveness.")
    print("7. Stock popular sizes and categories to maximize sales.")
    print("8. Segment customers for targeted promotions based on order frequency and location.")

if __name__ == "__main__":
    analyze_sales_data('Amazon Sale Report.csv')
