# NYT-GPT
"We can try to understand the New York Times effect on man." - The Bee Gees.


Let's search the New York Times using natural language!

## Prerequisites
You will need .json files containing the API keys for the New York Times and OpenAI in the parent directory. Templates for these files are included in the repository.

## Installation
Clone the repository to your local machine:
git clone https://github.com/andresgomezsar/NYT-GPT.git

Install the required packages using `pip` (requirements.txt file in repo):
pip install -r requirements.txt

## How it works
NYT-GPT allows users to search the New York Times using natural language prompts. The program preprocesses the user's input using GPT-3's Language Model to extract the three main elements of a basic search query for the New York Times API: keyword, begin_date, and end_date.

This novel approach enables users to make vague and complex searches, such as:

- "Find articles about Bill Gates since Steve Ballmer took over as CEO of Microsoft."
- "Find articles about Juan Manuel Santos since his reelection as president of Colombia, until the Peace Referendum."

It can also handle simple and straightforward searches, such as:

- "Climate change August 2015 January 2018."

After the search is performed, the program returns a dataframe with information from the New York Times API, including the byline and article summary. This data is then analyzed using Natural Language Processing (via the TextBlob package) to determine the overall sentiment of each article. The results are displayed as a bar chart that shows sentiment both by article and by monthly averages.

## Usage
Input your natural language query in the program.
The program will preprocess the query and perform the search.
The results will be displayed in a bar chart, showing the sentiment of each article and the monthly average sentiment.

## Limitations
- The accuracy of the date extraction may not always be perfect and may be off by a few days or months.
- The full text of the articles is not included in the results due to limitations imposed by the New York Times API.
- TextBlob package was trained on movie review data, which tends to overestimate negativity of the news articles (more nuanced language).

## Contributing
We welcome contributions to the development of this program! You can contribute by:

- Reporting bugs and suggesting new features.
- Submitting pull requests with bug fixes or new features.

Note: To make this work you will need .json files in the parent directory for both the NYT API key and the Open AI key. I have added templates here (move them one directory up)

## Future Development
- Incorporating spaCy NLP for sentiment analysis.
- Allowing users to search for specific authors, sections of the New York Times, and more.
- Implementing algorithm to filter unrelated articles pulled by the NYT API
- Generating text-based summaries and answers to questions about the articles in the query

Enjoy!

## Example Outputs:
![Sentiment Graph](https://github.com/andresgomezsar/NYT-GPT/blob/main/NYT_GPT_Output1.jpg?raw=true)

![Sentiment Graph](https://github.com/andresgomezsar/NYT-GPT/blob/main/NYT_GPT_Output2.jpg?raw=true)


## Licensing
The code in this repository is licensed under the MIT License, which is a permissive open-source software license that allows you to use, modify, and distribute the software for both commercial and non-commercial purposes, as long as you include a copy of the license in your own project and give credit to the original authors. By using or modifying this code, you agree to comply with the terms of the license.

To get started, simply clone this repository and follow the instructions in this readme file to set up and run the project. If you encounter any issues or have any questions, please contact me.

I welcome contributions to this project! If you would like to contribute code, documentation, or other improvements, please fork this repository and submit a pull request with your changes. By contributing to this project, you agree to license your contributions under the MIT License, and to give credit to the original authors.

Thank you for your interest in this project, and I hope that you find it useful and informative!


