from fastapi import FastAPI

## 1. fastAPI 앱 객체 생성
app = FastAPI()

## 2. get 요청: index page
@app.get('/')
def index():
    return 'welcome'

## 3. get 요청
@app.get('/info')
def info():
    return {'message': 'hello'}

## 4. get 요청: URL 경로 매개변수 사용
@app.get('/products/{id}')
def info_production(id: int):
    return f'상품번호: {id}'

## 5. get 요청: URL 경로 매개변수 사용
@app.get('/hello/{name}')
def greet_user_name(name: str):
    return {'name': f'Hello, {name}!'}

## 6. post 요청: JSON 데이터 받기
from pydantic import BaseModel

## BaseModel: Json 데이터 받을 때 구조 정의
class User(BaseModel):
    userName: str
    age: int

@app.post('/user')
def create_user(user:User):
    print('user:', user)
    print('userName:', user.userName)
    print('age:', user.age)
    return {
        'message': '사용자 정보가 등록되었습니다',
        'user_info': user
    }

## 상품 정보 저장
items = {}

## 사용자 모델 정의
## 상품 정보: 상품 번호(itemID), 상품명(itemName), 가격(price)
class Item(BaseModel):
    itemID: int
    itemName: str
    price: int

## Route: API
## 상품 등록
## 요청 URL: /item
## 요청 method: post
@app.post('/item')
def create_item(item: Item):
    print('item >>', item)
    items[item.itemID] = item.model_dump()
    return '[post] /item 처리됨'

## 전체 데이터 조회
## 저장된 모든 상품의 정보를 리턴: type list
## 요청 URL: /items
## 요청 method: get
@app.get('/items')
def get_items():
    return list(items.values())