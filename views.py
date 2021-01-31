from django.shortcuts import render
import joblib



def home(request):
    return render(request,"home.html",{})

def result(request):
    cls = joblib.load('Finalmodel1.sav')

    lis = []

    lis.append(request.GET['Temperature'])
    lis.append(request.GET['Presure'])
    lis.append(request.GET['Humidity'])
    lis.append(request.GET['Speed'])

    print(lis)
    ans = cls.predict([lis])


    return render(request,"result.html",{'ans':ans,'lis':lis})
