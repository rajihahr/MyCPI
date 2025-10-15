import pandas as pd

# Load your dataset
df = pd.read_csv("/data/original_cpi_2d_core.csv")

# Clean whitespace or case issues
df["division"] = df["division"].astype(str).str.strip().str.lower()

# Create the mapping
division_map = {
    "overall": "Overall",
    "01": "Food and Beverages",
    "02": "Alcoholic Beverages & Tobacco",
    "03": "Clothing and Footwear",
    "04": "Housing, Utilities, Gas & Other Fuels",
    "05": "Household Furnishings, Equipment & Maintenance",
    "06": "Health",
    "07": "Transport",
    "08": "Information & Communication",
    "09": "Recreation, Sport & Culture",
    "10": "Education",
    "11": "Restaurant & Accommodation Services",
    "12": "Insurance & Financial Services and Personal Care",
    "13": "Social Protection & Miscellaneous Goods and Services"
}

# Map division names
df["division_name"] = df["division"].apply(lambda x: division_map.get(str(x), "Unknown"))

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Add readable month and year
df["month_name"] = df["date"].dt.strftime("%B")
df["year"] = df["date"].dt.year

# Add a clear, natural-language summary
df["summary"] = (
    "On " + df["month_name"] + " " + df["year"].astype(str) +
    ", the Core CPI for " + df["division_name"] +
    " was " + df["index"].astype(str) + "."
)

# Reorder columns for clarity
df = df[["date", "month_name", "year", "division_name", "index", "summary"]]

# Save the improved dataset
output_path = "/data/updated_cpi_2d_core_v1.csv"
df.to_csv(output_path, index=False)

print(f"✅ Enhanced file saved as {output_path}")