@register.inclusion_tag('core/includes/main_nav.html', takes_context=True)
def main_menu(context, menu_name=None, current_page=None):
    """
    Retrieves the MenuElement(s) under the NavigationMenu with given menu_name
    """

    if menu_name is None or current_page is None:
        return None
    try:
        menu_items = NavigationMenu.objects.get(menu_name=menu_name).items

    except ObjectDoesNotExist:
        return None

    return {
        'links': menu_items,
        'request': context['request']
    }