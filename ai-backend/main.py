import openai
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# OpenAI API 설정
openai.api_key = "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"

# 네이버 API 설정
URL = "https://openapi.naver.com/v1/search/encyc.json"
NAVERAPIKEY = { "X-Naver-Client-Id": "rUgonfL9PeB980TGm6Lr",
                "X-Naver-Client-Secret": "1m9f9uPZ1i"}

async def get_search_info(query):
    params = {'query': query, 'display': 1}

    headers = NAVERAPIKEY
    response = requests.get(URL, params=params, headers=headers)

    if response.status_code != 200:
        return None
    
    return response.json()

async def naver_local_search(query, display):
    # 네이버 애플리케이션의 client_id와 client_secret 키 설정
    headers = NAVERAPIKEY

    # 지역 검색 요청 파라미터 설정
    params = {
        "sort" : "comment",
        "query" : query,
        "display" : display
    }

    # 지역 검색 URL과 요청 파라미터
    naver_local_url = "https://openapi.naver.com/v1/search/local.json"

    # 지역 검색 요청
    response = requests.get(naver_local_url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    # 지역 검색 결과 확인
    return response.json().get('items')

async def get_foods_list(disease, allergy, vegan):
    # 사용자의 질병, 알레르기, 비건 여부에 따라 음식 리스트 반환 코드
    # 예를 들어, 비건이면 비건 식단을, 알레르기가 있다면 알레르기에 주의해야 하는 식단을 추천할 수 있습니다.

@app.route('/api/ai/recommend_food', methods=['POST'])
async def recommend_food():
    request_data = request.get_json()

    user_location = request_data.get('user_location')
    user_disease = request_data.get('user_disease')
    user_allergy = request_data.get('user_allergy')
    user_vegan = request_data.get('user_vegan')
    food_name = request_data.get('food_name')

    food_info = get_search_info(food_name)

    if food_info is None:
        response_data = {
            'recommended_foods': [],
            'unavailable_foods': [],
            'error': '음식 정보를 가져오지 못했습니다.'
        }

        return jsonify(response_data)
    
    # 네이버 API에서 음식 정보를 받아와서 활용
    # 예를 들어, 음식의 칼로리, 성분 정보 등을 추출

    recommended_foods = []  # 추천 가능한 음식 리스트
    unavailable_foods = []  # 먹을 수 없는 음식 리스트

    # OpenAI API 호출을 통해 음식 추천
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You will be presented with food names and your job is to provide a set of tags. Provide your answer in bullet point form.\nAnd if specific person can't eat provided food, tell me who can't eat due to allergy or disease\nDepending on whether the user is vegan or not, please determine whether he can eat or not and print it out as a tag:"
            },
            {
                "role": "user",
                "content": f"Disease: {user_disease}\nAllergy: {user_allergy}\nVegan: {user_vegan}"
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    recommended_foods.append(completion.choices[0].message.content)  # OpenAI에서 받은 음식을 추가

    response_data = {
        'recommended_foods': recommended_foods,
        'unavailable_foods': unavailable_foods,
        'error': None
    }

    # 음식 정보 출력
    print("음식 정보:", food_info)
    # OpenAI 응답 출력
    print("OpenAI 응답:", recommended_foods)

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
