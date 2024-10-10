import openai

openai.api_key = 'your-api-key'

def generate_poem(theme, style, first_line):
    prompt = f"Write a {style} poem about {theme}. Start with: '{first_line}'" if first_line else f"Write a {style} poem about {theme}."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    return response.choices[0].text.strip()
