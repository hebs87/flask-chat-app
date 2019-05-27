# 1. Import os so we have access to the environment variables
import os
# 2. Import Flask from flask and import redirect for the redirect function to work
from flask import Flask, redirect

# 3. Initialise a new instance of our Flask application
app = Flask(__name__)
# 11. Create empty list to store our messages
messages = []

def add_messages(username, message):
    '''12. Create function to append the user's messages to the variable list'''
    messages.append("{0}: {1}".format(username, message))

def get_all_messages():
    '''13. Get all of the messages and separate them with a br so each message
    is displayed on a new line'''
    return "<br>".join(messages)

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
    '''9. Display chat messages
    Function that binds to our route decorator that returns a string to the
    user that says "Welcome", followed by the username and the messages list
    from the get_all_messages function
    The Welcome, username is in h1 tags so that all message diplay below it'''
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())

# 9. Create app route decorator that allows the user to enter a message
# It is in angled brackets, as this is when the user types it after their username
# eg. https://flask-chat-hebs87.c9users.io/hebs87/Hello
@app.route('/<username>/<message>')
def send_message(username, message):
    '''10. Create a new message and redirect the user back to the chat page
    Function that binds to our route decorator that returns the list of messages
    to the user by calling our add_messages function, and then redirects the
    user back to the user's personalised welcome page'''
    add_messages(username, message)
    return redirect("/" + username)

# 6. Run our environment and set variables
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)