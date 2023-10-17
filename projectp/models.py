from django.db import models

class Project(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="The name of the project."
    )
    creation_time = models.DateTimeField(
        auto_now_add=True,
        help_text="Projects start time."
    )
    completion_time = models.DateTimeField(
        null=True,
        help_text="Projects end time"
    )

    def __str__(self):
        return self.name

class Task(models.Model):
    class Status(models.TextChoices):
        NOT_START = "NOT_START", 'Not start'
        IN_WORKING = "IN_WORKING", "In working"
        DONE = "DONE", "Done"

    name = models.CharField(
        max_length=20,
        help_text="The name of the task."
    )
    description = models.TextField(
        help_text="The description of task."
    )
    complete_status = models.CharField(
        max_length=20,
        default=Status.NOT_START,
        choices=Status.choices,
        help_text="Task completion status."
    )
    creation_time = models.DateTimeField(
        auto_now_add=True,
        help_text="Time when task was created."
    )
    planned_end_task = models.DateTimeField(
        help_text="Planned end time of task."
    )
    end_time = models.DateTimeField(
        null=True,
        help_text="Time of the end of task"
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
