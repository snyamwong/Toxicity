# Toxicity
Conversion, software version 7.0

## Setting up a Virtual Environment

Not necessarily required, but helps a lot with 

https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

## Installing pip packages

```pip install -r requirements.txt```

Also remember to update the requirements.txt whenever you install a new package!

(Ideally we would have a linter tool to update requirements.txt whenever you push a commit but for a small scale project like this - there's no need).

## Updating requirements.txt

Whenever you install a new pip package:

```pip freeze > requirements.txt```
