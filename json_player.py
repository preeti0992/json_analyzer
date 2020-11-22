import json
import codecs
import os
from flask import Flask, render_template, url_for, json

def load_json():
    # file_name = 'input.json'
    # file_name = 'sample.json'
    file_name = 'sample_array.json'
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static\data", file_name)

    data = json.load(open(json_url, encoding="utf8"))
    
    attributes = get_attributes(data)
    return {'data': data, "attributes":attributes}
    # return {"attributes":attributes}
    # return attributes
    # return data

def get_attributes(data):
    if isinstance(data, dict):
        return list(data.keys())
    elif isinstance(data, list):
        # create a set of keys from all objects in list
        get_attributes(data[0])


