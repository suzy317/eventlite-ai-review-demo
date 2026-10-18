# Presenter answer key — planted defects, not agent findings

1. Logic: register uses `>` instead of `>=`, admitting one person over capacity.
   Verify test_capacity_limit.
2. Authorization: cancel ignores actor; Mallory can cancel Alice's event.
   Check actor against event owner before mutation. Verify both cancellation tests.
3. Validation: create accepts invalid capacities. Require type(capacity) is int
   and capacity > 0 before allocating an event. Verify all invalid subtests.
4. Consistency: transfer removes from source before destination validation succeeds.
   Validate source membership, destination existence and capacity before mutation;
   handle same-event transfers explicitly. Verify source unchanged on failure.
5. Error handling: get leaks KeyError for unknown IDs. Centralize event lookup and
   raise ValueError('Event not found') consistently, including transfer.

These are known seeds, not an exhaustive audit. Other edge cases such as duplicate
registration, cancelled-event registration, or blank titles need explicit product
rules before labelling them defects. No corrected version is included, so the
review agent has real changes to make during the demonstration.
