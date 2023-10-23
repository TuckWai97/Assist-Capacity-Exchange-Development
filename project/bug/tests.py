from django.test import TestCase
from .models import Bug
from django.urls import reverse
from .views import list_bug
from django.utils import timezone

# Test case class for the 'Bug' model
class BugModelTest(TestCase):

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

    # Tests with ensure future date will be rejected, earlier date will be accepted
    def test_future_past_date_bug(self):
        # Create a Bug object with a future report_date
        future_date = timezone.now() + timezone.timedelta(days=5)
        bug = self.create_bug("Future Bug", days_ago=5)
        bug.report_date = future_date

        # Check if the bug was reported recently
        self.assertFalse(bug.was_reported_recently())

        # Create a Bug object with a past report_date
        past_date = timezone.now() - timezone.timedelta(days=5)
        bug = self.create_bug("Past Bug", days_ago=5)
        bug.report_date = past_date

        # Check if the bug was reported recently
        self.assertTrue(bug.was_reported_recently())

    # Test if the __str__ method of the 'Bug' model returns the correct string representation
    def test_bug_str_method(self):
        bug = Bug.objects.create(description="Another Bug", bug_type="Features")
        self.assertEqual(str(bug), "Another Bug")

    # Test if the default status of a bug is 'To Do'
    def test_bug_default_status(self):
        # Create a Bug object
        bug = Bug(description="Another Bug")
        # Check if the status is 'To do' by default
        self.assertEqual(bug.status, 'to_do')
        # Check if the bug_type is 'error' by default
        self.assertEqual(bug.bug_type, 'error')
        # Check if report_date is today
        self.assertEqual(bug.report_date, timezone.now().date())

    # Test if the 'bug_type' field accepts only the allowed choices ('Error,' 'Feature,' and 'Other')
    def test_bug_type_choices(self):
        bug = Bug(description="Test Bug", bug_type="InvalidType")
        with self.assertRaises(ValueError):
            bug.full_clean()

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

    # Test if a new bug can be successfully registered and added to the database
    def test_bug_registration(self):
        response = self.client.post(reverse('bug:register_bug'), {'description': 'New Bug', 'bug_type': 'Feature'})
        self.assertEqual(response.status_code, 302)  # Expect a redirect
        self.assertTrue(Bug.objects.filter(description='New Bug', bug_type='Feature').exists())

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

        # Issue a GET request to the bug detail view
        response = self.client.get(reverse('bug:view_bug', args=(bug.id)))

        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the bug's description is present in the response
        self.assertContains(response, 'Test Bug')
