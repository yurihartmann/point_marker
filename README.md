# Point Marker

#### Requirements
 - Python 3.*
 - Pip
 
## How to run:

1. `pip install virtualenv`

2. `virtualenv venv`

3. Active virtualvenv
- Mac OS / Linux
`source venv/bin/activate`
- Windows
`venv\Scripts\activate`

4. `pip install -r requirements.txt`

5. `python3 run.py`

Ready: Access the `http://127.0.0.1:5000/` to use

## Unittest:
Execute the same way for run without 6 step and execute:
- `python3 -m pytest --cov=app/`
