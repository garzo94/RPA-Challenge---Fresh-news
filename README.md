# NY Times Data Scraper
### Introduction

This project is a data scraper for [NT Times](https://https://www.nytimes.com/). The project is built using the Model-View (MC) architecture, with a virtual environment for dependencies management.

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
git clone https://github.com/your-username/nytimes-scraper.git
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

