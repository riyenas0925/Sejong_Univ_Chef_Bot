from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
 
# Create your views here.
def keyboard(request):
    return JsonResponse(
        {
            'type' : 'buttons',
            'buttons' : ['학생회관','진관홀','우정당','군자관']
        }
    )

@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str=json.loads(message)
    return_str= return_json_str['content'] #버튼 항목중 무엇을 눌렀는가
    today_date = datetime.date.today().strtime("%m월 %d일")

    return JsonResponse({ #return 밑에는 공통어
        'message': {
            'text': today_date + '의' + return_str + '메뉴입니다\n' + get_menu(return_str)
        },
        'keyboard': {
            'type' : 'buttons',
            'buttons' : ['학생회관','진관홀','우정당','군자관']
        }
    })


def get_menu(cho):
    if cho == '학생회관':
        'message':{
            'text': '슨두부 3500'
        }
