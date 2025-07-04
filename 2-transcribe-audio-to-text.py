""" 


"""
## whisper 모델 불러오기
import whisper
import os
import json
from config import AUDIO_FILE, SUBTITLE_DIR, SUBTITLE_FILE, SUBTITLE_JSON_FILE

## tiny, base, small, medium, large
print('1. 모델 불러오기')
model = whisper.load_model('small')

## 오디오 파일을 텍스트로 변환
print('2.1 오디오 -> 텍스트 변환 전')
# audio_path = './source/audio/test.wav'
result = model.transcribe(AUDIO_FILE)
print('2.2 오디오 -> 텍스트 변환 후: 완료')

## 변환된 텍스트 출력
print('3. 변환된 텍스트 출력')
print(result)

## 텍스트를 파일로 저장
print('4.1. subtitle 폴더 생성 시작')
# output_dir = './source/subtitle'
os.makedirs(SUBTITLE_DIR, exist_ok=True)
print('4.2. subtitle 폴더 생성 완료')

print('5.1. 파일 경로 생성 시작')
# output_path = os.path.join(output_dir, 'test.txt') 
# output_path_json = os.path.join(output_dir, 'test.json') 
print('5.2. 파일 경로 생성 완료')

print('6.1. text, segments 를 파일로 저장 시작')
with open(SUBTITLE_FILE, 'w', encoding='utf-8') as file:
    file.write(result['text'])
with open(SUBTITLE_JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(result['segments'], f, indent=2, ensure_ascii=False)
print('6.2. 텍스트를 파일로 저장 종료')