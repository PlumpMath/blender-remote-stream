import bge

# get the controller the script is attached to
cont = bge.logic.getCurrentController()
obj = cont.owner
# get the reference pointer (ID) of the internal texture
print("====start")

# set up ffmpeg/icecast/vlc on the server side and read here. 
# Frame rate and all can be adjusted. ffmpeg is optimized for this.
# Blender natively supports ffmpeg
def main():
    print('refresh')
    if not hasattr(bge.logic, 'video'):
        ID = bge.texture.materialID(obj, 'IMgsoc.jpg')
        bge.logic.video = bge.texture.Texture(obj, ID)
        # a ffmpeg server is serving on the port 8090, Blender reads the stream
        # from the mjpeg file
        bge.logic.video.source = bge.texture.VideoFFmpeg('http://127.0.0.1:8090/webcam.mjpeg')
        bge.logic.video.source.play()
    bge.logic.video.refresh(True)

     
    
print("====end")
