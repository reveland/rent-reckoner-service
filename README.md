## Rent Reckoner

### Install
The service was written/tested in python 3 ([download link](https://www.python.org/downloads/))

Then you gonna need some python package
```
pip numpy python-dateutil flask
```

### Run
Run this command in the root directory 
```
python ./rent_reckoner/rest.py
```

### Endpoints
|URL|Description|
|-|-|
|/habitations/<int:habitant_id>/residents/<int:resident_id>/dept|gives back the resident dept|
|/habitations/<int:habitant_id>/bills|gives back the bills in a ui desider format|

You can test them like
```
curl localhost:5000/habitations/4/residents/0/dept
```

### Modify the input data
You can create an own habitation by just create a file in `rent-reckoner/data/` with `habitation_` prefix, there is a example file named `rent-reckoner/data/habitation_aradi`

The desirable file structure:
```
{
    "id": <int>,
    "residents": [
        {
            "name": <string>,
            "start": <string>, // like "2016-09-01T00:00:00"
            "end": <string>, // like "2017-09-01T00:00:00"
            "paid": <string>, // like "500" (should be int)
            "id": <int>
        }
    ],
    "bills": [
        {
            "start": <string>, // like "2016-09-01T00:00:00"
            "end": <string>, // like "2016-09-01T00:00:00"
            "type": <string>,
            "amount": <int> // like 500 
        }
    ]
}
```

### UI
To see the bills you need a [rent-reckoner-ui](https://github.com/reveland/rent-reckoner-ui)
