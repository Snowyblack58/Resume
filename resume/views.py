from collections import OrderedDict

from django.db.models import Case, When, Value, IntegerField
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Experience, Project, Skill


class IndexView(View):
    def tokenize_description(self, text):
        return [s.strip() for s in text.split('\n') if s.strip()]

    def get_raw_experiences_in_order(self):
        return Experience.objects.annotate(  # 1 is highest priority
                priority=Case(
                    When(experience_type='e', then=Value(2)),
                    When(experience_type='w', then=Value(1)),
                    When(experience_type='l', then=Value(3)),
                    output_field=IntegerField()
                )
            ).order_by('priority', '-end_date')
        

    def get_experiences(self):
        exps = self.get_raw_experiences_in_order()
        grouped_exps = OrderedDict()  # OrderedDict to order by priority
        for exp in exps:
            exp_type = exp.get_experience_type_readable()
            if exp_type not in grouped_exps:
                grouped_exps[exp_type] = []
            grouped_exps[exp_type].append({
                'organization': exp.organization,
                'organization_link': exp.organization_link,
                'logo_url': exp.logo_url,
                'subtitle': exp.subtitle,
                'location': exp.location,
                'start_date': exp.start_date,
                'end_date': exp.end_date,
                'is_present': exp.is_present(),
                'is_one_month': exp.is_one_month(),
                'description_sentences': self.tokenize_description(exp.description),
            })
        return grouped_exps
        

    def get_projects(self):
        raw_projects = Project.objects.order_by('-end_date')
        projects = []
        for project in raw_projects:
            projects.append({
                'project_name': project.project_name,
                'project_link': project.project_link,
                'logo_url': project.logo_url,
                'subtitle': project.subtitle,
                'languages': project.languages,
                'start_date': project.start_date,
                'end_date': project.end_date,
                'is_present': project.is_present(),
                'is_one_month': project.is_one_month(),
                'description_sentences': self.tokenize_description(project.description),
            })
        return projects

    def get_raw_skills_in_order(self):
        return Skill.objects.annotate(  # 1 is highest priority
                priority=Case(
                    When(skill_category='co', then=Value(1)),
                    When(skill_category='wb', then=Value(2)),
                    When(skill_category='da', then=Value(3)),
                    When(skill_category='o', then=Value(4)),
                    output_field=IntegerField()
                )
            ).order_by('priority', '-proficiency', 'skill_name')

    def get_skills(self):
        skills = self.get_raw_skills_in_order()
        grouped_skills = OrderedDict()  # OrderedDict to order by priority
        for skill in skills:
            skill_category = skill.get_skill_category_readable()
            if skill_category not in grouped_skills:
                grouped_skills[skill_category] = []
            grouped_skills[skill_category].append({
                'name': skill.skill_name,
                'proficiency': skill.proficiency,
            })
        return grouped_skills

    def get(self, request):
        context = {
            'sections': [
                'intro',
                'experiences',
                'projects',
                'skills',
            ],
            'anchors': [
                'intro',
                'education',
                'work',
                'leadership',
                'projects',
                'skills',
            ],
            'experiences': self.get_experiences(),
            'projects': self.get_projects(),
            'skills': self.get_skills(),
        }
        return render(request, 'resume/index.html', context)
