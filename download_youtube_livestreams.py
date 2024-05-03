# HOW TO USE:
#
# 3 variables need to be specified:
# 1. url (to youtube video)
# 2. prefix (that you will be using for naming the folder and files of the downloaded video materials; recommend to include "date" in prefix)
#
# the `download_video` flag can be set to True if you want to download the video
#
# make sure to comment out other assignments to these variables if you're just leaving them in the script!

from chat_downloader import ChatDownloader
import os
import json
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import shutil

## todo: handle duplicates! (default is overwriting)
## todo: encode emojis as emoji characters osmehow

## IMPORTANT SETUP STEP: comment out the variables that you aren't using

download_video = False  # change to true if you want to download the video

# abc7
url = 'https://www.youtube.com/watch?v=v3bAl2VshnA'
prefix = 'abc7_2024-04-30.csv'

# fox11
# url= 'https://www.youtube.com/watch?v=Y8ZMvzS2nIg'
# prefix = 'fox11_2024-04-30'

# film the police
# url = 'https://www.youtube.com/watch?v=ZVEHoNAR9lo&t=10s'
# prefix = 'ftpla_2024-04-30'
# video_id = 'ZVEHoNAR9lo'

# 2024-05-01
# abc7
# url = 'https://www.youtube.com/watch?v=U37hA_jMJFg'
# prefix = 'abc7_2024-05-01'
# video_id = 'U37hA_jMJFg'

# film the police (part 1)
# url = 'https://www.youtube.com/watch?v=mSDL0CDl2RA'
# prefix = 'ftpla_part-1_2024-05-01'

# film the police (part 2)
# url = 'https://www.youtube.com/watch?v=UVUh6JdFAUk'
# prefix = 'ftpla_part-2_2024-05-01'

# make directory
# todo: check if exist
os.chdir(os.path.abspath(os.path.dirname( __file__ )))
if os.path.exists(prefix):
    shutil.rmtree(prefix, ignore_errors=True)    
os.mkdir(prefix)


# concatenate filenames
csv_filename = prefix + "\\" + prefix + "_chat.csv"
json_filename = prefix + "\\" + prefix + "_chat.json"
video_filename = prefix + "_video.mp4"

# download livestream chats (csv and json versions)
print('creating chat csv file...')
chat = ChatDownloader().get_chat(url)       # create a generator
messages = list()
for message in chat:
    messages.append(message)
    with open(csv_filename, 'a', encoding="utf-8") as csv_file:
        csv_file.write(message['time_text'] + ',' + message['author']['name'] + ',' + message['message'] + '\n')

print('creating chat json file...')
with open(json_filename, 'a') as output_file:
    json.dump(messages, output_file)

# download video
if download_video == True:
    print('downloading video...')
    yt = YouTube(url)
    yt.streams.filter(progressive=True).order_by('resolution').desc().first().download(output_path = prefix, filename = video_filename)    # filter streams and download highest resolution

print('done!')
# todo: transcription
# todo: save transcript; need to figure out caption disabled
# YouTubeTranscriptApi.get_transcript(video_id)
# with open(transcript_filename, 'w') as output_file:
#     json.dump(messages, output_file)