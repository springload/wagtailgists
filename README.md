# wagtailgists
Useful snippets for Wagtail. Under permanent construction.

##Models stuff

Including abstract classes (interfaces), utilities, signals and so on...

* [Models](./models/models.md)
* [Tags](./customtags/customtags.md)
* [Snippets](./snippets/snippets.md)

## Generate clean fixtures

This is the ultimate mofo command to generate clean fixtures for your project:

```
./manage.py dumpdata --indent=4 -e contenttypes -e auth.permission -e auth.group -e sessions -e wagtailcore.site -e wagtailcore.pagerevision -e wagtailcore.grouppagepermission -e wagtailimages.filter -e wagtailimages.rendition --natural-primary --natural-foreign > core/fixtures/initial_data.json
```

Some apps that my be useful listed here:

https://github.com/torchbox/wagtail/wiki/Contributed-apps-and-website-code

