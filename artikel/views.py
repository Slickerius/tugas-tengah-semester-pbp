from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Artikel

def index(request):
    return render(request, 'index.html', {}) 

class ArtikelListView(ListView):
    model = Artikel
    template_name = 'artikel_list.html'
    paginate_by = 9

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        if query:
            object_list = self.model.objects.filter(Q(body__icontains=query) | Q(title__icontains=query)).order_by('-id')
        else:
            object_list = self.model.objects.all().order_by('-id')
        return object_list

class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArtikelDetailView , self).get_context_data(**kwargs)
        context['articles'] = Artikel.objects.order_by('-id')[:10]
        return context