from flask import Flask, render_template, redirect, url_for, flash, request
from PIL import Image
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from MostCommonColorFinder import MostCommonColorFinder
import os




app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config["UPLOAD_FOLDER"] = "static/Bilder"

file_path = ""


class UploadImageForm(FlaskForm):
    file = FileField(label = "...", render_kw={"title": "Wähle eine Datei", "placeholder": "Wähle eine Datei", " class": "btn btn-primary"})
    submit = SubmitField('Öffnen', render_kw={"class": "btn btn-outline-secondary"})



img_data = []

#df = pd.read_csv('C:\Users\Stefan\')




"""@app.route('/', methods=['GET', 'POST'])
def start():  # put application's code here

    global file_path

    form = UploadImageForm()

    if request.method == 'POST':
        file = form.file.data
        filename = secure_filename(file.filename)
        file_path = app.config['UPLOAD_FOLDER'] + "/" + filename
        file.save(file_path)
        print(file_path)
        #img_to_load = form.file.data

        if not file_path == "":
            img = Image.open(file_path)
            img.convert("RGB")

            width, height = img.size

            for x in range(0, width):
                for y in range(0, height):
                    r, g, b = img.getpixel((x, y))

                    img_data.append((r, g, b))
                    # print(img.getpixel((x, y)))
                    # print(img_data)

            columns = ["r", "g", "b"]

            img_df = pd.DataFrame(data=img_data, columns=columns)

            most_common_colors = []

            most_common_colors = img_df.value_counts().head()
            color_values_ready = []

            # print(most_common_colors)

            for _ in range(0, 5):
                color_values_ready.append(list(most_common_colors.index[_]))

            print("___________")
            print(color_values_ready)



        return redirect(url_for("start", img_to_load=file_path))

    return render_template("start.html", form = form, img_to_load=file_path)
"""

most_common_color_finder = MostCommonColorFinder()
top_5_colors = []
@app.route('/', methods=['GET', 'POST'] )
def start():  # put application's code here
    global top_5_colors

    form = UploadImageForm()

    if request.method == 'POST':
        file = form.file.data
        filename = secure_filename(file.filename)
        most_common_color_finder.filepath = app.config['UPLOAD_FOLDER'] + "/" + filename
        file.save(most_common_color_finder.filepath)
        #img_to_load = form.file.data
        top_5_colors = most_common_color_finder.find_color()
        print(top_5_colors)


        #most_common_colors = most_common_color_finder.find_color()
        return redirect(url_for('start', img_to_load=most_common_color_finder.filepath, most_common_colors = top_5_colors))

    return render_template("start.html", form = form, img_to_load=most_common_color_finder.filepath, most_common_colors = top_5_colors, counter = most_common_color_finder.counter)




if __name__ == '__main__':
    app.run()
