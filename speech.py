# 导入必要的库
import edge_tts
import asyncio
import os
import openpyxl

# 读取excel表格的C、F列
wb = openpyxl.load_workbook('16h_it.xlsx')
sheet = wb.active
texts = []
for row in sheet.iter_rows(min_row=2):
    text = row[5].value
    print(text)
    filename = row[2].value
    if not text:  
      continue 
    texts.append({'text': text,'filename': filename})
print(texts)

# texts = [ {
#     'text': 'Il dispositivo si sta avviando, attendere prego.',
#     'filename': 'ai_asking.wav'
# }, ]

# voice = 'zh-CN-XiaoyiNeural'
voice = 'it-IT-ElsaNeural'
volume = '+100%'


async def get_speech(text, filename):
    tts = edge_tts.Communicate(text=text, voice=voice, volume=volume)
    await tts.save(filename)


async def main():
  # 创建speech文件夹
    os.makedirs('speech', exist_ok=True)
    tasks = []
    for text_dict in texts:
        filename_with_path = os.path.join('speech', text_dict['filename'])
        task = asyncio.create_task(
            get_speech(text_dict['text'], filename_with_path))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
