# Web-Scraping-Challenge

## Step 1- Scraping

Completed the initial scraping using the file **mission_to_mars.ipynb** and the following links:

* mars_news_url  = 'https://mars.nasa.gov/news/'
* jpl_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
* featured_image_url = https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/assets/images/logo_nasa_trio_black@2x.png
* mars_facts_url = 'https://space-facts.com/mars/'
* mars_hemis_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    These links were used to obtain the data for Mars News, Mars Space Images, Mars Facts, and the Mars Hemispheres. For Images, both the image links and the titles were saved using Dictionary key-value pairs.

## Step 2- MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above, and created a Database named **mars_app**.

* **app.py**  utilizes a Flask server to execute the following:
    * **scrape_mars.py**  which scrapes the NASA mars site for Facts, Hemispheres Data, Images, and Featured articles.
    * **index.html**  creates an HTML page to displayed the data scraped from the various Nasa Mars webpages.






## Images

![Mars_scrape_html.png](Mission_to_Mars\Images\Mars_scrape_html.png)
![cerberus_enhanced.jpg](Mission_to_Mars\Images\cerberus_enhanced.jpg)
![syrtis_major_enhanced.png](Mission_to_Mars\Images\syrtis_major_enhanced.jpg)
![schiaparelli_enhanced.png](Mission_to_Mars\Images\schiaparelli_enhanced.jpg)
![valles_marineris_enhanced.png](Mission_to_Mars\Images\valles_marineris_enhanced.jpg)
![PIA17652_ip.jpg](Mission_to_Mars\Images\PIA17652_ip.jpg)