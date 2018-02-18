# app.wsgi
import sys
from app import app

# Expand Python classes path with your app's path
sys.path.insert(0, "/flask_apps/iot_button")

# Put logging code (and imports) here ...
# Initialize WSGI app object
application = app
