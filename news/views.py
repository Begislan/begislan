from django.shortcuts import render, redirect
from .models import Articles
from .form import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView




# Create your views here.
def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'news': news})

class NewsDatailView(DetailView):
    model = Articles
    template_name = 'datails_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'create.html'

    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news-delete.html'



def create(request):
    error = ''
    error = ''
    if request.method =='Post':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'
    else:
        error_ = "Ошибка"

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error,
        'error_': error_
    }
    return render(request, 'create.html', data)