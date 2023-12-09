import requests

cookies = {
    'BITRIX_RM_GUEST_ID': '33411926',
    'BX_USER_ID': '67ebad0b38450f2c44c84ef68496187d',
    'SLG_G_WPT_TO': 'ru',
    '_ga': 'GA1.2.1030976922.1702137782',
    '_gid': 'GA1.2.1734403421.1702137782',
    'SLG_GWPT_Show_Hide_tmp': '1',
    'SLG_wptGlobTipTmp': '1',
    '_ym_uid': '1702137783495500880',
    '_ym_d': '1702137783',
    '_ym_isad': '2',
    'BITRIX_RM_LAST_VISIT': '09.12.2023+19%3A04%3A13',
    '_ga_WK4S4NZFYC': 'GS1.2.1702137783.1.1.1702137864.60.0.0',
    'PHPSESSID': '476d1a276f933f4212917fb69f4065c3',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'BITRIX_RM_GUEST_ID=33411926; BX_USER_ID=67ebad0b38450f2c44c84ef68496187d; SLG_G_WPT_TO=ru; _ga=GA1.2.1030976922.1702137782; _gid=GA1.2.1734403421.1702137782; SLG_GWPT_Show_Hide_tmp=1; SLG_wptGlobTipTmp=1; _ym_uid=1702137783495500880; _ym_d=1702137783; _ym_isad=2; BITRIX_RM_LAST_VISIT=09.12.2023+19%3A04%3A13; _ga_WK4S4NZFYC=GS1.2.1702137783.1.1.1702137864.60.0.0; PHPSESSID=476d1a276f933f4212917fb69f4065c3',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
    'sec-ch-ua': '"Opera";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://rusmuseum.ru/', cookies=cookies, headers=headers)

with open('result.html', 'w') as file:
    file.write(response.text)
