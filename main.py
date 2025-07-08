import os
from datetime import datetime, timedelta

import whisper
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

## 디렉토리 생성
## 동영상이 저장되는 폴더: uploads
## srt 파일이 저장되는 폴더: output
UPLOAD_DIR = './uploads'
OUTPUT_DIR = './output'

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

## whisper 모델 로드
model = whisper.load_model('small')

## FastAPI app 생성
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 프론트엔드 주소
    allow_credentials=True,
    allow_methods=["*"],                      # 모든 HTTP 메서드 허용
    allow_headers=["*"],                      # 모든 헤더 허용
)

@app.get('/')
def index():
    return '환영합니다.'

def format_time(seconds):
    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600) // 60)
    seconds = int(td.total_seconds() % 60)
    milliseconds = int((td.total_seconds() % 1) * 1000)

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}'

## 요청 URL: /create_subtitled_video
## 요청 method: post
## return: '요청 처리됨'

@app.post('/create_subtitled_video')
async def create_subtitled_video(file: UploadFile = File(...)):
    print('\n==비디오 처리 시작==')

    ## video 파일명 저장
    ## temp_video_20250707_1720.mp4
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    temp_video_path = os.path.join(UPLOAD_DIR, f'temp_video_{timestamp}.mp4')
    
    ## 업로드 영상 저장
    contents = await file.read()
    with open(temp_video_path, 'wb')as file:
        file.write(contents)

    result = model.transcribe(temp_video_path)

    segments = result['segments']

    ## srt 파일: 파일명 지정
    srt_filename = f'subtitle_{timestamp}.srt'
    srt_path = os.path.join(OUTPUT_DIR, srt_filename)

    with open(srt_path, 'w', encoding='utf-8') as file:
        for i, seg in enumerate(segments, 1):
            start = format_time(seg['start'])
            end = format_time(seg['end'])
            text = seg['text'].strip()
            file.write(f'{i}\n')
            file.write(f'{start} --> {end}\n')
            file.write(f'{text}\n\n')

    return {
    "srt": [
        {
            "index": i,
            "start": format_time(seg['start']),
            "end": format_time(seg['end']),
            "text": seg['text'].strip()
        } for i, seg in enumerate(segments, 1)
    ]
}
