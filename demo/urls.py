from django.conf.urls import url 
from . import tagging_data_view,tagging_data_writefile_view

urlpatterns = [
    url(r'^$', tagging_data_writefile_view.tagging_push),
    url(r'^tagging_data', tagging_data_view.showtagging_data),
    url(r'^tagging-get', tagging_data_writefile_view.tagging_push)
]
