# 1. Import os so we have access to the environment variables
import os
# 14. Import datetime function, which will allow us to include timestamps on out messages
from datetime import datetime
# 2. Import Flask from flask and import redirect for the redirect function to work
# 16. Import the render_template module from flask
# 17. Once created index.html file, import request and session modules:
# request handles username form; session handles the session variable
# 27. REFACTORING - add url_for module
from flask import Flask, redirect, render_template, request, session, url_for

# 3. Initialise a new instance of our Flask application
app = Flask(__name__)
# 18. To generate session ID, we need to assign secret key (normally set as environment variable in production)
# randomstring123 is the default value if Flask can't find the variable called SECRET
app.secret_key = os.getenv("SECRET", "randomstring123")

# 12. Create empty list to store our messages
messages = []

def add_message(username, message):
    '''13. Create function to append the user's messages to the variable list'''
    # 15. Create new variable to store the date and time
    # strftime method take our time and stringifys it to a given format
    now = datetime.now().strftime("%H:%M:%S")
    # 22. Create dictionary with key: value pairs that we can access
    # timestamp = now variable; from = username variable, message = message variable
    # 23. Amend the append method to refer to the dictionary instead
    # was messages.append("({0}) {1}: {2}".format(now, username, message))
    messages.append({"timestamp": now, "from": username, "message": message})

'''
def get_all_messages():
    13. Get all of the messages and separate them with a br so each message
    is displayed on a new line
    *****This can be deleted once steps 22 & 23 have been completed*****
    return "<br>".join(messages)
'''

# 4. Create our app.route() decorator
# 19. Once form updated in HTML file, add GET and POST methods to the index route
@app.route('/', methods=["GET", "POST"])
# 5. Define our function that is going to be bound to our decorator
def index():
    '''7. Main page with instructions. The idea is that we will be able to supply
    a username followed by a message.
    This function will link to the template in our homepage (render_template)'''
    # 20. Include an if statement to say if the method = POST, we want the
    # session cookie to equal the username that the user entered
    if request.method == "POST":
        session["username"] = request.form["username"]
    
    # 21. If the username exists, we will redirect to our personal chat page -
    # redirect to the contents of the session username variable (to route in step 8)
    if "username" in session:
        return redirect(url_for("user", username=session["username"]))
        
    return render_template("index.html")

# 8. Create new app route decorator for the username - this is treated as a variable
# It is in <>, as this is when the user types it in the address bar at the end of the URL
# eg. https://flask-chat-hebs87.c9users.io/hebs87
# 25. After creating textarea in chat.html file, add the post method
@app.route('/chat/<username>', methods=["GET", "POST"])
def user(username):
    '''9. Display chat messages and add using POST methods
    Function that binds to our route decorator that returns a string to the
    user that says "Welcome", followed by the username and the messages list
    from the get_all_messages function ***Remove after step 23***
    The Welcome, username is in h1 tags so that all message diplay below it'''
    
    # 26. If a message has been posted, we want to add it to our messages list
    if request.method == "POST":
        # Get username from our session variable
        username = session["username"]
        # Get the message that came from our form
        message = request.form["message"]
        # Call our add_message function and add the two variables that we've created
        add_message(username, message)
        # Then we redirect our user back - this gets rid of the POST data so it doesn't keep posting when page refreshes
        return redirect(url_for("user", username=session["username"]))
    
    # This can be removed on step 24. return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
    # 24. Once chat.html created, we want to pass in our variables here
    return render_template("chat.html", username=username, chat_messages=messages)
    
'''
NO LONGER NEEDED AFTER REFACTORING
# 10. Create app route decorator that allows the user to enter a message
# It is in angled brackets, as this is when the user types it after their username
# eg. https://flask-chat-hebs87.c9users.io/hebs87/Hello
@app.route('/<username>/<message>')
def send_message(username, message):
    11. Create a new message and redirect the user back to the chat page
    Function that binds to our route decorator that returns the list of messages
    to the user by calling our add_message function, and then redirects the
    user back to the user's personalised welcome page
    add_message(username, message)
    return redirect("/" + username)
'''

# 6. Run our environment and set variables - debug to True
# 28. Add default values and set debug to false (saves doing this in Heroku)
app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "5000")), debug=False)