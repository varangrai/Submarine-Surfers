# Submarine Surfers
 
Background:

Computer vision produces numerical or symbolic information from images and high-dimensional data. It involves machine learning, data mining, database knowledge discovery, and pattern recognition. Potential business uses of image recognition technology are found in healthcare, automobiles – driverless cars,

marketing campaigns, etc.

Problem Statement:

You are working on an autonomous underwater vehicle that is navigating underwater avoiding obstacles and achieving targets. In the navigation there comes a gate of which you know the dimensions and color. The bot must pass through it without touching it in order to complete the mission.

You have to write code for detecting the gate and to know its center in order for the bot to pass through it.
You will get the raw images from the camera and you’ll have to perform image processing on it and get the results.

# Image Preprocessing

main.py file preprocesses the image.

Input folder stores the raw image.
Input1 folder stores the preprocessed image after CLAHE application
Output folder stores after ULAP application

# Object detection
Object detection is performed in the notebook, ``Submarine_Surfers.ipynb``, using methods of contouring and thresholding using Canny Edge Detection.
