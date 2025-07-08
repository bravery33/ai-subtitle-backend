from datetime import datetime

print(datetime.now())

timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
file_name = f'subtitle-{timestamp}.srt'
print(timestamp)