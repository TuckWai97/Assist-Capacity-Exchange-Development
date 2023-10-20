from django.db import models
from datetime import date

# Create your models here.
class Bug(models.Model):
    description =models.TextField()

    # create a sqeuence for bug type consists f iterables of exactly two items
    # to use as choices for the field 'bug_type'.
    # (value, human_readable_name)
    # first element in each tuple is actual value to be set, for example 'error',
    # the second element is the human_readable name.
    BUG_TYPES = [
        ('error', "Error"),
        ('new_feature', "New Feature"),
        ('enhancement', "Enhancement"),
        ('security_vulnerability', "Security Vulnerability"),
        ('others', "Others"),

    ]

    # date.today from datetime.date.today()
    # get current date by using class method today()
    report_date = models.DateField(default=date.today)

    STATUS = [
        ('to_do', "To do"),
        ('in_progress', "In progress"),
        ('done', "Done"),
    ]

    #
    bug_type = models.CharField(
        max_length=25,
        choices=BUG_TYPES,
        default='error',
    )

    # add default_choice as todo since it requires admin to open the issue 
    status = models.CharField(
        max_length=15,
        choices=STATUS,
        default='to_do',
        )

    #__str__() method is added
    # Django will change the display name from object name to return a string that is same
    #as the display name of the model
    #display an object in the Django admin site and as the value inserted into a template when it displays an object. 
    def __str__(self):
        return self.description
