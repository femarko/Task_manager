import uuid

from enum import Enum
from dataclasses import dataclass


class TaskStatus(str, Enum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


@dataclass
class TaskModel:
    id: uuid
    name: str
    description: str
    status: TaskStatus


def create_task_model(
        name: str,
        description: str,
        status: TaskStatus,
        id: uuid = None,
) -> TaskModel:
    return TaskModel(
        id=id,
        name=name,
        description=description,
        status=status
    )