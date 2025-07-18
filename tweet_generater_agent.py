
# install required packages

# pip install google-generativeai --quiet
# pip install ipywidgets --quiet # create a beautiful UI

# ------------------------------------------------------------

# import libraries
import google.generativeai as genai 
import ipywidgets as widgets 
from IPython.display import display, Markdown
 

# Set up Gemini API 

API_KEY = "AIzaSyCDEbDm0bDAMYTi8uUvLWEPiWuLeHWDXkA"
genai.configure(api_key = API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# define the input form 

topic_input = widgets.Text(
    description = "Topic",
    layout = widgets.Layout(width = '400px')
)


tone_input = widgets.Dropdown(
    description = "Tone",
    options = ['Professional','Casual','Motivational','Informative'],
    layout = widgets.Layout(width = '400px')
)


audience_input = widgets.Text(
    description = "Audience",
    layout = widgets.Layout(width = '400px')
)

hashtag_input = widgets.Text(
    description = "Hashtags",
    layout = widgets.Layout(width = '400px')
)

submit_button = widgets.Button(
    description = "Generate Tweet",
    button_style = 'Success',
    tooltip = 'click to generate tweet',
    layout = widgets.Layout(width = '400px')
)

output = widgets.Output()

# Generate Tweet Function

def generate_tweet(b):
    Output.clear_output()
    prompt = f"""
    You are an expert Content Writer 
    generate a tweet about the topic "{topic_input.value}".
    use a tone {tone_input.value}.
    generate tweet for audience {audience_input.value}.
    Include the {hastag_input.value}.
    keep  it under 200 characters
    """.strip()

    with output:
        try:
            response = model.generate_content(prompt)
            tweet = response.text.strip()
            display(Markdown(f"### Generated Tweet : \n\n (tweet)"))
        except Exeption as e:
            print("Error: ",e) 



submit_button.on_click(generate_tweet)
        


# display the form 


form = widgets.VBox([
    widgets.HTML(value="<h3> Tweet Generator Agent</h3>"),
    topic_input,
    tone_input,
    audience_input,
    hashtag_input,
    submit_button,
    output
])


display(form)
