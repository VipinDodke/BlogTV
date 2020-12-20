from django.urls import path
from . import views
app_name ='video'
urlpatterns = [
    path('',views.index,name="BlogHome" ),
    path('code_and_anime/about/',views.about,name="AboutUS" ),
    path('code_and_anime/contact/',views.contact,name="Contact" ),
    path('code_and_anime/video/',views.video,name="Video"),
    path('code_and_anime/view/<int:myid>/',views.view,name="PageView"),
    path('code_and_anime/like_post/',views.like_post,name="like-post" ),
   # path('blog/hinglish/',views.hinglish,name="hinglish" ),
]
