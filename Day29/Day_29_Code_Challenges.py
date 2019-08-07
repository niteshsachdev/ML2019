"""
Q1. This is the guides code challenge where you have to first scrapp images from the internet and use them for training the CNN model.
This CNN model is multiclass model where you have to predict three classes beloging to the training dataset.

a. Scrapping Images of Pokemon using Bing's API. The three pokemon images you need to scrap are:
Bulbasaur, Charmander and Pikachu.

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 01 13:44:58 2018

@author: Kunal_Vaid
"""

# import the necessary packages
import requests
import cv2
import os

# set your Microsoft Cognitive Services API key along with (1) the
# maximum number of results for a given search and (2) the group size
# for results (maximum of 50 per request)
API_KEY = "<Your API Key>"
PATH = 'C:/Users/hp/Downloads/Pokemons/'
MAX_RESULTS = 250
GROUP_SIZE = 50

if not os.path.isdir(PATH):
    os.mkdir(PATH)

# set the endpoint API URL
URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

# store the search term in a convenience variable then set the
pokemons = []

while True:
    name = raw_input("Enter pokemon Name: ").lower()
    if not name:
        break
    pokemons.append(name)


for term in pokemons:
    # headers and search parameters
    headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
    params = {"q": term, "offset": 0, "count": GROUP_SIZE}
    
    # make the search
    print("[INFO] searching Bing API for '{}'".format(term))
    search = requests.get(URL, headers=headers, params=params)
    search.raise_for_status()
    
    # grab the results from the search, including the total number of
    # estimated results returned by the Bing API
    results = search.json()
    estNumResults = min(results["totalEstimatedMatches"], MAX_RESULTS)
    print("[INFO] {} total results for '{}'".format(estNumResults,
    	term))
     
    # initialize the total number of images downloaded thus far
    total = 0
    folder = PATH + term

    if not os.path.isdir(folder):
        os.mkdir(folder)
        
    # loop over the estimated number of results in `GROUP_SIZE` groups
    for offset in range(0, estNumResults, GROUP_SIZE):
        # update the search parameters using the current offset, then
        # make the request to fetch the results
        print("[INFO] making request for group {}-{} of {}...".format(offset, offset + GROUP_SIZE, estNumResults))
        params["offset"] = offset
        search = requests.get(URL, headers=headers, params=params)
        search.raise_for_status()
        results = search.json()
        print("[INFO] saving images for group {}-{} of {}...".format(offset, offset + GROUP_SIZE, estNumResults))
        
        # loop over the results
        for v in results["value"]:
            # try to download the image
            try:
                # make a request to download the image
                print("[INFO] fetching: {}".format(v["contentUrl"]))            
                r = requests.get(v["contentUrl"], timeout=30)
                 
                # build the path to the output image
                ext = v["contentUrl"][v["contentUrl"].rfind("."):]
                img_type = v["encodingFormat"]
                
                p = os.path.sep.join([folder, "{}.{}".format(str(total).zfill(6), img_type)])
                
                
                if str(img_type) != "animatedgif":
                # write the image to disk
                    f = open(p, "wb")
                    f.write(r.content)
                    f.close()
                    total += 1
                    
                    # try to load the image from disk
                    image = cv2.imread(p)
        
                    # if the image is `None` then we could not properly load the
                    # image from disk (so it should be ignored)
                    if image is None:
                            print("[INFO-DEL] deleting: {}".format(p))
                            os.remove(p)
                            continue
     
            # catch any errors that would not unable us to download the
            # image
            except Exception as e:
                # check to see if our exception is in our list of
                # exceptions to check for
                print "[ERROR]: ",str(e)

            
    print "*"*50            
    print "[END] Images Donwloaded for",term
    print "*"*50
    

b. Train the CNN model using this training dataset. You need to apply data augmentation before training the model.

# Convolutional Neural Network

# Installing Tensorflow
# pip install tensorflow

# Installing Keras
# pip install --upgrade keras

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 3, activation = 'softmax'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'categorical')

classifier.fit_generator(training_set,
                         steps_per_epoch = 100,
                         epochs = 10,#25
                         validation_data = test_set,
                         validation_steps = 200)

# Part 3 - Making new predictions

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('dataset/single_prediction/pokemon1.png', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices

# {'bulbasaur': 0, 'charmander': 1, 'pikachu': 2}

if int(result[0][0]) == 1:
    prediction = 'Bulbasaur'
elif int(result[0][1]) == 1:
    prediction = 'Charmander'
else:
    prediction = 'Pikachu'

print (prediction)


c. Predict the test image label: Bulbasaur, Charmander or Pikachu.

"""







"""
Q2. Code Challenge
code challenge - election data

1. Fetch the top parties of each state within each constituency with their vote %.

2. Visualize the top parties vote % in each constituency for Rajasthan.

3. Visualize the total seats gained by each party in each states.

4. Visualize the total seats won by the parties in the whole country
"""


import pandas as pd
dataset=pd.read_csv("election.csv")

#1. Fetch the top parties of each state within each constituency with their vote %.

top_party=dataset.groupby(['State','Constituency'])
top_party_try=dataset.groupby(['State','Constituency']).groups

new_data=top_party.get_group(('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'))
top=dataset[dataset['%']==top_party['%'].values]
top_party_new=top_party[top_party['%'].max()]