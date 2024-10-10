# AI-Generated Poetry Assistant

## Project Overview
The **AI-Generated Poetry Assistant** is an interactive web application that uses **OpenAI GPT-3** to generate poems. Users can input a theme, select a poetry style (e.g., haiku, sonnet, free verse), and either get a fresh poem or complete an unfinished one with AI assistance. This project demonstrates the use of generative AI in a creative context.

## Features
- **Keyword-based poem generation**: Users provide a theme, and the AI generates poetry based on that input.
- **Style selection**: Choose from different poetry styles such as Haiku, Sonnet, or Free Verse.
- **Line continuation**: Start with an opening line, and the AI will complete the rest of the poem.
- **Interactive editing**: Regenerate or modify specific lines based on the AI's suggestions.


## Prerequisites

To run this project, you need the following:
- **Python 3.x** installed.
- An OpenAI account with an API key. You can sign up and get your key at [OpenAI](https://beta.openai.com/signup/).

## Installation and Setup
Below provides information on how to setup the project

### Clone the Repository
Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/AI-Generated-Poetry-Assistant.git
    cd AI-Generated-Poetry-Assistant

### Install the Dependencies using PIP
    pip install -r requirements.txt

### Set Up Your OpenAI API Key
1. Open poetry_generator.py.
2. Replace 'your-api-key' with your actual OpenAI API key:
    ```python
    openai.api_key = 'your-api-key'

### Run the Application
After the first 3 steps, we are now able to run the Flask application
    ```bash
    python app.py

### Access the Application
Open your browser and go to http://127.0.0.1:5000/. You’ll see a simple interface where you can input a theme, select the style of the poem, and provide the first line for the poem (optional).


## Usage
1. Enter a theme or keyword (e.g., "love", "nature", "adventure").
2. Select the style (Haiku, Sonnet, or Free Verse).
3. Optionally, provide a first line to have the AI complete your poem.
4. Click Generate Poem to see the AI’s creation.
5. If you want to refine or regenerate, simply adjust the input and submit again.

## Example
Inputs :
theme: nature
style: Haiku
First line: the sun sets

## License
This project is licensed under the MIT License - see the LICENSE file for details.





