# Import pandas for creating DataFrame and saving Excel file
import pandas as pd
# Import requests to fetch webpage data
import requests
# Import BeautifulSoup to parse HTML content
from bs4 import BeautifulSoup

# Create empty list to store all book details from all 50 pages
book_details = []

# Loop through pages from 1 to 50
for all_pages in range(1,51):
     # Create dynamic URL for each page using f-string
    url = f"https://books.toscrape.com/catalogue/page-{all_pages}.html" 

     # Send request to website and get response
    get_response = requests.get(url)
     # Extract raw HTML content from response
    got_content = get_response.content 
     # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(got_content,"html.parser")

     # Find all book containers from the page
    list_of_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    # Loop through each book one by one
    for details in list_of_books:
        takeout_tag = details.find("h3").find("a") # Find h3 tag → then find a tag inside it
        book_name =  takeout_tag.text.strip() # Extract book title and remove extra spaces
        book_link = f"https://books.toscrape.com/catalogue/{takeout_tag["href"]}"  # Create full book link using f-string
        price_tag =  details.find("p", class_="price_color").text.strip()# Extract book price
        availibilty = details.find("p", class_="instock availability").text.strip()# Extract stock availability text

     # Store one book's details in dictionary format
        all_details = ({
                "Name of Book": book_name,
                "Selling Price": price_tag,
                "In stock" : availibilty,
                "Buy Link": book_link
            })
     # Append dictionary into main list   
        book_details.append(all_details)

# Convert full list into pandas DataFrame
df = pd.DataFrame(book_details)
# Export DataFrame to Excel file with worksheet name 
df.to_excel(r"C:\Users\hp\Downloads\scraping\book_details.xlsx", sheet_name= "Book Scraping info", index= False)

# Print success message
print("Data successfully saved to Excel file")

