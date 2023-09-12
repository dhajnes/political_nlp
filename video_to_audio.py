

from moviepy.editor import VideoFileClip
import os

# video = VideoFileClip("example.mp4")

audio_sources_path = "audio_sources/"
video_sources_path = "video_sources/"

audio_names = [os.path.splitext(file)[0] for file in os.listdir(audio_sources_path) if file.endswith('.mp3')]
video_names = [os.path.splitext(file)[0] for file in os.listdir(video_sources_path) if file.endswith('.mp4')]

for vid_name in video_names:
    if vid_name not in audio_names:
        vid = VideoFileClip(video_sources_path + vid_name + ".mp4")
        vid.audio.write_audiofile(audio_sources_path + vid_name + ".mp3")