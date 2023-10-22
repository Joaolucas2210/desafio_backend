import json


class Storage:
    def __init__(self,file_path):
        self.path = file_path

    async def save(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f)

    async def insert(self, data):
        print(data)
        insert_data = {
            "imdbID": data["imdbID"],
            "Title": data["Title"],
            "Year": data["Year"],
            "Plot": data["Plot"],
            "imdbRating": data["imdbRating"],
            "Director": data["Director"],
        }
        res = await self.get(insert_data["imdbID"])
        if res:
            return False

        storage = await self.load()
        storage["data"].append(insert_data)
        await self.save(storage)
        return True

    async def update(self, id, key, value):
        storage= await self.load()
        for item in storage["data"]:
            if item["imdbID"] == id:
                item[key] = value
        await self.save(storage)

    async def get(self, id):
        storage= await self.load()
        for item in storage["data"]:
            if item["imdbID"] == id:
                return item


    async def load(self):
        with open(self.path, 'r') as f:
            return json.load(f)

    async def find_by_title(self, title: str):
        storage = await self.load()
        results = []
        for item in storage["data"]:
            if title in item["Titles"]:
                results.append(item)
        return results

    async def find_all(self):
        storage = await self.load()
        return storage["data"]
