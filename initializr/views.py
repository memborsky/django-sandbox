from django.shortcuts import render_to_response

def index(request):
    page_details = {
        'title': "Welcome to the initializr bootstrap.",
        'stylesheets': {
            "initializr/stylesheets/bootstrap.min.css",
            "initializr/stylesheets/bootstrap-responsive.min.css",
            "initializr/stylesheets/main.css",
        },
        'javascript': {
            "initializr/javascript/vendor/jquery-1.8.3.min.js",
            "initializr/javascript/vendor/modernizr-2.6.2.min.js",
            "initializr/javascript/vendor/bootstrap.min.js",
            "initializr/javascript/main.js",
        },
    }

    return render_to_response('initializr/index.html', {'page': page_details})
