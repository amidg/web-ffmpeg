import os
import subprocess

# Directory containing the .ass files
input_directory = "/path/to/your/ass/files/"

# Output directory for the .srt files
output_directory = "/path/to/output/"

# Make sure the output directory exists, create it if not
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Iterate through all .ass files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".ass"):
        input_file = os.path.join(input_directory, filename)
        output_file = os.path.join(output_directory, os.path.splitext(filename)[0] + ".srt")

        # Run the ffmpeg command
        cmd = ["ffmpeg", "-i", input_file, "-c:s", "srt", output_file]

        try:
            subprocess.run(cmd, check=True)
            print(f"Converted {input_file} to {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {input_file}: {e}")

