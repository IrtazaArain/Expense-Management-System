from django.contrib import admin
from .models import Expense, Budget

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'amount', 'category', 'date', 'created_at')
    list_filter = ('category', 'date')

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')  # Fields to display in the admin list view
    search_fields = ('user__username',)  # Enable search by username
    list_filter = ('user',)