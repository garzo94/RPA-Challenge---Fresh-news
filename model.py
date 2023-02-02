from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime, timedelta, date
import pandas as pd
import requests
import time
import re



class ScrapedData:
    def __init__(self,search_phrase, section, num_months):
        self.search_phrase = search_phrase
        self.section = section
        self.num_months =  num_months
        self.current_date = datetime.today()
        self.data = data = {
            "title":[],
            "description":[],
            "date":[],
            "filename":[],
            "phrase_count":[],
            "contains_amount_of_money":[],
        }


    def scrape(self) -> None:
        driver = webdriver.Chrome()
        driver.get("https://www.nytimes.com/")

        # handle search button
        search_button = driver.find_element(By.CLASS_NAME, "css-tkwi90")
        search_button.click()
        search_input = driver.find_element(By.CSS_SELECTOR, "input")
        search_input.send_keys(self.search_phrase)
        search_input.submit()
        time.sleep(0.5)

        # handle checkbox section
        section_button = driver.find_element(By.CLASS_NAME, "css-4d08fs")
        section_button.click()
        checkbox_section =  driver.find_element(By.XPATH,f"//*[contains(@value,'{self.section}')]")
        checkbox_section.click()
        time.sleep(1)

        # handle sort by newest filter
        sort_by_button = driver.find_element(By.CLASS_NAME,"css-v7it2b")
        sort_by_button.click()
        newest_option = driver.find_element(By.XPATH,"//*[contains(@value, 'newest')]")
        newest_option.click()
        time.sleep(1)

        
        #  finding all the news in the current page
        news_list = driver.find_elements(By.CLASS_NAME, "css-1l4w6pd")
        # getting data for every news
        for news in news_list:
            # get title
            title = news.find_element(By.CLASS_NAME,"css-2fgx4k").text
            # get description
            try:
                description = news.find_element(By.CLASS_NAME,"css-16nhkrn").text
            except:
                description = ""

            # news date
            news_date = news.find_element(By.CLASS_NAME,"css-17ubb9w").text

            # picture filename
            try:
                picture = news.find_element(By.CLASS_NAME,"css-rq4mmj").get_attribute(name="src")
                filename = picture.split("/")[-1].split("?")[0]
                self.download_news_picture(src = picture, filename = filename)
            except:
                filename = "Image no found"

            # count of search phrases in the title and description
            count = self.phrase_count(title, description)

            # True or False, depending on whether the title or description contains any amount of money
            match = self.money_in_text(title, description)

            # date from when I want to extract the news
            start_date = self.current_date - timedelta(days=self.num_months*30)
            # checking latest news and saving data
            if "ago" in news_date:
                #saving data
                self.save_data(title, description, news_date, filename, count, match)
                
            # checking latest news with different formatting
            else:
                try:
                    date = datetime.strptime(news_date, "%b. %d, %Y").date()
                except:
                    date = datetime.strptime(news_date, "%b. %d").replace(year=self.current_date.year).date()
                if date > start_date.date():
                    self.save_data(title, description, news_date, filename, count, match)

       

    def phrase_count(self, title:str, description:str) -> int:
        title_and_description = self.get_title_description_string(title, description)
        count  = title_and_description.count(self.search_phrase.lower())
        return count

    def money_in_text(self, title:str, description:str) -> bool:
        title_and_description = self.get_title_description_string(title, description)
        pattern = re.compile(r'\$\d+[.,]\d+|\d+\s(dollars|USD)', re.IGNORECASE)
        match = pattern.search(title_and_description)
        if match:
            return True
        else:
            return False

    def get_title_description_string(self, title:str, description:str) -> str:
        title_and_description = title.lower() + " " + description.lower()
        return title_and_description

    def download_news_picture(self,src:str, filename:str) ->None:
        # Download the news picture and specify the file name in the excel file
        response = requests.get(src)
        with open(f"images/{filename}", "wb") as f:
            f.write(response.content)

    def save_data(self, title:str, description:str, date:str, filename:str, phrase:str, match:str)->None:
         self.data["title"].append(title)
         self.data["description"].append(description)
         self.data["date"].append(date)
         self.data["filename"].append(filename)
         self.data["phrase_count"].append(phrase)
         self.data["contains_amount_of_money"].append(match)




    def save_to_excel(self, filename:str) -> None:
        df = pd.DataFrame(self.data)
        # write the data frame to an Excel file
        df.to_excel(f'./excel_files/{filename}', index=False)
