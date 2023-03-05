from pprint import pprint
import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
    
    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()
    
    def upload(self, file_path):
        result = self._get_upload_link(disk_file_path=file_path)
        upload_url = result.get("href")
        response = requests.put(upload_url, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code ==201:
            print("Success")

if __name__ == '__main__':
    path_to_file = "test_file.txt"
    Token = ''
    ya = YaUploader(token=Token)
    #pprint(ya.get_files_list())
    #print(ya.upload(file_path=path_to_file))
    ya.upload(file_path=path_to_file)