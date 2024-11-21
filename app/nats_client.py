import asyncio
from typing import Any
from django.conf import settings

from nats.aio.client import Client

nats_client: Client = Client()

async def connect_to_nats():
    await nats_client.connect(servers=[settings.NATS_URL])

def publish_message(subject: str, message: Any):
    asyncio.run(nats_client.publish(subject, message.encode()))