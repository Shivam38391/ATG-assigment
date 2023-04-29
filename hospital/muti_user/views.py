from django.shortcuts import redirect, render
from .forms import CustomUserForm , BlogPostForm
from .models import CustomUser , BlogPost
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        # print(request.POST)
        form = CustomUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            """ there are two method
            1.crete the user using  the form and
            create a new user using create_user method
            
            """
            
            user_name = form.cleaned_data['username'] # to get the password
        
            password = form.cleaned_data['password'] # to get the password
            user = form.save(commit=False)
            user.set_password(password) # to implement hashing in password
            user.save()
            messages.success(request,f"{user_name} your account has been succesfully register")
            return redirect('home')
    
    else:
        form = CustomUserForm()
    
    context = {
        'form': form,
    }
    
    return render(request, "muti_user/register.html", context)




@login_required
def dashboard(request):
    current_user = request.user
    allposts = BlogPost.objects.filter(is_draft=False)
    
    user_post = BlogPost.objects.filter(author=current_user)
    alldoc = CustomUser.objects.filter(role=1).all()
    
    context ={
        "allpost" : allposts,
        "user_post" : user_post,
        "alldoc": alldoc,
    }
    return render(request, "muti_user/dashboard.html", context)



###############createPost #########################

@login_required
def createpost(request):
    
    c= request.user
    
    if request.user.is_authenticated and request.user.role == 1:
        c= request.user
        d= request.user.username
        # print(f"user  {c} and username  {d}")
        
        form = BlogPostForm()
        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                messages.success(request,f"{c} your post is successfully been posted")
                return redirect('muti_user:dashboard')
        # else:
        #     form = BlogPostForm()
        return render(request, 'muti_user/createpost.html', {'form': form})
    else:
        messages.success(request,f"{c} your are login as Patient only Doctor's are allowed to create BlogPost, first logout and login as Doctor")
        return redirect('muti_user:login')

