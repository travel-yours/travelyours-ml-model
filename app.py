from flask import Flask, request, render_template, jsonify, redirect
import tensorflow as tf
import numpy as np
import os
from tensorflow import keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
import keras.utils as image
from werkzeug.utils import secure_filename
from flask_cors import CORS

# Define Flask App
app = Flask(__name__)
CORS(app)

# load model
model_path = './models/model7.h5'
model = tf.keras.models.load_model(model_path)


def model_predict(img_path, model):
    image = tf.keras.preprocessing.image.load_img(img_path)
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = image_array / 255.0  # Normalisasi
    image_array = tf.image.resize(image_array, (150, 150))  # Resize
    input_data = tf.expand_dims(image_array, axis=0)
    predictions = model.predict(input_data)
    return predictions



@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predicts():
    if request.method == 'POST':
        # Get file from request
        imageCamera = request.files['imageCamera']
        # Save the file to ./images
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'images', secure_filename(imageCamera.filename))
        imageCamera.save(file_path)
        predictions = model_predict(file_path, model)

        test_labels = ["647a94e9066891e6d6b9fcad",
                       "647ab21fc2b29a1e07d90855",
                       "647ab354c2b29a1e07d90858",
                       "647ab91f9f8ccada06b1b475",
                       "647b72c6abf8c758f2bf4325",
                       "647ca178d681d9032d5d63db",
                       "647ca296d681d9032d5d63dd",
                       "647ca329789e7a9317ac1356",
                       "647ca456d681d9032d5d63df",
                       "647ca59cd681d9032d5d63e1",
                       "647caa51e853d9aaccbf0fbd",
                       "647cab24e853d9aaccbf0fc2",
                       "647cabd6e853d9aaccbf0fc4",
                       "647cacb1e853d9aaccbf0fc6",
                       "647cada3e853d9aaccbf0fc8",
                       "647cae11e853d9aaccbf0fca"]
        
        test_labels_text = [
            'borobudur',
            'jendral_sudirman',
            'martapura',
            'monas',
            'monumen_lobar',
            'monumen mataram metro',
            'monumen_selamat_datang',
            'monumen_surabaya',
            'museum_tsunami',
            'pantai_penyu',
            'prambanan',
            'pura_suranadi',
            'rumah_aceh',
            'sarinah_ mall',
            'taman_sangkreang',
            'tugu_jogja',
        ]
        pred_class_index = np.argmax(predictions)
        if predictions[0][pred_class_index] > 0.7:
            result = test_labels[pred_class_index]
            result_name = test_labels_text[pred_class_index]
        else:
            result = ""
            result_name = "Maaf, hasil belum tersedia"

        destination_url = f"https://travelyours-api-4zcm2uhcpq-as.a.run.app/destination/{result}"

        return redirect(destination_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
