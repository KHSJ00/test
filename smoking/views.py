from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Borough, SmokingArea, SmokingAreaType, Fine
from django.views import generic


def fullopen(request):
    return render(request, 'smoking/fullopen.html')

def fullclose(request):
    return render(request, 'smoking/fullclose.html')

def littleopen(request):
    return render(request, 'smoking/littleopen.html')

def etc(request):
    return render(request, 'smoking/etc.html')

def boroughlist(request):
    return render(request, 'smoking/boroughlist.html')

def smokingmap(request):
    return render(request, 'smoking/map.html')

def location(request) :
    return render(request, 'smoking/location.html')

def cp_cd(request) :
    return render(request, 'smoking/cp_cd.html')

def graph(request) :
    return render(request, 'smoking/graph.html')

def graph_age(request) :
    return render(request, 'smoking/graph_age.html')

def graph_gender(request) :
    return render(request, 'smoking/graph_gender.html')

def graph_borough(request) :
    return render(request, 'smoking/graph_borough.html')

def graph_cigaretteprice(request) :
    return render(request, 'smoking/graph_cigaretteprice.html')

def graph_gender_age_amount(request) :
    return render(request, 'smoking/graph_gender_age_amount.html')

def direction(request) :
    return render(request, 'smoking/direction.html')

def gangnam_map(request) :
    return render(request, 'smoking/gangnam_map.html')

def gangdong_map(request) :
    return render(request, 'smoking/gangdong_map.html')

def gangbuk_map(request) :
    return render(request, 'smoking/gangbuk_map.html')

def gangseo_map(request) :
    return render(request, 'smoking/gangseo_map.html')

def gwanak_map(request) :
    return render(request, 'smoking/gwanak_map.html')

def gwangjin_map(request) :
    return render(request, 'smoking/gwangjin_map.html')

def guro_map(request) :
    return render(request, 'smoking/guro_map.html')

def geumcheon_map(request) :
    return render(request, 'smoking/geumcheon_map.html')

def nowon_map(request) :
    return render(request, 'smoking/nowon_map.html')

def dobong_map(request) :
    return render(request, 'smoking/dobong_map.html')

def dongdaemun_map(request) :
    return render(request, 'smoking/dongdaemun_map.html')

def dongjak_map(request) :
    return render(request, 'smoking/dongjak_map.html')

def dongdaemun_map(request) :
    return render(request, 'smoking/dongdaemun_map.html')

def mapo_map(request) :
    return render(request, 'smoking/mapo_map.html')

def seodaemun_map(request) :
    return render(request, 'smoking/seodaemun_map.html')

def seocho_map(request) :
    return render(request, 'smoking/seocho_map.html')

def seongdong_map(request) :
    return render(request, 'smoking/seongdong_map.html')

def seongbuk_map(request) :
    return render(request, 'smoking/seongbuk_map.html')

def songpa_map(request) :
    return render(request, 'smoking/songpa_map.html')

def yangcheon_map(request) :
    return render(request, 'smoking/yangcheon_map.html')

def yeongdeungpo_map(request) :
    return render(request, 'smoking/yeongdeungpo_map.html')

def yongsan_map(request) :
    return render(request, 'smoking/yongsan_map.html')

def eunpyeong_map(request) :
    return render(request, 'smoking/eunpyeong_map.html')

def jongro_map(request) :
    return render(request, 'smoking/jongro_map.html')

def jung_map(request) :
    return render(request, 'smoking/jung_map.html')

def jungrang_map(request) :
    return render(request, 'smoking/jungrang_map.html')

def test(request) :
    return render(request, 'smoking/test.html')

def cp_cd_2016(request) :
    return render(request, 'smoking/cp_cd_2016.html')

def cp_cd_2017(request) :
    return render(request, 'smoking/cp_cd_2017.html')

def cp_cd_2018(request) :
    return render(request, 'smoking/cp_cd_2018.html')

def cp_cd_2019(request) :
    return render(request, 'smoking/cp_cd_2019.html')

def cp_cd_2020(request) :
    return render(request, 'smoking/cp_cd_2020.html')


def complaint_crackdown(request) :
    return render(request, 'smoking/complaint_crackdown.html')
def complaint_crackdown_2016(request) :
    return render(request, 'smoking/complaint_crackdown_2016.html')
def complaint_crackdown_2017(request) :
    return render(request, 'smoking/complaint_crackdown_2017.html')
def complaint_crackdown_2018(request) :
    return render(request, 'smoking/complaint_crackdown_2018.html')
def complaint_crackdown_2019(request) :
    return render(request, 'smoking/complaint_crackdown_2019.html')
def complaint_crackdown_2020(request) :
    return render(request, 'smoking/complaint_crackdown_2020.html')


from django.views.generic import View
from django.shortcuts import render

class ChartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'smoking/cp_cd.html')