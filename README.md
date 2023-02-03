# NY Times Data Scraper
### Introduction

This project is a data scraper for [NT Times](https://https://www.nytimes.com/). The project is built using the Model-Controller (MC) architecture, with a virtual environment for dependencies management.

![This is an image](https://github.com/garzo94/RPA-Challenge---Fresh-news/blob/main/ezgif.com-gif-maker.gif)

### Excel file output:
![This is an image](https://github.com/garzo94/RPA-Challenge---Fresh-news/blob/main/screenshot_excel_file.png)


### Requirements
- Python 3.x
- Selenium
- Pandas
- Requests
- Openpyxl
- Pip
- Virtualenv

### Installation

1. Clone the repository:
```
git clone git@github.com:garzo94/RPA-Challenge---Fresh-news.git
```
2. Create a virtual environment:
```
virtualenv venv
```
3. Activate the virtual environment:
```
source venv/bin/activate
```
4. Install the required packages:
```
pip install -r requirements.txt
```

### Usage
1. Run the scraper:
```
python main.py
```
2. The scraped data will be stored in a CSV file named scraped_data.xlsx in the project directory, and images will be downloaded to the images folder.

