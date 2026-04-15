from django.shortcuts import render,redirect,get_object_or_404
from .models import Postjob
from .models import Adminregister
from .models import Userdetailsreview
from .models import Application
from django.contrib.auth.models import User
# Create your views here.






def companies(request):
    return render(request, 'companies.html')




def logout(request):
     request.session.flush()
     return redirect('login') 


from .models import Register

def register_page(request):
    if request.method == "POST":
        username=request.POST.get("username")
        FullName=request.POST.get("FullName")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
        mobileNo=request.POST.get("mobileNo")

        if password == confirmpassword:
            
            Register.objects.create(
                username=username,
                FullName=FullName,
                email=email,
                password=password,
                mobileNo=mobileNo
            )

            return redirect("login")
        else:
            return render(request,"register.html",{'msg':"password does not exist"})
        
    return render(request,"register.html")

def login_page(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = Register.objects.filter(username=username).first()

        if user and user.password == password:
            request.session['user_id'] = user.id
            request.session['username'] = user.FullName
            

            return redirect('home')   

        else:
            return render(request, "login.html", {"msg": "Invalid login"})

    return render(request, 'login.html')

def postjob(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        job_type = request.POST.get('job_type')
        description = request.POST.get('description')

        Postjob.objects.create(
            title=title,
            company=company,
            location=location,
            salary=salary,
            job_type=job_type,
            description=description,
            is_active=True 
        )

        return redirect('postjob')  

    jobs = Postjob.objects.all()
    return render(request, 'postjob.html', {'jobs': jobs})

 


   

def home(request):
    jobs = None   
    title = None
    location = None
    job_type = None

    username = request.session.get('username', 'Guest')

    details = Userdetails.objects.filter(first_name = request.session.get('username')).first()

    if request.method == "POST":
        title = request.POST.get('title')
        location = request.POST.get('location')
        job_type = request.POST.get('job_type')

        jobs = Postjob.objects.all() 
       
        if title:
            jobs = jobs.filter(title__icontains=title)

        if location:
            jobs = jobs.filter(location__icontains=location)

        if job_type:
            jobs = jobs.filter(job_type=job_type)

   

    return render(request, 'home.html', {
        'username': username,
        'jobs': jobs,
        "details":details

    })
def adminlogin_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        user = Adminregister.objects.filter(email=email, password=password).first()

        if user:
           request.session['user_id'] = user.id
           request.session['name']=user.name
           
           

           return redirect('adminhome')
         
        else:
             return render(request, "adminlogin.html", {"msg": "invalid login"})
        
    return render(request,'adminlogin.html')
           
    
  
   

def adminregister_page(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword = request.POST.get("confirmpassword")
      

        if password == confirmpassword:
            
          Adminregister.objects.create(
                name=name,
                email=email,
                password=password,
                
            )

        return redirect("adminlogin")
        
    return render(request,"Adminregister.html")

def admin_home(request):
    total_users = User.objects.count()
    total_jobs = Postjob.objects.count()
    total_applications = Application.objects.count()
    selected = Application.objects.filter(status="Selected").count()

    recent_jobs = Postjob.objects.order_by('-id')[:5]
    recent_users = User.objects.order_by('-id')[:5]
    recent_applications = Application.objects.select_related('job').order_by('-id')[:5]

    context = {
        'total_users': total_users,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'selected': selected,

        'recent_jobs': recent_jobs,
        'recent_users': recent_users,
        'recent_applications': recent_applications,
    }

    return render(request, 'adminhome.html', context)
    
    
   

from .models import Userdetails

def userdetails_page(request):

    if request.method == "POST":

        user_id = request.session.get('user_id')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        position = request.POST.get('position')
        company = request.POST.get('company')
        designation= request.POST.get('designation')
        experience = request.POST.get('experience')
        state = request.POST.get('state')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        portfolio = request.POST.get('portfolio')
        resume = request.FILES.get('resume') 


        Userdetails.objects.create(
            first_name=first_name,
            last_name=last_name,
            position=position,
            company=company,
            designation = designation,
            experience=experience,
            state=state,
            city=city,
            phone=phone,
            email=email,
            address=address,
            dob=dob,
            portfolio=portfolio,
            resume=resume
        )

        return redirect('userdetailsreview')  

    return render(request, 'userdetails.html')    



#  Review Page
# def userdetails_review(request):
#     user_id = request.session.get('user_id') 

#     if not user_id:
#         return redirect('login')
    
#     user=Register.objects.get(id=user_id)


#     users=Userdetails.objects.all()

#     return render(request, 'userdetailsreview.html', {
#         'users': users,})

# #  Update Page

# def update_userdetails(request, id):

#     details = Userdetails.objects.get(id=id)

#     if request.method == "POST":
#         details.first_name = request.POST.get('first_name')
#         details.last_name = request.POST.get('last_name')
#         details.position = request.POST.get('position')
#         details.company = request.POST.get('company')
#         details.designation = request.POST.get('designation')
#         details.experience = request.POST.get('experience')
#         details.state = request.POST.get('state')
#         details.city = request.POST.get('city')
#         details.phone = request.POST.get('phone')
#         details.email = request.POST.get('email')
#         details.address = request.POST.get('address')
#         details.dob = request.POST.get('dob')
#         details.portfolio = request.POST.get('portfolio')

#         if request.FILES.get('resume'):
#             details.resume = request.FILES.get('resume')


#         details.save()


#         return redirect('userdetails')
    
    
#     return render(request, 'updateuserdetails.html', {'details': details})
    
#    Delete

# def delete_userdetails(request, id):

#     details = Userdetails.objects.filter(id=id).first()

#     if not details:
#      return redirect('userdetailsreview')

#     if request.method == 'POST':
#          details.delete()
#          return redirect('userdetailsreview')
   

#     return render(request,'deleteuserdetails.html',{'details':details})


def apply_job(request, job_id):
    job = Postjob.objects.get(id=job_id)


    # if Application.objects.filter(user=request.user, job=job).exists():
    #     return redirect('appliedjobs')

    if request.method == "POST":
        
  
        Application.objects.create(
            job=job,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            experience=request.POST.get('experience'),
            resume=request.FILES.get('resume')
        )

        
        return redirect('appliedjobs')

    return render(request, 'apply.html', {'job': job})

def applicants(request,job_id):
    apps = Application.objects.filter(job_id=job_id)
    applications = Application.objects.all()

    return render(request, 'applicants.html', {
        'applications': applications,
        'applications':apps
    })

def browsejob_page(request):
    jobs=Postjob.objects.all()
    user = request.user 

    if request.method == "POST":
        title = request.POST.get('title')
        location = request.POST.get('location')
        
        jobs = Postjob.objects.all()

        if title:
            jobs =jobs.filter(title__icontains=title)

        if location:
            jobs =jobs.filter(location__icontains=location)

    return render(request, 'browsejob.html', {'jobs': jobs,'user':user})

def profile_review(request):
    user_id = request.session.get('user_id') 

    if not user_id:
        return redirect('login')
    
    users=Profile.objects.filter(user_id=user_id) 


    return render(request, 'profile.html', {
        'users': users,
        })

#  Update Page
def userdetails_update(request,id):

    profile = Profile.objects.filter(id=id).first()

    if not profile:
     return redirect('profile')

    if request.method == "POST":
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.position = request.POST.get('position')
        profile.company = request.POST.get('company')
        profile.designation = request.POST.get('designation')
        profile.experience = request.POST.get('experience')
        profile.state = request.POST.get('state')
        profile.city = request.POST.get('city')
        profile.phone = request.POST.get('phone')
        profile.email = request.POST.get('email')
        profile.address = request.POST.get('address')
        profile.dob = request.POST.get('dob')
        profile.portfolio = request.POST.get('portfolio')

        if request.FILES.get('resume'):
            profile.resume = request.FILES.get('resume')

        profile.save()

        return redirect('profile')

    return render(request, 'userdetailsupdate.html', {'details': profile})

#  Delete

def userdetails_delete(request,id):

   profile = Profile.objects.filter(id=id).first()

   if not profile:
    return redirect('profile')

   if request.method == 'POST':
        profile.delete()
        return redirect('profile')
   

   return redirect('profile')

from .models import Profile

def Profile_page(request):

    user_id = request.session.get('user_id')

    if not user_id:
        return redirect('login')
    

    user = get_object_or_404(Register, id=user_id)

    if request.method == "POST":


        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        position = request.POST.get('position')
        company = request.POST.get('company')
        designation= request.POST.get('designation')
        experience = request.POST.get('experience')
        state = request.POST.get('state')
        city = request.POST.get('city')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        dob = request.POST.get('dob')
        portfolio = request.POST.get('portfolio')
        resume = request.FILES.get('resume') 


        Profile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            position=position,
            company=company,
            designation = designation,
            experience=experience,
            state=state,
            city=city,
            phone=phone,
            email=email,
            address=address,
            dob=dob,
            portfolio=portfolio,
            resume=resume
        )

        return redirect('profile')  

    return render(request, 'pro.html')  



def update_status(request, id):
    app = Application.objects.get(id=id)

    if request.method == "POST":
        status = request.POST.get('status')
        app = Application.objects.get(id=id)
        app.status = status
        app.save()


    return redirect('applicants', app.job.id) 



def applied_jobs(request):
    applications = Application.objects.all()
    return render(request, 'appliedjobs.html', {'applications': applications})

def delete_application(request, id):
    app = Application.objects.get(id=id)
    app.delete()
    return redirect('appliedjobs')

def update_application_status(request, id, status):
    app = Application.objects.get(id=id)
    app.status = status
    app.save()
    return redirect('appliedjobs')

from django.db.models import Q

def admin_dashboard(request):
    query = request.GET.get('q')
    job_type = request.GET.get('type')

    jobs = Postjob.objects.all()


    if query:
        jobs = Postjob.objects.filter(
            Q(title__icontains=query) |
            Q(company__icontains=query)
        )

    # FILTER
    if job_type and job_type != "All":
        jobs = Postjob.objects.filter(job_type=job_type)

    total_users = User.objects.count()
    total_jobs = Postjob.objects.count()
    total_applications = Application.objects.count()
    selected = Application.objects.filter(status="Selected").count()
    
    recent_users = User.objects.order_by('-id')[:5]
    recent_jobs = Postjob.objects.order_by('-id')[:5]
    recent_applications = Application.objects.select_related('job', 'user').order_by('-id')[:5]


    context = {
        "jobs":jobs,
        'total_users':5,
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'selected': selected,
        'recent_users':recent_users,
        'recent_jobs':recent_jobs,
        'recent_applications':recent_applications,
    }

    return render(request, 'admindashboard.html', context)

def jobupdate(request, id):
    job = get_object_or_404(Postjob, id=id)
 
    if request.method == "POST":
        job.title = request.POST.get('title')
        job.company = request.POST.get('company')
        job.location = request.POST.get('location')
        job.salary = request.POST.get('salary')
        job.description = request.POST.get('description')
        job.save()
        return redirect('admindashboard')
 
    return render(request, 'jobupdate.html', {'job': job})

def delete_job(request, id):
    if request.method == "POST":
        job = get_object_or_404(Postjob, id=id)
        job.delete()
    return redirect('admindashboard')

def close_job(request, job_id):
    job = get_object_or_404(Postjob, id=job_id)
    job.is_active =False
    job.save()
    return redirect('Postjob')