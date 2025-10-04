from os import getenv
import google.generativeai as genai


def get_llm():
    genai.configure(api_key=getenv('GOOGLE_API_KEY'))
    return genai.GenerativeModel('gemini-2.5-flash')

def generate_response(llm_model,query_type, query=None, image=None,audio_file=None):
    if(query_type == 'Text' and query is not None):
      return llm_model.generate_content(query).text
    if(query_type == 'Image' and image is not None):
        text_prompt = 'describe the image in two lines'
        return llm_model.generate_content([text_prompt,image]).text
    if(query_type == 'Audio'and audio_file is not None):
          audio_file= genai.upload_file(path=audio_file)
          prompt='Create a Transcript of the auido file.'
          return llm_model.generate_content([prompt, audio_file]).text
    else:
        return "Please provide a valid input"
