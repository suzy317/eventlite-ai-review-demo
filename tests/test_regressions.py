import unittest
from eventlite import EventService


class RegressionTests(unittest.TestCase):
    def setUp(self):
        self.service = EventService()

    def test_capacity_limit(self):
        self.service.register(1, "bob")
        self.service.register(1, "carol")
        with self.assertRaises(ValueError):
            self.service.register(1, "dave")

    def test_only_owner_can_cancel(self):
        with self.assertRaises(PermissionError):
            self.service.cancel(1, "mallory")
        self.assertEqual(self.service.get(1)["status"], "draft")

    def test_capacity_must_be_positive_integer(self):
        for invalid in [0, -1, 1.5, True, "ten"]:
            with self.subTest(capacity=invalid):
                with self.assertRaises(ValueError):
                    self.service.create("Talk", invalid, "alice")

    def test_failed_transfer_preserves_source(self):
        self.service.register(1, "bob")
        with self.assertRaises(ValueError):
            self.service.transfer(1, "bob", 999)
        self.assertIn("bob", self.service.get(1)["attendees"])

    def test_missing_event_has_domain_error(self):
        with self.assertRaisesRegex(ValueError, "Event not found"):
            self.service.get(999)
