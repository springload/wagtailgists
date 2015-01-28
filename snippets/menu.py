
class LinkFields(models.Model):

    """
    Represents a link to an external page, a document or a fellow page
    """
    link_external = models.URLField(
        "External link",
        blank=True,
        null=True,
        help_text='Set an external link if you want the link to point somewhere outside the CMS.'
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose an existing page if you want the link to point somewhere inside the CMS.'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        on_delete=models.SET_NULL,
        blank=True,
        related_name='+',
        help_text='Choose an existing document if you want the link to open a document.'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_external:
            return self.link_external
        elif self.link_document:
            return self.link_document.url
        else:
            return "#"

    panels = [
        MultiFieldPanel([
            PageChooserPanel('link_page'),
            FieldPanel('link_external'),
            DocumentChooserPanel('link_document'),
            ],
            "Link"
        ),
    ]

    class Meta:
        abstract = True


class MenuElement(LinkFields):
    explicit_name = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        help_text='If you want a different name than the page title.'
    )
    short_name = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        help_text='If you need a custom name for responsive devices.'
    )
    css_class = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="CSS Class",
        help_text="Optional styling"
    )

    @property
    def title(self):
        if self.explicit_name:
            return self.explicit_name
        elif self.link_page:
            return self.link_page.title
        elif self.link_document:
            return self.link_document.title
        else:
            return None

    @property
    def url(self):
        return self.link

    def __unicode__(self):
        if self.explicit_name:
            title = self.explicit_name
        else:
            title = self.link_page.title
        return "%s ( %s )" % (title, self.short_name)

    class Meta:
        verbose_name = "Menu item"
        description = "Elements appearing in the main menu"

    panels = LinkFields.panels + [
        FieldPanel('explicit_name'),
        FieldPanel('short_name'),
        FieldPanel('css_class'),
    ]


class NavigationMenuMenuElement(Orderable, MenuElement):
    parent = ParentalKey(to='core.NavigationMenu', related_name='menu_items')


class NavigationMenuManager(models.Manager):

    def get_by_natural_key(self, name):
        return self.get(menu_name=name)


@register_snippet
class NavigationMenu(models.Model):

    objects = NavigationMenuManager()
    menu_name = models.CharField(max_length=255, null=False, blank=False)

    @property
    def items(self):
        return self.menu_items.all()

    def __unicode__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Navigation menu"
        description = "Navigation menu"


NavigationMenu.panels = [
    FieldPanel('menu_name', classname='full title'),
    InlinePanel(NavigationMenu, 'menu_items', label="Menu Items", help_text='Set the menu items for the current menu.')
]