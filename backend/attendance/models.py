from django.db import models

# Create your models here.

class Attendance(models.Model):
    date = models.DateField()
    absentees = models.ManyToManyField('accounts.Student', related_name='absences')
    subject = models.ForeignKey('allocation.Subject', on_delete=models.SET_NULL, null=True, related_name='attendances')
    classroom = models.ForeignKey('allocation.Classroom', on_delete=models.SET_NULL, null=True, related_name='attendances')
    
    def __str__(self):
        return f'{self.classroom} - {self.subject} - {self.date}'
