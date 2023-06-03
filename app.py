from flask import Flask, request, render_template, jsonify
import tensorflow as tf
import numpy as np
import os
import json

from tensorflow import keras

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
import keras.utils as image
from werkzeug.utils import secure_filename


# Define Flask App
app = Flask(__name__)

# load model
model_path = './models/model7.h5'
model = tf.keras.models.load_model(model_path)


def model_predict(img_path, model):

    # image = tf.keras.preprocessing.image.load_img('/content/tugujogja.jpg', target_size=(150, 150))
    image = tf.keras.preprocessing.image.load_img(img_path, target_size=(150, 150))
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = image_array / 255.0  # Normalize pixel values between 0 and 1
    input_data = tf.expand_dims(image_array, axis=0)  # Add batch dimension
    predictions = model.predict(input_data)

    return predictions

# img = image.load_img(img_path, target_size=(150, 150))

# # Preprocessing the image
# x = image.img_to_array(img)
# x = np.expand_dims(x, axis=0)
# x = preprocess_input(x, mode='caffe')

# preds = model.predict(x)
# return preds


# Halaman Home
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predicts():
    if request.method == 'POST':
        # Get file from request
        imageCamera = request.files['imageCamera']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'images', secure_filename(imageCamera.filename))
        imageCamera.save(file_path)

        predictions = model_predict(file_path, model)

        # Get the predicted class index with highest probability

        test_labels = [
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

        response = {"name": result}

        return jsonify(response)

        # # Decode predictions
        # pred_class = decode_predictions(preds, top=1)   # ImageNet Decode
        # result = str(pred_class[0][0][1])               # Convert to string
        # return result


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    prediction = model_predict(data, model)
    return {'prediction': prediction.tolist()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

