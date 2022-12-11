from django.conf import settings
from django.shortcuts import render, HttpResponse
from app01.database import PgSql
import json
# Create your views here.

db = PgSql()

def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')


def upload(request):
    
    if request.method == 'GET':
        return render(request, 'upload.html')
    else:
        ProductName = request.POST['ProductName']
        print(request.POST)
        p_type = request.POST['type']
        file = request.FILES['upload']
        price = request.POST['price']
        description = request.POST['description']
        filename = '%s' %(file)
        root = '%s/%s'%(settings.MEDIA_ROOT, filename)
        with open(root, 'wb') as f:
            for i in file.chunks():
                f.write(i)
        id = db.getProductID()
        db.updateNextProductID(id)
        db.addProductInfo(id, price, description)
        db.addProduct(ProductName, p_type, id, filename, 'Zesen')
        return render(request, 'upload.html')


def mainpage(request):
    return render(request, "mainPage.html")

def profile(request):
    return render(request, "Account.html")

def marketfront(request):
    return render(request, "marketfront.html")

def loadposts(request):
    return HttpResponse(json.dumps(db.loadProductInfo()), content_type ="application/json")




