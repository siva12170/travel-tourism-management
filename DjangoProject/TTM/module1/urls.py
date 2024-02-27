from.views import *
"""
URL configuration for TTM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *
urlpatterns = (
    # path('admin/', admin.site.urls),
    path("hello2/", hello1),
    path('hello123/', hello123),
    path('', newhomepage, name='newhomepage'),
    path('travelpackage/', travelpackage, name='travelpackage'),
    path('printcon/', printtoconsole,name='print_to_console'),
    path('p/', print1, name='print1'),
    path('r/',random12,name='rando1'),
    path('ran/', random123,name='rando'),
    path('getdate',get_date,name='get_date'),
    path('time/',tzfunctioncall,name='pytzexample'),

    path('dbase', registerloginfunction, name='dbase'),
    path('chartgen/',pie_chart,name='chart_form'),
    path('destina/',destin,name='destination1'),
    path('app/',thread,name='threadapp'),
    path('login/', login, name='login1'),
    path('register/', signup, name='signup2'),
    path('login1/',login1,name='login12'),
    path('signup1/',signup1,name='signup12'),
    path('contact/', contact, name='contact'),
    path('contactmail/', contactmail, name='contactmail'),

)
