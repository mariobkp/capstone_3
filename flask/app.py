import os
import json
import secrets
import numpy as np
import pandas as pd
from PIL import Image


# Flask
from flask import Flask, render_template, url_for, request, redirect, flash
from forms import EnterDataForm, DemoDataForm

# Keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
# import tensorflow_hub as hub
# import tensorflow_datasets as tfds
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.models import Model

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras import applications
from sklearn.metrics import pairwise_distances

from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# sklearn
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity

# gpus = tf.config.experimental.list_physical_devices('GPU')
# if gpus:
#     # Restrict TensorFlow to only allocate 1*X GB of memory on the first GPU
#     try:
#         tf.config.experimental.set_virtual_device_configuration(
#             gpus[0],
#             [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2400)])
#         logical_gpus = tf.config.experimental.list_logical_devices('GPU')
#         print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
#     except RuntimeError as e:
#     # Virtual devices must be set before GPUs have been initialized
#         print(e)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'reallystrongandsecretkey69'

mens=pd.read_csv('../mens.csv', index_col=0)

tfidf = TfidfVectorizer(lowercase=True, tokenizer=None,
                        analyzer='word', max_features=1000)

document_tfidf = tfidf.fit_transform(mens['tags'])

# reconstructed_model = keras.models.load_model('retrainresnet')

# new_model = Model(reconstructed_model.inputs, reconstructed_model.layers[-2].output)

extracted_features = np.load('resnet_features.npy')
Productids = np.load('resnet_feature_product_ids.npy')
Productids = list(Productids)


@app.route('/', methods=['POST', 'GET'])

def index():

    if request.method == "POST":
        user_prod = request.form["content"] # Form from index.html

        try:
            # see similar products

            # return redirect('/') to reload page
            pass

        except:
            return "There was an issue searching for similar products"

    else:
        return render_template("index.html")

#   @app.route('/delete')
#   possibly delete item if not applicable? get next
#   see video at 32 min

@app.route('/update', methods=["GET", "POST"])
def update():

    form = EnterDataForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)

            if form.tags.data:
                with open('text.txt', 'w') as f:
                    f.write(str(form.tags.data))
            
            return redirect(url_for('intelligence'))

    return render_template("update.html", title='Update', form=form)

@app.route('/demo', methods=["GET", "POST"])
def demo():
    form = DemoDataForm()

    if form.validate_on_submit():
        if form.item.data:
            with open('id.txt', 'w') as f:
                f.write(str(form.item.data))
            if form.tags.data:
                with open('text.txt', 'w') as f:
                    f.write(str(form.tags.data))

        return redirect(url_for('intelligence'))

    else:
        return render_template("demo.html", title='Demo', form=form)


@app.route('/about')
def about():
    return redirect('https://github.com/mariobkp/capstone_3')

@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')


# def save_picture(form_picture):
    
#     output_size = (224, 224)

#     picture_path = os.path.join(app.root_path, 'static/imgs/imgs/', 'current.jpg')


#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)

#     return picture_path

# def preproc():
#     x = ImageDataGenerator(rescale= 1. / 255, preprocessing_function=tf.keras.applications.resnet.preprocess_input) \
#     .flow_from_directory(directory='static/imgs/', target_size=(224,224), batch_size=1)[0][0]

#     return new_model.predict(x, batch_size=1)


# @app.route('/intelligence', methods=["GET", "POST"])
# def intelligence():

#     feats = preproc()
    
#     image_file = url_for('static', filename='imgs/imgs/' + 'current.jpg')

#     pairwise_dist = pairwise_distances(extracted_features, feats.reshape(1,-1))
    
#     f = open("text.txt", "r")

#     if len(str(f.read())) > 0:
#         keywords = str(f.read())

#         queryTFIDF = tfidf.fit(mens['tags'])
#         queryTFIDF = queryTFIDF.transform(keywords)
        
#         cosine_similarities = cosine_similarity(queryTFIDF, document_tfidf).flatten()
        
#         indices = cosine_similarities.argsort()[:-(20):-1]
        
#         pid = []

#         for i in indices:
#             pid.append(int(Productids.index(str(i))))
        
#         pairwise_dist = pairwise_distances(extracted_features[pid], feats.reshape(1,-1))
        
#     indices = np.argsort(pairwise_dist.flatten())[0:10]

#     df = mens[['image_link','title', 'price']].loc[indices]

#     json_records = df.reset_index().to_json(orient ='records') 
#     d = [] 
#     d = json.loads(json_records)

#     recommended_price = "Recommended price range"

#     return render_template("intelligence.html", title='Intelligence', image_file = image_file, 
#         keywords = keywords, recommended_price=recommended_price, d=d)  

@app.route('/intelligence', methods=["GET", "POST"])
def intelligence():

    i = open("id.txt", "r")
    i = i.read()

    if os.path.exists("text.txt"):
        keywords = open("text.txt", "r")
        keywords = keywords.read()

    image_file = mens['image_link'].iloc[int(i)]

    doc_id = Productids.index(i)
    pairwise_dist = pairwise_distances(extracted_features, extracted_features[doc_id].reshape(1,-1))
    
    if os.path.exists("text.txt"):

        tfidf = TfidfVectorizer(lowercase=True, tokenizer=None,
                                analyzer='word', max_features=1000)

        
        queryTFIDF = tfidf.fit(mens['tags'])
        queryTFIDF = queryTFIDF.transform([keywords])
        
        cosine_similarities = cosine_similarity(queryTFIDF, document_tfidf).flatten()
        
        indices = cosine_similarities.argsort()[:-30:-1]

        pid = []

        for i in indices:
            pid.append(int(Productids.index(str(i))))
        
        pairwise_dist = pairwise_distances(extracted_features[pid], extracted_features[doc_id].reshape(1,-1))

        df = mens[['image_link','title', 'price']].loc[indices[1:6]]

        json_records = df.reset_index().to_json(orient ='records') 
        d = [] 
        d = json.loads(json_records)

        recommended_price = 'Recommended price range: $' + str(np.round(np.min(df.price),2)) + ' to ' + '$' + str(np.round(np.max(df.price),2))

        return render_template("intelligence.html", title='Intelligence', image_file = image_file, 
                                keywords = keywords, recommended_price=recommended_price, d=d)  
        
    else:
        indices = np.argsort(pairwise_dist.flatten())

        df = mens[['image_link','title', 'price']].loc[indices[1:6]]

        json_records = df.reset_index().to_json(orient ='records') 
        d = [] 
        d = json.loads(json_records)

        recommended_price = 'Recommended price range: $' + str(np.round(np.min(df.price),2)) + ' to ' + '$' + str(np.round(np.max(df.price),2))

        return render_template("intelligence.html", title='Intelligence', image_file = image_file, 
                                recommended_price=recommended_price, d=d)  

if __name__ == "__main__":
    app.run(debug=True)