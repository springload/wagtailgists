class BlogIndexPage(RoutablePageMixin, Page):

    """
    Index page for blog elements. We want to use field category in the url to create custom URL for each blog entry. This
    class will handle 3 different URL patterns. Examples: /blog/category-one/first-blog-post  /blog/category-one/  /blog
    """
    # Let's use kickass subpage_urls to pass categories using regexps as slugs in the url LIKE A BOSS
    subpage_urls = (
        url(r'^(?P<category>[-a-zA-Z0-9_]+)/$', 'category_index', name='category_index'),
        url(r'^(?P<category>[-a-zA-Z0-9_]+)/(?P<article>[-a-zA-Z0-9_]+)/$', 'article_index', name='article_index'),
        url(r'^$', 'main', name='main'),
    )

    def article_index(self, request, category=None, article=None):
        """
        Handles articles URLS /blog/category/article
        """
        try:
            article = BlogPage.objects.select_related('category').live() \
                .filter(category__slug=category, slug=article)[0]
        except ObjectDoesNotExist:
            raise Http404
        except IndexError:
            raise Http404
        # Update template context
        context = article.get_context(request)
        return render(request, 'template_we_wanna_use.html', context)

    def category_index(self, request, category=None):
        """
        Handles articles URLS /blog/category/ and /blog/article (in case coming from admin)
        """
        # First check slug is not a news article (could be if request coming from admin)
        try:
            article = BlogPage.objects.select_related('category').get(slug=category)
            if article.live:
                return self.article_index(request, article.category.slug, article.slug)
            else:
                raise Http404
        except ObjectDoesNotExist:
            # If category not found go to 404
            categories = Category.objects.all()
            try:
                self.category = categories.get(slug=category)
            except ObjectDoesNotExist:
                raise Http404
            # Update template context
            context = super(BlogIndexPage, self).get_context(request)
            # Filter by category
            pages = self.children().filter(category__slug=category)
            # We could filter by tag or whatever
            tag = request.GET.get('tag')
            if tag:
                pages = pages.filter(tags__name=tag)
            # Cool pagination shit
            page = request.GET.get('page')
            paginator = Paginator(pages, settings.PAGINATION_PER_PAGE)  # Show 10 per page
            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)

            context['pages'] = pages
            return render(request, 'template_we_wanna_use.html', context)


    def main(self, request):
        """
        Handles main landing page URLS /blog/ where a special filter is applied. You could tweak the kind of posts
        you'd like to retrieve, this is just an example.
        """
        # Update template context
        context = super(BlogIndexPage, self).get_context(request)
        # Vars to pass to context
        pages = self.children()
        is_landing_page = True
        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            pages = pages.filter(tags__name=tag)
            is_landing_page = False

        if is_landing_page:  # Landing news page without passing any category or filter
            limit = 3
            pages = pages.filter(category__slug='news')[:limit]
        else:
            limit = settings.PAGINATION_PER_PAGE
            page = request.GET.get('page')
            paginator = Paginator(pages, limit)  # Show 10 per page
            try:
                pages = paginator.page(page)
            except PageNotAnInteger:
                pages = paginator.page(1)
            except EmptyPage:
                pages = paginator.page(paginator.num_pages)
        self.is_landing_page = is_landing_page
        context['pages'] = pages
        return render(request, 'template_we_wanna_use.html', context)
