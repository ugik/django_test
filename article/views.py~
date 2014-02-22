from django.shortcuts import render_to_response
from article.models import Article
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView

def articles(request):
	language = 'en-us'
	session_language = 'en-us'
	
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']

	if 'lang' in request.session:
		session_language = request.session['lang']

	return render_to_response('articles.html',
							{'articles': Article.objects.all(),
							 'language' : language,
							 'session_language' : session_language})

def article(request, article_id=1):
	return render_to_response('article.html',
							{'article': Article.objects.get(id=article_id) })

def language(request, language='en-us'):
	response = HttpResponse('setting language to %s' % language)
	response.set_cookie('lang', language)
	request.session['lang'] = language

	return response


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

