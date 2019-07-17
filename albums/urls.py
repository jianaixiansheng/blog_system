from django.urls import path
from . import views

app_name="albums"

urlpatterns = [
    path('photo_album/<int:is_delete>',views.photo_album,name="photo_album"),
    path("photo_graph/<int:album_id>/<int:is_delete>",views.photo_graph,name="photo_graph"),
    path("upload_album/",views.upload_album.as_view(),name="upload_album"),
    path("upload_graph/<int:album_id>",views.upload_graph.as_view(),name="upload_graph"),
    path("delete_graph/<int:album_id>/<int:graph_id>",views.delete_graph,name="delete_graph"),
    path("delete_album/<int:album_id>",views.delete_album,name="delete_album"),
]
