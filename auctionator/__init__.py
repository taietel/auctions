from flask import Blueprint
from .notifications import *
from .products import *
from .users import *


views = [product_views, notifications_views, users_views]
