  

# django-sonar

  

`django-sonar` is a Django application that provides tools for monitoring and analyzing Django projects. This documentation will guide you through the installation, configuration, and usage of `django-sonar`.

  

## Table of Contents

  

- [Requirements](#requirements)

- [Installation](#installation)

- [Configuration](#configuration)

- [Usage](#usage)

- [Contributing](#contributing)

- [License](#license)

  

## Requirements

  

- Python 3.6+

- Django 2.2+

  

## Installation

  

To install `django` and `django-sonar`, you can use pip:

  

```bash
pip  install  django
pip  install  django-sonar

```



## Configuration

  

To configure `django-sonar` in your Django project, follow these steps:

  

1.  **Add `django-sonar` to your `INSTALLED_APPS`**:

  

```python
INSTALLED_APPS = [
...
'django_sonar',
...
]

```


2.  **3.  Add the urls to the main  urls.py file  in your project folder:**:

  

```bash

urlpatterns = [
    ...
    path('sonar/', include('django_sonar.urls')),
    ...
]
```
 

3.  **Update Your Settings**:

  

Configure `django-sonar` settings in your `settings.py` file:

  ```python
  # make sure to import os at the top of the file
import os

# Media files settings
STATIC_URL =  'static/'

# Media files settings

MEDIA_URL =  '/media/'  # URL that handles the media served from MEDIA_ROOT

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

```python

DJANGO_SONAR = {
    'excludes': [
        STATIC_URL,
        MEDIA_URL,
        '/sonar/',
        '/admin/',
        '/__reload__/',
    ],
}
```


4.  **Add DjangoSonar middleware**:
And finally add the DjangoSonar middleware to your middlewares to enable the data collection:
  
```python

MIDDLEWARE = [
  ...
  'django_sonar.middlewares.requests.RequestsMiddleware',
  ...
]

```

  

## Usage

 ### Install the PostgreSQL database adapter
  The application has to be configured to use postgreSQL as django default sqlite database doesnt supports jsonfield
```

pip install psycopg2

```
  
  ### Run Migration

  

Finally, run the migrations to prepare the data collection tables:


```

python manage.py migrate

```
  ### Testing

Now run the server for testing:


```

python manage.py runserver

```
  

### Monitoring

  

Once installed and configured, `django-sonar` automatically starts monitoring your Django project. You can access the monitoring dashboard by visiting:

  

```

http://<your-domain>/sonar/

```

## License

  

`django-sonar` is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

  

---

  

Thank you for using `django-sonar`! If you have any questions or need further assistance, please open an issue on our [GitHub repository](https://github.com/yourusername/django-sonar/issues).