@hooks.register('insert_editor_css')
def editor_css():
    """
    Add extra CSS files to the admin. These can be also found in the base.html template but
    because some sub-templates override the "extra_css" block we have to include them here as well.
    """
    css_files = [
        'wagtailadmin/css/vendor/font-awesome-4.2.0/css/font-awesome.min.css',
        'wagtailadmin/css/admin.css',
        'wagtailadmin/scss/layouts/home.scss',
    ]

    css_includes = format_html_join(
        '\n', '<link rel="stylesheet" href="{0}{1}">', ((settings.STATIC_URL, filename) for filename in css_files))
    return css_includes