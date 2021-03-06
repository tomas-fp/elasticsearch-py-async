import asyncio
from elasticsearch_async import AsyncElasticsearch

client = AsyncElasticsearch(hosts=['localhost'])

async def print_info():
    info = await client.info()
    print(info)

loop = asyncio.get_event_loop()
loop.run_until_complete(print_info())
loop.close()
client.transport.close()
