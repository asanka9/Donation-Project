from django.shortcuts import render,redirect
from .models import Projects,Activity,News
from .forms import ProjectRegisterForm,CreditCardForm,ActivityForm
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.decorators import login_required
from .models import Activity as asa
def home(request):
    try:
        users = asa.objects.filter(projectname = Projects.objects.filter(completed = True).first().project_name)
    except:
        users = None
    context = {
        'posts': Projects.objects.filter(accepted = True , completed = False, success = False),
        'completed_post':Projects.objects.filter(completed = True).first(),
        'users' : users,
        'news' : News.objects.filter(accepted = True).first()
    }
    return render(request, 'web/home.html', context)


def about(request):
    return render(request, 'web/about.html', {'title': 'About'})

def create_post(request):
    if request.method == 'POST':
        form = ProjectRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            project_name = form.cleaned_data.get('project_name')
            messages.success(request, f'Post created for {project_name}!')
            return redirect('web-home')
    else:
        form = ProjectRegisterForm
    context = {
        'p_form': form
    }
    return render(request, 'web/create_post.html', context)


class Activity(View):
    def get(self,request,id,*args,**kwargs):
        if request.method == 'POST':
            form = CreditCardForm(request.POST)
            if form.is_valid():
                projectname = id
                username = name
                amount = form.cleaned_data.get('amount')
                user_image = User.objects.get(username=username).profile.image
                user_title = User.objects.get(username=username).profile.user_description
                project_image = Projects.objects.get(project_name=projectname).image
                project_desc = Projects.objects.get(project_name=projectname).decription

                my_activity = {
                    'username' : username,
                    'projectname' : projectname,
                    'amount' : amount,
                    'user_image' : user_image,
                    'user_title' : user_title,
                    'project_image' : project_image,
                    'project_desc' : project_desc
                }
                act_form = ActivityForm()
                if act_form.is_valid(): 
                    act_form.save()
                #amount = form.cleaned_data.get('amount')
                #messages.success(request, f'Post created for {project_name}!')
                return redirect('web-home')
        else:
            form = CreditCardForm
        context = {
            'p_form': form
        }
        return render(request, 'web/pay.html', context)
    def post(self,request,id,*args,**kwargs):
        print('**************************************************')
        if request.method == 'POST':
            form = CreditCardForm(request.POST)
            if form.is_valid():
                projectname = id
                username = request.user.username
                amount = form.cleaned_data.get('amount')
                user_image = User.objects.get(username=username).profile.image.url
                user_title = User.objects.get(username=username).profile.user_description
                if user_title is None:
                    user_title = '~~~~'
                project_image = Projects.objects.get(project_name=projectname).image.url
                project_desc = Projects.objects.get(project_name=projectname).decription

                my_activity = {
                    'username' : username,
                    'projectname' : projectname,
                    'amount' : amount,
                    'user_image' : user_image,
                    'user_title' : user_title,
                    'project_image' : project_image,
                    'project_desc' : project_desc
                }
                act_form = ActivityForm(my_activity)
                print(act_form)
                if act_form.is_valid(): 
                    print("HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
                    act_form.save()
                    project_name =projectname
                    balance = amount
                    project = Projects.objects.get(project_name= project_name)
                    project.current_balance = amount + project.current_balance
                    project.pecentage = (project.current_balance / project.expected)*100
                    if(project.current_balance>= project.expected):
                        project.success = True
                    project.save()
                    messages.success(request, f'You donation aded for {project_name}!')
                return redirect('web-home')
        else:
            form = CreditCardForm
        context = {
            'p_form': form
        }
        return render(request, 'web/pay.html', context)