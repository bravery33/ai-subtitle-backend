import os
from datetime import datetime, timedelta

import whisper

from config import SUBTITLE_DIR, VIDEO_FILE


## 기존 작업(1~3) 한 파일로 만들기
def format_time(seconds):
    td = timedelta(seconds=seconds)
    hours = int(td.total_seconds() // 3600)
    minutes = int((td.total_seconds() % 3600) // 60)
    seconds = int(td.total_seconds() % 60)
    milliseconds = int((td.total_seconds() % 1) * 1000)

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}'

def generate_srt_from_video(input_video_path, subtitle_dir):
    ## 1. 영상 -> segment
    print('\n\n1. 영상 -> Whisper로 텍스트 변환(segments 포함)')

    # 모델 생성
    model = whisper.load_model('small')

    # 텍스트 변환
    result = model.transcribe(input_video_path)

    # segments만 저장
    segments = result['segments']

    ## 2. segment -> srt 저장
    print('\n\n2. segments -> srt 저장')
    ## srt 파일: 고유한 파일명 지정
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    subtitle_srt_path = os.path.join(subtitle_dir, f'subtitle_{timestamp}.srt')

    with open(subtitle_srt_path, 'w', encoding='utf-8') as file:
        for i, seg in enumerate(segments, 1):
            start = format_time(seg['start'])
            end = format_time(seg['end'])
            text = seg['text'].strip()
            file.write(f'{i}\n')
            file.write(f'{start} --> {end}\n')
            file.write(f'{text}\n\n')

        print(f'3. [srt 생성] 완료 -> {subtitle_srt_path}')

    return subtitle_srt_path

## 함수 호출
if __name__ == '__main__':
    print('VIDEO_FILE >>', VIDEO_FILE)
    print('SUBTITLE_SRT_FILE >>', SUBTITLE_DIR)
    generate_srt_from_video(VIDEO_FILE, SUBTITLE_DIR)