# yusuke-hi-rei add start
'''
 アプリケーションのルーティング設定
'''

from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
]

# yusuke-hi-rei add end
