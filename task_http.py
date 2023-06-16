import requests

#
# url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
# request = requests.get(url).json()
# heroes_list = ['Hulk', 'Captain America', 'Thanos']
# int_hero_dict = {}
# for hero in heroes_list:
#     for heroes in request:
#         if heroes['name'] == hero:
#             int_hero_dict.update({hero: heroes['powerstats']['intelligence']})
# print(f'Самый интеллектуальный герой: {[k for k,v in int_hero_dict.items() if v == max(int_hero_dict.values())]}')
#
#


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path_to_file: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for path in path_to_file:
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            params = {'path': path}
            headers = {'Autorization': token}
            response = requests.get(url, params=params, headers=headers)
            url_for_upload = response.json().get('href', '')
            with open(path, 'rb') as f:
                requests.put(url_for_upload, files={'file': f})


file = ['jaguar.jpeg', 'leopard.jpg', 'lion.jpg']
if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = file
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


