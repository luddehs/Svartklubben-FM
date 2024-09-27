from django.shortcuts import render
from .models import About


def about_me(request):
    """
    Renders the About page displaying information related to :model:`About`.
    This view retrieves the most recently updated About entry from the database
    and passes it to the template for rendering.

    **Context**
    ``about``
         The most recent instance of :model:`about.About`.
    **Template:**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
