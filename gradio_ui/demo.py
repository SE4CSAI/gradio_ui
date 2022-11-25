import os
import gradio as gr
import requests
from PIL import Image

def predict(image):
    image.save("image.jpg")
    f = open("image.jpg", "rb")
    files = {"file": ("image.jpg", f)}
    pred = requests.post("http://ec2-3-88-219-227.compute-1.amazonaws.com/upload_image", files = files)
    # send the file to the database
    r = requests.post("http://127.0.0.1:8000/upload_image", files=files)
    return pred.text

gr.Interface(predict, inputs=gr.inputs.Image(type="pil"), outputs="json").launch()