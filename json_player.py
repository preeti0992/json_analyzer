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
    # return data
    
    # attributes = get_attributes(data)
    # return attributes
    # return {'data': data, "attributes":attributes}

    # attributes = get_attributes(data['dogs'])
    # return {"attributes":attributes}

    attributes = get_attributes(data['people'])
    return {"attributes":attributes}

def get_attributes(data):
    if isinstance(data, dict):
        return set(data.keys())
    elif isinstance(data, list):
        # create a set of keys from all objects in list
        # return get_attributes(data[0])
        attr_list = set()
        for d in data:
            attr_list =attr_list | get_attributes(d)
        attr_list = list(attr_list)
        return attr_list


