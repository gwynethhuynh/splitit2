# splitit2

## Notes
- `python manage.py migrate`: Applies database migrations. When you create a Django model (Python class that defines the structure of a database table), you need a way to reflect these changes in the database. Migrations generate SQL commands to create, modify, or delete database tables and fields based on changes in the models
    - Migrations directory keeps track of changes to database 
- Add `rest_framework` to `INSTALLED_APPS` in backend/settings.py. Django REST framework is a toolkit for building Web APIs in Django (serialization, authentication, view classes, etc)
- Add `corsheaders` to `INSTALLED_APPS` in backend/settings.py. CORS is a security feature implemented by web browsers to prevent web pages from making requests to my Django backend by default. 
    - CORS Headers: to allow cross-origin requests, you need to configure your Dajngo backend to include the necessary CORS headers in its HTTP responses. The headers specify which domains or origins are allowed to make requests to your backend. 