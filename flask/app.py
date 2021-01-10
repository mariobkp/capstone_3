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
    return render_template("about.html", title="About") 

@app.route('/contact')
def contact():
    return render_template("contact.html", title='Contact')


def process_image(form_picture):
    pass

def process_text(form_tags):
    pass

@app.route('/intelligence', methods=["GET", "POST"])
def intelligence():
    form = EnterDataForm()
    if form.validate_on_submit():
        # if form.picture.data:
            # image_features = process_image(form.picture.data)
        # if form.tags.data:
        return redirect(url_for('intelligence'))
    return render_template("intelligence.html", title='Intelligence', form=form)  

if __name__ == "__main__":
    app.run(debug=True)