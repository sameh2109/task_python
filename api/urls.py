from django.conf.urls import url 
from api import views 

 
urlpatterns = [ 
    url('add_machine', views.add_coffeemachine),
    url('products_machine', views.show_coffeemachine),
    url(r'^get_machine/(?P<id>\w+)$', views.api_coffeemachine_detail),
    url(r'^delete_machine/(?P<id>\w+)$',views.api_coffeemachine_delete),
    url('add_pod', views.add_coffeepod),
    url('products_pod', views.show_coffeepod),
    url(r'^get_pod/(?P<id>\w+)$', views.api_coffeepod_detail),
    url(r'^delete_pod/(?P<id>\w+)$',views.api_coffeepod_delete)
    
]
