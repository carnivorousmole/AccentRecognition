import os
import shutil


def delete_empty_subdirs(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                shutil.rmtree(dir_path)
                parent_dir = os.path.dirname(dir_path)
                while parent_dir != directory:
                    if not os.listdir(parent_dir):
                        shutil.rmtree(parent_dir)
                        parent_dir = os.path.dirname(parent_dir)
                    else:
                        break

def delete_subdirs_with_one_underscore(directory):
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path) and subdir.count("_") == 1:
            shutil.rmtree(subdir_path)


def delete_subdirs_without_underscore(directory):
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path) and "_" not in subdir:
            shutil.rmtree(subdir_path)

def merge_directories(source_dir, target_dir):
    dirs_to_merge = [os.path.join(source_dir, name) for name in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, name))]
    for dir1 in dirs_to_merge:
        for subdir in os.listdir(dir1):
            subdir_path = os.path.join(dir1, subdir)
            if os.path.isdir(subdir_path):
                if os.path.isdir(os.path.join(target_dir, subdir)):
                    merge_directories(subdir_path, os.path.join(target_dir, subdir))
                else:
                    shutil.move(subdir_path, target_dir)
            else:
                if not os.path.isfile(os.path.join(target_dir, subdir)):
                    shutil.move(subdir_path, target_dir)

# source_dir = "/Users/dylanwalsh/Code/input/audio_files"
# target_dir = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split_reorganized"
# merge_directories(source_dir, target_dir)

delete_empty_dir = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split_regrouped"
delete_empty_subdirs(delete_empty_dir)

delete_subdirs_without_underscore_dir = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split_regrouped"
delete_subdirs_without_underscore(delete_subdirs_without_underscore_dir)
delete_subdirs_with_one_underscore(delete_subdirs_without_underscore_dir)