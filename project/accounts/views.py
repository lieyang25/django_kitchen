from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm, LoginForm, FoodForm, EntryForm

from django.shortcuts import render
from .models import Pizza, Entry

#新的
@login_required
def page(request):
    """披萨店主页"""
    return render(request,'page.html')
@login_required
def pizzas(request):
    pizzas = Pizza.objects.order_by('time_added')
    context = {'pizzas':pizzas}
    return render(request,'pizzas.html',context)
@login_required
def pizza(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    entries = pizza.entry_set.order_by('-date_added')
    context = {'pizza':pizza,'entries':entries}
    return render(request,'pizza.html',context)
#旧的
def index(request):
    return render(request,'index.html')
# 用户注册视图
def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '注册成功！')
            return render(request,'index.html')  # 重定向到主页
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

# 用户登录视图
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            #从经过验证的数据中获取用户名。
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #使用authenticate函数验证用户凭据（用户名和密码）。如果用户名和密码正确，返回用户对象user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'欢迎回来, {username}!')
                return render(request,'page.html')  # 重定向到主页
            else:
                messages.error(request, '用户名或密码不正确')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# 用户登出视图
def logout_view(request):
    logout(request)
    messages.success(request, '您已成功登出！')
    return render(request,'index.html')  # 重定向到主页
#添加话题
@login_required
def new_food(request):
    if request.method != 'POST':
        form = FoodForm()
    else:
        form = FoodForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:pizzas')
    #传递数据
    context = {'form':form}
    return render(request,'new_food.html',context)
#添加条目
@login_required
def new_entry(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = pizza
            new_entry.save()
            return redirect('accounts:pizza',pizza_id = pizza_id)

    context = {'pizza':pizza,'form':form}
    return render(request,'new_entry.html',context)
#编辑条目
@login_required
def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:pizza',pizza_id=topic.id)

    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'edit_entry.html',context)
