from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Experience

# Create your views here.
class IndexView(View):
    def tokenize_description(self, text):
        return [s.strip() for s in text.split('\n') if s.strip()]

    def get_experiences(self):
        experiences = Experience.objects.order_by('experience_type')
        experience_objects = []
        for experience in experiences:
            experience_objects.append({
                'type': experience.get_experience_type_readable(),
                'organization': experience.organization,
                'organization_link': experience.organization_link,
                'logo_url': experience.logo_url,
                'subtitle': experience.subtitle,
                'location': experience.location,
                'start_date': experience.start_date,
                'end_date': experience.end_date,
                'is_present': experience.is_present(),
                'description_sentences': self.tokenize_description(experience.description),
            })
        return experience_objects

    def get(self, request):
        context = {
            'sections': [
                'banner',
                'intro',
                'experiences',
                'skills',
                'projects',
            ],
            'experiences': self.get_experiences(),
        }
        return render(request, 'resume/index.html', context)