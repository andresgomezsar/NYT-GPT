# NYT-GPT
Program to search the New York Times using natural language

Note: To make this work you will need .json files in the parent directory for both the NYT API key and the Open AI key. I have added templates here (move them one directory up)

How it works:

- User inputs any search query they want for the NYT API using natural language. That query is preprocessed using the GPT-3 LLM to create the three main elements of the query for a basic search using the NYT API: keyword, begin_date, and end_date.

This novel way allows the user to query the New York Times using vague prompts such as:
 
  - Find articles about Bill Gates since Steve Ballmer took over as CEO of Microsoft: GPT is able to determine that the keyword here is Bill Gates, and that Steve Ballmer is a reference to the date, not the search itself. This type of query can lead to some inaccuracy in the dates (sometimes it is off by a a few days, or a month or two).
  
  - Find articles about Juan Manuel Santos since his reelection as president of Colombia, until the Peace Referendum. 
  
Of course, it can also handle more traditional searches with dates:

  - Find articles about Climate change from august 2015 to January 2018
  
  
Also very simple, short queries without actionable commands:

  - Climate change august 2015 jan 2018
  
After that, the user has the ability to see a dataframe with all the information sent back by The Times (unfortunately this excludes the full text but has byline and article summary). All the text is merged into one column that is then analyzed using Natural Language Processing (TextBlob package). The final output is a nice bar chart that shows sentiment both by article and by monthly averages.

NEXT:
- Incorporating spacy NLP for sentiment analysis
- Letting users query specific authors, sections of the NYT, and more


Enjoy!
