"""Simple task and ticket management examples."""

import json
from dataclasses import asdict, dataclass
from typing import Any, Dict


class TaskFileError(Exception):
    """Raised when task data cannot be saved or loaded."""


class TicketError(Exception):
    """Raised when ticket data is invalid."""


class Task:
    """Represent a task that can be stored as JSON."""

    def __init__(self, task_id: int, title: str, completed: bool = False) -> None:
        """Create a task with an identifier, title, and completion state."""
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self) -> Dict[str, Any]:
        """Return the task as a dictionary suitable for JSON encoding."""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "completed": self.completed,
        }

    def save(self, file_path: str) -> None:
        """Save this task to a JSON file."""
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(self.to_dict(), file, indent=2)
        except (OSError, TypeError, ValueError) as error:
            raise TaskFileError(
                f"Unable to save task to {file_path!r}: {error}"
            ) from error

    @classmethod
    def load(cls, file_path: str) -> "Task":
        """Load a task from a JSON file."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (OSError, json.JSONDecodeError) as error:
            raise TaskFileError(
                f"Unable to load task from {file_path!r}: {error}"
            ) from error

        if not isinstance(data, dict):
            raise TaskFileError("Task JSON must contain an object.")

        try:
            task_id = data["task_id"]
            title = data["title"]
            completed = data["completed"]
        except KeyError as error:
            raise TaskFileError("Task JSON contains invalid task data.") from error

        # Check exact JSON field types before constructing the Task.
        if (
            isinstance(task_id, bool)
            or not isinstance(task_id, int)
            or not isinstance(title, str)
            or not title.strip()
            or not isinstance(completed, bool)
        ):
            raise TaskFileError("Task JSON contains invalid task data.")

        # The values are validated, so no implicit type conversion is needed.
        return cls(task_id=task_id, title=title, completed=completed)


@dataclass
class Ticket:
    """Represent a ticket that can be validated before use."""

    ticket_id: int
    title: str
    is_open: bool


def validate_ticket(ticket: Ticket) -> None:
    """Validate a ticket identifier and title."""
    if not isinstance(ticket.ticket_id, int) or ticket.ticket_id <= 0:
        raise TicketError("ticket_id must be a positive integer.")
    if not isinstance(ticket.title, str) or not ticket.title.strip():
        raise TicketError("title must be a non-empty string.")


def main() -> None:
    """Run a working example of task persistence and ticket validation."""
    file_path = "example_task.json"

    # Create and persist a task, then load it back from disk.
    task = Task(task_id=1, title="Complete the Python exercise")
    task.save(file_path)
    loaded_task = Task.load(file_path)
    print(f"Loaded task: {loaded_task.to_dict()}")

    # Validate a ticket and report the successful result.
    ticket = Ticket(ticket_id=101, title="Example support ticket", is_open=True)
    validate_ticket(ticket)
    print(f"Validated ticket: {asdict(ticket)}")


if __name__ == "__main__":
    main()
