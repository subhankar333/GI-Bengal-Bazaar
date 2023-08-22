
from django.contrib import admin
from django.urls import path,include
from adminpanel import views

urlpatterns = [
    path('',views.index), 
    path('connect',views.connect),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.Logout),
    path('logoutpage',views.logoutpage),

    #manage users

    path('userinfo',views.userinfo),
    path('userinfo/search_first_name',views.user_info_search_first_name),
    path('userinfo/search_last_name',views.user_info_search_last_name),
    path('userinfo/search_mobile',views.user_info_search_mobile),
    path('userinfo/search_pin',views.user_info_search_pin),
    path('userinfo/search_city',views.user_info_search_city),
    path('userinfo/search_state',views.user_info_search_state),
    path('userinfo/adduser',views.adduser),
    path('userinfo/submit_data',views.submit_data),
    path('userinfo/delete/<str:mobile>',views.delete_user),
    path('userinfo/update/<str:mobile>',views.update_data),
    path('userinfo/submit_update_data',views.submit_update_data),

    # order section ---
    path('order',views.order),
    path('order/search_order_id',views.order_search_order_id),
    path('order/search_product_id',views.order_search_product_id),
    path('order/search_mobile',views.order_search_mobile),
    path('order/search_price',views.order_search_price),
    path('order/search_number_product',views.order_search_number_product),
    path('order/search_date',views.order_search_date),
    path('order/delete/<int:order_id>',views.delete_order),


    #manage product

    path('product',views.Product),   
    path('product/search_product_id',views.product_search_product_id),
    path('product/search_product_name',views.product_search_product_name),
    path('product/search_price',views.product_search_price),
    path('product/search_offer',views.product_search_offer),
    path('product/search_product_type',views.product_search_product_type),
    path('product/search_location',views.product_search_location),
    path('product/search_number_product',views.product_search_number_product),
    path('product/product_add',views.product_add),
    path('product/submit_product_data',views.submit_product_data),
    path('product/delete/<int:id>',views.product_delete),
    path('product/update/<int:id>',views.product_update),
    path('product/update_data/<int:id>',views.submit_update_data),

    # reviews section 

    path('managereviews',views.managereviews),
    path('managereviews/search_Reviews_id',views.managereviews_search_Reviews_id),
    path('managereviews/search_order_id',views.managereviews_search_order_id),
    path('managereviews/search_mobile',views.managereviews_search_mobile),
    path('managereviews/search_product_id',views.managereviews_search_product_id),
    path('managereviews/search_rating',views.managereviews_search_rating),
    path('managereviews/search_time_created',views.managereviews_search_time_created),
    path('managereviews/delete/<int:id>',views.managereviews_delete),

    # manage_cart

    path('manage_cart',views.manage_cart),
    path('manage_cart/search_mobile',views.manage_cart_search_mobile),
    path('manage_cart/search_product_id',views.manage_cart_search_product_id),
    path('manage_cart/search_number_product',views.manage_cart_search_number_product),
    path('manage_cart/delete/<str:mobile>',views.delete_bag),


    # iswishlist
    path('iswishlist',views.Iswishlist),
    path('iswishlist/search_love_id',views.iswishlist_search_love_id),
    path('iswishlist/search_mobile',views.iswishlist_search_mobile),
    path('iswishlist/search_product_id',views.iswishlist_search_product_id),
    path('iswishlist/delete/<int:loveid>',views.delete_wishlist),

    #manage_contact

    path('manage_contact',views.manage_contact),
    path('manage_contact/search_mobile',views.manage_contact_search_mobile),
    path('manage_contact/search_contact_id',views.manage_contact_search_contact_id),
    path('manage_contact/delete/<int:contact_id>',views.delete_contact),
    
    #manage_card

    path('manage_card',views.manage_card),
    path('manage_card/search_card_id',views.manage_card_search_card_id),
    path('manage_card/search_mobile',views.manage_card_search_mobile),
    path('manage_card/search_card_number',views.manage_card_search_card_number),
    path('manage_card/search_name',views.manage_card_search_name),
    path('manage_card/search_expiry',views.manage_card_search_expiry),
    path('manage_card/search_cvv',views.manage_card_search_cvv),
    path('manage_card/delete/<int:card_id>',views.card_delete),

    #manage_restaurent_user

    path('manage_restaurent_user',views.manage_restaurent_user),

]
