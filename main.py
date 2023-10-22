import asyncio
from src.utils.env_config import EnvConfig
from src.infra.storage.storage import Storage
from src.adapters.http.http import AsyncHttpClient
from quart import Quart,request,jsonify
from termcolor import cprint

app = Quart(__name__)

@app.route('/title', methods=['GET'])
async def get_title():
    title_name = request.args.get('title')
    await asyncio.sleep(2)
    httpClient= AsyncHttpClient()
    url = EnvConfig.get('URL')
    api_key = EnvConfig.get('API_KEY')
    request_url = f"{url}?apikey={api_key}&t={title_name}"
    response = await httpClient.get(request_url)
    print(response.json())
    request_storage = Storage("./requestStorage.json")
    is_okay = await request_storage.insert(response.json())
    if not is_okay:
        return jsonify({"message":"Title already exists"})
    inserted_title = await request_storage.get(response.json()["imdbID"])
    return jsonify(inserted_title)

@app.route('/title/<string:id>', methods=['GET'])
async def add_favorites(id):
    request_storage = Storage("./requestStorage.json")
    local_storage = Storage("./local_storage.json")

    request_title = await request_storage.get(id)
    if request_title == None:
        return jsonify("Bad Request"), 400
    is_okay= await local_storage.insert(request_title)
    if not is_okay:
        return jsonify({"message":"Title already exists"})
    local_title = await local_storage.get(id)
    return jsonify(local_title)


@app.route('/favorites', methods=['GET'])
@app.route('/favorites/<string:title>', methods=['GET'])
async def list_titles(title=None):
    local_storage = Storage("./local_storage.json")
    if title:
        favorite = await local_storage.get(title)
        if not favorite:
            return jsonify({"message": "Title not found"}), 404
        return jsonify({"message": favorite})
    favorites = await local_storage.find_all()
    return jsonify({"message": favorites})




if __name__ == '__main__':
    print(EnvConfig.get('API_KEY'))
    #asyncio.run(main())
    app.run(host="localhost",port=8080)



