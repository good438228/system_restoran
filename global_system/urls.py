from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.food_list, name='food_list'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='global_system/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:food_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('table_list', views.table_view, name='table_list_view'),
    path('tables/<int:table_id>/', views.table_detail, name='table_detail'),
    path('food/<int:pk>/', views.food_detail, name='food_detail'),
    path('book/', views.book_table, name='book_table'),
    path('reviews/', views.review_list, name='review_list'),
    path('leave-review/', views.leave_review, name='leave_review'),
    path('cart/buy/', views.buy, name='buy'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)