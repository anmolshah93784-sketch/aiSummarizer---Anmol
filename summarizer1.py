from huggingface_hub import InferenceClient
HF_TOKEN = "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"

client = InferenceClient(api_key=HF_TOKEN)

def summarize_notes(My_notes):
    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {"role": "user", "content": f"You are a professor and you have to summarize the notes in bullet points:\n\n{My_notes}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    My_notes = input("Enter your notes: ")
    print("Hey buddy!\nYour summarised notes are below\nKeep learning...")
    
    Result = summarize_notes(My_notes)
    print(Result)
