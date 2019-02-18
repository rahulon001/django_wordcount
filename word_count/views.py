# from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')


def count(request):
    data = request.GET['full_text_area']
    word_list = data.split()
    lenght_wordlist = len(word_list)
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
    sorted_list = sorted(word_dict.items(), key = operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'full_text':data, 'word_list':lenght_wordlist,
     'word_dict':sorted_list})

def about(request):
    return render(request,'about.html')
