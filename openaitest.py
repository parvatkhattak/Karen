import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n\nDear [Boss Name],\n\nI am writing to inform you of my decision to resign from my position as [position] with [company], effective [date]. I am grateful for the opportunity you gave me and the experiences I gained in the last [duration of employment].\n\nI wish you and [company] nothing but the best.\n\nSincerely,\n[Your Name]"
    }
  ],
  "created": 1685827970,
  "id": "cmpl-7NT9eiVsRc6UMtoah4QJQktgvrkJz",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 81,
    "prompt_tokens": 9,
    "total_tokens": 90
  }
}

Process finished with exit code 0

'''