import moviepy.editor as mp
import numpy as np
import plotly.graph_objs as go
import os

def calculate_loudness(audio):
    # Root mean square (RMS) amplitude
    rms = np.sqrt(np.mean(np.square(audio)))
    return rms

def create_loudness_graph(video_file):
    # Load the video file
    video = mp.VideoFileClip(video_file)

    frame_rate = video.fps
    duration = video.duration
    frame_loudness = []
    timestamps = []

    for t in np.arange(0, duration, 1/frame_rate):
        audio = video.audio.subclip(t, t+1/frame_rate)
        loudness = calculate_loudness(audio.to_soundarray())
        frame_loudness.append(loudness)
        timestamps.append(t)

    loudness_trace = go.Scatter(x=timestamps, y=frame_loudness, mode='lines', name='Loudness')
    
    loudness_threshold = 0.1 # Adjust the threshold as needed
    loud_segments = [t for t, loud in zip(timestamps, frame_loudness) if loud > loudness_threshold]
    
    loud_segments_trace = go.Scatter(
        x=loud_segments,
        y=[0] * len(loud_segments),
        mode='markers+text',
        name='Loud Parts',
        text=[f'Time: {round(t, 2)}s' for t in loud_segments],
        textposition='top center',
        marker=dict(size=8, color='red')
    )

    layout = go.Layout(
        title='Loudness Over Time',
        xaxis=dict(title='Time (seconds)'),
        yaxis=dict(title='Loudness'),
        showlegend=True
    )

    fig = go.Figure(data=[loudness_trace, loud_segments_trace], layout=layout)

    # Save the graph as an HTML file
    output_filename = os.path.splitext(os.path.basename(video_file))[0] + '_loudness_graph.html'
    fig.write_html(output_filename)

    # Display the interactive graph
    fig.show()

if __name__ == "__main__":
    input_files = ["video.mkv", "video.mp4"]
    
    for video_file in input_files:
        if os.path.isfile(video_file):
            create_loudness_graph(video_file)
        else:
            print(f"File not found: {video_file}")
