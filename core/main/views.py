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
        testimonialtitle = TestimonialTitle.objects.all()
        testimonial = Testimonial.objects.all()
        happyclienttitle = HappyClientTitle.objects.all()
        client = Client.objects.all() 
        newsletter = NewsLetter.objects.all()
        projecttitle2 = ProjectTitle2.objects.all()
        project2 = Project2.objects.all()
        viewallprojectbutton = ViewAllProjectButton.objects.all()
        seeallpostbutton = SeeAllPostButton.objects.all()
        addres = Addres.objects.all()
        headerlogo = HeaderLogo.objects.all()
        headercontact = HeaderContact.objects.all()
        headergetaquotebutton = HeaderGetAQuoteButton.objects.all()
        footeraboutUs = FooterAboutUs.objects.all()
        footerworkinghour = FooterWorkingHour.objects.all()
        footerservice = FooterService.objects.all()
        footernavigation = FooterNavigation.objects.all()
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
            'projectcategory': projectcategory,
            'testimonial': testimonial,
            'testimonialtitle': testimonialtitle,
            'happyclienttitle': happyclienttitle,
            'client': client,
            'newsletter': newsletter,
            'projecttitle2': projecttitle2,
            'project2': project2,
            'viewallprojectbutton': viewallprojectbutton,
            'seeallpostbutton': seeallpostbutton,
            'addres': addres,
            'headerlogo': headerlogo,
            'headercontact': headercontact,
            'headergetaquotebutton': headergetaquotebutton,
            'footeraboutUs': footeraboutUs,
            'footerworkinghour': footerworkinghour,
            'footerservice': footerservice,
            'footernavigation': footernavigation})

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


class AboutListView(ListView):
    template_name = 'about.html'

    def get(self, request):
        aboutbg = AboutBG.objects.all()
        return render(request, self.template_name, {'aboutbg': aboutbg})