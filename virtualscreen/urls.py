from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('v-activate/', views.v_assistant, name='v_as'),
    path('Contact_Us/', views.contact, name='contact'),
    path('V_Doodle/', views.vdoodle, name='vdoodle'),
    path('V_Doodle/launch', views.launch_vdl, name='lvdl'),
    path('classroom/', views.classroom, name='classroom'),
    path('class-launch/', views.class_launch, name='cls'),
    path('instructions/', views.inst, name='instructions'),
    # path('grocery_tute/', views.groceryplace, name='groceryplace'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/launch', views.checkout_launch, name='chk'),
    path('key/', views.virtual_board, name='virtual-keyboard'),
    path('about/', views.about, name='about'),
    
]
