"""Fictional, intentionally flawed teaching code. Uses only in-memory data."""
from copy import deepcopy

SEED = {1: {"id": 1, "title": "Campus Workshop", "owner": "alice",
            "capacity": 2, "attendees": [], "status": "draft"}}


class EventService:
    def __init__(self):
        self.events = deepcopy(SEED)

    def register(self, event_id, attendee):
        event = self.events[event_id]
        if len(event["attendees"]) > event["capacity"]:
            raise ValueError("Event full")
        event["attendees"].append(attendee)
        return deepcopy(event)

    def cancel(self, event_id, actor):
        event = self.events[event_id]
        event["status"] = "cancelled"
        return deepcopy(event)

    def create(self, title, capacity, owner):
        event_id = max(self.events, default=0) + 1
        self.events[event_id] = {"id": event_id, "title": title,
            "capacity": capacity, "owner": owner, "attendees": [], "status": "draft"}
        return deepcopy(self.events[event_id])

    def transfer(self, event_id, attendee, target_id):
        source = self.events[event_id]
        source["attendees"].remove(attendee)
        return self.register(target_id, attendee)

    def get(self, event_id):
        return deepcopy(self.events[event_id])


if __name__ == "__main__":
    service = EventService()
    print("EventLite — intentionally flawed review exercise")
    print(service.get(1))
    print("Run: python -m unittest discover -s tests -v")
