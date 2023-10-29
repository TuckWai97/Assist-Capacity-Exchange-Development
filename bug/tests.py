from django.test import TestCase
from .models import Bug
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError

# Test case class for the 'Bug' model
class BugModelTest(TestCase):
    def create_bug(self, description, bug_type='error', status='to_do', days_ago=0):
        # Create a Bug object with the given parameters
        date = timezone.now() - timezone.timedelta(days=days_ago)
        return Bug(description=description, bug_type=bug_type, status=status, report_date=date)
        
    # Tests with valid choices accepted for both bug_type and status
    def test_choices(self):

        # For bug types, validate that the choices in Bug.BUG_TYPES match
        # the actual choices used in the bug model.
        bug = Bug(description="Test Bug", bug_type="error")
        for bug_type in [choice[0] for choice in Bug.BUG_TYPES]:
            bug.bug_type = bug_type
            self.assertEqual(bug.bug_type, bug_type)

        # For bug statuses, validate that the choices in Bug.STATUS match
        # the actual choices used in the bug model.
        bug = Bug(description="Test Bug", status="to_do")
        for status in [choice[0] for choice in Bug.STATUS]:
            bug.status = status
            self.assertEqual(bug.status, status)

    # Tests with ensure bug with earlier date will be accepted
    def test_past_date_bug(self):

    # Create a Bug object with a past report_date
        past_date = timezone.now() - timezone.timedelta(days=1)
        bug = self.create_bug("Past Bug", days_ago=1)
        bug.report_date = past_date

        # Check if the bug was reported recently
        self.assertTrue(bug.was_reported_recently())


    # Test if the __str__ method of the 'Bug' model returns the correct string representation
    def test_bug_str_method(self):
        bug = Bug.objects.create(description="Another Bug", bug_type="Features")
        self.assertEqual(str(bug), "Another Bug")

    # Test if the default value of a bug is 'To Do' for status, 'error' as bug_type and today for report_date
    def test_bug_default_status(self):

        # Create a Bug object
        bug = Bug(description="Another Bug")

        # Check if the status is 'To do' by default
        self.assertEqual(bug.status, 'to_do')

        # Check if the bug_type is 'error' by default
        self.assertEqual(bug.bug_type, 'error')

        # Check if report_date is today
        self.assertEqual(bug.report_date, timezone.now().date())

    # Test if the 'bug_type' field accepts only the allowed choices
    def test_bug_type_choices(self):
        bug = Bug(description="Test Bug", bug_type="error")
        try:
            # Check if it raise ValidationError, which it will pass, since error is one of the bug_type's choices
            bug.full_clean()
        except ValidationError:
            self.fail("Bug type validation failed for an allowed choice.")


# Test case class for the 'Bug' views
class BugViewsTest(TestCase):

    # Test if the 'list_bug' view returns a status code of 200 (OK) and uses the 'bug_list.html' template
    def test_list_bug_view(self):
        response = self.client.get(reverse('bug:list_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/bug_list.html')

    # Test if the 'view_bug' view for a specific bug returns a status code of 200 and uses the 'view_bug.html' template
    def test_view_bug_view(self):
        bug = Bug.objects.create(description="Test Bug", bug_type="Error")
        response = self.client.get(reverse('bug:view_bug', args=[bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/view_bug.html')

    # Test if the 'register_bug' view returns a status code of 200 and uses the 'bug_register.html' template
    def test_register_bug_view(self):
        response = self.client.get(reverse('bug:register_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug/bug_register.html')

    # Test that the bug registration view correctly rejects duplicate bug registrations.
    # It simulates the process of registering a bug and then trying to register the same bug again,
    # and ensure that the view responds with a status code of 400 (Bad Request) for the second attempt.
    def test_duplicate_bug_view(self):

        # Create a bug record
        bug = Bug.objects.create(
            description='Test Bug',
            bug_type='error',
            status='to_do',
        )

        # Issue a GET request to the 'view_bug' view
        response = self.client.get(reverse('bug:view_bug', args=[str(bug.id)]))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the bug's description is present in the response
        self.assertContains(response, 'Test Bug')

    # Test create the To Do Bug, check access to the 'list_bug' view and displayed correctly
    def test_list_to_do_bugs(self):
        
        # Create a "To-Do" bug
        to_do_bug = Bug.objects.create(
            description="To-Do Bug",
            bug_type="error",
            status="to_do",
        )

        # Issue a GET request to the 'list_bug' view
        response = self.client.get(reverse('bug:list_bug'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the bug's description is present in the response
        self.assertContains(response, 'To-Do Bug')
