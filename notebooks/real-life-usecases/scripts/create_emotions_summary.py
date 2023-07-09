"""
This script takes all the songs we have and use the lyric to create a list of 8 emotions we then use to replace the lyric itself.
This is needed to properly match user's emotions to the songs.
"""

import json
from collections import defaultdict
from pathlib import Path
from langchain.chains import LLMChain
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
import openai
import os
from dotenv import load_dotenv, find_dotenv
from openai.error import InvalidRequestError

_ = load_dotenv(find_dotenv())
openai.api_type = os.environ.get("OPENAI_API_TYPE")
openai.api_base = os.environ.get("OPENAI_API_BASE")
openai.api_version = os.environ.get("OPENAI_API_VERSION")
openai.api_key = os.environ.get("OPENAI_API_KEY")

prompt = PromptTemplate(
    input_variables=["song", "delimeter"],
    template="""\
I am building a retrieval system. Given the following song lyric
{delimeter}{song}{delimeter}
You are tasked to produce a list of 8 emotions that I will later use to retrieve the song. 
Please provide only a list of comma separated emotions.\
""",
)

llm = AzureChatOpenAI(deployment_name="gpt4", temperature=0.7)

chain = LLMChain(llm=llm, prompt=prompt)

temp_folder = Path(os.path.dirname(__file__)).parent.parent.parent / "temp"

with open(temp_folder / "lyrics_with_spotify_url.json", "r") as f:
    data = json.load(f)

new_data = defaultdict(list)

for movie, songs in data.items():
    for song in songs:
        try:
            emotions = chain.run(song=song["text"], delimeter="---")
        except InvalidRequestError:
            print(f"> Skipping '{song['name']}' due to invalid request error")
            continue
        print(f"{song['name']}: {emotions}")
        new_data[movie].append(
            {"name": song["name"], "text": emotions, "embed_url": song["embed_url"]}
        )


with open(temp_folder / "emotions_with_spotify_url.json", "w") as f:
    json.dump(new_data, f)
