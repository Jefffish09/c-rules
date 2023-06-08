
from datetime import datetime
from urllib.request import urlopen


github_proxy = False
if github_proxy:
    gp = "https://ghproxy.com/"
else:
    gp = ""
timeout = 100
encoding = "utf-8"

original_ini_url = f"{gp}https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/config/ACL4SSR_Online_Full_MultiMode.ini"
repo_name = "c-rules"
custom_proxy_group_format_string = "`select`[]🎥 奈飞节点`[]🚀 节点选择`[]♻️ 自动选择`[]🇸🇬 狮城节点`[]🇭🇰 香港节点`[]🇨🇳 台湾节点`[]🇯🇵 日本节点`[]🇺🇲 美国节点`[]🇰🇷 韩国节点`[]🚀 手动切换`[]DIRECT"

# Direct
self_direct_list_url = f"{gp}https://raw.githubusercontent.com/Jefffish09/{repo_name}/main/self_direct.list"
direct_name = "Self-Direct"
ruleset_direct = f"ruleset={direct_name},{self_direct_list_url}"
custom_proxy_group_direct = f"custom_proxy_group={direct_name}{custom_proxy_group_format_string}"
# Proxy
self_proxy_list_url = f"{gp}https://raw.githubusercontent.com/Jefffish09/{repo_name}/main/self_proxy.list"
proxy_name = "Self-Proxy"
ruleset_proxy = f"ruleset={proxy_name},{self_proxy_list_url}"
custom_proxy_group_proxy = f"custom_proxy_group={proxy_name}{custom_proxy_group_format_string}"

print(f"Current time: {datetime.now():%Y-%m-%d %H:%M:%S}")
print("Downloading the original .ini file...")
response = urlopen(original_ini_url, timeout=timeout)
original_ini = response.read().decode(encoding)

print("Modifying the .ini file...")
loc_1 = original_ini.find(";设置规则标志位\n") + 9
ini_1 = f"{original_ini[:loc_1]}{ruleset_direct}\n{ruleset_proxy}\n{original_ini[loc_1:]}"

loc_2 = ini_1.find(";设置分组标志位\n") + 9
ini_2 = f"{ini_1[:loc_2]}{custom_proxy_group_direct}\n{custom_proxy_group_proxy}\n{ini_1[loc_2:]}"

print("Generating the new .ini file...")
with open("rules.ini", "w", encoding=encoding, errors="ignore") as w:
    w.write(ini_2)

print("All finished!")
