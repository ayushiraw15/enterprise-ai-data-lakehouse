from faker import Faker
import random
import pandas as pd

# Initialize Faker
fake = Faker("en_IN")

# Sample data
cities = [
    "Delhi",
    "Mumbai",
    "Jaipur",
    "Pune",
    "Hyderabad",
    "Bangalore",
    "Chennai"
]

merchants = [
    "Amazon",
    "Flipkart",
    "Swiggy",
    "Zomato",
    "Paytm",
    "Uber",
    "ATM"
]

devices = [
    "Mobile",
    "Laptop",
    "Tablet"
]

transactions = []

for i in range(1000):

    amount = round(random.uniform(100, 100000), 2)

    if amount > 50000:
        status = "Fraud"
    else:
        status = "Normal"

    transactions.append({

        "transaction_id": f"T{i+1}",

        "customer_name": fake.name(),

        "city": random.choice(cities),

        "merchant": random.choice(merchants),

        "device": random.choice(devices),

        "amount": amount,

        "status": status

    })

df = pd.DataFrame(transactions)

df.to_csv("data/raw/transactions.csv", index=False)

print(df.head())

print("\nDataset Created Successfully!")