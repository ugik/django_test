from django.shortcuts import render_to_response
from article.models import Article
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from forms import ArticleForm
from django.core.context_processors import csrf

from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt

import logging
logr = logging.getLogger(__name__)


def article(request, article_id=1):
    if not request.user.is_authenticated():
	    return HttpResponseRedirect('/accounts/login')

    return render_to_response('article.html',
                         {'article': Article.objects.get(id=article_id) },
                              context_instance=RequestContext(request))

def articles(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')

    args = {}
    args.update(csrf(request))

    language = 'en-us'
    session_language = 'en-us'
	
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render_to_response('articles.html', args, context_instance=RequestContext(request))

def language(request, language='en-us'):
    response = HttpResponse('setting language to %s' % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language

    return response

def create(request):
    
    form = ArticleForm()

    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_article.html', args, context_instance=RequestContext(request))

def like_article(request, article_id):
	if article_id:
		a = Article.objects.get(id=article_id)
		a.likes += 1
		a.save()
	
	return HttpResponseRedirect('/articles/get/%s' % article_id)


def add_comment(request, article_id):
	a = Article.objects.get(id=article_id)

	if request.method == "POST":
		f = CommentForm(request.POST)
		if f.is_valid():
			c = f.save(commit=False)
			c.pub_date = timezone.now()
			c.article = a
			c.save()

			return HttpResponseRedirect("/articles/get/%s" % article_id)

	else:
		f = CommentForm()

	args = {}
	args['article'] = a
	args['form'] = f

	return render_to_response('add_comment.html', args)

def search_titles(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''
	
	logr.debug(search_text)
	articles = Article.objects.filter(title__contains=search_text)

	return render_to_response('ajax_search.html', {'articles' : articles})


import json
import os
# os.environ['HOME']
@csrf_exempt
def push(request):
	data = 'None'
	json_data = json.loads(request.body)
	try:
		json_data['home'] = os.environ['HOME']
	except KeyError:
		HttpResponseServerError("Malformed data")
	return HttpResponse(json.dumps(json_data))

#_____________________________________________________________________
# Hello examples:
# basic
def hello(request):
	html = "<html><body>Hi %s, this works.</body></html>" % 'GK'
	print request.GET
	return HttpResponse(html)

# using template
def hello_template(request):
	t = get_template('hello.html')
	html = t.render(Context({'name': 'GK'}))
	return HttpResponse(html)

# using template
def hello_bootstrap(request):
	t = get_template('helloBootstrap.html')
	html = t.render(Context({'name': 'GK'}))
	return HttpResponse(html)

# using simple template
def hello_template_simple(request):
    import pdb; pdb.set_trace()
    return render_to_response('hello.html', {'name': 'GK'}, context_instance=RequestContext(request))

# using class
class HelloTemplate(TemplateView):
	template_name = 'hello_class.html'

	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = 'Mike'
		return context

