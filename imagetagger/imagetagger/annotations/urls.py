from django.conf.urls import url

from . import views

app_name = 'annotations'
urlpatterns = [
    url(r'^export/(\d+)/auth/$', views.export_auth, name='export_auth'),
    url(r'^export/(\d+)/download/$', views.download_export, name='download_export'),
    url(r'^export/(\d+)/$', views.create_export, name='create_export'),
    url(r'^manage/annotation/(\d+)/$', views.manage_annotations, name='manage_annotations'),
    url(r'^annotation/delete/(\d+)/$', views.delete_annotation, name='delete_annotation'),
    url(r'^annotation/(\d+)/$', views.annotate, name='annotate'),
    url(r'^annotation/edit/(\d+)/save/$', views.edit_annotation_save, name='edit_annotation_save'),
    url(r'^annotation/edit/(\d+)/$', views.edit_annotation, name='edit_annotation'),
    url(r'^verify/(\d+)/$', views.verify, name='verify'),
]