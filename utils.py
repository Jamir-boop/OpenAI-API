import datetime
import subprocess
import re
import os


def ensure_directory_exists(directory_path):
    """
    Ensure that a directory exists. If it doesn't, create it.

    Args:
    directory_path (str): Path to the directory.
    """
    if directory_path and not os.path.exists(directory_path):
        os.makedirs(directory_path)



def response_log(response, remove_spaces=False):
    """
    Log the response to a file with a timestamp.

    Args:
    response (str): The response to log.
    remove_spaces (bool): If True, remove spaces from the response.
    """
    response = ' '.join(str(response).strip().split('\n'))
    
    if remove_spaces:
        response = response.replace(" ", "")
    else:
        response = re.sub(r'\s+', ' ', response)    

    log_str = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {response}\n"
    log_file_path = "response.log"
    
    ensure_directory_exists(os.path.dirname(log_file_path))

    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(log_str)


def temp_log(transcript):
    """
    Log the transcript to a file with a timestamp in the filename.

    Args:
    transcript (str): The transcript to log.
    """
    log_directory = "logs"
    log_filename = f"{log_directory}/response{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    
    ensure_directory_exists(log_directory)

    with open(log_filename, "a", encoding="utf-8") as f:
        f.write(str(transcript))


def extract_audio(path_video, path_audio):
    """
    Extract audio from a video file using FFmpeg.

    Args:
    path_video (str): The path to the input video file.
    path_audio (str): The path to the output audio file.
    """
    subprocess.run(['ffmpeg', '-i', path_video, '-vn',
                   '-acodec', 'copy', path_audio])
