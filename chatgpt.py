#This is an Open AI Chatbot (GPT-3.5). Which can answer any question. 🤖

#You can ask anything as you wish.😀

# ⚠️ It may not work in some terminal if the answer is huge! So, ask any simple and short questions (Example: what is cat?) 

import os
os.system('pip install -qq openai')
print ("type your question :");
ask = input()

import openai

openai.api_key = "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"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{ask}"}])


print(f"""{ask}

{completion.choices[0].message.content}""")
