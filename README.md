# Pretty Thrifty Clothing Identification and Pricing Tool

## Motivation

* From microplastics in the ocean, to carbon emissions in the air, and sometimes questionable labor practices, the fashion industry has widespread environmental and societal impacts. 
* The "fast fashion" trend of cheap-in-price and cheap-in-quality, will maybe arguably making self-expression through clothing easier, has had a terrible effect on the environment. Discarded clothing, rather than being recycled or repaired, end up in landfills at best, litter at worst.
* As individual consumers, we can do a small part in changing our mindset and our habits by buying and selling used clothing rather than the "use and discard" mentality.
* In an effort to aid and encourage the practice of reselling clothing, I would like to create a tool to aid thrift stores, consigners, resellers in more efficient pricing.
* I propose to scrape clothing sales data from eBay, store both the image and some text data in AWS S3, and create a Flask app pricing tool. The interface will allow users to provide an image of an item, ostensibly a store/reseller/buyer trying to gauge the "value" of an item of clothing, and optionally provide the brand name. The app will then return similar items along with the respective prices.
* In an effort to limit the scope, I would like to look only at men's clothing and shoes for this project. May also be best to look only at current eBay listings rather than already sold items.

## Data Scraping/Cleaning

* May also consider using weights like ImageNet or Fashion MNIST.
* AWS, BeautifulSoup, sklearn, TensorFlow, PySpark, Flask.

* I first scraped my data from eBay. As I was already scraping the data from eBay, I decided I'd use their item classification breakdown as follows:
  - Boots
  - Casual Shirts
  - Casual Shoes
  - Coats/Jackets
  - Dress Shirts
  - Dress Shoes
  - Jeans
  - Pants
  - Polos
  - Shorts
  - Sneakers
  - Suits
  - Sweaters
  - T-shirts
* In keeping with the spirit of the project, I only scraped pre-owned items, however I ended up scraping almost the entirety of eBay's used clothing listings.
* In all, there were over 400,000 rows of listing data (each row corresponding to a listing).
* After cleaning and filtering, I ended up with 10,000 items per category totalling 140,000 items.

## Transfer Learning

* As I imagined the impetus behind the project was to develop a business tool for individuals and enterprises, I wanted to use a model that would allow for efficient deployment even for mobile devices. As such from the start I focused on two Neural Network architectures: Mobilenet and ResNet50. These two types of neural networks represent two different approaches to improving accuracy and efficiency.

* MobileNet
  * MobileNet is a streamlined and (as the name implies) mobile version of the Xception architecture. This model represents "going wider" with respect to it's layers.
 
 * ResNet
  * Residual Net, or ResNet, represents "going deeper" and specifically sought to address the question of why adding more layers doesn't always increase accuracy.
  * The "residual" part of the title refers to its solution of not trying to map directly, but map to residuals.
  * ResNet50 is the lightweight model in the ResNet family.
 
 *

## Retraining

## Natural Language Processing

## Application Development

## Future Work
