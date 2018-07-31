from django.db import models
from django.utils.timezone import localdate

class Experience(models.Model):
    EXPERIENCE_TYPES = (
        ('e', 'Education'),
        ('w', 'Work'),
        ('l', 'Leadership'),
    )
    experience_type = models.CharField(
        max_length=1,
        choices=EXPERIENCE_TYPES)
    organization = models.CharField(max_length=75)
    organization_link = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
    caption = models.CharField(max_length=75)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def is_present(self):
        return (self.end_date - localdate()).days >= 0

    def get_experience_type_readable(self):
        for abbreviation, readable in self.EXPERIENCE_TYPES:
            if abbreviation == self.experience_type:
                return readable
        return ''

    def is_one_month(self):
        return (self.end_date.month == self.start_date.month) and (self.end_date.year == self.start_date.year)

    def __str__(self):
        return '{}: {}'.format(
            self.get_experience_type_readable(),
            self.organization
        )


class Project(models.Model):
    project_name = models.CharField(max_length=75)
    project_link = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=75)
    languages = models.CharField(max_length=75, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)

    def is_present(self):
        return (self.end_date - localdate()).days >= 0

    def is_one_month(self):
        return (self.end_date.month == self.start_date.month) and (self.end_date.year == self.start_date.year)

    def __str__(self):
        return 'Project: {}'.format(self.project_name)


class Skill(models.Model):
    SKILL_CATEGORIES = (
        ('co', 'Core'),
        ('wb', 'Web'),
        ('da', 'Data'),
        ('o', 'Other'),
    )
    LEVELS = [
        (1, '1 Basic'),
        (2, '2 Novice'),
        (3, '3 Intermediate'),
        (4, '4 Advanced'),
        (5, '5 Expert'),
    ]

    skill_category = models.CharField(
        max_length=2,
        choices=SKILL_CATEGORIES)
    skill_name = models.CharField(max_length=75)
    proficiency = models.IntegerField(choices=LEVELS)

    def get_skill_category_readable(self):
        for abbreviation, readable in self.SKILL_CATEGORIES:
            if abbreviation == self.skill_category:
                return readable
        return ''

    def __str__(self):
        return '{}: {}'.format(self.get_skill_category_readable(), self.skill_name)