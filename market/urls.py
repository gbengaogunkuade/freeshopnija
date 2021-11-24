from django.urls import path
from market import views




app_name = 'market'


urlpatterns = [
    path('', views.MarketListView.as_view(), name='market_home'),
    path('create/', views.marketCreate, name='create'),
    path('search/', views.searchView, name='market_search'),
    path('search_result/', views.searchResultView, name='market_search_result'),
    path('market_category_vehicles/', views.marketCategoryVehicleView.as_view(), name='market_category_vehicles'),
    path('market_category_phones/', views.marketCategoryPhoneView.as_view(), name='market_category_phones'),
    path('market_category_electronics/', views.marketCategoryElectronicsView.as_view(), name='market_category_electronics'),
    path('market_category_fashion/', views.marketCategoryFashionView.as_view(), name='market_category_fashion'),
    path('market_category_baby_products/', views.marketCategoryBabyProductsView.as_view(), name='market_category_baby_products'),
    path('market_category_others/', views.marketCategoryOthersView.as_view(), name='market_category_others'),
    path('<slug:slug>/', views.MarketDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', views.MarketUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.MarketDeleteView.as_view(), name='delete'),
]





# urlpatterns = [
#
#     path('create/', views.marketCreate, name='create'),
#     path('<slug:slug>/', views.MarketDetailView.as_view(), name='detail'),
#     path('<slug:slug>/update/', views.MarketUpdateView.as_view(), name='update'),
#     path('<slug:slug>/delete/', views.MarketDeleteView.as_view(), name='delete'),
#     path('', views.MarketListView.as_view(), name='market_home'),
#     path('<str:username>/', views.MarketSellerListView.as_view(), name='market_user_post'),
#     path('search/', views.searchView, name='market_search'),
#     path('search_result/', views.searchResultView, name='market_search_result'),
#     path('market_category_vehicle/', views.marketCategoryVehicleView, name='market_category_vehicle'),
#     path('market_category_phone/', views.marketCategoryPhoneView, name='market_category_phone'),
#
#
#
#
# ]







