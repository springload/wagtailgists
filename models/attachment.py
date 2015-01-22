class Attachment(models.Model):

    """
    Represents a link to a document
    """
    attachment = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )
    title = models.CharField(max_length=255, help_text="Attachment title")

    panels = [
        FieldPanel('title'),
        DocumentChooserPanel('attachment'),
    ]