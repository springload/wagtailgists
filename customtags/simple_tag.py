

@register.inclusion_tag('your_tag_template.html', takes_context=False)
def trades_tiles(variables=None):
    """
    Simple tag accepting params and passing them to the html defined in the registry call.
    You can always set takes_context=True and get stuff from the context (should be passed as
    the first parameter in the function!).
    """
    return {
        'vars': variables
    }