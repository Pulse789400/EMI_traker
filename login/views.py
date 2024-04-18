from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from login.models import BaseSales
from login.models import  UserProfile

# Create your views here.
def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you have been logged in')
            return redirect('home')
        else:
            return render(request, 'login/index.html', {'error': 'Sorry. The Username and Passwords do not match.'})
    else:
        if request.user.is_authenticated:
            Group=BaseSales.objects.filter(Division=request.user.userprofile.Division,Head_Quarter=request.user.userprofile.Head_Quarter)[0].Group
            Category=BaseSales.objects.filter(Division=request.user.userprofile.Division,Head_Quarter=request.user.userprofile.Head_Quarter)[0].Category
            data=BaseSales.objects.filter(Division=request.user.userprofile.Division,Head_Quarter=request.user.userprofile.Head_Quarter)[0]
        else:
            pass
        if request.user.is_authenticated and request.user.userprofile.Design =='BM':
            context={'name':request.user.first_name,
        'profile': request.user.userprofile,'data': data
        }
            return render(request,"data/manager_data.html",context)
            
        elif(request.user.is_authenticated):
            if Category == 'GT':
                if Group == 'Diamond Territory':
                    table={'10':'10000','20':'20000','30':'30000','40':'40000','50':'50000'}
                    sales={'Sales1':str(int(int(data.Final_Base_PCPM)*1.1)),'Sales2':str(int(int(data.Final_Base_PCPM)*1.2)),'Sales3':str(int(int(data.Final_Base_PCPM)*1.3)),'Sales4':str(int(int(data.Final_Base_PCPM)*1.4)),'Sales5':str(int(int(data.Final_Base_PCPM)*1.5))}
                    
                elif Group == 'Platinum Territory':
                    table={'10':'7500','20':'15000','30':'22500','40':'30000','50':'40000'}
                    sales={'Sales1':str(int(int(data.Final_Base_PCPM)*1.1)),'Sales2':str(int(int(data.Final_Base_PCPM)*1.2)),'Sales3':str(int(int(data.Final_Base_PCPM)*1.3)),'Sales4':str(int(int(data.Final_Base_PCPM)*1.4)),'Sales5':str(int(int(data.Final_Base_PCPM)*1.5))}
                    
                elif Group == 'Gold Territory':
                    table={'10':'4000','20':'7500','30':'12500','40':'17500','50':'25000'}
                    sales={'Sales1':str(int(int(data.Final_Base_PCPM)*1.1)),'Sales2':str(int(int(data.Final_Base_PCPM)*1.2)),'Sales3':str(int(int(data.Final_Base_PCPM)*1.3)),'Sales4':str(int(int(data.Final_Base_PCPM)*1.4)),'Sales5':str(int(int(data.Final_Base_PCPM)*1.5))}
                    
                elif Group == 'Silver Territory':
                    table={'10':'NA','20':'5000','30':'7500','40':'10000','50':'15000'}
                    sales={'Sales1':'NA','Sales2':str(int(int(data.Final_Base_PCPM)*1.2)),'Sales3':str(int(int(data.Final_Base_PCPM)*1.3)),'Sales4':str(int(int(data.Final_Base_PCPM)*1.4)),'Sales5':str(int(int(data.Final_Base_PCPM)*1.5))}
                    
                else:
                    table={}
                    sales={}
                    
            else:
                if Group == 'Tier-I Territory':
                    if (int(data.Final_Base_PCPM) + 50000) > 160000:
                        sales={'sales':str(int(data.Final_Base_PCPM) + 50000),'incentive':'20000'}
                    else:
                        sales={'sales':'160000','incentive':'20000'}

                elif Group == 'Tier-II Territory':
                    if (int(data.Final_Base_PCPM) + 40000) > 100000:
                        print(int(data.Final_Base_PCPM) + 40000)
                        sales={'sales':str(int(data.Final_Base_PCPM)+ 40000),'incentive':'15000'}
                    else:
                        sales={'sales':'100000','incentive':'15000'}

                elif Group == 'Tier-III Territory':
                    if (int(data.Final_Base_PCPM) + 30000) > 50000:
                        sales={'sales':str(int(data.Final_Base_PCPM)+ 30000),'incentive':'10000'}
                    else:
                        sales={'sales':'50000','incentive':'10000'}
                else:
                    sales={'sales':'','incentive':''}
                table={}



                
                

                
                
            

            
            
            #sales={'Sales1':str(data.Final_Base_PCPM),'Sales2':data.Final_Base_PCPM,'Sales3':data.Final_Base_PCPM,'Sales4':data.Final_Base_PCPM,'Sales5':data.Final_Base_PCPM}
            




           
            context = {
                'name':request.user.first_name,
        'profile': request.user.userprofile,
        'data': data,
         'table':table,
         'sales':sales
         }
            
            return render(request,"data/data.html",context)
        
        else:
            return render(request, 'login/index.html',{})



    
    

def login_request(request):
    pass

def logout_request(request):
    logout(request)
    return redirect('home')