import urllib.request
import urllib.parse

import json
import shutil


class Api:
    def __init__(self, ip):
        self.ip = ip
        self.pairing_data = {"your_id": "02:00:00:00:00:00",
                             "your_name": "motorolaMoto G 2014", "your_ip": "10.0.0.208", "your_sys": "9"}

    def do_request(self, type, endpoint, text=True, post=False, output_path=False):
        url = f"http://{self.ip}:24170/eos/{type}/{endpoint}"

        if post:
            data = urllib.parse.urlencode(post)
            data = data.encode('ascii')
            req = urllib.request.Request(url, data=data)
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            req.get_method = lambda: 'POST'
        else:
            req = urllib.request.Request(url)

        if not output_path:
            with urllib.request.urlopen(req) as f:
                response = f.read()

            if text:
                response = response.decode("UTF-8")
                try:
                    return json.loads(response)
                except:
                    return response
            else:
                return response
        else:
            # Download the file from `url` and save it locally under `file_name`:
            with urllib.request.urlopen(url) as response, open(output_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)

    def pairing(self):
        return self.do_request("method", "pairing", True, self.pairing_data)

    def get_device_name(self):
        return self.do_request("method", "get_device_name")

    def device_name_get(self):
        return self.do_request("query", "device_name_get")

    def get_recent_file(self):
        return self.do_request("method", "get_recent_file")

    def get_input_source(self):
        return self.do_request("method", "get_input_source")

    def get_record_remain_time(self):
        return self.do_request("method", "get_record_remain_time")

    def get_box_whole_infos(self):
        return self.do_request("method", "get_box_whole_infos")

    def sys_language_get(self):
        return self.do_request("query", "sys_language_get")

    def record_remain_time_get(self):
        return self.do_request("query", "record_remain_time_get")

    def input_source_type_get(self):
        return self.do_request("query", "input_source_type_get")

    def recent_file_get(self):
        return self.do_request("query", "recent_file_get")

    def get_partitions_count(self):
        return self.do_request("method", "get_partitions_count")

    def partition_count_get(self):
        return self.do_request("query", "partition_count_get")

    def get_file_info(self):
        return self.do_request("method", "get_file_info")

    def file_info_get(self):
        return self.do_request("query", "file_info_get")

    def get_files_infos(self, file_name_path, start_index=0, end_index=64):
        post_data = {"file_name_path": file_name_path,
                     "start_index": start_index, "end_index": end_index}
        return self.do_request("method", "get_files_infos", text=True, post=post_data)

    def files_infos_get(self):
        return self.do_request("query", "files_infos_get")

    def get_file_content(self, local_path, output_path=False):
        local_path_encoded = urllib.parse.quote_plus(local_path)

        return self.do_request("method", f"get_file_content/content_name={local_path_encoded}", text=False, post=False, output_path=output_path)

    def download_file(self, local_path, output_path):
        self.get_file_content(local_path, output_path)

    def irkey_send(self, command):
        translation = {
            "power": 1,
            "menu": 3,
            "up": 5,
            "down": 6,
            "left": 7,
            "right": 8,
            "ok": 9,
            "capture": 12
        }

        if not command in translation:
            raise ValueError("Command not recognised")
        
        post_data = { "key_id": translation[command] }

        return self.do_request("method", "irkey_send", post=post_data)

    def keep_alive(self):
        return self.do_request("method", "keep_alive")

    def get_box_status(self):
        return self.do_request("method", "get_box_status")

    def status_get(self):
        return self.do_request("query", "status_get")

    def take_image(self):
        return self.do_request("method", "take_image")

    def snapshot_fullpath_get(self):
        return self.do_request("query", "snapshot_fullpath_get")

    def start_record(self):
        return self.do_request("method", "start_record")

    def get_record_info(self):
        return self.do_request("method", "get_record_info")

    def get_record_elapse_time(self):
        return self.do_request("method", "get_record_elapse_time")

    def record_info_get(self):
        return self.do_request("query", "record_info_get")

    def record_elapse_time_get(self):
        return self.do_request("query", "record_elapse_time_get")

    def stop_record(self):
        return self.do_request("method", "stop_record")
