from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class HomeListView(ListView):
    template_name = 'index.html'

    def get(self, request):
        homecarusel1 = HomeCarusel1.objects.all()
        homecarusel2 = HomeCarusel2.objects.all()
        homecarusel3 = HomeCarusel3.objects.all()
        aboutus = AboutUs.objects.all()
        service = Service.objects.all()
        value = Value.objects.all()
        valuecategory = ValueCategory.objects.all()
        yourneed = YourNeed.objects.all()
        fact = Fact.objects.all()
        specialist = Specialist.objects.all()
        skill1 = Skill1.objects.all()
        skill2 = Skill2.objects.all()
        serviceavatar = ServiceAvatar.objects.all()
        projecttitle = ProjectTitle.objects.all()
        projectcategory = ProjectCategory.objects.all()
        return render(request, self.template_name, {
            'homecarusel1': homecarusel1,
            'homecarusel2': homecarusel2, 
            'homecarusel3': homecarusel3,
            'aboutus': aboutus,
            'service': service,
            'value': value, 
            'valuecategory': valuecategory,
            'yourneed': yourneed,
            'fact': fact,
            'specialist': specialist, 
            'skill1': skill1,
            'skill2': skill2,
            'serviceavatar': serviceavatar,
            'projecttitle': projecttitle,
            'projectcategory': projectcategory})

class HomeValueSubCatDetailView(DetailView):
    template_name = 'index.html'

    def get(self, request, id):
        valuecategorysubcategory = ValueCategorySubcategory.objects.get(pk=id)
        return render(request, self.template_name, {'valuecategorysubcategory': valuecategorysubcategory})


class HomeProjectCategorySubCatDetailView(DetailView):
    template_name = 'index.html'

    def get(self, request, id):
        projectcategorysubcategory = ProjectCategorySubcategory.objects.get(pl=id)
        return render(request, self.template_name, {'projectcategorysubcategory': projectcategorysubcategory})