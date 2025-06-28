import datetime

def global_context(request):
    """Add global context variables to all templates."""
    return {
        'current_year': datetime.datetime.now().year,
    }