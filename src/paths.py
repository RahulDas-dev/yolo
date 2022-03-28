import os

__current_dir = os.path.dirname(os.path.abspath(__file__))

project_dir = os.path.abspath(os.path.join(__current_dir, os.pardir))

model_directory = os.path.join(project_dir, "model")

data_directory = os.path.join(project_dir, "data")

train_directory = os.path.join(data_directory, "train")

test_directory = os.path.join(data_directory, "test")

class_paths = os.path.join(data_directory, "classes.txt")

src_directory = os.path.join(project_dir, "src")

model_config = os.path.join(src_directory, "yolov5s6.yaml")
