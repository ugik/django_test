from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from article.models import Article

def articles(request):
	return render_to_response('articles.html',
							{'articles': Article.objects.all() })

def article(request, article_id=1):
	return render_to_response('article.html',
							{'article': Article.objects.get(id=article_id) })


#_____________________________________________________________________
# Hello examples:
# basic
def hello(request):
	html = "<html><body>Hi %s, this works.</body></html>" % 'GK'
	return HttpResponse(html)

# using template
def hello_template(request):
	t = get_template('hello.html')
	html = t.render(Context({'name': 'GK'}))
	return HttpResponse(html)

# using simple template
def hello_template_simple(request):
	return render_to_response('hello.html', {'name': 'GK'})

# using class
class HelloTemplate(TemplateView):
	template_name = 'hello_class.html'

	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = 'Mike'
		return context
