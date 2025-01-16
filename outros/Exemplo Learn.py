from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)
#setx OPENAI_API_KEY "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"
print(completion.choices[0].message)
