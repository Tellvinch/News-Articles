from flask import render_template, request, redirect, url_for
from . import main
from ..models import Sources
from ..requests import get_sources, get_articles, search_article


#Views
@main.route('/')
def index():
    '''
    Function that returns the index page with its data
    '''
    all_sources = get_sources('all')
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
    sports_sources = get_sources('sports')
    entertainments_sources = get_sources('entertainments')
    health_sources = get_sources('health')
    science_sources = get_sources('science')
    title = 'News and More News'
    search_article = request.args.get('article_query')

    if search_article:
        return redirect(url_for('main.search', article_name=search_article))
    else:
        return render_template('index.html', title=title, all=all_sources, business=business_sources, technology=technology_sources, sports=sports_sources, entertainments=entertainments_sources, health=health_sources, science=science_sources)

@main.route('/articles/<source>')
def articles(source):
    '''
    view articles from a particular source page that returns its  data
    '''

    articles = get_articles(source)
    return render_template('article.html', articles=articles)

@main.route('/search/<article_name>')
def search(article_name):
    '''
    Method that displays the search result
    '''

    article_name_list = article_name.split('')
    article_name_format = "+".join(article_name_list)
    search_articles = search_article(article_name_format)
    return render_template('search.html', articles = search_articles)                