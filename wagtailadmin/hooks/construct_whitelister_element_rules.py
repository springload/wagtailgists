@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    """
    Whitelist custom elements to the hallo.js editor
    """
    return {
        'blockquote': allow_without_attributes,
        'cite': allow_without_attributes,
        'a': attribute_rule({'href': check_url, 'class': True}),
    }