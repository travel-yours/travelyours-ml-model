import cv2
from keras.models import load_model
import numpy as np
import tensorflow as tf

# Load model from H5 file
model = load_model('./travelyours-ml-model/models/TLmodelv2.h5')

# Function to perform object detection on live camera feed
def detect_objects():
    # Open the video capture
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read the frame from the camera
        ret, frame = cap.read()
        
        # Preprocess the frame for model input
        # image = cv2.resize(frame, (150, 150))
        # image = np.array(image)
        # image = np.expand_dims(image, axis=0)
        # image = np.expand_dims(image, axis=-1)
        # image = image / 255.0  # Normalize pixel values

        # image = tf.keras.preprocessing.image.load_img('input.jpg')

        # Convert the PIL image to a TensorFlow tensor
        image = tf.keras.preprocessing.image.img_to_array(frame)/255.0

        # Expand the dimensions to create a batch of size 1
        image = tf.expand_dims(image, axis=0)

        # Resize the image to the desired size using tf.image.resize()
        target_size = (150, 150)
        resized_image = tf.image.resize(image, target_size)
        
        # Perform prediction using the loaded model
        prediction = model.predict(resized_image)

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

        # Get the predicted label
        pred_class_index = np.argmax(prediction)
        if prediction[0][pred_class_index] > 0.6:
            result = test_labels[pred_class_index]
        else:
            result = "Tidak ada di database"

        # Display the frame with the predicted label
        cv2.putText(frame, result, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.imshow('Live Object Detection', frame)

        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture and close the window
    cap.release()
    cv2.destroyAllWindows()

# Call the function for object detection on live camera feed
detect_objects()