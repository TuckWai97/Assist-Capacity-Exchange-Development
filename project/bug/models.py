from django.db import models
# import date function from datetime module
from datetime import date
from django.utils import timezone
# Create your models here.
class Bug(models.Model):
    # description of the Bug
    description =models.TextField()

    # create a sequence(or list) for bug type consists f iterables of exactly two items
    # to use as choices for the field 'bug_type'.
    # (value, human_readable_name)
    # first element in each tuple is actual value to be set, for example 'error',
    # the second element is the human_readable name, which user will see on the website.
    BUG_TYPES = [
        ('error', "Error"),
        ('new_feature', "New Feature"),
        ('enhancement', "Enhancement"),
        ('security_vulnerability', "Security Vulnerability"),
        ('others', "Others"),

    ]

    # `DateField` class return a date represented in Python, stores in `report_date`
    # get the current date when the bug model is created with `date.today` if this field is not expclicitly provided.
    # created a `formatted_date` method to format the date, this is optional
    report_date = models.DateField('date reported',default=date.today)

    # status with choices
    STATUS = [
        ('to_do', "To do"),
        ('in_progress', "In progress"),
        ('done', "Done"),
        ('Won\'t Fix', 'Won\'t Fix'),
        ('Duplicate', 'Duplicate'),
        ('Invalid', 'Invalid'),

    ]

    # add default value as 'error', if value is not explicitly specified when create Bug.
    bug_type = models.CharField(
        max_length=25,
        choices=BUG_TYPES,
        default='error',
    )

    # add default value as 'todo' since it requires admin to open the issue 
    status = models.CharField(
        max_length=15,
        choices=STATUS,
        default='to_do',
        )

    #__str__() method is added
    #Return human- readable string representation of the Bug model. 
    # if there is not this method, it will return object representation by default
    def __str__(self):
        return self.description
    
    # Get date in format "YYYY-MM-DD" from `strftime` Python method
    # You can use this function to format the date in case you would like to
    #def formatted_date(self):
    #    return self.report_date.strftime("%Y-%m-%d")
    # Optional code to check the report_date if it is within the last day
    def was_reported_recently(self):
        return self.report_date >= timezone.now() - timezone.timedelta(days=1)
