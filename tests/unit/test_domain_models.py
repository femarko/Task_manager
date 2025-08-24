from src.domain.models import (
    TaskModel,
    create_task_model,
    TaskStatus
)


def test_create_task_model_returns_domain_task_model_instance():
    result = create_task_model(
        name="Test Task",
        description="Test Description",
        status=TaskStatus.CREATED,
    )
    assert isinstance(result, TaskModel), f"Expected: {TaskModel}, got: {type(result)}."
    assert result.name == "Test Task"
    assert result.description == "Test Description"
    assert result.status == TaskStatus.CREATED
