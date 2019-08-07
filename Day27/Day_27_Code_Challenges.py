"""
Q1. 

(Click Here To Download Training data File): 
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json

(Click Here To Download Test data File):
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json


This is the data for local classified advertisements. It has 9 prominent sections: jobs, resumes, gigs, personals, housing, community, services, for-sale and discussion forums. Each of these sections is divided into subsections called categories. For example, the services section has the following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), we provide to you data from four sections

        for-sale
        housing
        community
        services

and we have selected a total of 16 categories from the above sections.

        activities
        appliances
        artists
        automotive
        cell-phones
        childcare
        general
        household-services
        housing
        photography
        real-estate
        shared
        temporary
        therapeutic
        video-games
        wanted-housing

Each category belongs to only 1 section.

About Data:

        city (string) : The city for which this Craigslist post was made.
        section (string) : for-sale/housing/etc.
        heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program has all the fields but category which you have to predict as the answer.

A total of approximately 20,000 records have been provided to you, proportionally represented across these sections, categories and cities. The format of training data is the same as input format but with an additional field "category", the category in which the post was made.

Task:

    Given the city, section and heading of an advertisement, can you predict the category under which it was posted?
    Also Show top 5 categories which has highest number of posts
"""
import json
import pandas as pd

with open('Advertisement_training_data.json') as json_train:
    data=json_train.read()
data=data[data.find('{'):]
data=pd.read_json(data,lines=True)
features_train=data.iloc[:,1:].values
labels_train=data.iloc[:,0].values

with open('Advertisement_test_data.json','r',encoding='utf-8') as json_test:
    data_test=json_test.read()
data_test=data_test[data_test.find('{'):]
data_test=pd.read_json(data_test,lines=True)
features_train=data.iloc[:,1:].values
labels_train=data.iloc[:,0].values



"""
Q2. Facial Recognition + OpenCV Python

Facial recognition is a biometric software application capable of uniquely identifying or verifying a person by comparing and analyzing.

Things that you need in this project: OpenCV and face_recognition

The project is mainly a method for detecting faces in a given image by using OpenCV-Python and face_recognition module. The first phase uses camera to capture the picture of our faces which generates a feature set in a location of your PC.

• The face_recognition command lets you recognize faces in a photograph or folder full for photographs.

It has two simple commands

Face_ recognition- Recognise faces in a photograph or folder full for photographs.
face_detection - Find faces in a photograph or folder full for photographs.
For face recognition, first generate a feature set by taking few image of your face and create a directory with the name of person and save their face image.


Then train the data by using the Face_ recognition module.By Face_ recognition module the trained data is stored as pickle file (.pickle).

By using the trained pickle data, we can recognize face.

The main flow of face recognition is first to locate the face in the picture and the compare the picture with the trained data set.If the there is a match, it gives the recognized label.
(Ref: https://github.com/sriram251/-face_recognition)


"""

#import the required libraries 
import numpy as np 
import matplotlib.pyplot as plt 
import cv2 


import subprocess
print("Enter Person name ")
name=input()
output=subprocess.getstatusoutput("mkdir E:\Forsk ML\ML2019\Day27\{}".format(name))
if (output[0]==0):
    pass
else:
    print("error: {}".format(output))


cap = cv2.VideoCapture(0)
face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret, photo = cap.read()
    face_coord  = face_detect.detectMultiScale(photo)
    if face_coord is ():
        pass
    else:
        x = face_coord[0][0]
        y = face_coord[0][1]
        w = face_coord[0][2]
        h = face_coord[0][3]
    
        r_photo = cv2.rectangle(photo , (x,y), (x+w,y+h), (0,255,0),  5 )

        cv2.imshow('my photo', r_photo)
        if cv2.waitKey(1) == 13:
            break
        
cv2.destroyAllWindows()
cap.release()


#creating dataset

# Load functions
def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

# Initialize Webcam
cap = cv2.VideoCapture(0)
count = 0

# Collect 100 samples of your face from webcam input
while True:

    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Save file in specified directory with unique name
        file_name_path = name+'/face' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)

        # Put count on images and display live count
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Face Cropper', face)
        
    else:
        print("Face not found")
        pass

    if cv2.waitKey(1) == 13 or count == 100: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()      
print("Collecting Samples Complete")


# pip install  opencv-contrib-python
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
print(cv2.__version__)
# Get the training data we previously made
data_path=name+'/'
# a=listdir('d:/faces')
# print(a)
# """
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

# Create arrays for training data and labels
Training_Data, Labels = [], []

# Open training images in our datapath
# Create a numpy array for training data
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
# 
# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)
boxes = face_recognition.face_locations(rgb, model= "hog")


model=cv2.face_LBPHFaceRecognizer.create()
# Initialize facial recognizer
# model = cv2.face_LBPHFaceRecognizer.create()
# model=cv2.f
# NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()

# Let's train our model 
model.train(np.asarray(Training_Data), np.asarray(Labels))
print("Model trained sucessefully")