# Pretty Thrifty Clothing Identification and Pricing Tool

## Motivation

* From microplastics in the ocean, to carbon emissions in the air, and sometimes questionable labor practices, the fashion industry has widespread environmental and societal impacts. 
* The "fast fashion" trend of cheap-in-price and cheap-in-quality, will maybe arguably making self-expression through clothing easier, has had a terrible effect on the environment. Discarded clothing, rather than being recycled or repaired, end up in landfills at best, litter at worst.
* As individual consumers, we can do a small part in changing our mindset and our habits by buying and selling used clothing rather than the "use and discard" mentality.
* In an effort to aid and encourage the practice of reselling clothing, I would like to create a tool to aid thrift stores, consigners, resellers in more efficient pricing.
* I proposed to scrape clothing sales data from eBay, store both the image and some text data, and create a Flask app pricing tool. The interface will allow users to provide an image of an item, ostensibly a store/reseller/buyer trying to gauge the "value" of an item of clothing, and optionally provide the brand name or other relevant text. The app will then return similar items along with the respective prices.
* In an effort to limit the scope, I would like to look only at men's clothing and shoes for this project. May also be best to look only at current eBay listings rather than already sold items.

* Multi-input model taking both image and text data to return a price range estimate determined from similar listings

* Furthermore, in the age of the side gig, working from home, and multiple income streams, it can also be a way to make money (if only ultimately to buy different used clothes).

## Data Scraping/Cleaning

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

* Based on out of the box performance testing both models with images from my dataset, I decided to proceed with ResNet50 for image feature extraction.

* These two models are exceedingly complex and training them, even these "smaller" versions, wouldn't be practical in many cases and luckily through the miracle of transfer learning you or I can tune these models to our own tasks.

* ResNet takes in a 224 x 224 pixel image with the 3 color channels and runs it through a specific preprocess method.

* ResNet is structured as 5 blocks of convolutional layers.

## Retraining

* I tested freezing and retraining different layers and in studying the way ResNet is set up, I ended up retraining the entire fifth block of the model on my data for 30 epochs and saved the model for feature extraction.

* Lastly the final layer in the model is a classification layer based on the ImageNet dataset of 1000 images. In training I replaced the output layer with a Dense layer with 14 classes.

* However, the final layer isn't needed when all I'm looking for are the images "features"

* Removed final output layer and replaced with a GlobalPooling2D layer

* Ran each image through the retrained model and saved the 2048 features

## Natural Language Processing

* In addition to the image data, I also scraped each listing for the seller-added text attributes (brand, size, color, material, etc.) describing the item. These keywords or tags were then coalesced with the listing title and category into what's called a "bag of words.

* Because many of the listings, especially within the same category, would have similar descriptors, I used a TF-IDF vectorizer to  transform the word data into a usable number format

* I created a custom list of "stop words," meaning words that are filtered out, and limited the number of features to 1000. Vectorizing words can lead to a sparse set if the number of features isn't limited, meaning the data isn't "concentrated" enough for effective analysis.

## Final Model

* The final model is essentially a two-part image and text combination neural network and word vectorizing algortihm to return similar listings to guide the reseller. Similar items are first returned based on the image data, and optionally can be further filtered through the use of user input keywords. A recommended price range is returned based on the top 5 most similar items.

## Application Development

* Flask, a popular Python web application framework was used for the front-end of the tool

## Future Work

* First and foremost, use cloud computing to overcome the GPU and memory issues
* Deploy full model on Flask
* Store results in database
* Time series analysis
