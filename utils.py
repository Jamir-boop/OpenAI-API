import datetime


def log_completion(response, clean_spaces=1):
    response = ' '.join(str(response).strip().split('/n'))

    if clean_spaces == 1:
        response = response.replace(" ", "")

    log_str = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {response}/n"

    with open("response.log", "a") as f:
        f.write(log_str)


def local_logger(transcript):
    with open(f"local_response{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log", "a") as f:
        f.write(str(transcript))


def extract_audio(path_video, path_audio):
    import subprocess

    input_path = path_video
    output_path = path_audio
    subprocess.run(['ffmpeg', '-i', input_path, '-vn',
                   '-acodec', 'copy', output_path])

# extract_audio("C:/Users/Jeiser Vargas/Videos/2023-04-04_11-43-58.mkv", "C:/Users/Jeiser Vargas/Downloads/audio.m4a")