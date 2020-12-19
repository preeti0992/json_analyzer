## JSON player!

This project explores a sample JSON file as input, explores all attributes for the sample JSON.

### Input
#### Sample data
```
{
    "people" :[
        {
            "name": "Bob",
            "languages": ["English", "French"]
        },
        {
            "name": "Katy",
            "languages": ["English", "Spanish"]
        }
    ],

    "dogs": [
        {
            "name": "Marley",
            "breed": "Poodle",
            "age": 1
        },
        {
            "name": "Spike",
            "breed": "Buster",
            "vaccinated": true
        }
    ]
}
```

### Output
Output is a list of attributes.

### Run instructions
`pip install -r requirements.txt`\
`$env:FLASK_ENV = "development"`
`python -m flask run`

#### See JSON data
 http://127.0.0.1:5000/

#### See JSON attributes for part of JSON file
http://127.0.0.1:5000/attributes


