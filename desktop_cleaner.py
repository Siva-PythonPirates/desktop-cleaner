import os
import shutil
import logging

# Define the source directory and destination directories
source_dir = r"C:\Users\Sivashankar\Downloads"
dest_dir_sfx = r"C:\Users\Sivashankar\Music"
dest_dir_music = r"C:\Users\Sivashankar\Music"
dest_dir_video = r"C:\Users\Sivashankar\Videos"
dest_dir_image = r"C:\Users\Sivashankar\Pictures"
dest_dir_documents = r"C:\Users\Sivashankar\Documents"

# Define the file extensions for each type of file
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"]
video_extensions = [".mp4", ".mov", ".avi", ".wmv", ".flv", ".mkv"]
audio_extensions = [".mp3", ".wav", ".ogg", ".flac", ".m4a"]
document_extensions = [".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

# Set up the logging
logging.basicConfig(filename="desktop_cleaner.log", level=logging.INFO)

# Define the function to move files
def move_file(src, dst):
    try:
        shutil.move(src, dst)
        logging.info(f"Moved file: {src} to {dst}")
    except Exception as e:
        logging.error(f"Error moving file: {src} to {dst}: {str(e)}")

# Define the function to check the file type
def check_file_type(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in image_extensions:
        return dest_dir_image
    elif file_extension.lower() in video_extensions:
        return dest_dir_video
    elif file_extension.lower() in audio_extensions:
        return dest_dir_music
    elif file_extension.lower() in document_extensions:
        return dest_dir_documents
    else:
        return dest_dir_sfx

# Move the files
for root, dirs, files in os.walk(source_dir):
    for file in files:
        file_path = os.path.join(root, file)
        dest_dir = check_file_type(file_path)
        move_file(file_path, dest_dir)