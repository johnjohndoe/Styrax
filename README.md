# Styrax

A RESTful JSON-API to access geospatial tree data stored in a PostgreSQL/PostGIS database.
The application is written in Django using GeoDjango.

The development happens as part of the *Django mentoring initiative* in Berlin.


## Dependencies

* postgresql-9.3-postgis-2.1
* python3-dev


## Setup

For your development setup create *styrax/settings.py with the following content:

``` python
from styrax.settings_development import *

# Overwrite settings if needed
```

Please mind that it won't be committed to the repository since it is excluded there.


## Usage

Visit the following paths to access the API and documentation:

* http://localhost:8000/api
* http://localhost:8000/docs/
