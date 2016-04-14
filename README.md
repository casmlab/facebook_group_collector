FacebookGroupCollector
=====================================

This repo contains [Jupyter](http://jupyter.org/) notebooks and Python scripts for collecting and analyzing data from [Facebook](http://www.facebook.com).

## Required packages
- unicodecsv

## What's in the repo

- [```fetch.html```](fetch.html) - HTML code that is used to collect raw data from Facebook by using [Graph API and JavaScript SDK](https://developers.facebook.com/docs/javascript).
- [```merge.py```](merge.py) - Python code that combines raw downloaded data into one giant file, and adds meta data including Facebook group ID, Group name, last post ID, last post, and all other content ("[data]").
- [```parse.py```](parse.py) - Parse the raw data into wanted JSON schema. See more about the schema in [```FacebookCollectorWorkflow.ipynb```](FacebookCollectorWorkflow.ipynb)
- [```toCSV.py```](toCSV.py) - The Python action that convert clean JSON data into CSV format.
- [```FacebookCollectorWorkflow.ipynb```](FacebookCollectorWorkflow.ipynb) - Jupyter notebook that explains the collection and analysis processes and runs the scripts 

## In case of emergency

We are not actively supporting the repo, but we will try to help if we can. Email [info@casmlab.org](mailto:info@casmlab.org) if you'd like some help or have questions. If you find bugs or have a feature request, please [submit an Issue](https://help.github.com/articles/creating-an-issue/).