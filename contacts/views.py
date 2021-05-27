from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def contact(request):
     if request.method == 'POST':
       # Get Form values
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']
       user_id = request.POST['user_id']

       if request.user.is_authenticated:
         user_id = request.user.id
         has_contacted = Contact.objects.all().filter(user_id=user_id)
         if has_contacted:
           messages.error(request, 'You have already contacted this user.')


       contact = Contact(
       first_name = first_name,
       last_name =last_name,
       email = email,
       phone = phone,
       message = message,
       user_id = user_id )

       contact.save()

       messages.success(request, 'Your contact has been added!')

       return render(request, 'accounts/dashboard.html')
       
       #Check if passwords match
       
     else:
        return render(request, 'accounts/register.html')