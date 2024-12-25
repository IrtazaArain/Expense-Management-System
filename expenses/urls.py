from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('expenses/', views.expense_list, name='expense-list'),
    path('add/', views.add_expense, name='add-expense'),
    #path('expenses/edit/<int:pk>/', views.edit_expense, name='edit-expense'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete-expense'),
    path('budget/add/', views.add_or_update_budget, name='add_budget'),
]

