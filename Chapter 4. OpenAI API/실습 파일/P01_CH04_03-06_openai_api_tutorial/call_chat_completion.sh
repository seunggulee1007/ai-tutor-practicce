#!/usr/bin/env bash


curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "너는 감정분류를 수행한다. user의 텍스트의 감정이 긍정이면 positive, 부정적이면 negative를 출력한다."
      },
      {
        "role": "user",
        "content": "이 영화 너무 재미있다."
      }
    ]
  }'
