class IndexPage(models.Model):

    """
    Abstract Index Page class. Declare a couple of abstract methods that should be implemented by
    any class implementing this interface.
    """
    # Just one instance allowed
    def clean(self):
        validate_only_one_instance(self)

    def children(self):
        raise NotImplementedError("Class %s doesn't implement aMethod()" % (self.__class__.__name__))

    def get_context(self, request):
        raise NotImplementedError("Class %s doesn't implement aMethod()" % (self.__class__.__name__))

    class Meta:
        abstract = True