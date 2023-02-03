from model import ScrapedData, MoneyChecker, TitleDescriptionConcatenator, PhraseCounter

def main():
    filename = 'scraped_data.xlsx'
    counter = PhraseCounter()
    checker = MoneyChecker()
    concatenator = TitleDescriptionConcatenator()

    # Initialize the ScrapedData model
    scraped_data = ScrapedData(search_phrase = "Economy", section = "Business", num_months = 2, counter = counter, checker = checker, concatenator = concatenator)

    # Scrape data from the website
    scraped_data.scrape()
   

    # Save the scraped data to an Excel file
    scraped_data.save_to_excel(filename)

if __name__ == '__main__':
    main()