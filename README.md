# reSaleScout
Reselling made easier.

In this folder you will find notebooks, .py scripts, and supporting files used to run my application, reSaleScout, which uses historical sale data from two auction websites to predict where sellers will make a higher profit based on the type, brand, and condition of their women's clothing item.

Play around at: www.resale.fun

Below, an overview of the contents of this repository:

### eBay_scraper.ipynb, poshmark_scraper.ipynb
These notebooks detail my application of BeautifulSoup, pandas, NumPy, requests, etc. to scrape data for 10 of the most popular women's clothing brands listed on eBay and poshmark. The HTML and data storage differed between the two sites slightly, thus the two notebooks.

### Data_exploration.ipynb
Cleaning and polishing some data.

### Postgres_scrapers.ipynb
Setting up a PostgreSQL database and querying a bit.

### Random forests.ipynb
Random forest instantiation- but that's not all! A hint of XGBoost as well.

### /CSVs
Important .csv files I don't want to lose if my computer perishes.

### .pkl, cat files
Pickled models, binary vectors, used in my application deployment scripts.

### __init__.py, resale.py, run.py
The initialization, application, and executable files used to deploy my application on AWS.

### landing.html
My template folder. There are files associated with this template that are replaceable- the guts of this HTML doc are the important bit.
