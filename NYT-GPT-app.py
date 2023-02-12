from textblob import TextBlob
import requests, math, time
import csv, pathlib
import pandas as pd
import os
import openai
import json
import seaborn as sns
import json
import sys

print("This program uses an ML natural language model (GPT-3) to summarize and analyze articles in the NYT\nto summarize and do sentiment analysis on a given subject, person, or location (or any other keyword) over time")
print("\nYou can input your query using natural language like this: \nSearch all articles about Michael Jackson from 1990 to his death")
print("\nSearch all articles about Enron since its IPO up to its collapse")

print("\nNote: If you want detailed and accurate answers, it is better to include the dates in the query.")

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

#### OPEN AI GPT-3 API KEY ####
# Open the JSON file in read mode (OpenAI)
with open("../api_key.json", "r") as f:
    data = json.load(f)

# Get the API key from the JSON data
api_key = data["api_key"]

# Set the API key
openai.api_key = api_key



########

#### NYT API KEY ####
#Open the JSON files in read mode (NYT API Key)
with open("nyt_key.json", "r") as f:
    # Load the JSON data from the file
    data = json.load(f)
    # Get the API key from the JSON data
    nyt_key = data["api_key"]

# Set the API key
nyt_key = api_key

#### USER INPUT ####
query = str(input("Enter the search query: "))

#turning the response from natural language to variables that are readable by the NYT API
response_keyword = openai.Completion.create(
  model="text-davinci-003",
  prompt="Find the main keyword (a name, a location, etc) from this query and nothing else: " + query,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

keyword = response_keyword.choices[0].text

def remove_leading_trailing_spaces(obj):
    # Use the strip() method to remove leading and trailing spaces
    return obj.strip()

keyword = remove_leading_trailing_spaces(keyword)

response_date = openai.Completion.create(
  model="text-davinci-003",
  prompt="In number format, and adding no extra text tell me the year, month, day (YYYYMMDD) relevant to this query (there should be two dates, beggining and end separated by a single comma). If no indication of time in query, output NA. Years start on 0101 and end 1231. If no end date, add today's date: " + query,
  temperature=0.5,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

dates = response_date.choices[0].text

# Split the input string into a list of dates
dates = dates.split(",")

# Assign the first date to begin_date
begin_date = dates[0]

# Assign the second date to end_date
end_date = dates[1]

# We need to remove all spaces and non-numeric characters
begin_date = ''.join([c for c in begin_date if c.isdigit()])
end_date = ''.join([c for c in end_date if c.isdigit()])

print(begin_date)
print(end_date)
print(keyword)