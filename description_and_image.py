import os
import sys
import requests
import json

# i stored my api key as a environmental variable
key = os.environ['ETSY_API_KEY']

def get_data_and_image_for_listing_id(listing_id):
    suffix = "?region=US&language=en&currency=USD&fields=title,tags,description&includes=Images&api_key="
    base = "https://openapi.etsy.com/v2/apps/listings/"
    url = base + str(listing_id) + suffix + key
    r = requests.get(url)

    if r.status_code == 200:
        response_json = json.loads(r.text)
        return response_json['results'][0]
    else:
        return None


# get the api info from a file of listing ids
def get_descriptions_and_images_for_file(filename):

    ## assuming one listing id per line and nothing else
    with open(filename, 'r') as file:
        for line in file:
            listing_id = line.trim()
            des = get_description_for_listing_id(listing_id)
            if des:
                print des


# example for getting a single description
results = get_data_and_image_for_listing_id(176554532)
print results['title']
print results['tags']
print results['description']
print results['Images']


