# Built-in dependencies
from typing import List, Union

# Local dependencies
from event_driven_backtester.event.event import Event


class EventQueue:

    def __init__(self) -> None:

        self.queue: List[Event] = []

        return

    def add_event(self, event: Event) -> None:

        self.queue.append(event)

        return

    def pop_event(self) -> Union[Event, None]:

        if self.queue:
            return self.queue.pop()

        return None
