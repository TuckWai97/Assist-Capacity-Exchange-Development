from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# Import message module from Django
from django.contrib import messages
from .models import Bug
from .forms import BugRegistrationForm

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

# function to register bug
def register_bug(request):
    if request.method == "POST":
        # Handle form submission and save the bug registration info
        form = BugRegistrationForm(request.POST)
        if form.is_valid():
            bug= form.save()
            # You can add a success message
            #messages.success(request,  'Bug is registered successfully!')
            # redirect back to bug detail page after successful registering a bug             
            return redirect('view_bug', bug.id)
    else:
        # If it is not POST request, display the registration form
        form = BugRegistrationForm()

    return render(request, 'bug_register.html', {'form': form})

# function with a list of fields of the bug
def view_bug(request, bug_id):
#bug = Bug.objects.get(id=bug_id)
    # Retrieve specific bug using its ID or handle 404 error if it does not exist
    #pk means as primary key as variable to store bug's ID
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'view_bug.html', {'bug':bug})

def list_bug(request):
    # Retrieve all bugs from the database
    bugs = Bug.objects.all()
    return render(request, 'bug_list.html', {'bugs':bugs})
