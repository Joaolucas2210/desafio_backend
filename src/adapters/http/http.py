import httpx

class AsyncHttpClient:
    def __init__(self):
        self.client = httpx.AsyncClient(verify=False)

    async def get(self, url, params=None, headers=None):
        return await self.client.get(url, params=params, headers=headers)
