from groq import Groq

client = Groq(
    api_key="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",
)
while True:
    me= input("Me: ")
    
    if me =="exit" or me =="bye":
        break
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": me,
            }
        ],
        model="llama3-8b-8192",
    )

    print("Ans: ",chat_completion.choices[0].message.content)
    print("--------------------------------")