from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from rollpay.forms import *
from django.contrib.auth import authenticate, login, logout
from django.db.models import F
from rollpay import strings
from rollpay.models import *


def home(request):
	user=request.user
	return render_to_response('rollpay/home.html',{'user':user},context_instance=RequestContext(request),)
#------------------------------------account_edit---------------------------------------

def account_edit(request):
    form=UserProfileChange()
    if request.method=='POST':
        form=UserProfileChange(request.POST)
        if form.is_valid():
            form.save()
            form.messeges=u'your information has been updated'
    return render_to_response("accounts/profile_change.html",{'form':form},context_instance=RequestContext(request),)
#---------------------------------------------facebook_login------------------------------------




	 
#-------------------------------------registration--------------------------------------
def register(request):
	userform=UserProfileForm()
	if request.method=="POST":
		userform=UserProfileForm(request.POST)
		if userform.is_valid():
			userform.save()
			return HttpResponseRedirect("/")
	return render_to_response("accounts/register.html",{'userform':userform},context_instance=RequestContext(request),)

#-------------------------------------login----------------------------------------------

def login_view(request):
    username = request.POST["username"]
    password = request.POST["pass"]
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")
#-------------------------------------logout-----------------------------------------------
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
#---------------------------------------------User DashBoadrd------------------------------
def dashboard(request):
	return render_to_response("rollpay/dashboard.html",{'header':'header'},context_instance=RequestContext(request),)


#---------------------------------------myorder------------------------------------------

def myorders_view(request):
	orders=Order.objects.filter(user=request.user)
	return render_to_response("rollpay/myorders.html",{'orders':orders},context_instance=RequestContext(request),)


#------------------------------------------------order update view-----------------------
def order_update(request,number):
	order=Order.objects.get(number=number)
	form=TrackLinkForm()
	if request.method=="POST":
		form=TrackLinkForm(request.POST)
		if form.is_valid():
			url=form.cleaned_data['url']
			order.track_link=url
			order.save()
		else:
		    return HttpResponseRedirect('/invalid/')
			
	return render_to_response("rollpay/order_update.html",{'form':form,'order':order},context_instance=RequestContext(request),)

#-------------------------------affiliate sites view-----------------------------------------

def flipkart_redirect(request):
	merchant=Merchant.objects.get(name='Flipkart.com')
	total_order=Order.objects.count()
	order=Order.objects.create(number=total_order+1,merchant=merchant,user=request.user)
	order.save()
	param1=order.number
#-------profile=UserProfile.objects.filter(username=request.user.username)
	param2=Order.objects.filter(user=request.user).count()
	url=merchant.url
 	item_link=url+merchant.affiliate_id+'affExtParam1=%d&'%param1+'affExtParam2=%d'%param2
	order.item_link=item_link
	order.save()

	return HttpResponseRedirect(item_link)




