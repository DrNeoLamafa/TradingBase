from django.shortcuts import render
from django.db.models import Count, F, Value
import random
from datetime import datetime
from datetime import timedelta
import json
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import Group
from .models import *
from django_tables2 import RequestConfig
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.conf import settings
import xlwt


def base(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/center')
    return render(request, 'base.html')

def center(request):
    username = request.user.username
    try:
        if request.user.groups.get().name == 'shopmanager':
            group = request.user.groups.get().name
            return shopmanager(request, username, group)
        if request.user.groups.get().name == 'sectionmanager':
            group = request.user.groups.get().name
            return sectionmanager(request, username, group)
        if request.user.groups.get().name == 'basamanager':
            group = request.user.groups.get().name
            return basamanager(request, username, group)
    except:
        return render(request, "wait.html")
    

    

 
# Функция регистрации
def regist(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = RegistForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return HttpResponseRedirect('/login')
    else: # Иначе
        # Создаём форму
        form = RegistForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'register.html', data)


def shopmanager(request, username, group):

    upsec = updateSec()
    insec = insertSec()
    delsec = deleteSec()

    addtype = TypeItem()
    search = Search()
    update = updateForm()
    delete = deleteForm()
    insert = insertForm()
    maginfo = Shops.objects.get(заведующий=username)
    section = Section_shop.objects.filter(номермагазина=maginfo.номер)
    item = Item_shop.objects.filter(номермагазина=maginfo.номер)

    if request.method == "POST" and 'insert' in request.POST:
        form = insertForm(request.POST)
        if form.is_valid():
            new = Item_shop()
            new = form.save(commit=False)
            new.номермагазина = Shops.objects.get(номер=maginfo.номер)
            
            new.save()
            messages.success(request, 'Успешно')

            return HttpResponseRedirect('/center')

    if request.method == "POST" and 'update' in request.POST:
        try:
            up = Item_shop.objects.get(артикул=request.POST.get("артикул"))
                
            upform = updateForm(request.POST, instance=up)
            if upform.is_valid():
                upform.save()
                up.save()

                return HttpResponseRedirect('/center')
        except:
            messages.error(request, 'Неверный артикул')

            return HttpResponseRedirect('/center')

    if request.method == "POST" and 'delete' in request.POST:
        delform = deleteForm(request.POST)
        try:
            if delform.is_valid():
                    Item_shop.objects.get(артикул=request.POST.get("артикул")).delete()
                
                
                    return HttpResponseRedirect('/center')
        except:
            messages.error(request, 'Неверный артикул')

            return HttpResponseRedirect('/center')


    if request.method == "POST" and 'addtype' in request.POST:
        addtype = TypeItem(request.POST)
        if addtype.is_valid():
                new = addtype.save(commit=False)
                new.save()
            
            
                return HttpResponseRedirect('/center')


    if request.method == "POST" and 'insec' in request.POST:
        insec = insertSec(request.POST)
        if insec.is_valid():
            newsec = Section_shop()
            newsec = insec.save(commit=False)
            newsec.номермагазина = Shops.objects.get(номер=maginfo.номер)
            
            newsec.save()

            return HttpResponseRedirect('/center')

    if request.method == "POST" and 'upsec' in request.POST:
        try:
            upsecnew =  Section_shop.objects.get(номеротдела=request.POST.get("номеротдела"))
                
            upsec = updateSec(request.POST, instance=upsecnew)
            if upsec.is_valid():
                upsec.save()
                upsecnew.save()

                return HttpResponseRedirect('/center')
        except:
            messages.error(request, 'Неверный номер')

            return HttpResponseRedirect('/center')

    if request.method == "POST" and 'delsec' in request.POST:
        
        delsec = deleteSec(request.POST)
        if delsec.is_valid():
                Section_shop.objects.get(номеротдела=request.POST.get("номеротдела")).delete()
            
            
                return HttpResponseRedirect('/center')

    if request.method == "POST" and 'search' in request.POST:
    
        search = Search(request.POST)
        if search.is_valid():
                item = Item_shop.objects.filter(название__iexact=request.POST.get("название"))
            
            
                return render(request, 'center.html', {'search': search, 'addtype': addtype, 'group':group, 'maginfo': maginfo, 'username': username, 'item': item, 'insert': insert, 'delete': delete, 'section': section, 'update': update, 'delsec': delsec, 'insec': insec, 'upsec': upsec})


      
                
            
                
    return render(request, 'center.html', {'search': search, 'addtype': addtype, 'group':group, 'maginfo': maginfo, 'username': username, 'item': item, 'insert': insert, 'delete': delete, 'section': section, 'update': update, 'delsec': delsec, 'insec': insec, 'upsec': upsec})


def sectionmanager(request, username, group):
    
    update = updateForm()

    maginfo = Shops.objects.get(отделмагазин__заведующий=username)
    section = Section_shop.objects.get(заведующий=username)
    item = Item_shop.objects.filter(номеротдела=section.номеротдела)


    if request.method == "POST" and 'update' in request.POST:
        
        up = Item_shop.objects.get(артикул=request.POST.get("артикул"))
            
        upform = updateForm(request.POST, instance=up)
        if upform.is_valid():
            upform.save()
            up.save()

            return HttpResponseRedirect('/center')

    



      
                
            
                
    return render(request, 'center.html', {'section': section,'group': group, 'maginfo': maginfo, 'username': username, 'item': item, 'update': update})


def basamanager(request, username, group):
    basainfo = Base.objects.get(заведующий = username)



    basaupdate = basaupForm()
    basadelete = basadeleteForm()
    basainsert = basainForm()
    

    if request.method == "POST" and 'insert' in request.POST:
        baup = basainForm(request.POST)
        if baup.is_valid():
            new = Item_base()
            new = baup.save(commit=False)
            new.база = Base.objects.get(номер=basainfo.номер)
            
            new.save()

            return HttpResponseRedirect('/center')

    if request.method == "POST" and 'update' in request.POST:
      
        up = Item_base.objects.get(артикул=request.POST.get("артикул"))
        baup = basaupForm(request.POST, instance=up)
        if baup.is_valid():
            baup.save()
            up.save()

            return HttpResponseRedirect('/center')
        
             

    if request.method == "POST" and 'delete' in request.POST:
        badel = deleteForm(request.POST)
        if badel.is_valid():
                Item_base.objects.get(артикул=request.POST.get("артикул")).delete()
            
            
                return HttpResponseRedirect('/center')
    try:
        item = Item_base.objects.filter(база=basainfo.номер)
        magazine = Shops.objects.filter(торговаябаза=basainfo.номер)
    
    except: 
        return render(request, 'center.html', {'group':group,  'basainfo': basainfo, 'username': username, 'insert': basainsert, 'delete': basadelete,  'update': basaupdate})

    
    return render(request, 'center.html', {'group':group, 'magazine': magazine, 'basainfo': basainfo, 'username': username, 'item': item, 'insert': basainsert, 'delete': basadelete,  'update': basaupdate})



def export_xls(request):

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename={date}-product.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Товар')
 
    # Sheet header, first row
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['Артикул', 'Номер магазина', 'Номер отдела', 'Название', 'Тип', 'Количество', 'Цена' ]
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    maginfo = Shops.objects.get(заведующий=request.user.username)
    rows = Item_shop.objects.filter(номермагазина=maginfo.номер).values_list('артикул', 'номермагазина', 'номеротдела', 'название', 'тип', 'количество', 'цена')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
    return response



def export_xls_section(request):

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    response['Content-Disposition'] = 'attachment; filename={date}-product.xls'.format(
        date=datetime.now().strftime('%Y-%m-%d'),
    )

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Товар')
 
    # Sheet header, first row
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['Артикул', 'Номер отдела', 'Название', 'Тип', 'Количество', 'Цена' ]
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    
    section = Section_shop.objects.get(заведующий=request.user.username)
    rows = Item_shop.objects.filter(номеротдела=section.номеротдела, количество=0).values_list('артикул', 'номеротдела', 'название', 'тип', 'количество', 'цена')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
    return response