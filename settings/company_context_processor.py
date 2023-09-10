from .models import Company





def get_company_data(requset):
    data = Company.objects.last()
    return{'company_data':data}