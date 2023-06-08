
from datetime import datetime
from pathlib import Path
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
current_path = Path("update_ini.py").parent.absolute()

# Check if QX folder existing
qx_path = current_path / "QX"
if not qx_path.is_dir():
    qx_path.mkdir()

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

print("Generating QX self_direct.list...")
with open("self_direct.list", "r", encoding=encoding, errors="ignore") as r:
    self_direct_qx_content = r.read()
self_direct_qx_content_list = self_direct_qx_content.split("\n")
new_self_direct_qx_content_list = []
for i in self_direct_qx_content_list:
    if len(i):
        if not i.startswith("#"):
            i += ",Self-Direct\n"
        else:
            i += "\n"
    else:
        i += "\n"
    new_self_direct_qx_content_list.append(i)
self_direct_qx_content = "".join(new_self_direct_qx_content_list)
qx_self_direct_path = qx_path / "self_direct.list"
with qx_self_direct_path.open("w", encoding=encoding, errors="ignore") as w:
    w.write(self_direct_qx_content)
print("Generating QX self_proxy.list...")
with open("self_proxy.list", "r", encoding=encoding, errors="ignore") as r:
    self_proxy_qx_content = r.read()
self_proxy_qx_content_list = self_proxy_qx_content.split("\n")
new_self_proxy_qx_content_list = []
for i in self_proxy_qx_content_list:
    if len(i):
        if not i.startswith("#"):
            i += ",Self-Proxy\n"
        else:
            i += "\n"
    else:
        i += "\n"
    new_self_proxy_qx_content_list.append(i)
self_proxy_qx_content = "".join(new_self_proxy_qx_content_list)
qx_self_proxy_path = qx_path / "self_proxy.list"
with qx_self_proxy_path.open("w", encoding=encoding, errors="ignore") as w:
    w.write(self_proxy_qx_content)

print("All finished!")
