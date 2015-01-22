@hooks.register('register_admin_menu_item')
def register_menu_item():
    url = '/new/url/'

    return MenuItem(
        'New Item',
        url,
        classnames='icon icon-image',
        order=500
    )
