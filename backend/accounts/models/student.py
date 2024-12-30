from typing import final

from django.db import models

from accounts.models import Account
from allocation.models.parent import Parent


@final
class Student(models.Model):
    IDENTITY_PROOF_CHOICES = [
        (
            "adhaar",
            "Adhaar Card",
        ),
        (
            "pan",
            "PAN Card",
        ),
        (
            "voter",
            "Voter ID",
        ),
        (
            "passport",
            "Passport",
        ),
        (
            "driving",
            "Driving License",
        ),
    ]

    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, related_name="student_info", null=False
    )


    classroom = models.ForeignKey(
        "allocation.Classroom",
        on_delete=models.SET_NULL,
        related_name="students",
        null=True,
    )

    guardian1 = models.ForeignKey(
        Parent,
        on_delete=models.SET_NULL,
        null=True,
        related_name="students_guardian1",
    )

    guardian2 = models.ForeignKey(
        Parent,
        on_delete=models.SET_NULL,
        null=True,
        related_name="students_guardian2",
    )

    address_proof = models.FileField(
        "Address Proof", upload_to="student_address_proofs", blank=False
    )

    birth_certificate = models.FileField(
        "Birth Certificate", upload_to="student_birth_certificates", blank=False
    )

    identity_proof_type = models.CharField(
        "Identity Proof Type",
        max_length=10,
        choices=IDENTITY_PROOF_CHOICES,
        blank=False,
    )

    identity_proof_number = models.CharField(
        "Identity Proof Number", max_length=50, blank=False
    )

    identity_proof = models.FileField(
        "Identity Proof", upload_to="student_identity_proofs", blank=False
    )

    character_certificate = models.FileField(
        "Character Certificate", upload_to="student_character_certificates", blank=False
    )

    id_card = models.FileField("ID Card", upload_to="student_id_cards", blank=False)

    leaving_certificate = models.FileField(
        "Leaving Certificate", upload_to="student_leaving_certificates"
    )

    def __str__(self):
        return self.account.username
