## [HOME | RETURN](https://github.com/plexoio/musa/blob/main/documentation/readme/erd/erd.md)

# ERD & Code recommendations & Voting System Architecture

## Model Relationships

We have the **VoteCard model**, which is designed to facilitate the creation of voting cards for different campaigns. This model has relationships with the Category model, the VoteRecord model, and the User model, serving their respective purposes.

Through the admin panel, we utilize the **ElectedPerson model** to record the names of candidates. Each candidate is associated with a specific VoteCard, indicating the campaign they are part of. Furthermore, the ElectedPerson model has a boolean attribute that signifies whether that person has been elected, and this value will be updated once the voting campaign concludes.

When users cast their votes, entries are added to the **VoteRecord table**. This table captures the specific VoteCard being voted on, the voter's ID, the timestamp of the vote, and the chosen candidate (elected person). The list of available candidates for voting is derived from the selections stored in the ElectedPerson table.

With this architecture in place, I can leverage Python to compute the number of votes corresponding to a specific VoteCard and candidate. This tally will be based on the entries in the VoteRecord table.

## Preventing Duplicate Voting

How do I make sure that one user cannot vote twice for the same vote_card?

### 1. Database Level Constraint:

Set a **unique constraint** on the combination of `voter` and `vote_card` in the `VoteRecord` model. This ensures that no two records can exist with the same user and vote_card combination.

```python
class VoteRecord(models.Model):
    vote_card = models.ForeignKey(VoteCard, on_delete=models.CASCADE)
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['vote_card', 'voter']
```

### 2. Application Level Check:

Before creating a new vote record, check if one already exists with the provided `voter` and `vote_card` combination. If it exists, do not allow the new record to be created.

```python
def vote(request, vote_card_id):
    user = request.user
    vote_card = VoteCard.objects.get(id=vote_card_id)

    if VoteRecord.objects.filter(vote_card=vote_card, voter=user).exists():
        return HttpResponse("You've already voted for this card!")
    else:
        VoteRecord.objects.create(vote_card=vote_card, voter=user)
        return HttpResponse("Vote recorded!")
```

### 3. Frontend Measures:

If you're displaying the `vote_card` items on a frontend application (like a website), you can disable or hide the voting button for those items the user has already voted for. This can be determined by checking the existence of a `VoteRecord` for the user-vote_card combination. Using AJAX, you can also dynamically check if a user has voted before rendering the option to vote.

### 4. Regular Audits:

Periodically, you can run scripts or queries to detect any anomalies in the voting data, like users voting multiple times. This will serve as an additional check and balance.

### 5. Enhance Security:

Ensure that your application's endpoints (APIs or views) that handle voting are secured to prevent tampering or unauthorized voting attempts. Rate limiting can also be set up on the voting endpoints to prevent spamming.

## Displaying Vote Counts

If you want to display the count of votes a specific `VoteCard` has received on the frontend, you don't need a direct attribute on the `VoteCard` model. Instead, you can compute this on-the-fly from the `VoteRecord` model. The advantage of this approach is that the data remains dynamic and there's no risk of it becoming outdated or out of sync with the actual votes.

### 1. Using the ORM Query:

Given a specific `VoteCard`, you can find out how many votes it has received by querying the `VoteRecord` model.

```python
votes_count = VoteRecord.objects.filter(vote_card=some_vote_card).count()
```

### 2. Displaying on the Frontend:

Once you have the count, you can pass it to the frontend (e.g., to your template if you're using Django) and display the number of votes that `VoteCard` has received.

### 3. Optimization:

If you expect a high volume of votes and frequent page refreshes or loads, continuously querying the database every time to get the count might be inefficient. In such a case, consider the following:

- **Caching**: Use caching mechanisms to store the vote count. Update the cache either periodically or whenever a new vote is recorded.
  
- **Dedicated Field**: If real-time accuracy isn't crucial, you can have a dedicated field in the `VoteCard` model, say `vote_count`, which stores the count. You then increment this field every time a new vote is recorded. However, be cautious with this approach as it can lead to race conditions in a high-concurrency environment.

## Recommendations and Considerations

Your database models seem well thought out and structured, especially in light of the clarified relationships and attributes discussed earlier.

### 1. Data Integrity:

Ensure that your ORM or database setup has appropriate constraints. This includes ensuring that ForeignKeys cannot be null (unless intentionally designed that way) and ensuring that unique constraints are enforced.

### 2. Security:

- Passwords: Ensure that the `PasswordField` in the `User Model` securely hashes and salts passwords. Never store plain text passwords.
  
- Authorization: The `role` in the `User Model` implies that there may be different types of users with different permissions. Make sure you have proper authorization checks in place.

### 3. Scalability:

If you expect a large number of votes or users, consider the scalability of your database and application. Indexing certain fields (e.g., `email`, `username`, `category_name`) might be beneficial to speed

 up query times. Also, think about optimizing complex queries and possibly employing caching mechanisms for frequently accessed data.

### 4. Additional Functionalities:

Depending on the specific use case of your application, consider functionalities like anonymous voting, real-time vote tallying, or integrating with third-party authentication providers.

### 5. Testing:

Before deploying or rolling out new features, thorough testing is crucial. This includes unit tests, integration tests, and end-to-end tests.

### 6. Frontend Integration:

As you design the frontend, think about user experience (UX). Display informative messages in cases where a user might be trying to vote for something they already voted for, or if their session expires.

## Database Indexing with Django

In Django, to speed up database operations on specific fields, you can index those fields. Indexing can significantly improve read operations at the expense of slightly slower write operations (due to the overhead of maintaining the index).

### 1. For the `email` field in the User Model:

```python
email = models.EmailField(unique=True, db_index=True)
```

### 2. For the `username` field in the User Model:

```python
username = models.CharField(max_length=30, unique=True, db_index=True)
```

### 3. For the `category_name` field in the Category Model:

```python
category_name = models.CharField(max_length=100, db_index=True)
```

**Note**:

- **Uniqueness**: The `unique=True` argument automatically creates an index for that field. So, if you've set a field to be unique, you don't need to specify `db_index=True` again for that field.

- **Monitoring and Performance**: Regularly monitor the performance of your database and queries to determine if the indexes are providing the desired speed-up or if they need to be adjusted. There are tools and extensions like Django Debug Toolbar that can help with this.

## Language Translations

In Django, the `{% trans %}` template tag is used to translate strings. This is part of Django's internationalization (i18n) and localization (l10n) framework.

To add or modify translations for your project, you'll typically follow these steps:

1. **Enable Internationalization**: 
   Make sure you have the following in your `settings.py`:
   ```python
   USE_I18N = True
   ```

2. **Add Middleware and Context Processor**:
   Again in `settings.py`, ensure you have:
   ```python
   MIDDLEWARE = [
       ...
       'django.middleware.locale.LocaleMiddleware',
       ...
   ]

   TEMPLATES = [
       {
           ...
           'OPTIONS': {
               'context_processors': [
                   ...
                   'django.template.context_processors.i18n',
                   ...
               ],
           },
       },
   ]
   ```

3. **Setup Languages**:
   Define the languages you plan to support in your `settings.py`:
   ```python
   LANGUAGES = [
       ('en', _('English')),
       ('es', _('Spanish')),
       ... # other languages
   ]
   ```

4. **Define Translations**:
   Use the `makemessages` command to generate a `.po` file for each language. This file will contain all the strings that need translation:
   ```bash
   python manage.py makemessages -l es  # For Spanish
   ```

   This will generate a file in `locale/es/LC_MESSAGES/django.po`.

5. **Edit `.po` Files**:
   Open the `.po` file and add translations for each string. For instance:
   ```po
   msgid "Delete Account"
   msgstr "Eliminar cuenta"
   ```

6. **Compile Messages**:
   After adding translations, compile them to create `.mo` files:
   ```bash
   python manage.py compilemessages
   ```

7. **Use in Templates**:
   Now, in your templates, you can use the `{% trans %}` tag to mark strings for translation:
   ```html
   {% load i18n %}
   <button>{% trans "Delete Account" %}</button>
   ```

When you add new strings in your templates using the `{% trans %}` tag, you'll need to repeat steps 4-6 to update and compile your translations.

Remember, translations rely on both the `.po` and `.mo` files. The `.po` file is human-readable and where you add your translations, while the `.mo` file is machine-readable and what Django uses at runtime.

### Catching - Cache

Caching is an essential aspect of optimizing web applications, as it can significantly reduce server load and improve response times. Django offers various caching mechanisms, and implementing them requires consideration of what parts of your application benefit most from caching.

Here's a step-by-step guide to implement caching in a Django project:

### 1. Choose a Cache Backend:
Django supports several cache backends:
- **Memory Cache** (locmem)
- **Filesystem Cache**
- **Database Cache**
- **Memcached**
- **Redis**

For production, **Memcached** and **Redis** are recommended. Redis offers more features than Memcached, but both are effective.

### 2. Configure Cache in `settings.py`:

For **Memcached**:
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
```

For **Redis** (using `django-redis` package):
```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

### 3. Cache Your Views:

The simplest form of caching is per-view caching.

Use the `cache_page` decorator:
```python
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache for 15 minutes
def my_view(request):
    # ...
```

### 4. Template Fragment Caching:

If caching an entire view is too broad, you can cache specific template fragments using the `{% cache %}` template tag.

```html
{% load cache %}
{% cache 500 sidebar_for_user user.username %}
    <!-- Expensive rendering here -->
{% endcache %}
```

### 5. Cache Database Queries:

Django's ORM will cache query results for the duration of a request. To cache querysets for a longer time, use the `cache` API.

```python
from django.core.cache import cache

def get_data():
    data = cache.get('my_key')
    if data is None:
        data = MyModel.objects.all()
        cache.set('my_key', data, 60 * 15)  # 15 minutes
    return data
```

### 6. Middleware Caching:

Django provides cache middleware that can be added to `MIDDLEWARE` in `settings.py`:
- `UpdateCacheMiddleware`: Caches each URL as it's requested.
- `FetchFromCacheMiddleware`: Checks the cache for the requested URL.

Ensure `UpdateCacheMiddleware` is the first middleware class and `FetchFromCacheMiddleware` is the last.

### 7. Clearing Cache:

Sometimes, you might need to clear or bypass the cache:
- `cache.clear()`: Clears the entire cache.
- `cache.delete('my_key')`: Clears a specific cache key.
- For development, use the `CACHE_BYPASS` parameter in the URL to bypass cache.

### 8. Advanced Caching:

- **Vary on Headers**: Use `@vary_on_headers('User-Agent')` to maintain a separate cache for different user agents.
- **Vary on Cookies**: Use `@vary_on_cookie` to cache page versions based on user sessions.
- **Versioning**: When the data changes, increase a version number and use it in the cache key to avoid stale data.

### Recommendations:

- Monitor cache efficiency (hit/miss ratio).
- Regularly review cached data to ensure it's still relevant.
- Be careful with caching authenticated user data. Make sure not to expose one user's data to another.

Remember, while caching can drastically improve performance, it can also introduce complexities, especially regarding data freshness. Always test your caching strategy thoroughly.