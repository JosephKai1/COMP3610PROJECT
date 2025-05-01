# Blueprints are imported explicitly instead of using *
from .dashboard import dashboard_views
from .trends import trend_views
from .analysis import analysis_views
from .comparison import comparison_views
from .auth import auth_views

# Blueprints must be added to this list
views = [
    dashboard_views, 
    trend_views,
    analysis_views,
    comparison_views,
    auth_views
]
