from django.shortcuts import render, redirect
from classroom_integration.forms import CredentialsForm
from classroom_integration.models import Credentials


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'account/register.html')

def classroom(request):
    return render(request, 'classroom/general.html')

def classroom_courses(request):
    return render(request, 'classroom/courses.html')

def classroom_account(request):
    form = CredentialsForm()
    return render(request, 'classroom/account.html')

def account_save(request):
    if request.method == 'POST':
        client_id = request.POST['listing_id']
        api_key = request.POST['listing']

        # Check if user has made inquiriy already
        if request.user.is_authenticated :
            user = request.user
            teacher = Credentials.objects.filter(credentials__user_id=user)
            if not teacher:
                messages.error(request, 'Erro ao tentar salvar credenciais')
                return redirect('classroom/account')
            else :
                credentials = Credentials(teacher=teacher, client_id=client_id, api_key='api_key')
                credentials.save()
        else :
            messages.error(request, 'Usuario precisa estar conectado para salvar as informações')
        

    return redirect('classroom/account')
        
    