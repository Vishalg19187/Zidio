import pandas as pd

# Load dataset
df = pd.read_excel("gpt stock data.xlsx", sheet_name="Sheet1")

print("Original shape:", df.shape)

# 1. Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 2. Drop rows where date is missing
df = df.dropna(subset=["date"])

# 3. Handle missing values
# Fill missing numeric values with median
num_cols = ["open", "close", "volume"]
for col in num_cols:
    if df[col].isnull().sum() > 0:
        df[col].fillna(df[col].median(), inplace=True)

# Fill missing ticker values with mode
if df["ticker"].isnull().sum() > 0:
    df["ticker"].fillna(df["ticker"].mode()[0], inplace=True)

# 4. Remove duplicates
df.drop_duplicates(inplace=True)

# 5. Sort by date (just to keep data in order)
df.sort_values(by="date", inplace=True)

# 6. Save cleaned dataset
df.to_csv("cleaned_stock_data.csv", index=False)

print("Cleaned shape:", df.shape)
print("Cleaned dataset saved as cleaned_stock_data.csv")
