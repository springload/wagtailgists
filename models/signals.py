# Signals to clean up some undesired HTML markup in RichTextFields

PAGE_CLASSES = [your classes in here
]


@receiver(pre_save)
def pre_page_save(sender, instance, **kwargs):
    """
    Strip empty <p> elements from any RichTextField and other stuff when saved instance is one of the following
    classes: classes in here
    """
    if (kwargs.get('created', True) and not kwargs.get('raw', False)):
        if (sender in PAGE_CLASSES):
            for field in instance._meta.fields:
                if sender._meta.get_field(field.name).__class__.__name__ == "RichTextField":
                    field_to_string = getattr(instance, field.name)
                    field_to_string = re.sub(r"\n", "", field_to_string)
                    # Clean empty paragraphs
                    field_to_string = re.sub(r"<p>(<br/>|<br>)*</p>", "", field_to_string)
                    # Wrap images and embeds into figures instead of paragraphs
                    field_to_string = re.sub(
                        r"<p>((<img.+/.[^>]+>)|(<embed.[^>]+embedtype=\"image\".[^>]+/>))+:?(<br>|<br/>)*</p>",
                        r"<figure>\1</figure>",
                        field_to_string
                    )
                    clean_field = replace_tags(
                        field_to_string, {"<b>": "<strong>", "<i>": "<em>", "</b>": "</strong>", "</i>": "</em>"}
                    )
                    #  Replace content field
                    setattr(instance, field.name, clean_field)


@receiver(pre_save, sender=PageRevision)
def pre_page_revision_save(sender, instance, **kwargs):
    """
    Strip empty <p> elements from any RichTextField only when related page is a your_class in here
    """
    if (kwargs.get('created', True) and not kwargs.get('raw', False)):
        if isinstance(instance.page, your_class):
            mirror_page = instance.as_page_object()
            for field in mirror_page._meta.fields:
                if instance.page._meta.get_field(field.name).__class__.__name__ == "RichTextField":
                    field_to_string = getattr(mirror_page, field.name)
                    field_to_string = re.sub(r"\n", "", field_to_string)
                    # Clean empty paragraphs
                    field_to_string = re.sub(r"<p>(<br/>|<br>)*</p>", "", field_to_string)
                    # Wrap images and embeds into figures instead of paragraphs
                    field_to_string = re.sub(
                        r"<p>((<img.+/.[^>]+>)|(<embed.[^>]+embedtype=\"image\".[^>]+/>))+:?(<br>|<br/>)*</p>",
                        r"<figure>\1</figure>",
                        field_to_string
                    )
                    clean_field = replace_tags(
                        field_to_string, {"<b>": "<strong>", "<i>": "<em>", "</b>": "</strong>", "</i>": "</em>"}
                    )
                    #  Replace content field
                    setattr(mirror_page, field.name, clean_field)
                    #  To json again
                    instance.content_json = mirror_page.to_json()
