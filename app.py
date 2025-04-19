!pip install -q gradio
import gradio as gr


def sentence_builder(Casualties, Event, Location, Time, Situation_Report, Response):
    response_text = "Response is needed urgently." if not Response else "Response efforts in place."
    
    # Incorporate Time and Situation_Report into the output
    return f"""At {Time}, a {Event} occurred in {Location}, affecting approximately {Casualties} people. {Situation_Report}. {response_text}"""


iface = gr.Interface(
    sentence_builder,
    [
        gr.Slider(0, 500, label="Estimated Casualties"),
        gr.Dropdown(["Floods", "Earthquake", "Volcanic eruption", "Gun violence", "Landslides", "Fire"], label="Type of Event"),
        gr.Textbox(label="Location", placeholder="Enter the location"),
        gr.Textbox(label="Time of report", placeholder="Enter the time"),
        gr.Textbox(label="Observation", placeholder="What is the situation"),
        gr.Checkbox(label="Has response been deployed?"),
    ],
    "text",
    examples=[
        [0, "Volcanic eruption", "Sicily", "10:25pm", "Sightings of fires", False],
        [300, "Floods", "Mathare Primary School", "12:00 noon", "Water levels rising", False],
        [100, "Earthquake", "Salzburg near Taxham", "03:00am", "cracks on buildings", True],
    ],
)

iface.launch(pwa=True,share=True)