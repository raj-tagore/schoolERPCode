
from django.db import models
from attachments.models import Attachment
from users.models import User

# Create your models here.
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent_account')
    phone = models.CharField('Phone number', max_length=20, blank=True)
    whatsapp = models.CharField('WhatsApp number', max_length=20, blank=True)
    occupation = models.CharField('Occupation', max_length=400, blank=True)
    office_address = models.TextField(blank=True, null=True)
    annual_income = models.CharField('Annual Income', max_length=50, blank=True)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_account')
    identifier = models.BigIntegerField('ID')
    qualifications = models.TextField('Qualifications', blank=True)
    phone = models.CharField('Phone number', max_length=20, blank=True)
    whatsapp = models.CharField('WhatsApp number', max_length=20, blank=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_account')
    
    # Basic Fields
    student_no = models.CharField(max_length=50, unique=True)
    roll_no = models.CharField(max_length=50, blank=True, null=True)
    standard = models.CharField(max_length=50, blank=True, null=True)
    division = models.CharField(max_length=10, blank=True, null=True)

    address = models.TextField(blank=True, null=True)
    aadhar_card_no = models.CharField(max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=100, blank=True, null=True)
    birth_place = models.CharField(max_length=100, blank=True, null=True)
    mother_tongue = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    caste = models.CharField(max_length=100, blank=True, null=True)
    medical_info = models.TextField(blank=True, null=True)

    # Guardians
    guardian_1 = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name='student_guardian1')
    guardian_2 = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True, blank=True, related_name='student_guardian2')

    '''
    Current concept:
    We are not trying to eliminate paperwork completely, we are only trying to make processes easy.
    I assume schools will never eliminate physical records. 
    Hence we only ask for a minimal amount of data.
    Also we do not ask for any documents at present, we will generate them when required and print them.
    '''

    # Previous School Details
    # previous_school_student_id = models.CharField(max_length=50, blank=True, null=True)
    # prev_school_name = models.CharField(max_length=255, blank=True, null=True)
    # prev_school_address = models.TextField(blank=True, null=True)
    # prev_school_udise_no = models.CharField(max_length=100, blank=True, null=True)
    # prev_school_board = models.CharField(max_length=100, blank=True, null=True)

    # Attachments (OneToOne Fields)
    # address_proof = models.OneToOneField(
    #     Attachment,
    #     on_delete=models.SET_NULL,
    #     null=True, 
    #     blank=True,
    #     related_name='student_address_proof'
    # )
    # birth_certificate = models.OneToOneField(
    #     Attachment,
    #     on_delete=models.SET_NULL,
    #     null=True, 
    #     blank=True,
    #     related_name='student_birth_certificate'
    # )
    # identity_proof = models.OneToOneField(
    #     Attachment,
    #     on_delete=models.SET_NULL,
    #     null=True, 
    #     blank=True,
    #     related_name='student_identity_proof'
    # )
    # character_certificate = models.OneToOneField(
    #     Attachment,
    #     on_delete=models.SET_NULL,
    #     null=True, 
    #     blank=True,
    #     related_name='student_character_certificate'
    # )
    # id_card = models.OneToOneField(
    #     Attachment,
    #     on_delete=models.SET_NULL,
    #     null=True, 
    #     blank=True,
    #     related_name='student_id_card'
    # )
    # leaving_certificate = models.OneToOneField(
    #     Attachment,
    #     on_delete=models.SET_NULL,
    #     null=True, 
    #     blank=True,
    #     related_name='student_leaving_certificate'
    # )

    # # Attachments (ManyToMany Field for multiple files)
    # report_cards = models.ManyToManyField(
    #     Attachment,
    #     blank=True,
    #     related_name='student_report_cards'
    # )


    def __str__(self):
        return f"{self.student_no} - {self.standard} {self.division}"

