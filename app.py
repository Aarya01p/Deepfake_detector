import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.efficientnet import preprocess_input

# Load model
model = tf.keras.models.load_model("deepfake_detector_v2.keras")

IMG_SIZE = (224, 224)

def predict(image):
    image = image.resize(IMG_SIZE)
    image = np.array(image)

    image = preprocess_input(image.astype(np.float32))
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image, verbose=0)[0][0]

    fake_prob = float(prediction)
    real_prob = 1.0 - fake_prob

    if prediction >= 0.5:
        label = "❌ FAKE"
    else:
        label = "✅ REAL"

    return (
        label,
        {
            "Real": real_prob,
            "Fake": fake_prob
        }
    )

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=[
        gr.Textbox(label="Prediction"),
        gr.Label(label="Confidence")
    ],
    title="Deepfake Detection using EfficientNetB0",
    description="Upload a face image to determine whether it is REAL or FAKE."
)

demo.launch()