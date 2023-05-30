import os
import imghdr
import shutil
import time
import glob
import datetime

URL = r'C:\Users\user\AppData\Local\osu!\Songs'
CLEAN = ['osb', 'mp4', 'avi', 'flv', 'm4v']
CLEAN_MUSIC = ['ogg', 'wav']

def search_all_files_return_by_time_reversed(path, reverse=True):
  return sorted(glob.glob(os.path.join(path, '*')), key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))), reverse=reverse)

for file_full_path in search_all_files_return_by_time_reversed(URL):
    file = file_full_path.split('\\')[-1]
    is_get_mp3_file = 0
    music_list = []
    photo_list = []
    for data in os.listdir(file_full_path):
        data_path = file_full_path + '\\' + data
        data_end = data.split('.')[-1]
        if data_end == 'osu':
            continue
        elif data_end in CLEAN:
            print(data_path, '删除')
            os.remove(data_path)
        elif os.path.isdir(data_path):
            print(data_path, '删除文件夹')
            shutil.rmtree(data_path)
        elif data_end.lower() == 'mp3':
            is_get_mp3_file += 1
        elif data_end in CLEAN_MUSIC:
            music_list.append(data_path)
        elif imghdr.what(data_path) or data_end == 'jpg':
            photo_list.append(data_path)
        else:
            print(data_path, '其他格式')
    if is_get_mp3_file:
        for music in music_list:
            print(music, '删除音乐')
            os.remove(music)
    elif music_list:
        ogg_num = 0
        wav_num = 0
        for music in music_list:
            print(music, '没mp3')
            if music.split('.')[-1] == 'ogg':
                ogg_num += 1
            elif music.split('.')[-1] == 'wav':
                wav_num += 1
        rm_end = ''
        if ogg_num == 1 and wav_num > 1:
            rm_end = 'ogg'
        elif ogg_num > 1 and wav_num == 1:
            rm_end = 'wav'
        if rm_end:
            for music in music_list:
                print(music, '删除音乐')
                os.remove(music)
        elif len(music_list) > 1:
            os.startfile(file_full_path)
            time.sleep(10)
    if len(photo_list) > 1:
        if datetime.datetime.fromtimestamp(os.path.getmtime(photo_list[0])).date() != datetime.datetime.now().date():
            continue
        for photo in photo_list:
            print(photo, '多张图片')
        os.startfile(file_full_path)
        time.sleep(10)
    if is_get_mp3_file > 1:
        print(file, '多个MP3')
        os.startfile(file_full_path)
        time.sleep(10)