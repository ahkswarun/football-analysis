from utils import read_video, save_video
from trackers import Tracker
import os

def main():
    # Read video
    video_frames = read_video('input/input.mp4')
    print(f"Total frames read: {len(video_frames)}")
    
    #initialize
    tracker=Tracker('best.pt')
    
    tracks=tracker.get_object_tracks(video_frames,read_from_stub=True,stub_path='stubs/track_stubs.pkl')
    
    # Draw output 
    ## Draw object Tracks
    output_video_frames = tracker.draw_annotations(video_frames, tracks)

    # Save video
    save_video(output_video_frames, 'output/output.avi')
    print("Video saved successfully!")

if __name__ == "__main__":
    main()
