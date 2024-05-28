from faker import Faker
import pandas as pd

fake = Faker()

data = { 
    'First Name': [],
    'Last Name': [],
    'DOB': [],
    'Email': [],
    'City': [],
    'Country': [],\
    'ZipCode': [],
}

for i in range(11):
    data['First Name'].append(fake.first_name())
    data['Last Name'].append(fake.last_name())
    data['DOB'].append(fake.date_of_birth())
    data['Email'].append(fake.email())
    data['City'].append(fake.city())
    data['ZipCode'].append(fake.zipcode())
    data['Country'].append(fake.country())

df = pd.DataFrame(data)

print(df)

#Generate a styled DataFrame and view it by saving the DataFrame to an HTML file and then opening that file in a web browser
# Define the table style to add borders
styles = [
    {'selector': 'table', 'props': [('border-collapse', 'collapse')]},
    {'selector': 'th, td', 'props': [('border', '1px solid black'), ('padding', '5px')]},
]

styled_df = df.style.set_table_styles(styles)

styled_df.to_html('styled_table.html')

print("Styled table saved as 'styled_table.html'. Open this file in a web browser to view the table with borders.")

