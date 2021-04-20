from django.shortcuts import render, redirect
from .models import *
import random
# Create your views here.


def IndexPage(request):
    try:
        print(f"Main Id:{request.session['id']}")
    except:
        print("Id Doesn`t found")
    finally:
        return render(request, "app/index.html")


def RegisterPage(request):
    return render(request, "app/pages-register.html")


def LoginPage(request):
    return render(request, "app/pages-login.html")


def DashBoardPage(request):
    return render(request, "app/dashboard.html")


def DashBoardSettingPage(request, pk):
    getAdmin = Admin.objects.get(id=pk)
    if getAdmin.Role == "Artist":
        getUser = Artist.objects.get(Artist=getAdmin)
        print(
            f"For Update:Email={getUser.Artist.Email} | Role={getUser.Artist.Role}")
    elif getAdmin.Role == "Customer":
        getUser = Customer.objects.get(Customer=getAdmin)
        print(
            f"For Update:Email={getUser.Customer.Email} | Role={getUser.Customer.Role}")
    else:
        print("Role Not found")
    return render(request, "app/dashboard-settings.html", {'user': getUser})


def RegisterUser(request):
    role = request.POST['role']
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = int(request.POST['phone'])
    email = request.POST['email']
    passwd = request.POST['password']
    passwd_r = request.POST['password-repeat']
    gender = request.POST['gender']
    location = request.POST['loc']
    loc = location.capitalize()

    user = Admin.objects.filter(Email=email)
    print(user)
    if len(user) > 0:
        msg = f"{role} Already Exist"
        return render(request, "app/pages-register.html", {'msg': msg})
    else:
        validate_password = passwd == passwd_r
        if validate_password == False:
            msg = "Password doesn't match"
            print(msg)
            return render(request, "app/pages-register.html", {'msg': msg})
        else:
            Otp = random.randint(100000, 999999)
            admin = Admin.objects.create(
                Email=email, Password=passwd, Role=role, Otp=Otp)
            if role == 'Artist':
                artist = Artist.objects.create(
                    Artist=admin, Firstname=fname, Lastname=lname, PhoneNumber=phone, Gender=gender, Loc=loc)
            elif role == "Customer":
                customer = Customer.objects.create(
                    Customer=admin, Firstname=fname, Lastname=lname, PhoneNumber=phone, Gender=gender, Loc=loc)
            return redirect('login-page')


def LoginUser(request):
    if request.method == "POST":
        role = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']

        user = Admin.objects.filter(Email=email, Role=role)
        if len(user) > 0:
            if user[0].Password == password:
                if user[0].Role == "Artist":
                    art = Artist.objects.get(Artist=user[0])
                    request.session['id'] = user[0].id
                    request.session['role'] = user[0].Role
                    request.session['email'] = user[0].Email
                    request.session['firstname'] = art.Firstname
                    return redirect("/")
                else:
                    if user[0].Role == "Customer":
                        cus = Customer.objects.get(Customer=user[0])
                        request.session['id'] = user[0].id
                        request.session['role'] = user[0].Role
                        request.session['email'] = user[0].Email
                        request.session['firstname'] = cus.Firstname
                        return redirect("/")
            else:
                msg = "Password is invalid"
                return render(request, "app/pages-login.html", {'msg': msg})
        else:
            msg = f"{role} doesn't exist"
            return render(request, "app/pages-login.html", {'msg': msg})


def LogOut(request):
    del request.session['id']
    del request.session['role']
    del request.session['email']
    del request.session['firstname']
    return redirect("/")


def UpdateUser(request, pk):
    getAdmin = Admin.objects.get(id=pk)
    print(f"Get---------------->Admin for update:::::::::::::::{getAdmin}")
    if getAdmin.Role == 'Artist':
        getArtist = Artist.objects.get(Artist=getAdmin)
        getArtist.Firstname = request.POST['fname'] if request.POST['fname'] else getArtist.Firstname
        getArtist.Lastname = request.POST['lname'] if request.POST['lname'] else getArtist.Lastname
        getAdmin.Email = request.POST['email'] if request.POST['email'] else getAdmin.Email
        getAdmin.Password = request.POST['passwd'] if request.POST['passwd'] else getAdmin.Password
        try:
            getArtist.ProfilePic = request.FILES['img'] if request.FILES['img'] else getArtist.ProfilePic
        except Exception as error:
            print(f"Update Image Exception-------------->:{error}")
        finally:
            getArtist.PhoneNumber = request.POST['phone'] if request.POST['phone'] else getArtist.PhoneNumber
            getArtist.Designation = request.POST['Designation'] if request.POST['Designation'] else getArtist.Designation
            getArtist.Intro = request.POST['intro'] if request.POST['intro'] else getArtist.Intro
            getArtist.Loc = request.POST['location'] if request.POST['location'] else getArtist.Loc
            rate = float(request.POST['rate'] )
            getArtist.rate = rate
            getAdmin.save()
            getArtist.save()
            request.session['email'] = getAdmin.Email
            request.session['firstname'] = getArtist.Firstname

    else:
        if getAdmin.Role == 'Customer':
            getCustomer = Customer.objects.get(Customer=getAdmin)
            getCustomer.Firstname = request.POST['fname'] if request.POST['fname'] else getCustomer.Firstname
            getCustomer.Lastname = request.POST['lname'] if request.POST['lname'] else getCustomer.Lastname
            getAdmin.Email = request.POST['email'] if request.POST['email'] else getAdmin.Email
            getAdmin.Password = request.POST['passwd'] if request.POST['passwd'] else getAdmin.Password
            try:
                getCustomer.ProfilePic = request.FILES['img'] if request.FILES['img'] else getCustomer.ProfilePic
            except Exception as error:
                print(f"Update Image Exception-------------->:{error}")
            finally:
                getCustomer.PhoneNumber = request.POST['phone'] if request.POST['phone'] else getCustomer.PhoneNumber
                getCustomer.Loc = request.POST['location'] if request.POST['location'] else getCustomer.Loc
                getAdmin.save()
                getCustomer.save()
                request.session['email'] = getAdmin.Email
                request.session['firstname'] = getCustomer.Firstname

    url = f"/dashboard-setting/{pk}/"
    return redirect(url)

def AllArtistPage(request):
    getAllArtist = Artist.objects.all()
    return render(request, "app/all-artist.html",{'allart':getAllArtist})

def ArtistProfile(request,pk):
    getArtProfile = Artist.objects.get(id=pk)
    return render(request, "app/single-freelancer-profile.html",{'artpro':getArtProfile})

def BookArtistPage(request,pk):
    getArtist = Artist.objects.get(id=pk)
    return render(request, "app/book_artist.html",{'artist':getArtist})

def BookArtist(request,pk):
    des = request.POST['des']
    GetAdminCust = Admin.objects.get(id=request.session['id'])
    getCustomer = Customer.objects.get(Customer=GetAdminCust)
    getArtist = Artist.objects.get(id=pk)
    CreateArtReq = BookArtistReq.objects.create(Cust=getCustomer,Artist=getArtist,Des=des)
    url = f"/book-artist/{pk}"
    return redirect(url) 

def MyWorkReq(request):
    getAdmminArtist = Admin.objects.get(id=request.session['id'])
    getArtist = Artist.objects.get(Artist=getAdmminArtist)
    getreq = BookArtistReq.objects.all().filter(Artist=getArtist,Status="Status")
    return render(request, "app/dashboard-manage-jobs.html",{'req':getreq})