from django.shortcuts import render,HttpResponse,redirect
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . EmailBackend import EmailBackEnd
# Create your views here.
def blogindex(request):
    allblogs = Blogs.objects.all()
    return render(request,'blogindex.html')

def blogregister(request):
    if request.method == 'POST':
        usernames = request.POST['usernames']
        email = request.POST['emails']
        passwords = request.POST['passwords']
        print(usernames, passwords)
        User.objects.create_user(username=usernames, password=passwords,email=email)
        return redirect('blogindex')
    else:
        return render(request, 'blogregister.html')

def bloglogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = EmailBackEnd.authenticate(request, username=email,
                                         password=password)
        login(request,user)
        return redirect('blogindex')
    else:
        return render(request,'bloglogin.html')
def editprofile(request):
    return render(request,'editprofile.html')
def commentonblog(request,id):

    blogname = Blogs.objects.get(id=id)
    if request.method == 'POST':
        comments = request.POST['comment']
        commentsave = comment(
            blogname = blogname,
            commentatorname = request.user,
            commentonblog = comments,
        )
        commentsave.save()
        return HttpResponse("comments is done")
    else:
        return render(request,'comments.html',{'id':id})
def createblog(request):
    ids = request.user
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        blog = Blogs(
            blodid = ids,
            title = title,
            description = description
        )
        blog.save()
        return redirect('blogindex')
    else:
        return render(request,'createblog.html')

def blogdelete(request,id):
    blog_delete = Blogs.objects.get(id=id)
    blog_delete.delete()
        # return HttpResponseRedirect(reverse('index'))
    return HttpResponse('blog deleted')
def totalviews(request,id):
    totalseen = Blogs.objects.get(id=id)
    totalseen.no_of_views = totalseen.no_of_views+1
    totalseen.save()
    return HttpResponse('total number of views saved')
def readblog(request,id):
    blogread = Blogs.objects.get(id=id)
    totalseen = Blogs.objects.get(id=id)
    totalseen.no_of_views = totalseen.no_of_views + 1
    totalseen.save()
    return render(request,'readblog.html',{'blogread':blogread,'id':id})
def bloglogout(request):
    logout(request)
    return redirect('blogindex')
def blogupdate(request,id):
    updateblog = Blogs.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST['title']
        print(title)
        description = request.POST['description']
        print(description)
        updateblog.title = title
        updateblog.description = description
        updateblog.save()
        return redirect('blogindex')
    else:
        return render(request,'blogupdate.html',{'id':id,'updateblog':updateblog})

