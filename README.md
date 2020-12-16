# capstone_3

## Clothing Identification and Pricing Tool

* From microplastics in the ocean, to carbon emissions in the air, and sometimes questionable labor practices, the fashion industry has widespread environmental and societal impacts. 
* The "fast fashion" trend of cheap-in-price and cheap-in-quality, will maybe arguably making self-expression through clothing easier, has had a terrible effect on the environment. Discarded clothing, rather than being recycled or repaired, end up in landfills at best, litter at worst.
* As individual consumers, we can do a small part in changing our mindset and our habits by buying and selling used clothing rather than the "use and discard" mentality.
* In an effort to aid and encourage the practice of reselling clothing, I would like to create a tool to aid thrift stores, consigners, resellers in more efficient pricing.
* I propose to scrape clothing sales data from eBay, store both the image and some text data in AWS S3, and create a Flask app pricing tool. The interface will allow users to provide an image of an item, ostensibly a store/reseller/buyer trying to gauge the "value" of an item of clothing, and optionally provide the brand name. The app will then return similar items along with the respective prices.
* In an effort to limit the scope, I would like to look only at men's clothing and shoes for this project. May also be best to look only at current eBay listings rather than already sold items.
* May also consider using weights like ImageNet or Fashion MNIST.
* AWS, BeautifulSoup, sklearn, TensorFlow, PySpark, Flask.

## Podcast recommender

* As an avid podcast listener, I often find myself running through new episodes of my favorite podcasts each week, then left to wait until next Monday for new episodes to drop.
* When I'm looking for a new podcast, I often rely on shows or movies I like to find writers/actors whose podcasts I might want to listen to. I'd like to create a podcast recommender based on movie tastes.
* I would like to use Rotten Tomatoes data (https://www.kaggle.com/stefanoleone992/rotten-tomatoes-movies-and-critic-reviews-dataset) and either Spotify or Apple (depending on API ease of use) podcast information to deploy a Flask app that recommends podcasts based on user input movie titles.
* AWS, Apple iTunes/Spotify API, sklearn, TensorFlow, PySpark, Flask.
