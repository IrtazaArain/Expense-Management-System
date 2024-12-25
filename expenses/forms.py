from django import forms
from .models import Expense, Budget

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'title': 'Expense Title',
            'amount': 'Amount Spent',
            'category': 'Expense Category',
            'date': 'Date of Expense',
        }

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount']
        labels = {
            'amount': 'Budget Amount',
        }