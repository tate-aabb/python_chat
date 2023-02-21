import openai

#Set up the OpenAI API client
openai.api_key = "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"

#this loop will allow us ask questions continuously
while True:
    #Set up the model and prompt
    model_engine = "text-davinci-003"
    prompt = input("Ask me a question: ")
    if 'exit' in prompt or 'quit' in prompt:
        break

    #Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1, stop=None,
        temperature=0.5)
    #Extracting usefull part of response
    response = completion.choices[0].text

    #Printing response
    print(response)