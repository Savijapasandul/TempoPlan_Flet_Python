import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables
load_dotenv()

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Function to fetch data from Supabase table
def fetch_data_from_table(table_name):
    # Select all data from the table
    response = supabase.table(table_name).select("*").execute()

    # Check if request was successful
    if response.status_code == 200:
        data = response.json().get("data", [])
        return data
    else:
        print("Failed to fetch data from table:", response.text)

# Main function
def main():
    table_name = "rooms"  # Replace with the name of your table
    data = fetch_data_from_table(table_name)
    if data:
        print("Data from table '{}' :".format(table_name))
        for row in data:
            print(row)
    else:
        print("No data found in table '{}'".format(table_name))

if __name__ == "__main__":
    main()
