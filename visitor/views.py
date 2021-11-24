from django.shortcuts import render, redirect
from django.contrib import messages
from visitor.forms import UserRegistrationForm, UserEditForm, UserProfileForm
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import re


from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives




emailChecker = ''       # EMAIL CHECKING VARIABLE





# Create your views here.


# ABOUT
def about(request):

    context = {'page_has_Menu': True}

    return render (request, 'visitor/about.html', context)





# CONTACT
def contact(request):

    context = {'page_has_Menu': True}

    return render (request, 'visitor/contact.html', context)





# REGISTER
def freeshop_register(request):
    form = UserRegistrationForm()

    context = {'form': form, 'pageTitle': 'REGISTER', 'page_has_Menu': True}


    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        verify_email = request.POST['verify_email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        # EMAIL CHECKER (REGEX TO VERIFY EMAIL ADDRESS)
        emailChecker = re.fullmatch('([a-z]{1})([a-zA-Z0-9]+)(([_\-]{1}[a-zA-Z0-9]+)?)([@]{1})([a-z]+)'
                           '([\.]{1})([a-z]{2,3})(([\.]{1}[a-z]{2})?)',email)


        context = {'form': form, 'pageTitle': 'REGISTER', 'page_has_Menu': True}



        if emailChecker:        # REGEX TO VERIFY EMAIL ADDRESS
            if (email == verify_email) or (password1 == password2):
                if email == verify_email:
                    if password1 == password2:
                        if User.objects.filter(username=username).exists():     # CHECK IF USERNAME EXISTS IN THE MODEL "User"
                            messages.info(request, 'Username Taken! Please Use Another Username')
                            return render(request, 'visitor/register.html', {'form': form})
                        elif User.objects.filter(email=email).exists():          # CHECK IF EMAIL EXISTS IN THE MODEL "User"
                            messages.info(request, 'Email Taken! Please Use Another Email')
                            return render(request, 'visitor/register.html', {'form': form})
                        else:
                            # CREATE A NEW USER IF BOTH USERNAME AND EMAIL DO NOT EXIST IN THE MODEL "User"
                            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
                            user.save()     # SAVE THE NEW USER INTO THE MODEL
                            messages.success(request, f'Dear {first_name}, your username is {username}!')

                            # ------------------------------------------
                            # sending advanced mails in HTML format
                            # ------------------------------------------
                            subject, from_email, to = 'SUCCESSFUL REGISTRATION MAIL', 'admin@freeshop.com', email
                            text_content = f'Dear {first_name}, you have been successfully logged out.'
                            html_content = f'Dear <span style="color:blue; font-weight:bold;">{first_name}</span>, <br>You have been successfully registered with the following:<br><br>username: <strong>{username}</strong><br>password: <strong>{password1}</strong><br><br>Kind regards,'
                            email = EmailMultiAlternatives(subject, text_content, from_email, [to])
                            email.attach_alternative(html_content, "text/html")
                            email.send(fail_silently=False)
                            # ------------------------------------------

                            return redirect('freeshop_login')

                    else:
                        messages.info(request, 'Password do not match')
                        return render(request, 'visitor/register.html', context)

                else:
                    messages.info(request, 'Email Address do not match')
                    return render(request, 'visitor/register.html', context)

            else:
                messages.info(request, 'Email Address and Password do not match')
                return render(request, 'visitor/register.html', context)
        else:
            messages.error(request, 'Invalid Email Entered!')
            return render(request, 'visitor/register.html', context)

    return render(request, 'visitor/register.html', context)









# LOGIN
def freeshop_login(request):

    context = {'page_has_Menu': True}

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        # FIND OUT THE AUTHENTICITY OF BOTH THE USERNAME AND PASSWORD IN THE MODEL
        user = authenticate(username=username, password=password)

        if user:                        # IF USER IS AUTHENTICATED I.E. EXISTS
            if user.is_active:          # IF USER IS ACTIVE
                login(request, user)    # LOGIN THE USER
                messages.success(request, f'Dear {user.first_name}, you are now logged in!')
                return redirect('home')
            else:
                messages.error(request, f'{user.first_name} No Longer Active!')
                return redirect('home')
        else:
            messages.warning(request, 'Unsuccessful Login!')
            return redirect('freeshop_login')

    return render(request, 'visitor/login.html', context)






#---------------------------------------------------------------------------------------------------------------------
# LOGIN_TO_CONTINUE VIEW 
#---------------------------------------------------------------------------------------------------------------------

def freeshop_login_to_continue(request):

# POST method
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']            # get "next" from request.POST       

        # THIS AUTHENTICATES THE USER DETAILS
        visitor = authenticate(request, username=username, password=password)       

        if visitor:
            if visitor.is_active:               # THIS CHECKS IF USER IS STILL ACTIVE
                login(request, visitor)

                if next:                                # IF "next" EXISTS IN "request.POST"
                    messages.success(request, 'You are being redirected to the requested page!')
                    return redirect(next)               # RETURN THE VALUE OF "next" 

                else:
                    pass

            else:
                messages.error(request, 'Your account is no longer active on this site, contact site administrator')
                return redirect('freeshop_register')

        else:
            messages.error(request, 'You are not a registered member of this site, please register and try again')
            return redirect('freeshop_register')


    # GET method
    else:
        context = {'page_has_Menu': True}
        return render(request, 'visitor/login_to_continue.html', context)








# LOGOUT
@login_required
def freeshop_logout(request):
    currentUser = request.user.first_name      # ASSIGNING THE CURRENT LOGGED IN USER TO "currentUser" VARIABLE
    currentUserEmail = request.user.email

    logout(request)
    messages.success(request, f'Dear {currentUser}, You Have Been Successfully Logged Out!')


    # ------------------------------------------
    # sending simple mails
    # ------------------------------------------
    send_mail(
        'MY LOGOUT MAIL',                                                   # subject
        f'Dear {currentUser}, you have been successfully logged out.',      # message
        'owner@freeshop.com',                                               # from
        [currentUserEmail],                                                 # recipient
        fail_silently=False,
        )
    # # ------------------------------------------

    return redirect('freeshop_login')




# # --------------------------------------------SENDING MAILS ------------------------------------------

    # # ------------------------------------------
    # # sending advanced mails without attachment
    # # ------------------------------------------
    # email = EmailMessage(
    #     'Hello',                                                              # subject
    #     f'Dear {currentUser}, you have been successfully logged out.',        # message
    #     'ownerbig@freeshop.com',                                              # from
    #     [currentUserEmail, 'to2@example.com'],                                # recipients
    #     ['bcc@example.com'],                                                  # bcc
    # reply_to=['myowner@example.com'],                  
    # headers={'Message-ID': 'foo'},
    # )

    # # sending the mail
    # email.send(fail_silently=False)
    # # ------------------------------------------

    # return redirect('freeshop_login')




    # # ------------------------------------------
    # # sending advanced mails with attachment
    # # ------------------------------------------
    # email = EmailMessage(
    #     'Subject, LOGOUT successful',                                       # subject
    #     f'Dear {currentUser}, you have been successfully logged out.',      # message
    #     'ownerbig@freeshop.com',                                            # from
    #     [currentUserEmail, 'to2@example.com'],                              # recipients
    #     ['bcc@example.com'],                                                # bcc
    # reply_to=['myowner@example.com'],
    # headers={'Message-ID': 'foo'},
    # )

    # # attaching file to the mail
    # from pathlib import Path
    # photo = Path('C:\\Users\\GBENGA\\Pictures\\IBADAN.jpg')
    # email.attach_file(photo)

    # # sending the mail
    # email.send(fail_silently=False)
    # # ------------------------------------------

    # return redirect('freeshop_login')





    # # ------------------------------------------
    # # sending advanced mails in HTML format
    # # ------------------------------------------
    # subject, from_email, to = 'Subject, LOGOUT successful', 'admin@freeshop.com', currentUserEmail
    # text_content = f'Dear {currentUser}, you have been successfully logged out.'
    # html_content = f'Dear <span style="color:green; font-weight:bold;">{currentUser}</span>, <br>You have been successfully logged out.<br>Kind regards,'
    # # html_content = '<div style="background-color:yellow; height:200px; font-size:20px; padding:10px 5px 10px 5px;">Dear User, your logout from Freeshop was successful. Thanks for visiting, we hope to see you back here soon.<br><br>Kind regards,<br>Gbenga Ogunkuade<br>CEO Freeshop</div>'

    # email = EmailMultiAlternatives(subject, text_content, from_email, [to])
    # email.attach_alternative(html_content, "text/html")

    # # attaching file to the mail
    # from pathlib import Path
    # photo = Path('C:\\Users\\GBENGA\\Pictures\\IBADAN.jpg')
    # email.attach_file(photo)

    # # sending the mail
    # email.send(fail_silently=False)
    # # ------------------------------------------

    # return redirect('freeshop_login')


# # --------------------------------------------------------------------------------------------------------------




# PROFILE AND PROFILE UPDATE
@login_required         # USERS MUST BE LOGGED IN BEFORE THEY CAN ACCESS THEIR PROFILE PAGE
def freeshop_profile(request):
    u_form = UserEditForm(instance=request.user)
    p_form = UserProfileForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'page_has_Menu': True
    }


    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            currentUser = request.user.first_name
            messages.success(request, f'Dear {currentUser}, your account profile has been updated!')
            return redirect('freeshop_profile')


    return render(request, 'visitor/profile.html', context)










# PASSWORD CHANGE
@login_required
def freeshop_password_change(request):

    form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was updated successfully!')
            return redirect('freeshop_login')
        else:
            messages.warning(request, 'Please correct the error below.')


    return render(request, 'visitor/password_change.html', {'form': form})


