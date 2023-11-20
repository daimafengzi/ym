"""
💰 钢蹦阅读_V3.0    ♻231107     ⚠️更新检测文章判断逻辑

🔔 阅读赚金币，金币可提现，每天最低1—2元，邀请好友还可以赚更多，本脚本自动推送检测文章到微信，需要用户手动阅读过检测，过检测后脚本自动完成剩余任务，每天180篇，每篇100金币，3000金币可提现，提现秒到账，10000金币=1元。不需要下载app，在微信打开下方链接即可进入到活动页。

🔔 为了您能持久获得收益，请仔细阅读以下说明

👉 活动入口 微信打开： http://w.6mcyrj8t2qnq.cloud/?p=2903155   备用链接：https://tinyurl.com/3rcek97w   建议将链接添加至微信收藏，或添加到悬浮窗，方便进入查看和阅读检测文章

@进入后点击永久入口，保存二维码，当链接失效时扫码获取最新链接！

@建议一个微信号只运行一个阅读任务，否则会被列入风险用户，导致阅读无效，得不偿失！

@运行脚本前建议手动阅读5篇左右再使用脚本，不然100%黑！！！

@本脚本仅供学习交流，请在下载后的24小时内完全删除 请勿用于商业用途或非法目的，否则后果自负。

提示：
建议使用“pushplus推送加”接收检测文章，微信公众号关注“pushplus推送加”，点击pushplus进入到官网首页注册并激活消息，注册后获取您的token口令填写到下方(key=" ")。当然您也可以使用企业微信接收消息。
每轮有多篇检测文章，检测不过，有黑号的风险，导致阅读无效，如不能及时接收检测文章，或不能及时阅读检测文章，建议手动运行脚本，运行时注意接收消息并阅读检测文章，每篇阅读6秒以上。
每天180个任务不建议跑满，细水长流，如出现阅读更新中，建议几小时后再操作，平时在订阅号多读文章，多点赞评论，可以减小黑号的几率。
为了阅读账号安全，调试过程严谨反复运行脚本，可间隔2小时进行第二次调试，调试运行前应检查好各参数配置。

参数：
阅读文章时用抓包工具抓出cookie（搜索gfsessionid关键词），获取参数
变量名称：ydtoken     变量值：gfsessionid=o-0fIv9cGv3xxxxxxx; zzbb_info=%7B%22xxxxxxx
多账号用'&'隔开 例: 账号1&账号2
抓包请求中获取User-Agent填写到下方UA = ""               
      
定时:
自动定时规则cron： 0 7-23/3 * * *   (每天7-23点每3小时一次)，期间注意接收微信通知，阅读检测文章，(key参数必填)
手动定时规则cron： 0                (不自动运行)，每次手动运行脚本时务必注意阅读检测文章，每篇阅读6秒以上。
cron：0 7-23/3 * * *
"""


money_Withdrawal = 0  # 提现开关 1开启 0关闭
UA = "" #抓包获取User-Agent(🔔必填)
key = ""  # (🔔必填) key参数为pushplus的token口令，或企业微信webhook机器人后面的 key，用于推送接收检测文章



import random
import hashlib
import json
import os
import re
import time
from datetime import datetime
import requests



# 遍历所有账号
cookie = "xxx"
# 输出当前正在执行的账号
# 计算 sign
current_time = str(int(time.time()))
sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
sha256_hash = hashlib.sha256(sign_str.encode())
sign = sha256_hash.hexdigest()
url = "http://2477726.neavbkz.jweiyshi.r0ffky3twj.cloud/share"
headers = {
    "User-Agent": UA,
    "Cookie": cookie
}
data = {
    "time": current_time,
    "sign": sign
}
response = requests.get(url, headers=headers, json=data).json()
if response['code'] == 0:
    share_link0 = response['data']['share_link'][0]
    share_link1 = response['data']['share_link'][1]
    share_link2 = response['data']['share_link'][2]
    p_value = share_link0.split('=')[1].split('&')[0]
    # print(f"ID：{p_value}\n链接1：{share_link0}")
    # url = f'{share_link0}'
    headers = {
        "User-Agent": UA
    }
    response = requests.get(share_link0, headers=headers, allow_redirects=False)
    url1 = response.headers['Location']
    pattern = r'http://([^/]+)'
    match = re.search(pattern, url1)
    host = match.group(1)
else:
    print(response['message'])

print("============开始阅读文章============")
for o in range(40):
    # 计算 sign
    current_time = str(int(time.time()))
    sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
    sha256_hash = hashlib.sha256(sign_str.encode())
    sign = sha256_hash.hexdigest()
    url = f'http://{host}/read/task'
    headers = {
        "User-Agent": UA,
        "Cookie": cookie
    }
    data = {
        "time": current_time,
        "sign": sign
    }
    time.sleep(2)
    try:
        response = requests.get(url, headers=headers,  json=data, timeout=7).json()
    except requests.Timeout:
        print("❗请求超时，尝试重新发送请求...")
        response = requests.get(url, headers=headers,  json=data, timeout=7).json()
    if response['code'] == 1:
        print(f"❗{response['message']}\n")
        break
    else:
        try:
            link = response['data']['link']
            if "biz" in link:
                response = requests.get(url=link, headers=headers).text
                pattern = r'<meta\s+property="og:url"\s+content="([^"]+)"\s*/>'
                matches = re.search(pattern, response)
                pattern1 = r'nickname">(.*?)<'
                matches1 = re.search(pattern1, response)
                biz = link.split('__biz=')[1].split('&')[0]
                nickname = matches1.group(1) if matches1 else None
                print(f"--------------------------------------------------")
                print(f"第 {o+1} 篇检测获取成功-标识[{biz}]-[{nickname}]")
                # print(f"链接：[{link}]")

                print(f"发现目标[{biz}]--[{nickname}] 疑似检测文章！！！")

                url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key

                messages = [
                    f"出现检测文章！！！\n{link}\n请在60s内点击链接完成阅读",
                ]

                for message in messages:
                    data = {
                        "msgtype": "text",
                        "text": {
                            "content": message
                        }
                    }
                    headers = {'Content-Type': 'application/json'}
                    response = requests.post(url, headers=headers, data=json.dumps(data))
                    url = 'http://www.pushplus.plus/send'
                    data = {
                         "token": key,
                         "title": "出现检测文章！请在60s内完成阅读",
                         "content": f'<a href="\n{link}\n"target="_blank">点击阅读6s以上 \n{link}\n',
                         "template": "html"
                    }
                    response = requests.post(url, data=data).json()
                    print("已将文章推送至微信，请在60s内完成阅读，60s后继续运行")
                    time.sleep(60)
                    print("60s已到")
                    # 计算 sign
                    current_time = str(int(time.time()))
                    sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
                    sha256_hash = hashlib.sha256(sign_str.encode())
                    sign = sha256_hash.hexdigest()
                    url = f'http://{host}/read/finish'
                    headers = {
                        "User-Agent": UA,
                        "Cookie": cookie
                    }
                    data = {
                        "time": current_time,
                        "sign": sign
                    }
                    try:
                        response = requests.get(url, headers=headers, data=data, timeout=7).json()
                        print(f"是否检测：{response['data']['check']}")
                    except requests.Timeout:
                        print("❗请求超时，尝试重新发送请求...")
                        response = requests.get(url, headers=headers, data=data, timeout=7).json()
                        print(f"是否检测：{response['data']['check']}")
                    if response['code'] == 0:
                        gain = response['data']['gain']
                        read = response['data']['read']
                        gold = response['data']['gold']
                        remain = response['data']['remain']
                        print(f"第 {o+1} 篇检测阅读成功--获得钢镚：{gain} 💰\n今日阅读：{read} 篇--今日获取：{gold} 💰\n可提现钢镚：{remain} 💰")
                        print(f"--------------------------------------------------")
                    else:
                        print(f"❗过检测失败，请尝试重新运行")
                        break
            else:
                response = requests.get(link, headers=headers, allow_redirects=False)
                link1 = response.headers['Location']

                response = requests.get(url=link1, headers=headers).text
                pattern = r'<meta\s+property="og:url"\s+content="([^"]+)"\s*/>'
                matches = re.search(pattern, response)
                pattern1 = r'nickname">(.*?)<'
                matches1 = re.search(pattern1, response)
                biz = link1.split('__biz=')[1].split('&')[0]
                nickname = matches1.group(1) if matches1 else None
                print(f"--------------------------------------------------")
                sleep = random.randint(8, 15)
                print(f"第 {o+1} 篇文章-标识[{biz}]-[{nickname}]-模拟{sleep}秒")
                # print(f"链接：[{link1}]")
                time.sleep(sleep)
                # 计算 sign
                current_time = str(int(time.time()))
                sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
                sha256_hash = hashlib.sha256(sign_str.encode())
                sign = sha256_hash.hexdigest()
                url = f'http://{host}/read/finish'
                headers = {
                    "User-Agent": UA,
                    "Cookie": cookie
                }
                data = {
                    "time": current_time,
                    "sign": sign
                }
                try:
                    response = requests.get(url, headers=headers, data=data, timeout=7).json()
                    print(f"是否检测：{response['data']['check']}")
                    assert response['data']['check'] is False
                except requests.Timeout:
                    print("❗请求超时，尝试重新发送请求...")
                    response = requests.get(url, headers=headers, data=data, timeout=7).json()
                    print(f"是否检测：{response['data']['check']}")
                    assert response['data']['check'] is False
                if response['code'] == 0:
                    gain = response['data']['gain']
                    read = response['data']['read']
                    gold = response['data']['gold']
                    remain = response['data']['remain']
                    print(f"第 {o+1} 篇阅读成功--获得钢镚：{gain} 💰\n今日阅读：{read} 篇--今日获取：{gold} 💰\n可提现钢镚：{remain} 💰")
                    print(f"--------------------------------------------------")
                else:
                    print(f"❗阅读文章失败{response}")
                    break
        except KeyError:
            print(f"❗{response['message']}\n")
            break

if money_Withdrawal == 1:
    print(f"============开始微信提现============")
    current_time1 = datetime.now()
    # 计算 sign
    current_time = str(int(time.time()))
    sign_str = f'key=4fck9x4dqa6linkman3ho9b1quarto49x0yp706qi5185o&time={current_time}'
    sha256_hash = hashlib.sha256(sign_str.encode())
    sign = sha256_hash.hexdigest()
    url = f'http://{host}/withdraw/wechat'
    headers = {
        "User-Agent": UA,
        "Cookie": cookie
    }
    data = {
        "time": current_time,
        "sign": sign
    }
    response = requests.get(url, headers=headers, json=data).json()
    if response['code'] == 0:
        print(response['message'])
    elif response['code'] == 1:
        print(response['message'])
    else:
        print(f"❗错误{response}")
elif money_Withdrawal == 0:
    print(f"{'-' * 30}\n不执行提现")