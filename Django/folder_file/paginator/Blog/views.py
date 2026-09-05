from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.

def post_list(request):
    data = Post.objects.all().order_by('id')
    paginator = Paginator(data, 3) # Show 5 data per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_obj': page_obj})