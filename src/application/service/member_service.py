from __future__ import annotations

from django.contrib.auth import get_user_model

from ..libs import utils

Member = get_user_model()


def create_member(email: str, password: str) -> Member:
    member = Member.objects.create(
        email=email,
        password=utils.generate_bcrypt_hash(password)
    )
    member.full_clean()

    return member
