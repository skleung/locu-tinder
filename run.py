#!flask/bin/python
from app import app # imports the app variable; app variable holds the Flask instance
app.run(debug = True) # invokes the run method to start the server