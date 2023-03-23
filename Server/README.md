## A simple login system using Python, MongoDB and FastAPI

### Dependencies:
* [Python3]
* [FastAPI]
* [MongoDB]

### Getting started


* Create a virtual enviroment
windows: `python -m venv venv`
* Activate enviroment with
`.\venv\Scripts\activate`
* Install dependencies with
`pip3 install -r requirements.txt`

### FastAPI

* Run the following command `uvicorn index:app --reload` 
* API documentation available at http://localhost:8000/docs

### MongoDB Atlas
* Using the community edition
* Recommend using the [MongoDB for VS Code extension]
* Will need a `username` and `password` and IP may need to be whitelisted :lock:
* Connect with hosted atlas deployment using connection string `mongodb+srv://<username>:<password>@userscluster.tt2s9e7.mongodb.net/test`


[FastAPI]: <https://fastapi.tiangolo.com>
[MongoDB]: <https://mongodb.com/try/download/community>
[MongoDB for VS Code extension]: <https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode>
[Python3]: <https://www.python.org/downloads/release/python-3100/>



