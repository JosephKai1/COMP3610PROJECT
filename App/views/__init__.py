# Blueprints are imported explicitly instead of using *
from .dashboard import dashboard_views
from .trends import trend_views
from .analysis import analysis_views
from .auth import auth_views
from .admin import setup_admin

# Blueprints must be added to this list
views = [
    dashboard_views, 
    trend_views,
    analysis_views,
    auth_views
]
