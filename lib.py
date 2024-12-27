import ollama

messages = []


system_prompt = {
    'role': 'system',
    'content': 'You are an average discord user. I want you to act like one and do not use perfect grammar (just act like a normal person typing regularly with slang). You will recieve all the messages and only respond when appropriate. If you dont want to send a message, than just say NULL'
}

messages.append(system_prompt)

def send(chat):
    messages.append(
        {
            'role': 'user',
            'content': chat,
        }
    )
    

    response = ollama.chat(model='llama3.2', 
                           messages=messages)


    full_response = response['message']['content']
    

    messages.append(
        {
            'role': 'assistant',
            'content': full_response,
        }
    )

    
    return full_response


