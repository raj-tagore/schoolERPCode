from django.db import models

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    release_datetime = models.DateTimeField()
    due_datetime = models.DateTimeField()
    subject = models.ForeignKey('allocation.Subject', on_delete=models.SET_NULL, null=True, related_name='assignments')
    
    def __str__(self):
        return self.title
    
class StudentAssignment(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='assignments')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='students')
    status = models.CharField(max_length=50)
    submission_datetime = models.DateTimeField()
    