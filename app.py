from flask import Flask, request, render_template, jsonify
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
    image = tf.keras.preprocessing.image.load_img(
        img_path, target_size=(150, 150))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = image_array / 255.0
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

        test_labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
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
        result = test_labels[pred_class_index]
        result_name = test_labels_text[pred_class_index]
        response = {"uid": result, "name": result_name}
        return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
