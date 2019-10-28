from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import Claim, Post
from django.views.generic import ListView
from .filters import ClaimFilter, PostFilter

# Create your views here.

class ClaimListView(ListView):
    context_object_name = 'claims'
    template_name='adminapp/claim_list.html'

    def get_queryset(self):
        return Claim.objects.filter(accepted=None).order_by('-date_claimed')

    def post(self, request):
        claim_id = request.POST.get('claim_id')
        status = request.POST.get('status')

        claim = Claim.objects.get(id=claim_id)

        if (status == 'accept'):
            claim.accepted = True
            claim.item_claimed.claimed = True
            claim.item_claimed.save()
            claim.save()
            messages.success(request, f'Claim Accepted Successfully!')
            return redirect('claims_search')
        else:
            claim.accepted = False
            claim.item_claimed.claimed = False
            claim.item_claimed.save()
            claim.save()
            messages.warning(request, f'Claim Rejected')
            return redirect('claims_search')
            
def claim_search(request):
    claims = Claim.objects.filter(accepted=None).order_by('-date_claimed')
    claim_filter = ClaimFilter(request.GET, queryset=claims)
    return render(request, 'adminapp/claims_filter.html', {'filter':claim_filter})    

def adminposts_search(request):
    posts = Post.objects.order_by('-When')
    post_filter = PostFilter(request.GET, queryset=posts)
    return render(request, 'adminapp/adminposts_filter.html', {'filter':post_filter})  


    
                
