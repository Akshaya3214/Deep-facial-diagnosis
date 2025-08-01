from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('best_model2.h5')

# Disease descriptions
disease_info = {
    "acne": "Acne is a skin condition that occurs when hair follicles become clogged with oil and dead skin cells. Common in teenagers, but affects all ages.",
    "eczema": "Eczema causes red, itchy, inflamed skin. It is a chronic condition often triggered by irritants, allergens, or genetics.",
    "rosacea": "Rosacea causes facial redness, swelling, and visible blood vessels. Triggers include spicy food, alcohol, sun, and stress.",
    "healthy": "No visible facial skin issues detected. Keep up a good skincare routine!"
}

# Upload folder and allowed extensions
UPLOAD_FOLDER = 'static/uploaded_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the file is an allowed image type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Upload and predict route
@app.route('/predict', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return render_template('index.html', error="No file part")
    
    file = request.files['file']
    
    if file.filename == '':
        return render_template('index.html', error="No selected file")
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Preprocess image
        img = image.load_img(filepath, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Prediction
        pred = model.predict(img_array)
        pred_class = ['acne', 'eczema', 'healthy', 'rosacea'][np.argmax(pred)]
        confidence = np.max(pred) * 100  # Convert to percentage
        accuracy = (np.max(pred) * 100)  # The accuracy of the model prediction

        # Get disease info
        info = disease_info.get(pred_class, "No information available.")

        # Render the template with prediction details
        return render_template("index.html", 
                               prediction=pred_class.capitalize(), 
                               confidence=f"{confidence:.2f}%", 
                               disease_info=info, 
                               accuracy=f"{accuracy:.2f}%", 
                               image_path=filepath)

    return render_template('index.html', error="Invalid file type")

if __name__ == '__main__':
    app.run(debug=True)