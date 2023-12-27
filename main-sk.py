import semantic_kernel as sk
from semantic_kernel.connectors.ai import ChatRequestSettings, CompleteRequestSettings
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion, AzureChatCompletion, OpenAITextCompletion, OpenAIChatCompletion
# from semantic_kernel.connectors.ai.hugging_face import HuggingFaceTextCompletion
import asyncio
import os
from typing import AsyncIterable, Awaitable

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    # Configure OpenAI service
    # api_key, org_id = sk.openai_settings_from_dot_env()
    # oai_text_service = OpenAITextCompletion(ai_model_id="text-davinci-003", api_key=api_key, org_id=org_id)
    oai_chat_service = OpenAIChatCompletion(ai_model_id="gpt-3.5-turbo", api_key=api_key, org_id=org_id)


   
    chat_request_settings = ChatRequestSettings(
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5,
    )
    role = "system"
    content = "You are an AI assistant that helps people find information."
    message = { "role":role, "content":content }
    stream = oai_chat_service.complete_chat_stream_async(messages=[message], settings=chat_request_settings)
    async for text in stream:
        print(text, end = "") # end = "" to avoid newlines



if __name__ == "__main__":
    import asyncio

    asyncio.run(main())



