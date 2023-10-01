# VideoLoudnessAnalyzer

The Video Loudness Analyzer is a Python script that analyzes video files (MP4 or MKV) and generates an interactive graph showing the loudness in decibels (dB) over time. You can use this tool to visualize the loud parts of a video and easily identify when the audio reaches a certain loudness threshold.

## Installation

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.

## Usage

1. Place your video files (MP4 or MKV) in the same directory as the script.
2. Open a terminal or command prompt and navigate to the directory containing the script and your video files.
3. Run the program using `python main.py`.
4. The program will process each video file and create an interactive loudness graph.

## Configuration

You can adjust the loudness threshold by modifying the loudness_threshold_dB variable in the script. By default, it is set to 0.1 dB, but you can change it to any desired value.
- loudness_threshold_dB = 0.1  # Adjust the threshold as needed

## Output

The script will create an HTML file for each video, displaying the interactive loudness graph. The HTML file will be named based on the input video's filename with "_loudness_graph.html" appended to it.

## Dependencies

- moviepy
- numpy
- plotly
