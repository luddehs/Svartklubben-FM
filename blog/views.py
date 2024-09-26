from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    Displays a list of published blog posts related to :model:`Post`.
    This view retrieves all posts with a status of 'Published'
    and renders them in the specified template with pagination.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Displays the details of a single published post related to :model:`Post`.
    This view retrieves a specific blog post by its slug,
    ensuring it is published before rendering the detail template.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
