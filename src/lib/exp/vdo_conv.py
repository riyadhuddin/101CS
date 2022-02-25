# mp4 to webm video conversion
def vdo_conv(vdo_path, vdo_name):
    import os
    import subprocess
    # check if the file exists
    if os.path.isfile(vdo_path):
        # check if the file is a mp4 file
        if vdo_path.endswith(".mp4"):
            # create a new file name
            vdo_new_name = vdo_name + ".webm"
            # create a new file path
            vdo_new_path = os.path.join(os.path.dirname(vdo_path), vdo_new_name)
            # convert mp4 to webm
            subprocess.call(["ffmpeg", "-i", vdo_path, "-c:v", "libvpx", "-crf", "10", "-b:v", "1M", vdo_new_path])
            # check if the file exists
            if os.path.isfile(vdo_new_path):
                # remove the old file
                os.remove(vdo_path)
                # return the new file path
                return vdo_new_path
            # else
            else:
                # return the old file path
                return vdo_path
from os import startfile
# write main for vdo_conv
if __name__ == '__main__':
    # read video path
    vdo_path = "101CS/assets/video/vdo.mp4"
    # read video name
    vdo_name = 'vdo'
    # convert video
    vdo_new_path = vdo_conv(vdo_path, vdo_name)
    # print the new video path
    print(vdo_new_path)