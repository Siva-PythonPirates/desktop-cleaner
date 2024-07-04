Desktop Cleaner 
================

Table of Contents 
--------------------

* [Overview](#overview)
* [Setup](#setup)
* [How it works](#how-it-works)
* [File types and destinations](#file-types-and-destinations)
* [Logging](#logging)
* [Troubleshooting](#troubleshooting)
* [License](#license)

Overview 
----------

The Desktop Cleaner is a Python script designed to organize files on your desktop by moving them to specific directories based on their file type. The script uses the `os` and `shutil` modules to interact with the file system and the `logging` module to log events.

Setup 
--------

To use the Desktop Cleaner, you need to:

1. Replace the `source_dir` variable with the path to the directory you want to clean.
2. Replace the `dest_dir_sfx`, `dest_dir_music`, `dest_dir_video`, `dest_dir_image`, and `dest_dir_documents` variables with the paths to the directories where you want to move the files.
3. Run the script.

How it works 
--------------

The script uses the `os.walk` function to traverse the source directory and its subdirectories. For each file found, it uses the `check_file_type` function to determine the file type based on its extension. The file is then moved to the corresponding destination directory using the `move_file` function.

File types and destinations 
-----------------------------

The script supports the following file types and their corresponding destinations:

* Images: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg` -> `dest_dir_image`
* Videos: `.mp4`, `.mov`, `.avi`, `.wmv`, `.flv`, `.mkv` -> `dest_dir_video`
* Audio files: `.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a` -> `dest_dir_music`
* Documents: `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.ppt`, `.pptx` -> `dest_dir_documents`
* Other files: all other files -> `dest_dir_sfx`

Logging 
---------

The script logs events to a file named `desktop_cleaner.log` in the root directory. The log file includes information about the files moved, including the source and destination paths, and any errors that occur during the moving process.

Troubleshooting 
-------------------

If you encounter any issues while running the script, check the log file for errors. You can also modify the script to add additional logging or debugging statements to help you troubleshoot the issue.

License 
---------

This script is licensed under the MIT License. You are free to use, modify, and distribute it as you see fit.

Contributing 
--------------

Contributions are welcome! If you'd like to contribute to the script, please fork the repository and submit a pull request.
