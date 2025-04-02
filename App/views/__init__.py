# blue prints are imported 
# explicitly instead of using *
from .dashboard import dashboard_views
from .auth import auth_views
from .admin import setup_admin


views = [dashboard_views, auth_views] 
# blueprints must be added to this list