FacebookGroupCollector
=====================================

This repo contains [Jupyter](http://jupyter.org/) notebooks and Python scripts for collecting and analyzing data from [Facebook](http://www.facebook.com).

## What's in the repo

- [```facebook_group_fetch.html```](scripts/facebook_group_fetch.html) - HTML code that is used to input group link and collect raw data from Facebook by using [Graph API and JavaScript SDK](https://developers.facebook.com/docs/javascript).
- [```facebook_group_grabdata.js```](scripts/facebook_group_fetch.html) - Javascript code that is used in HTML file to collect raw data from Facebook by using [Graph API and JavaScript SDK](https://developers.facebook.com/docs/javascript).
- [```facebook_group_cache.py```](scripts/facebook_group_cache.py) - Python code that cache raw downloaded data, and adds meta data including Facebook group ID, Group name, last post ID, last post, and all other content ("[data]").
- [```facebook_group_parse.py```](scripts/facebook_group_parse.py) - Parse the raw data into wanted JSON schema. See more about the schema in [```FacebookCollectorWorkflow.ipynb```](FacebookCollectorWorkflow.ipynb)
- [```facebook_group_toCSV.py```](scripts/facebook_group_toCSV.py) - The Python action that convert clean JSON data into CSV format.
- [```facebook.ipynb```](facebook.ipynb) - Jupyter notebook that explains the collection and analysis processes and runs the scripts 

## In case of emergency

We are not actively supporting the repo, but we will try to help if we can. Email [info@casmlab.org](mailto:info@casmlab.org) if you'd like some help or have questions. If you find bugs or have a feature request, please [submit an Issue](https://help.github.com/articles/creating-an-issue/).
