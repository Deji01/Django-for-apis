from django.urls import path
from .views import (
    CategoriesView,
    MenuItemsView,
    SingleMenuItemView,
    CartView,
    OrderView,
    SingleOrderView,
    GroupViewSet,
    DeleiveryCrewViewSet
)

urlspatterns = [
    path("categories", CategoriesView.as_view()),
    path("menu-items", MenuItemsView.as_view()),
    path("menu-items/<int:pk>", SingleMenuItemView.as_view()),
    path("cart/menu-items", CartView.as_view()),
    path("orders", OrderView.as_view()),
    path("orders/<int:pk>", SingleOrderView.as_view()),
    path("groups/manager/users", GroupViewSet.as_view({
        "get": "list",
        "post": "create",
        "delete": "destroy"
    })),
    path("groups/delivery-crew/users", DeleiveryCrewViewSet.as_view({
        "get": "list",
        "post": "create",
        "delete": "destroy"
    }))
]