import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Results from CSV
results_df = pd.read_csv('s3://your-bucket/ecommerce_data/output/top_products.csv')

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(data=results_df, x='total_sales', y='product_category_name', palette='Blues_d')
plt.title('Top Selling Product Categories')
plt.xlabel('Total Sales')
plt.ylabel('Product Category')
plt.show()
