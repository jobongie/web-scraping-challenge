# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}

    # Mars News URL of page to be scraped
    mars_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news_url)
    html = browser.html
    news_soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest news title and paragraph
    news_title = news_soup.find_all('div', class_='content_title')[1].text
    news_body = news_soup.find_all('div', class_='article_teaser_body')[1].text

    # Mars Image to be scraped
    jpl_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_images_url)
    html = browser.html
    images_soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve featured image link, in pandas this takes you to the site for the featured image
    # but requires you to click on a button that reads "Full Image"
    # Even though the destination is a url path to a .png file the final destination is 
    # actually another site with many images...
    # featured_image_url = https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/assets/images/logo_nasa_trio_black@2x.png
    # I googled and asked TA's without any solution being found... so Quien Sabe
    relative_image_path = images_soup.find_all('img')[0]["src"]
    featured_image_url = jpl_images_url + relative_image_path

    # Mars facts to be scraped, converted into html table
    mars_facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(mars_facts_url)
    mars_facts_df = tables[0]
    mars_facts_df.columns = ["Description", "Value"]
    mars_html_table = mars_facts_df.to_html(index=False, justify='left')
    mars_html_table.replace('\n', '')
    
    # Mars hemisphere name and image to be scraped
    usgs_url = 'https://astrogeology.usgs.gov'
    hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemis_url)
    hemis_html = browser.html
    hemis_soup = BeautifulSoup(hemis_html, 'html.parser')

    # Mars hemispheres products data
    all_mars_hemis = hemis_soup.find('div', class_='collapsible results')
    mars_hemis = all_mars_hemis.find_all('div', class_='item')
    hemis_image_urls = []

    # Iterate through each hemisphere data
    for i in mars_hemis:

        # Collect Title
        hemis = i.find('div', class_="description")
        title = hemis.h3.text   

        # Collect image link by browsing to hemisphere page
        hemis_link = hemis.a["href"]    
        browser.visit(usgs_url + hemis_link)        
        image_html = browser.html
        image_soup = BeautifulSoup(image_html, 'html.parser')        
        image_link = image_soup.find('div', class_='downloads')
        image_url = image_link.find('li').a['href']

        # Create Dictionary to store title and url info
        image_dict = {}
        image_dict['title'] = title
        image_dict['img_url'] = image_url        
        hemis_image_urls.append(image_dict)

    # Mars 
    mars_dict = {
        "news_title": news_title,
        "news_body": news_body,
        "featured_image_url": featured_image_url,
        "fact_table": str(mars_html_table),
        "hemis_images": hemis_image_urls}

    return mars_dict