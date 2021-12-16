from django.test import TestCase
from base.models import Event
# Create your tests here.

class EventTestCase(TestCase):
    def setup(self):
        Event.objects.create(title="hello",
                             description="there")
        Event.objects.create(title="goodbye",
                             description="till tomorrow")

    def test_the_object_creations(self):
        hello=Event.objects.get(title="hello")
        goodbye=Event.objects.get(title="goodbye")
        self.assertEqual(hello.description, "there")
        self.assertEqual(goodbye.description,"till tomorrow")
