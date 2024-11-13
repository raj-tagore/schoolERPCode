from django.db import models

# Create your models here.

class Attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name='attendances')
    subject = models.ForeignKey('allocation.Subject', on_delete=models.SET_NULL, null=True, related_name='attendances')
    classroom = models.ForeignKey('allocation.Classroom', on_delete=models.SET_NULL, null=True, related_name='attendances')
    record = models.CharField(max_length=50, choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Late'), ('E', 'Excused')])
    
    def __str__(self):
        return f'{self.student} - {self.date}'