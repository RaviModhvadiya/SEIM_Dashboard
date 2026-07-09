from services.log_parser import parse_csv

df = parse_csv("uploads/sample.csv")

print(df.head())