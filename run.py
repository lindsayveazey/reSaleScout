#! /usr/bin/env python
from scout import app # /scout is where __init__.py and resale.py live on AWS; run.py located in dir above
app.run(host='0.0.0.0', debug=True)


