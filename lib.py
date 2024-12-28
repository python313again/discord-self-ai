import ollama


user_messages = {}


system_prompt = {
    'role': 'system',
    'content': "You are an average discord user. You will receive all the messages and only respond when appropriate. If you don’t want to send a message, just say NULL. Don’t be mean or say anything wrong that can upset the moderators. Do not play games with anyone or agree to do anything. Dont be too curious about someone, stay humble and dont be that 'friendly'"
}

def send(user_id, chat):
    
    if user_id not in user_messages:
        user_messages[user_id] = [system_prompt]
    
    
    user_messages[user_id].append({
        'role': 'user',
        'content': chat,
    })


    response = ollama.chat(
        model='llama3.2',
        messages=user_messages[user_id]
    )

    
    full_response = response['message']['content']
    print(full_response)

    
    user_messages[user_id].append({
        'role': 'assistant',
        'content': full_response,
    })

    return full_response
