from typing import final

from django.db import models

from accounts.models import Account
from allocation.models.qualification import Qualification


@final
class Teacher(models.Model):
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
        Account, on_delete=models.CASCADE, related_name="teacher", null=False
    )

    qualifications = models.ManyToManyField(
        Qualification, related_name="teachers", blank=True
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

    identity_proof_image = models.FileField(
        "Identity Proof Image", upload_to="teacher_identity_proofs", blank=False
    )

    tet_certification = models.FileField(
        "TET Certification", upload_to="teacher_tet_certifications", blank=False
    )

    character_certificate = models.FileField(
        "Character Certificate", upload_to="teacher_character_certificates", blank=False
    )

    id_card = models.FileField("ID Card", upload_to="teacher_id_cards", blank=False)

    def __str__(self):
        return self.account.username
