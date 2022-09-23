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