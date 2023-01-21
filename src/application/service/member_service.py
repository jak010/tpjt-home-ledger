from src.application.models import Member


def member_create(email: str, password: str) -> Member:
    member = Member.objects.create(email=email, password=password)

    member.save()

    return member
