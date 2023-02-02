from model import ScrapedData

def main():
    filename = 'scraped_data.xlsx'

    # Initialize the ScrapedData model
    scraped_data = ScrapedData(search_phrase = "Economy", section = "Business", num_months = 2)

    # Scrape data from the website
    try:
        scraped_data.scrape()
    except Exception as e:
        print("An unexpected error occurred:", e)

    # Save the scraped data to an Excel file
    scraped_data.save_to_excel(filename)

if __name__ == '__main__':
    main()