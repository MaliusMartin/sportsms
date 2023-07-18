from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Sport, Category, Detail,Post
# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def sports(request):
    sports = Sport.objects.all()
    # sports = Sport.objects.filter(owner=request.user).order_by('date_added')
    context = {'sports': sports, 'index':True}
    return render(request, 'core/sports.html', context)

def sport(request, sport_id):
    sport = Sport.objects.get(id=sport_id)
    # if sport.owner != request.user:
    #     raise Http404
    
    details = sport.detail_set.order_by('-date_added')
    context = {'sport':sport, 'details': details, 'index':True}
    return render(request, 'core/sport.html', context)

def index(request):
    sports = Sport.objects.all()
    categories = Category.objects.all()
    details = Detail.objects.order_by('-date_added')
    context = {'sports': sports, 'categories': categories, 'details': details}
    return render(request, 'core/index.html', context)


def detail(request, detail_id):
    detail = get_object_or_404(Detail, id=detail_id)
    context = {'detail': detail}
    return render(request, 'core/detail.html', context)



def about(request):
     return  render(request, 'core/about.html')



# def search(request):
#     query = request.GET.get('query')
#     results = Detail.objects.filter(text__icontains=query)
#     context = {'results': results, 'query': query}
#     return render(request, 'core/search.html', context)

def search(request):
    query = request.GET.get('query')
    results = Post.objects.filter(article__icontains=query)
    context = {'results': results, 'query': query}
    return render(request, 'core/search.html', context)


    



