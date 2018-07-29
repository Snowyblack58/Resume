from django.db import models
from django.utils.timezone import localdate

class Experience(models.Model):
    EXPERIENCE_TYPES = (
        ('e', 'Education'),
        ('w', 'Work'),
        ('l', 'Leadership')
    )
    experience_type = models.CharField(
        max_length=1,
        choices=EXPERIENCE_TYPES)
    organization = models.CharField(max_length=75)
    organization_link = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
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

    def __str__(self):
        return '{}: {}'.format(
            self.get_experience_type_readable(),
            self.organization
        )