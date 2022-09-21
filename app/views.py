from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import destinaton
from .models import guide
from .models import hotel
from .models import info
from .models import pack
from django.contrib import messages
# Create your views here.


# index 

def index(request,name='NA'):
    main_destination=destinaton.objects.filter(c_id = 0)
    uslength = destinaton.objects.filter(c_id = 2)
    uslength=len(uslength)
    guide_details = guide.objects.filter(g_place = 0)
    return render(request,'index.html',{'name':name,'destination':main_destination,'guide_details':guide_details,'u_s':uslength})



# back to inidex
def backindex(request,name='NA'):
    main_destination=destinaton.objects.filter(c_id = 0)
    guide_details = guide.objects.filter(g_place = 0)
    uslength = destinaton.objects.filter(c_id = 2)
    uslength=len(uslength)
    return render(request,'index.html',{'name':name,'destination':main_destination,'guide_details':guide_details,'u_s':uslength})





# login 

def login(request):
    main_destination=destinaton.objects.filter(c_id = 0)
    guide_details = guide.objects.filter(g_place = 0)
    if request.method == 'POST':
        name=request.POST.get('name1')
        password=request.POST.get('password1')
        user_info_check = info.objects.filter(user_name = name)
        if len(user_info_check) > 0:
            pass
        else:
            messages.error(request,'Invalid username')
            return redirect('login')
        for password_check in user_info_check:
            if password_check.user_password == password:
                pass
            else:
                messages.error(request,'Invalid Password')
                return redirect('login')
        return render(request,'index.html',{'name':name,'destination':main_destination,'guide_details':guide_details})
    else:
        return render(request,'login.html')



# registration

def registration(request):
    main_destination=destinaton.objects.filter(c_id = 0)
    guide_details = guide.objects.filter(g_place = 0)
    if request.method == 'POST':
        name = request.POST.get('name1')
        number = request.POST.get('number1')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        number_length = len(number)
        # # phone number
        if number_length == 10:
            pass
        else:
            messages.error(request,'phone number')
            return redirect('register')
        # password
        if password1 == password2:
            pass
        else:
            messages.info(request,'password not corect')
            return redirect('register')
        if len(password1) > 4 :
            pass
        else:
            messages.info(request,'password length')
            return redirect('register')
        # user name
        def lower(username=''):
            lower = any(c.islower() for c in username)
            return lower
        def upper(username=''):
            upper = any(c.isupper() for c in username)
            return upper
        def digit(username=''):
            digit = any(c.isdigit() for c in username)
            return digit
        if len(name) > 6:
            pass
        else:
            messages.info(request,'user name length is short')
            return redirect('register')
        c_lower = lower(name)
        c_upper = upper(name)
        c_digit = digit(name)
        if c_lower and c_upper and c_digit :
            # save to database
            infoobj = info()
            infoobj.user_name = name
            infoobj.user_phone_no = number
            infoobj.user_password = password1
            infoobj.save()
            return render(request,'index.html',{'name':name,'destination':main_destination,'guide_details':guide_details})
        elif not c_digit:
            messages.info(request,'use one digit')
            return redirect('register')
        elif not c_lower:
            messages.info(request,' use lower case')
            return redirect('register')
        elif not c_upper:
            messages.info(request,' use upper case')
            return redirect('register')
    return render(request,'registration.html')


# about the site 
def about(request,name):
    guide_details = guide.objects.filter(g_place = 0)
    return render(request,'about-site.html',{'guide_details':guide_details,'name':name})




# account 

def account(request,name):
    if len(name) > 2:
        try:
            packinfo = pack.objects.get(u_name = name)
        except:
            return render(request,'packcomfirm.html',{'name':name})
        hotelinfo = hotel.objects.get(h_name = packinfo.u_h_name)
        guidinfo = guide.objects.get(g_name = packinfo.u_g_name)
        maindestination = destinaton.objects.get(d_name = packinfo.u_main_destination)
        subdestination = destinaton.objects.get(d_name = packinfo.u_sub_destination)
        return render(request,'account.html',{'name':name,'packinfo':packinfo,'hotelinfo':hotelinfo,'maindestination':maindestination,
        'subdestination':subdestination,'guidinfo':guidinfo})
    return redirect('login')





# all gallery

def gallery(request,id,name):
    sub_destination = destinaton.objects.filter(c_id=id)
    placename = destinaton.objects.get(id=id)
    return render(request,'gallery.html',{'destination':sub_destination,'id':id,'name':name,'placename':placename})



# adventure gallery

def adventure(request,id,name):
    placename = destinaton.objects.get(id=id)
    sub_destination = destinaton.objects.filter(c_id=id).filter(d_type='A')
    return render(request,'gallery.html',{'destination':sub_destination,'id':id,'name':name,'placename':placename})

    

# nature gallery

def nature(request,id,name):
    placename = destinaton.objects.get(id=id)
    sub_destination = destinaton.objects.filter(c_id=id).filter(d_type='N')
    return render(request,'gallery.html',{'destination':sub_destination,'id':id,'name':name,'placename':placename})


# historical place

def historical(request,id,name):
    placename = destinaton.objects.get(id=id)
    sub_destination = destinaton.objects.filter(c_id=id).filter(d_type='H')
    return render(request,'gallery.html',{'destination':sub_destination,'id':id,'name':name,'placename':placename})

    
# hotel and details


def hotelandaboutplace(request,destination_id,name,id):
    destination_type = destinaton.objects.get(id=destination_id)
    hotel_filter = hotel.objects.all().filter(h_place_type = destination_type.d_type)
    guide_filter = guide.objects.filter(g_place=id).get(g_type = destination_type.d_type)
    return render(request, 'hotelanddetails.html',{'hotel_filter':hotel_filter,'name':name,'guide_filter':guide_filter,'id':id,'destination_id':destination_id})



# check room availablity 

def check(request,name,hotelname,hotelprice,id,destination_id,g_name):
    if len(name) > 2:
        guideinfo = guide.objects.get(g_name = g_name)
        maindestinationinfo = destinaton.objects.get(id = id)
        subdestinationinfo = destinaton.objects.get(id = destination_id)
        userinfo = info.objects.get(user_name = name)
        hotelinfo = hotel.objects.get(h_name = hotelname)
        perday = 1000
        total_price = int(guideinfo.g_salary) + int(hotelprice) + perday
        if request.method == 'POST':
            packinfo = pack.objects.filter(u_name = name)
            if len(packinfo) == 0:
                packobj = pack()
                packobj.u_name = userinfo.user_name
                packobj.u_phone = userinfo.user_phone_no
                packobj.u_c_id = userinfo.id
                packobj.u_h_name = hotelinfo.h_name
                packobj.u_h_image = hotelinfo.h_image
                packobj.u_g_name = guideinfo.g_name
                packobj.u_main_destination = maindestinationinfo.d_name
                packobj.u_sub_destination = subdestinationinfo.d_name
                packobj.save()
            return render(request,'finaloutput.html',{'name':name})
        else:
            return render(request,'payment.html',{'name':name,'hotelname':hotelname,'hotelprice':hotelprice,'g_name':g_name,'total_price':total_price
        ,'perday':perday})
    else:
        return redirect('login')


#  payment  success message

def delete(request,name):
    pack.objects.get(u_name = name).delete()
    return redirect('backindex',name)




# password change

def password(request):
    main_destination=destinaton.objects.filter(c_id = 0)
    guide_details = guide.objects.filter(g_place = 0)
    if request.method == 'POST':
        name=request.POST.get('name1')
        number = request.POST.get('number1')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user_info_check = info.objects.filter(user_name = name)
        if len(user_info_check) > 0:
            pass
        else:
            messages.error(request,'Invalid username')
            return redirect('password')
        for n in user_info_check:
            if n.user_phone_no == int(number):
                # edit password here
                if password1 == password2:
                    pass
                else:
                    messages.info(request,'password not corect')
                    return redirect('password')
                if len(password1) > 4:
                    pass
                else:
                    messages.info(request,'password length is short')
                    return redirect('password')
                if len(password1) <= 10:
                    pass
                else:
                    messages.info(request,'password length is long')
                    return redirect('password')

                # update password

                info.objects.filter(user_name = name).update(user_password = password1)
                return render(request,'index.html',{'name':name,'destination':main_destination,'guide_details':guide_details})
                
            else:
                messages.error(request,'Invalid Phone number')
                return redirect('password')
    else:
        return render(request,'forgectpassword.html')



# 