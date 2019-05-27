# 1. Import os so we have access to the environment variables
import os
# 2. Import Flask from flask
from flask import Flask

# 3. Initialise a new instance of our Flask application
app = Flask(__name__)

# 4. Create our app.route() decorator
@app.route('/')
# 5. Define our function that is going to be bound to our decorator
def index():
    return "<h1>Hello There!</h1>"

# 6. Run our environment and set variables
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)