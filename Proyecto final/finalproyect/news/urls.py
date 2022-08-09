from django.urls import path
from news.views import  List_articles, Detail_article, Create_article, Delete_article

urlpatterns = [
    path('list_news/', List_articles.as_view(), name='List_articles'), # Al usar class agregamos el .as_view()
    path('detail_news/<int:pk>/', Detail_article.as_view(), name='Detail_article'),
    path('delete_news/<int:pk>/', Delete_article.as_view(), name='Delete_article'),
    path('create_news/',Create_article.as_view(),name="create_article"),
   
]