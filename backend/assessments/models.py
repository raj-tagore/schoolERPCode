from django.db import models

# Create your models here.

class Assessment(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    syllabus = models.TextField()
    datetime = models.DateTimeField()
    venue = models.CharField(max_length=50)
    subject = models.ForeignKey('allocation.Subject', on_delete=models.SET_NULL, null=True, related_name='assessments')
    max_marks = models.IntegerField()
    passing_marks = models.IntegerField()
    
    
    def __str__(self):
        return self.title
    
class StudentAssessment(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='assessments')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='students')
    marks = models.IntegerField()
    
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.student.user.username + ' - ' + self.assessment.title