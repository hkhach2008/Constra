from audioop import maxpp
from distutils.command.upload import upload
from itertools import chain
from statistics import mode
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

class HomeCarusel1(models.Model):
    name1 = models.CharField('Carusel1 name 1', max_length=120)
    name2 = models.CharField('Carusel1 name 2', max_length=120)
    img = models.ImageField('Carusel1 image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeCarusel1'
        verbose_name_plural = 'HomeCarusels1'


class HomeCarusel2(models.Model):
    name1 = models.CharField('Carusel2 name 1', max_length=120)
    name2 = models.CharField('Carusel2 name 2', max_length=120)
    name3 = models.CharField('Carusel2 name 3', max_length=120)
    img = models.ImageField('Carusel2 image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeCarusel2'
        verbose_name_plural = 'HomeCarusels2'

class HomeCarusel3(models.Model):
    name1 = models.CharField('Carusel3 name 1', max_length=120)
    name2 = models.CharField('Carusel3 name 2', max_length=120)
    name3 = models.CharField('Carusel3 name 3', max_length=120)
    img = models.ImageField('Carusel3 image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HomeCarusel3'
        verbose_name_plural = 'HomeCarusels3'

class AboutUs(models.Model):
    name1 = models.CharField('AboutUs Title', max_length=25)
    name2 = models.CharField('AboutUs name1', max_length=75)
    about = models.TextField('AboutUs about')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUses'

class Service(models.Model):
    name = models.CharField('Service name', max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

class Value(models.Model):
    name = models.CharField('Value name', max_length=75)
    about = models.TextField('Value about')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Value'
        verbose_name_plural = 'Values'

class ValueCategory(models.Model):
    name = models.CharField('ValueCategory name', max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ValueCategory'
        verbose_name_plural = 'ValueCategories'

class ValueCategorySubcategory(models.Model):
    valuecategory = models.ForeignKey(ValueCategory, related_name='subcateg', on_delete=models.CASCADE) 
    about = models.TextField('ValueCategorySubcategory')

    def __str__(self):
        return self.about

    class Meta:
        verbose_name = 'ValueCategorySubcategory'
        verbose_name_plural = 'ValueCategorySubcategories'

class YourNeed(models.Model):
    name = models.CharField('YourNeed name', max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'YourNeed'
        verbose_name_plural = 'YourNeeds'


class Fact(models.Model):
    num = models.IntegerField('Fact num')
    name = models.CharField('Fact name', max_length=75)
    img = models.ImageField('Fact image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fact'
        verbose_name_plural = 'Facts'

class Specialist(models.Model):
    name1 = models.CharField('Specialist name1', max_length=75)
    name2 = models.CharField('Specialist name2', max_length=75)
    
    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'Specialist'
        verbose_name_plural = 'Specialists'


class Skill1(models.Model):
    name = models.CharField('Skill1 name', max_length=75)
    about = models.TextField('Skill1 about')
    img = models.ImageField('Skill1 image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill1'
        verbose_name_plural = 'Skills1'

class Skill2(models.Model):
    name = models.CharField('Skill2 name', max_length=75)
    about = models.TextField('Skill2 about')
    img = models.ImageField('Skill2 image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Skill2'
        verbose_name_plural = 'Skills2'

class ServiceAvatar(models.Model):
    img = models.ImageField('ServiceAvatar image', upload_to = 'media')

    def __str__(self):
        return 'Service avatar image'

    class Meta:
        verbose_name = 'ServiceAvatar'
        verbose_name_plural = 'ServiceAvatars'

class ProjectTitle(models.Model):
    name1 = models.CharField('ProjectTitle name1', max_length=75)
    name2 = models.CharField('ProjectTitle name2', max_length=75)

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'ProjectTitle'
        verbose_name_plural = 'ProjectTitles'

class ProjectCategory(models.Model):
    name = models.CharField('ProjectCategory name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ProjectCategory'
        verbose_name_plural = 'ProjectCategories'

class ProjectCategorySubcategory(models.Model):
    projectcategory = models.ForeignKey(ProjectCategory, related_name='subcat', on_delete=models.CASCADE)
    name1 = models.CharField('ProjectCategorySubcategory name1', max_length=50)
    name2 = models.CharField('ProjectCategorySubcategory name2', max_length=50)
    img = models.ImageField('ProjectCategorySubcategory image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'ProjectCategorySubcategory'
        verbose_name_plural = 'ProjectCategorySubcategories'

class TestimonialTitle(models.Model):
    name = models.CharField('Testimonials name1', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'TestimonialTitle'
        verbose_name_plural = 'TestimonialTitles'

class Testimonial(models.Model):
    name2 = models.CharField('Testimonials name2', max_length=50)
    name3 = models.CharField('Testimonials name3', max_length=50)
    about = models.TextField('Testimonial about')
    img = models.ImageField('Testimonial image', upload_to='media')

    def __str__(self):
        return self.name2

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

class HappyClientTitle(models.Model):
    title = models.CharField('HappyClientTitle title', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'HappyClientTitle'
        verbose_name_plural = 'HappyClientTitles'

class Client(models.Model):
    img = models.ImageField('Client image', upload_to='media')

    def __str__(self):
        return 'Client image'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

class NewsLetter(models.Model):
    name1 = models.CharField('NewsLetter name1', max_length=50)
    name2 = models.CharField('NewsLetter name2', max_length=50)
    name3 = models.CharField('NewsLetter name3', max_length=50)
    name4 = models.CharField('NewsLetter name4', max_length=50)

    def __str__(self):
        return 'NewsLetter content'

    class Meta:
        verbose_name = 'NewsLetter'
        verbose_name_plural = 'NewsLetters'

class ProjectTitle2(models.Model):
    title1 = models.CharField('ProjectTitle2 title1', max_length=50)
    title2 = models.CharField('ProjectTitle2 title2', max_length=50)

    def __str__(self):
        return self.title1

    class Meta:
        verbose_name = 'ProjectTitle2'
        verbose_name_plural = 'ProjectTitles2'

class Project2(models.Model):
    date = models.CharField('Project2 date', max_length=50)
    about = models.TextField('Project2 about')
    img = models.ImageField('Project2 image', upload_to='media')

    def __str__(self):
        return 'Project2 content'

    class Meta:
        verbose_name = 'Project2'
        verbose_name_plural = 'Projects2'

class ViewAllProjectButton(models.Model):
    name = models.CharField('ViewAllProjectButton name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ViewAllProjectButton'
        verbose_name_plural = 'ViewAllProjectButtons'

class SeeAllPostButton(models.Model):
    name = models.CharField('SeeAllPostButton name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SeeAllPostButton'
        verbose_name_plural = 'SeeAllPostButtons'

class Addres(models.Model):
    name = models.CharField('Addres name', max_length=75)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Addres'
        verbose_name_plural = 'Addreses'

class HeaderLogo(models.Model):
    name1 = models.CharField('Contact name1', max_length=75, blank=True)
    img = models.ImageField('Contact image', upload_to='media', blank=True)

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HeaderLogo'
        verbose_name_plural = 'HeaderLogos'

class HeaderContact(models.Model):
    name1 = models.CharField('Contact name1', max_length=50)
    name2 = models.CharField('Contact name2', max_length=75)

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'HeaderContact'
        verbose_name_plural = 'HeaderContacts'

class HeaderGetAQuoteButton(models.Model):
    name = models.CharField('HeaderGetAQuoteButton name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HeaderGetAQuoteButton'
        verbose_name_plural = 'HeaderGetAQuoteButtons'

class FooterAboutUs(models.Model):
    name = models.CharField('FooterAboutUs name', max_length=50)
    about = models.TextField('FooterAboutUs about')
    img = models.ImageField('FooterAboutUs image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'FooterAboutUs'
        verbose_name_plural = 'FooterAboutUses'

class FooterWorkingHour(models.Model):
    name = models.CharField('FooterWorkingHour name', max_length=50, blank=True)
    day = models.CharField('FooterWorkingHour day', max_length=75)
    hour = models.CharField('FooterWorkingHour hour', max_length=50)
    about = models.TextField('FooterWorkingHour about', blank=True)

    def __str__(self):
        return 'Working Hours'

    class Meta:
        verbose_name = 'FooterWorkingHour'
        verbose_name_plural = 'FooterWorkingHours'

class FooterService(models.Model):
    name = models.CharField('FooterService name', max_length=50, blank=True)
    service = models.CharField('FooterService service', max_length=75)

    def __str__(self):
        return self.service

    class Meta:
        verbose_name = 'FooterService'
        verbose_name_plural = 'FooterServices'

class FooterNavigation(models.Model):
    name = models.CharField('FooterNavigation name', max_length=50)
    href = models.CharField('FooterNavigation href', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'FooterNavigation'
        verbose_name_plural = 'FooterNavigations'

class AboutBG(models.Model):
    name1 = models.CharField('AboutBG name1', max_length=50, blank=True)
    name2 = models.CharField('AboutBG name2', max_length=50)
    img = models.ImageField('AboutBG image', upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name2

    class Meta:
        verbose_name = 'AboutBG'
        verbose_name_plural = 'AboutBGs'

class AboutWhoWeAre(models.Model):
    title = models.CharField('AboutWhoWeAre title', max_length=50, blank=True)
    about1 = models.TextField('AboutWhoWeAre about1')
    about2 = models.TextField('AboutWhoWeAre about2')
    about3 = models.TextField('AboutWhoWeAre about3')

    def __str__(self):
        return 'About who we are'

    class Meta:
        verbose_name = 'AboutWhoWeAre'
        verbose_name_plural = 'AboutWhoWeAres'

class AboutPageSlider(models.Model):
    title = models.CharField('AboutPageSlider title', max_length=50)
    img = models.ImageField('AboutPageSlider image', upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'AboutPageSlider'
        verbose_name_plural = 'AboutPageSliders'

class AboutFact(models.Model):
    num = models.IntegerField('Fact num')
    name = models.CharField('Fact name', max_length=75)
    img = models.ImageField('Fact image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'AboutFact'
        verbose_name_plural = 'AboutFacts'

class AboutTeamTitle(models.Model):
    title = models.CharField('AboutTeamTitle title', max_length=50)
    name = models.CharField('AboutTeamTitle name', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'AboutTeamTitle'
        verbose_name_plural = 'AboutTeamTitles'

class AboutTeam(models.Model):
    name1 = models.CharField('AboutTeam name1', max_length=50)
    name2 = models.CharField('AboutTeam name2', max_length=50)
    about = models.TextField('AboutTeam about')
    img = models.ImageField('AboutTeam image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'AboutTeam'
        verbose_name_plural = 'AboutTeams'

class TeamBG(models.Model):
    name1 = models.CharField('TeamBG name1', max_length=50, blank=True)
    name2 = models.CharField('TeamBG name2', max_length=50)
    img = models.ImageField('TeamBG image', upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name2

    class Meta:
        verbose_name = 'TeamBG'
        verbose_name_plural = 'TeamBGs'

class TeamTitle(models.Model):
    title = models.CharField('TeamTitle title', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TeamTitle'
        verbose_name_plural = 'TeamTitles'

class TeamTeam(models.Model):
    name1 = models.CharField('AboutTeam name1', max_length=50)
    name2 = models.CharField('AboutTeam name2', max_length=50)
    about = models.TextField('AboutTeam about')
    img = models.ImageField('AboutTeam image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'TeamTeam'
        verbose_name_plural = 'TeamTeams'

class TestimonialBG(models.Model):
    name1 = models.CharField('TestimonialsBG name1', max_length=50, blank=True)
    name2 = models.CharField('TestimonialsBG name2', max_length=50)
    img = models.ImageField('TestimonialsBG image', upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name2

    class Meta:
        verbose_name = 'TestimonialsBG'
        verbose_name_plural = 'TestimonialBGs'

class TestimonialQuoteTitle(models.Model):
    title = models.CharField('TestimonialTitle title', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TestimonialQuoteTitle'
        verbose_name_plural = 'TestimonialQuoteTitles'

class TestimonialQuote(models.Model):
    name1 = models.CharField('TestimonialQuote name1', max_length=50)
    name2 = models.CharField('TestimonialQuote name2', max_length=75)
    about = models.TextField('TestimonialQuote about')
    img = models.ImageField('TestimonialQuote image', upload_to='media')

    def __str__(self):
        return self.name1

    class Meta:
        verbose_name = 'TestimonialQuote'
        verbose_name_plural = 'TestimonialQuotes'


class FaqBG(models.Model):
    name1 = models.CharField('FaqBG name1', max_length=50, blank=True)
    name2 = models.CharField('FaqBG name2', max_length=50)
    img = models.ImageField('FaqBG image', upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.name2

    class Meta:
        verbose_name = 'FaqBG'
        verbose_name_plural = 'FaqBGs'

class FaqCatTitle1(models.Model):
    title = models.CharField('FaqCatTitle title1', max_length=75)

    def __str__(self):
        return 'Faq Category Titles1'

    class Meta:
        verbose_name = 'FaqCatTitle1'
        verbose_name_plural = 'FaqCatTitles1'

class FaqCatTitle2(models.Model):
    title = models.CharField('FaqCatTitle title2', max_length=75)

    def __str__(self):
        return 'Faq Category Titles2'

    class Meta:
        verbose_name = 'FaqCatTitle2'
        verbose_name_plural = 'FaqCatTitles2'

class FaqCat(models.Model):
    name = models.CharField('FaqCat name', max_length=175)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'FaqCat'
        verbose_name_plural = 'FaqCats'    

class FaqCatSubcat1(models.Model):
    faqcat = models.ForeignKey(FaqCat, related_name = 'subcat1', on_delete=models.CASCADE)
    about = models.TextField('FaqCatSubcat1')

    def __str__(self):
        return 'Faq Subcategory1 about'

    class Meta:
        verbose_name = 'FaqCatSubcat1'
        verbose_name_plural = 'FaqCatSubcats1'


class FaqCatSubcat2(models.Model):
    faqcat = models.ForeignKey(FaqCat, related_name = 'subcat2', on_delete=models.CASCADE)
    about = models.TextField('FaqCatSubcat1')

    def __str__(self):
        return 'Faq Subcategory2 about'

    class Meta:
        verbose_name = 'FaqCatSubcat2'
        verbose_name_plural = 'FaqCatSubcats2'