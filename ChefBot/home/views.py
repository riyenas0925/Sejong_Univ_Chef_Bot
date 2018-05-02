from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def keyboard(request):

        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['안녕','반가워']
                })

@csrf_exempt
def message(request):
        message = ((request.body).decode('utf-8'))
        return_json_str = json.loads(message)
        return_str = return_json_str['content']

        if return_str == '안녕':
            return JsonResponse({
                'message': {
                    'text': "안녕 버튼이 눌렸습니다. 테스트 메세지 입니다."
                }
            })
        
        if return_str == '반가워':
            return JsonResponse({
                'message': {
                    'text': "반가워 버튼이 눌렸습니다. 테스트 메세지 입니다."
                }
            })

