import matplotlib.pyplot as plt
import numpy as np
from darkflow.net.build import TFNet
import cv2


options = {"model": "C:\\Users\\gnane\\PycharmProjects\\untitled1\\darkflow-master\\cfg\\yolo_custom.cfg",
           "load": "C:\\Users\\gnane\\PycharmProjects\\untitled1\\darkflow-master\\bin\\yolo.weights",
           "batch": 5,
           "epoch": 30,
           "gpu": 0,
           "save":1000,
           "train": True,
           "annotation": "C:\\Users\\gnane\\PycharmProjects\\untitled1\\cig_butts\\train\\annotations\\",
           "dataset": "C:\\Users\\gnane\\PycharmProjects\\untitled1\\cig_butts\\train\\images\\"}
tfnet = TFNet(options)
tfnet.train()