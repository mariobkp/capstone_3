import os
import json
import pandas as pd


# Flask
from flask import Flask, render_template, url_for, request, redirect, flash
from forms import EnterDataForm

# Keras



app = Flask(__name__)

app.config['SECRET_KEY'] = 'reallystrongandsecretkey69'



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

@app.route('/update/', methods=["GET", "POST"])
def update():
    if request.method == "POST":
        pass
    else:
        return render_template("update.html")  
#
# change keywords possibly


@app.route('/about')
def about():
    return redirect('https://github.com/mariobkp/capstone_3')

@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')


def save_picture(form_picture):
    picture_path = os.path.join(app.root_path, 'static/', form_picture.filename)
    output_size = (224, 224)
    form_picture.save(picture_path)

def process_text(form_tags):
    pass



@app.route('/intelligence', methods=["GET", "POST"])
def intelligence():

    image_file = url_for('static', filename='imgs/' + 'default.jpg')

    keywords = 'Keywords or tags will be displayed here'

    recommended_price = "Recommended price range"

    form = EnterDataForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
        if form.tags.data:
            return redirect(url_for('intelligence'))

    
    df=pd.read_csv('../mens.csv', index_col=0)
    df=df.iloc[:5]
    json_records = df.reset_index().to_json(orient ='records') 
    d = [] 
    d = json.loads(json_records) 

    return render_template("intelligence.html", title='Intelligence', image_file = image_file, 
        keywords = keywords, recommended_price=recommended_price, form=form, d=d)  



if __name__ == "__main__":
    app.run(debug=True)