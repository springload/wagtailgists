@hooks.register('insert_editor_js')
def editor_js():
    """
    Add extra JS files to the admin
    """
    js_files = [
        'wagtailadmin/js/vendor/jquery.htmlClean.min.js',
        'wagtailadmin/js/vendor/rangy-selectionsaverestore.js',
        'wagtailadmin/js/hallo-plugins/hallo-markdown.js',
        'wagtailadmin/js/hallo-plugins/hallo-blockquote.js',
        'wagtailadmin/js/hallo-plugins/hallo-cite.js',
        'wagtailadmin/js/hallo-plugins/to-markdown.js',
        'wagtailadmin/js/hallo-plugins/showdown.js',
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )

    return js_includes + """<script type="text/javascript">
            registerHalloPlugin('blockquotebutton');
            registerHalloPlugin('citebutton');
            registerHalloPlugin('togglemarkdown');
            registerHalloPlugin('hallocleanhtml', {
              format: false,
              allowedTags: ['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'em', 'strong', 'br', 'div', 'ol', 'ul', \
                'li', 'a', 'figure', 'embed', 'blockquote', 'cite'],
              allowedAttributes: ['style'],
            });
            </script>"""