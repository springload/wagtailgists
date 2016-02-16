# Prod Gotchas

## Cache and middleware issues in the admin

Since Django 1.8 the `CACHE_MIDDLEWARE_ANONYMOUS_ONLY` it's deprecated. You can run into issues as all `/admin/` URLs will run through the cache middleware. This gets nasty when your custom views serve files without having them read.

Use the mighty `never_cache` decorator [https://docs.djangoproject.com/en/1.9/topics/http/decorators/#django.views.decorators.cache.never_cache](https://docs.djangoproject.com/en/1.9/topics/http/decorators/#django.views.decorators.cache.never_cache)

## Compressor

Django compressor is gonna be removed in the next Wagtail release (1.4) but with old version make sure your old templates are removed form the Linode server. Otherwise Django parses all folder and tries to compress all files inside the `compress` tag.

## Migrations

Same as the one below. Careful when migrations are being removed, or squashed, since old files need to be removed form the Linode machine. The `rsync` performed from CodeShio doesn't remove files, only copies the changed ones.