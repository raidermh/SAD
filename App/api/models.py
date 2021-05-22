from django.db import models
from django.contrib.auth.models import User


# Misiks models classes


class MisiksUser(User):
    patronymic_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.patronymic_name, self.last_name)


class ProjectState(models.TextChoices):
    NEW = 'new'
    IN_PROGRESS = 'inProgress'
    DONE = 'done'
    CANCELLED = 'cancelled'


class Project(models.Model):
    name = models.CharField(max_length=300)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    author = models.ForeignKey(MisiksUser, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=1000)
    state = models.CharField(default=ProjectState.NEW, choices=ProjectState.choices, max_length=10)

    def __str__(self):
        return self.name


class Role(models.Model):
    user = models.ForeignKey(MisiksUser, related_name='roles', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='users', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        self.title


class Specification(models.Model):
    name = models.CharField(max_length=300)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Release(models.Model):
    date = models.DateField(auto_now_add=True)
    approver = models.ForeignKey(MisiksUser, on_delete=models.SET_NULL, null=True)
    specification = models.OneToOneField(Specification, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s, согласовал %s" % (self.date, self.specification, self.approver)


class RequirementType(models.TextChoices):
    BUSINESS = 'Бизнес'
    FUNCTIONAL = 'Функциональные'


class RequirementStatus(models.TextChoices):
    NEW = 'new'
    IN_PROGRESS = 'inProgress'
    CORRECTION = 'correction'
    DONE = 'done'
    AT_APPROVAL = 'atApproval'
    APPROVED = 'approved'


class Requirement(models.Model):
    name = models.CharField(max_length=500)
    project = models.ForeignKey(Project, related_name='requirements', on_delete=models.CASCADE)
    type = models.CharField(choices=RequirementType.choices, max_length=14)
    description = models.CharField(max_length=5000)
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
    author = models.ForeignKey(MisiksUser, on_delete=models.SET_NULL, null=True)
    status = models.CharField(default=RequirementStatus.NEW, choices=RequirementStatus.choices, max_length=10)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True)
    release = models.ForeignKey(Release, related_name='requirements', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s %s" % (self.project, self.name)