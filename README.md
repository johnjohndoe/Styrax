[![Apache License](http://img.shields.io/badge/license-Apache%20License%202.0-lightgrey.svg)](http://choosealicense.com/licenses/apache-2.0/) [![VersionEye](https://www.versioneye.com/user/projects/569385cfaf789b002e000140/badge.svg)](https://www.versioneye.com/user/projects/569385cfaf789b002e000140)

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


## Authors

* [Tobias Preuss][tobias-preuss]


## License

    Copyright 2015-2016 Tobias Preuss

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

[tobias-preuss]: https://github.com/johnjohndoe
