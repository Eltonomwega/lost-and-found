from django.shortcuts import render,redirect
from mainapp.models import Post
from django.http import HttpResponseRedirect
from .forms import Posts, ClaimForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import Claim,Post
from django.views.generic import ListView
from users.models import Stratizen
from .filters import PostFilter
# Create your views here.
def homepage(request):  
    return render(request, 'mainapp/home.html', {'title':'Home'})

@login_required(login_url='/login/')
def claimitem(request):
    return render(request, 'mainapp/claimitem.html', {'title':'Claim Item'})

@login_required(login_url='/login/')
def postitem(request):
    if request.method == 'POST':
        form = Posts(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'The item has been posted successfully')
            return redirect('posts_search')
    else:
        form = Posts()

    return render(request,'mainapp/postitem.html',{'form':form},{'title':'Post Item'})

@login_required(login_url='/login/')
def viewitems(request):
    return render(request, 'mainapp/viewitems.html', {'title':'View Item'})

@login_required(login_url='/login/')
def claimitem(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.method == 'POST':
        claim_form = ClaimForm(request.POST, request.FILES)
        claim_form.instance.claimed_by = request.user
        claim_form.instance.item_claimed = post
        if claim_form.is_valid():
            claim_form.save()
            messages.success(request, f'Claim Submitted Successfully!')
            return redirect('posts_search')
    else:
        claim_form = ClaimForm()
    
    context = {
        'claim_form': claim_form,
        'post': Post.objects.get(id=post_id),
        'title':'Claim Item'
    }

    return render(request, 'mainapp/claimitem.html', context)
    
class ClaimCreateView(CreateView):
    model = Claim
    fields = ['description','location','time_from','time_to','image']
    

class PostListView(ListView):
      context_object_name = 'posts'

      def get_queryset(self):
            return Post.objects.filter(claimed=False).order_by('-When')

def posts_search(request):
    posts = Post.objects.filter(claimed=False).order_by('-When')
    post_filter = PostFilter(request.GET, queryset=posts)
    return render(request, 'mainapp/posts_filter.html', {'filter':post_filter})


