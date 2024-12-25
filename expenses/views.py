from django.shortcuts import render, redirect
from .forms import ExpenseForm, BudgetForm
from .models import Expense, Budget
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.db.models import Sum

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    
    # Get the user's budget
    budget = Budget.objects.filter(user=request.user).first()
    
    # Calculate total expenses for the user
    total_expenses = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Calculate remaining budget
    remaining_budget = budget.amount - total_expenses if budget else None
    
    # Determine if the user has exceeded their budget
    budget_exceeded = total_expenses > budget.amount if budget else False

    return render(
        request,
        'expenses/expense_list.html',
        {
            'expenses': expenses,
            'budget': budget,
            'remaining_budget': remaining_budget,
            'budget_exceeded': budget_exceeded,
        },
    )

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expenses:expense-list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)  # Ensure the expense belongs to the logged-in user
    if request.method == 'POST':
        expense.delete()
        return redirect('expenses:expense-list')
    return render(request, 'expenses/delete_expense.html', {'expense': expense})

@login_required
def add_or_update_budget(request):
    budget = Budget.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('expenses:expense-list')
    else:
        form = BudgetForm(instance=budget)

    return render(request, 'expenses/add_budget.html', {'form': form})