# blender-remote-stream

> This server and client allows one to stream a video over the network to a host running a Blender game engine. 

> **Applications** include integrating live video inside a game, live Virtual Reality applications, real-time game support

## Steps to get the setup working

1. Configure a ffmpeg server on the remote machine. For this, place the ffserver.conf file in the /etc/ directory of the remote machine. (ffmpeg must be installed first).
   
2. Start the server via the ffmpeg command specified in webcam.sh (run with superuser privileges on the remote machine). The server reads from /dev/video0 and serves it on the listening port.

3. The client machine has the Blender scene and script running. The address and port is specified in the script (127.0.0.1 and 8090 for the current test case)

## Current Issue

1. Video lag. Configuring ffmpeg server might solve this issue.