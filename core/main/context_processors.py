from .models import Addres, HeaderLogo, HeaderContact, HeaderGetAQuoteButton, FooterAboutUs, FooterWorkingHour, FooterService, FooterNavigation

def base_on_all_pages(request):
    return {'addres': Addres.objects.all(),
            'headerlogo': HeaderLogo.objects.all(),
            'headercontact': HeaderContact.objects.all(),
            'headergetaquotebutton': HeaderGetAQuoteButton.objects.all(),
            'footeraboutUs': FooterAboutUs.objects.all(),
            'footerworkinghour': FooterWorkingHour.objects.all(),
            'footerservice': FooterService.objects.all(),
            'footernavigation': FooterNavigation.objects.all()}