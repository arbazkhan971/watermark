from moviepy.editor import *

# Define the paths of the input and output files
input_path = "y2mate.com - What does Enqurious do_1080p.mp4"
output_path = "output.mp4"

# Load the video clip
clip = VideoFileClip(input_path)
imgg = "mentorskool.png"
# Load the watermark image
watermark = ImageClip(imgg)

# Set the position of the watermark
position = "center"

# Set the duration of the watermark clip
watermark_duration = clip.duration

# Set the opacity of the watermark
opacity = 0.5

# Add the watermark to the video clip
watermarked_clip = CompositeVideoClip([clip, watermark.set_duration(watermark_duration).set_opacity(opacity).set_position(position)])

# Write the watermarked video to the output file
watermarked_clip.write_videofile(output_path)
