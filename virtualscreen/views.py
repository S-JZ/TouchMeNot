from django.shortcuts import redirect, render
from django.contrib import messages
from virtual_doodle.speech import initialize_project
from virtual_doodle import Virtual_Doodle, Navigation
from .models import Contact
from django.contrib import messages


def home(request):
    return render(request, 'virtualscreen/index2.html')

def v_assistant(request):
    command = initialize_project()
    phone = ''
    if command == None:
        command = ''
    elif command[0] == 'chk':
        command, phone = command[0], command[1]
    context = {'cmd': command, 'phone': phone}
    return render(request, 'virtualscreen/index2.html', context)


def about(request):
    return render(request, 'virtualscreen/about_us.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone-number']
        message = request.POST['message']
        if str(name) == '' or str(email) == '' or str(len(phone_number)) == 0 or str(message) == '':
            messages.warning(
                request, 'Please enter the details before submmiting.')
            return redirect('contact')
        elif len(name) > 50:
            messages.warning(request, 'Maximum 50 characters allowed of name.')
            return redirect('contact')
        elif len(phone_number) != 10 or not str(phone_number).isdigit():
            messages.warning(request, 'Phone number is wrong.')
            return redirect('contact')
        else:
            contact = Contact(name=name, email=email,
                              phone_number=phone_number, message=message)
            contact.save()
            messages.success(
                request, 'Your message has been successfully recorded. We will talk to you soon.')
            return redirect('/')
    return render(request, 'virtualscreen/contact.html')


def class_launch(request):
    Navigation.navigate()
    messages.success(request, 'Thank you for using our Classroom!🌟')
    return render(request, 'virtualscreen/classroom.html')


def classroom(request):
    if request.method == 'POST':
        url = request.POST['option']
        context = {'url': url}
        return render(request, 'virtualscreen/classroom.html', context)
    return render(request, 'virtualscreen/classroom.html')


def groceryplace(request):
    return render(request, 'virtualscreen/groceryplace.html') 


def checkout(request):
    if request.method == 'POST':
        url = request.POST['option']
        phone = request.POST['phone']
        context = {'url': url, 'phone': phone}
        return render(request, 'virtualscreen/gf.html', context)
    return render(request, 'virtualscreen/gf.html')


def checkout_launch(request):
    if request.method == 'POST':
        Navigation.navigate()
        phone = request.POST['phone']
        context = {'phone' : phone}
        return render(request, 'virtualscreen/gf.html', context)
    return render(request, 'virtualscreen/gf.html')

def gf_thanks(request):
    return render(request, 'virtualscreen/gf_tq.html')


def virtual_board(request):
    return render(request, 'virtualscreen/keyboard.html')


def vdoodle(request):
    if request.method == 'POST':
        url = request.POST['option']
        context = {'url': url}
        return render(request, 'virtualscreen/doodle.html', context)
    return render(request, 'virtualscreen/doodle.html')


def launch_vdl(request):
    Virtual_Doodle.v_doodle()
    messages.success(request, 'Thank you for using our Virtual Doodle!🌟')
    return render(request, 'virtualscreen/doodle.html')

def inst(request):
    return render(request, 'virtualscreen/instructions.html')