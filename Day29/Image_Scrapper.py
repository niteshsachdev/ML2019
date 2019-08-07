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
API_KEY = "a797f30e2cf44df9a2c6bc9499dc6c6e"
PATH = 'drive/dataset/Pokemons/'
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
    folder = PATH+term

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
                # p = os.path.sep.join([args["output"], "{}{}".format(str(total).zfill(8), ext)])
                p = os.path.sep.join([folder, "{}.{}".format(str(total).zfill(6), img_type)])
                # p = p.replace("\\","/")
                
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
    
    
