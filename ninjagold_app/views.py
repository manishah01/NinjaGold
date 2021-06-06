from django.shortcuts import render, redirect
import random 
from time import gmtime, strftime

def index(request):
    if  "total_gold" not in request.session or "activities" not in request.session:
        request.session['total_gold'] = 0
        request.session['activities']= []
    context = {
        'activities': request.session['activities']
    }
    return render(request, 'ninja.html',context)

def process_money(request):
    if request.method == 'POST':  
        my_gold = request.session['total_gold']
        activities = request.session['activities']
        building_type = request.POST['type']

        if building_type == 'farm':
            gold_earned = round(random.randint(10,20))
            my_gold += gold_earned
        elif building_type == 'cave':
            gold_earned = round(random.randint(5,10))
            my_gold += gold_earned
        elif building_type == 'house':
            gold_earned = round(random.randint(2,5))
            my_gold += gold_earned
        else: 
            building_type == 'casino'
            gold_earned = round(random.randint(1,50))
            if gold_earned % 3:
                    my_gold -= gold_earned
            else:
                my_gold += gold_earned
        
        request.session['total_gold'] = my_gold
        date = strftime("on %Y-%m-%d, at %H:%M %p", gmtime())
        
        if building_type == 'casino':
            if gold_earned % 3:
                statement = f"OH NO! you lost {gold_earned} gold from the {building_type}, Boo! ({date})"
            else:
                statement = f"Awesome! you have earned {gold_earned} gold from the {building_type} ({date})"
        else: 
            statement = f"Awesome! you have earned {gold_earned} gold from the {building_type} ({date})"
        
        activities.insert(0, statement)
        request.session['activities'] = activities
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/process_money')