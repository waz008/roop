from typing import Literal
import gradio

Component = gradio.File or gradio.Image or gradio.Video
ComponentName = Literal[
    'source_file',
    'target_file',
    'reference_face_position_slider',
    'similar_face_distance_slider',
    'frame_processors_checkbox_group',
    'many_faces_checkbox'
]