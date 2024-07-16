from django.urls import path
from .views import BranchListView, VisitCreateView

urlpatterns = [
    path('branches/', BranchListView.as_view(), name='points_of_sale_list'),
    path('visits/', VisitCreateView.as_view(), name='create_visit'),
]
