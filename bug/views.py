from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView
from .models import Bug
from .forms import BugRegistrationForm
from django.utils import timezone
from django.urls import reverse

# Home page for Capacity Exchange project
def home(request):
    return render(request, 'bug/home.html')


# Define a view for creating a new Bug
class BugCreateView(CreateView):

    # Operates on the Bug model
    model = Bug  

    # Use the BugRegistrationForm
    form_class = BugRegistrationForm 

    # Render this form template
    template_name = 'bug/bug_register.html'  

    def get_success_url(self):

        # Reverse is a Django utility for building URLs. It takes a URL pattern name
        # and any arguments needed to create the URL.
        # In this case, it generates the URL for the detail view of the 'Bug' model
        # using the URL pattern name 'bug:view_bug'. We pass the bug's ID as an argument
        # to ensure that the URL is unique for each bug.
        success_url = reverse('bug:view_bug', kwargs={"pk": self.object.pk})

        # Add this line for debugging
        #print("Success URL:", success_url)  
        return success_url

# Define a view for displaying Bug details
class BugDetailView(DetailView):

    # Operates on the Bug model
    model = Bug

    # Render this detail template
    template_name = 'bug/view_bug.html'  

# Define a view for listing all Bugs
class BugListView(ListView):

    # Operates on the Bug model
    model = Bug

    # Render this list template  
    template_name = 'bug/bug_list.html'  
    context_object_name = 'bug_list'