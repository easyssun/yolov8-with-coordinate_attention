from ultralytics import YOLO
import torch

# Load a model
model = YOLO("./cfg/models/v8/yolov8n.yaml")  # build a new model from scratch

# Use the model
model.train(
    data="./your_data_yaml_path.yaml", 
    epochs=300,
    device=4,
    batch=32,
    patience=0,
    project="yolov8/runs/train",
    name="yolov8n",
    cache="disk",
    optimizer="Adam",
    lr0=0.001,
    lrf =0.001
    )  # train the model

metrics = model.val()  # evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format