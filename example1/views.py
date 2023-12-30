from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request,'contact.html')

def demo(request):
    return render(request,'certificates.html')

def userForm(request):
    res=0
    try:
        n1=int(request.GET.get('Num1'))
        n2=int(request.GET.get('Num2'))
        res=n1+n2
    except Exception as e:
        print(f'Error Occurred use to {str(e)}') 
    return render(request,"userForm.html",{'output':res})


