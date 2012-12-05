from django.shortcuts import render_to_response

def index(request):
    page_details = {
        'title': "Welcome to Skeleton.",
        'stylesheets': {
            "skeleton/stylesheets/base.css",
            "skeleton/stylesheets/skeleton.css",
            "skeleton/stylesheets/layout.css",
        }
    }

    return render_to_response('skeleton/index.html', {'page': page_details})
