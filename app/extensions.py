from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# This file is used to store all extensions used in the app
# add sqlalchemy extension
db = SQLAlchemy()
# add csrf extension
csrf = CSRFProtect()
