from django.shortcuts import render ,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from my_portfolio_app.models import ClasFormModel
# Create your views here.
def my_first_view(request):
    return render(request,"my_portfolio_app/my_first_page.html")

def my_second_view(request):
    return render(request,"my_portfolio_app/my_second_page.html")

def my_third_view(request):
    return render(request,"my_portfolio_app/my_third_page.html")

def contact_form_submit(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email_id = request.POST['email_id']
        contact_number = request.POST['contact_number']
        message = request.POST['message']
        ClasFormModel.objects.create(
            full_name = full_name,
            email_id = email_id,
            contact_number = contact_number,
            message = message,
        )
    return HttpResponseRedirect(reverse('my_portfolio_app:my_third_url'))

def contact_form_data(request):
    class_form_all_values = ClasFormModel.objects.all()
    data = {
        'class_form_all_values':class_form_all_values,
    }
    return render(request,'my_portfolio_app/my_forth_page.html',data)
    