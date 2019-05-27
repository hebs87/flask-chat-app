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
    '''7. Main page with instructions. The idea is that we will be able to supply
    a username followed by a message'''
    return "To send a message use /USERNAME/MESSAGE"

# 8. Create new app route decorator for the username - this is treated as a variable
# It is in <>, as this is when the user types it in the address bar at the end of the URL
# eg. https://flask-chat-hebs87.c9users.io/hebs87
@app.route('/<username>')
def user(username):
    '''9. Function that binds to our route decorator that returns a string to the
    user that says "Hi", followed by the username that they provided'''
    return "Hi " + username

# 9. Create app route decorator that allows the user to enter a message
# It is in angled brackets, as this is when the user types it after their username
# eg. https://flask-chat-hebs87.c9users.io/hebs87/Hello
@app.route('/<username>/<message>')
def send_message(username, message):
    '''10. Function that binds to our route decorator that returns a string to the
    user that says their username: message'''
    return "{0}: {1}".format(username, message)

# 6. Run our environment and set variables
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)