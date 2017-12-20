[![Rest API Basics LOGO](https://cfe2-static.s3-us-west-2.amazonaws.com/media/cfe-blog/rest-api-basics-with-the-django-rest-framework/rest_api_basics_logo.jpg)](https://www.codingforentrepreneurs.com/blog/rest-api-basics-with-the-django-rest-framework/)

# REST API Basics


This is a basic, and rapid fire, guide on how to build a REST API with Django & Python. For much deeper depth and understanding, check out our new course on [REST API](https://kirr.co/rfqyre).


### Software
- Django 1.11.8 (https://kirr.co/hjogvt)
- Python 3.6.3 (https://kirr.co/ftq97z)
- Django Rest Framework 3.7.3 (https://kirr.co/svez0s)
- Django Rest Framework JWT 1.11.0 (https://kirr.co/vpibmo)


### Related Source Code: https://kirr.co/9gqpkg


### Initial Setup
```
virtualenv -p python3 restapi-basics

# activate it 
# mac: `source bin/activate`
# windows: `.\Scripts\activate`

pip install django==1.11.8 djangorestframework==3.7.3 djangorestframework-jwt==1.11.0

mkdir src && cd src

django-admin startproject cfehome .
django-admin startapp postings
```



### Update your settings to reflect the following:

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'postings'
]



REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
```







