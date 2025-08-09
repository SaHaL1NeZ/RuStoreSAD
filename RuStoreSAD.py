from tqdm import tqdm 
import requests
import json
import os
def Clear():
    try:
        os.system('cls' if os.name=='nt' else 'clear')
    except:
        print('\n'*40)
def LanguageSelection():
    print('Выберите язык | Select the language')
    lang=input('Нажмите Enter | Type 2 and press enter: ').strip()
    Clear()
    if lang=='2':
        return 2
    else:
        return 1
def Decode(response):
    try:
        DecodedResponse=response.json()
        return DecodedResponse
    except json.JSONDecodeError:
        print('\nError while decoding response as JSON')
        print(f'Server response: {response.text}')
        return
def Suggestion(lang,AppName):
    if lang==1:
        print(f'\nВ таком случае, можете попробовать эти сайты:')
        print(f'https://apkcombo.com/ru/{AppName}')
        print(f'https://play.google.com/store/apps/details?id={AppName}&hl=ru')
    else:
        print(f'\nIn such case, you can try those sites:')
        print(f'https://apkcombo.com/{AppName}')
        print(f'https://play.google.com/store/apps/details?id={AppName}')
def Rewind(lang):
    if lang==1:
        ask=input('\nПерезапустить? Y/N (Да/нет) (Enter = Y по умолчанию): ').strip()
    else:
        ask=input('\nRestart? Y/N (Enter = Y by default): ').strip().lower()
    if ask!='y' and ask!='n':
        ask='y'
    if ask=='y':
        Clear()
        RuStoreSAD(lang)
    else:
        return
def RuStoreSAD(lang):
    print('''┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│  ███████████               █████████   █████                                  █████████    █████████   ██████████   │
│ ░░███░░░░░███             ███░░░░░███ ░░███                                  ███░░░░░███  ███░░░░░███ ░░███░░░░███  │
│  ░███    ░███  █████ ████░███    ░░░  ███████    ██████  ████████   ██████  ░███    ░░░  ░███    ░███  ░███   ░░███ │
│  ░██████████  ░░███ ░███ ░░█████████ ░░░███░    ███░░███░░███░░███ ███░░███ ░░█████████  ░███████████  ░███    ░███ │
│  ░███░░░░░███  ░███ ░███  ░░░░░░░░███  ░███    ░███ ░███ ░███ ░░░ ░███████   ░░░░░░░░███ ░███░░░░░███  ░███    ░███ │
│  ░███    ░███  ░███ ░███  ███    ░███  ░███ ███░███ ░███ ░███     ░███░░░    ███    ░███ ░███    ░███  ░███    ███  │
│  █████   █████ ░░████████░░█████████   ░░█████ ░░██████  █████    ░░██████  ░░█████████  █████   █████ ██████████   │
│ ░░░░░   ░░░░░   ░░░░░░░░  ░░░░░░░░░     ░░░░░   ░░░░░░  ░░░░░      ░░░░░░    ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░░░░░░    │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘''')
    if lang==1:
        print('                                                                      - RuStore Simple APK Downloader, автор SaHaL1NeZ')
    else:
        print('                                                                    - RuStore Simple APK Downloader, made by SaHaL1NeZ')
    if lang==1:
        AppName=input('Введите имя пакета приложения (напр., ru.rostel): ').strip().lower()
    else:
        AppName=input('Enter the app package name (e.g., ru.rostel): ').strip()
    if '#' in AppName:
        AppName=AppName.split('#',1)[0]
    if '&' in AppName:
        AppName=AppName.split('&',1)[0]
    if '/' in AppName:
        AppName=AppName.split('/')[-1]
    if not AppName:
        Clear()
        return RuStoreSAD(lang)
    for i in AppName:
        if (not i in 'abcdefghijklmnopqrstuvwxyz.'):
            Clear()
            return RuStoreSAD(lang)
    headers={'Content-Type':'application/json; charset=utf-8'}
    if lang==1:
        print(f'\nИщу "{AppName}", пожалуйста подождите...')
    else:
        print(f'\nSearching for "{AppName}", please wait...')
    try:
        response=requests.get(f'https://backapi.rustore.ru/applicationData/overallInfo/{AppName}',headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'\nError while connecting to the app info endpoint: {e}')
        Suggestion(lang,AppName)
        return Rewind(lang)
    DecodedResponse=Decode(response)
    if DecodedResponse.get('code')=='OK':
        AppID=DecodedResponse.get('body',{}).get('appId')
        if not AppID:
            print('\nError while getting app id from the app info endpoint.')
            print(f'Decoded server response: {DecodedResponse}')
            Suggestion(lang,AppName)
            return Rewind(lang)
    else:
        print('\nError while getting app id from the app info endpoint.')
        print(f'Decoded server response: {DecodedResponse}')
        Suggestion(lang,AppName)
        return Rewind(lang)
    payload={
        'appId':AppID,
        'firstInstall':True
    }
    try:
        response=requests.post('https://backapi.rustore.ru/applicationData/download-link',headers=headers,data=json.dumps(payload))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'\nError while requesting APK url info: {e}')
        Suggestion(lang,AppName)
        return Rewind(lang)
    DecodedResponse=Decode(response)
    if DecodedResponse.get('code')=='OK':
        apk_url=DecodedResponse.get('body',{}).get('apkUrl')
        if not apk_url:
            print('\nError while finding APK url.')
            print(f'Decoded server response: {DecodedResponse}')
            Suggestion(lang,AppName)
            return Rewind(lang)
        print(f'\nUrl for downloading APK: {apk_url}')
        ask=input('\nDo you want to download APK? Y/N (Enter = Y by default): ').strip().lower()
        if ask!='y' and ask!='n':
            ask='y'
        if ask=='y':
            try:
                with requests.get(apk_url,stream=True) as response:
                    response.raise_for_status()
                    TotalSize=int(response.headers.get('content-length',0))
                    with open(f'{AppName}.apk','wb') as file,tqdm(
                        desc=f'{AppName}.apk',
                        total=TotalSize,
                        unit='B',
                        unit_scale=True,
                        unit_divisor=1024,
                        bar_format='{desc} | {percentage:3.0f}% | {n_fmt}/{total_fmt} [Downloading speed: {rate_fmt}]'
                    ) as ProgressBar:
                        for chunk in response.iter_content(chunk_size=8192):
                            file.write(chunk)
                            ProgressBar.update(len(chunk))
                    if lang==1:
                        print(f'\n{AppName}.apk был успешно скачан в корневую папку программы.')
                    else:
                        print(f'\n{AppName}.apk was downloaded successfully in the root folder of program.')
                    return Rewind(lang)
            except requests.exceptions.RequestException as e:
                print(f'\nError while requesting a download: {e}')
                return Rewind(lang)
        else:
            return Rewind(lang)
    else:
        print('\nError while getting url for downloading APK.')
        print(f'Decoded server response: {DecodedResponse}')
        return Rewind(lang)
if __name__=='__main__':
    RuStoreSAD(LanguageSelection())