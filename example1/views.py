from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from form import UserForms

def Home(request):
    # data={
    #     "title":'My Websites',
    #     "bdata":"Hello Dosto Kaise ho aap log",
    #     "Course_list":['.Net','Python','Java'],
    #     "number":[1,20,3,4,50,8,10,60,80,100],
    #     "Student_details":[
    #         {'Name':'Nitesh',"Phone_No":9234567654},
    #         {'Name':'Sam',"Phone_No":7064570330}
    #     ]
    # }
    # return render(request,"index.html",data)
    return render(request,"index.html")

# def contactUs(request):
#     return HttpResponse("Welcome to our demo of Django")
# def blog(request):
#     return HttpResponse("Welcome to our blog page")

# def courses(request):
#     return HttpResponse("Welcome to our different cources")

# def coursesDetails(request,courseid):
#     return HttpResponse(courseid)

def blog(request):
    return render(request,'index.html')

def certificate(request):
    return render(request,'certificates.html')

def contact(request):
    if request.method=='GET':  #to display the data on contact page from userform
        output=request.GET.get('output')

    return render(request,'contact.html',{'output':output})

def submitdata(request):
    res=0
    data={}
    
    try:
        if request.method=='POST':
            # n1=request.GET.get('Num1')
            # n2=request.GET.get('Num2')
            #res=int(n1)+int(n2)
            n1=request.POST.get('Num1')
            n2=request.POST.get('Num2')
            print(int(n1)+int(n2))
            res=int(n1)+int(n2)
            data={
                'n1':n1,
                'n2':n2,
                'output':res
            }
            return HttpResponse(res)
    except Exception as e:
        print(f'Error Occurred use to {str(e)}') 
    
    

def demo(request):
    return render(request,'certificates.html')

def userForm(request):
    res=0
    data={}
    
    try:
        if request.method=='POST':
            # n1=request.GET.get('Num1')
            # n2=request.GET.get('Num2')
            #res=int(n1)+int(n2)
            n1=request.POST.get('Num1')
            n2=request.POST.get('Num2')
            print(int(n1)+int(n2))
            res=int(n1)+int(n2)
            data={
                'n1':n1,
                'n2':n2,
                'output':res
            }
            url='/contact/?output={}'.format(res)
            return HttpResponseRedirect(url)
        else:
            pass
    except Exception as e:
        print(f'Error Occurred use to {str(e)}') 
    

    return render(request,"userForm.html",data)
    # return render(request,"userForm.html",data)
    # return render(request,"userForm.html",{'output':res})


