import unittest
from eventlite import EventService


class SmokeTests(unittest.TestCase):
    def test_create_valid_event(self):
        self.assertEqual(EventService().create("Talk", 10, "alice")["capacity"], 10)

    def test_register_one_attendee(self):
        self.assertEqual(EventService().register(1, "bob")["attendees"], ["bob"])

    def test_owner_can_cancel(self):
        self.assertEqual(EventService().cancel(1, "alice")["status"], "cancelled")
