# English translation is down below
## RuStoreSAD - компактная, бесплатная и не требующая установки* программа на пк для загрузки приложений из [RuStore](https://www.rustore.ru).
## Использование простое:
1. Скачайте последнюю версию программы со [страницы релизов](https://github.com/SaHaL1NeZ/RuStoreSAD/releases)
2. После открытия программы нажмите Enter
3. Введите ссылку на приложение или имя его пакета
4. Если оно найдено - получите ссылку на загрузку
5. Хотите загрузить его в папку с программой - Enter

В [релизах](https://github.com/SaHaL1NeZ/RuStoreSAD/releases) есть 2 версии программы - с UPX сжатием (вес меньше, первый запуск чуть дольше*) и без.

На UPX сжатие могут жаловаться антивирусы - это ложное срабатывание (в случае с моей программой), на обычную версию - нет.

Почему? UPX сжатие затрудняет проверку файла, оно может использоваться вирусами для маскировки.

Страшно? Скачайте обычную версию, проверьте своим не НН антивирусом (на [VirusTotal](https://www.virustotal.com) есть НН антивирусы, жалующиеся на каждую программу сложнее калькулятора) или соберите программу самостоятельно, код открыт.
# Бесплатные альтернативы
Если вы не хотите ничего скачивать - [простой сайт](https://kolya00736.github.io/rustore-downloader) от [kolya00736](https://github.com/kolya00736/rustore-downloader).

Если вы пользователь Linux или влюблены в командную строку - [требующая установки утилита](https://github.com/ldmitryMorozovI/rustore_downloader) от ldmitryMorozovI
# Самостоятельная сборка на Windows
Скачайте [Python](https://www.python.org/downloads) версии 3 или больше и [git](https://git-scm.com/downloads).

Открываете терминал в корневой папке будущей программы, пишите "git clone https://github.com/SaHaL1NeZ/RuStoreSAD".

На всякий случай обновляете pip - "python -m pip install -U pip".

Скачиваете необходимые библиотеки - "pip install requests tqdm pyinstaller".

Наконец собираете программу - "pyinstaller --onefile --icon=RuStoreSAD.ico --version-file=v.txt --clean --noconfirm RuStoreSAD.py".

Дополнительно можно ещё использовать UPX в сборке программы, добавив в команду " --upx-dir="ПУТЬ_К_ПАПКЕ_UPX" ".
###### РуСторГРУСТНЫЙ 😔
# English:
## RuStoreSAD - a compact, free and portable PC program for downloading apps from [RuStore](https://www.rustore.ru).
## Usage is simple:
1. Download the latest version of program from [releases page](https://github.com/SaHaL1NeZ/RuStoreSAD/releases)
2. After launching the program, press Enter
3. Type the app's link or its package name
4. If found, you'll receive a download link
5. To download the app into the program's folder, press Enter

In the [releases](https://github.com/SaHaL1NeZ/RuStoreSAD/releases) there are two versions of the program - one compressed with UPX (smaller file size, slightly longer first startup*) and one isn't.

Antiviruses might flag the UPX-compressed version - this is a false positive (in the case of my program), the regular version won't be flagged

Why? UPX compression makes file analysis harder, it can be used by viruses to hide themselves.

Frightened? Download the regular version, scan it with your NOT NONAME antivirus (there are some noname antiviruses on [VirusTotal](https://www.virustotal.com) those flag every program that is more complicated than calculator) or build the program yourself - the source code is open.
# Free alternatives
If you don't want to download anything - use this [simple website](https://kolya00736.github.io/rustore-downloader) by [kolya00736](https://github.com/kolya00736/rustore-downloader).

If you're a Linux user or adore the command line - try the [installable tool](https://github.com/ldmitryMorozovI/rustore_downloader) by ldmitryMorozovI.
# Building the program for Windows
Download [Python](https://www.python.org/downloads) version 3 or higher and [git](https://git-scm.com/downloads).

Open a terminal in the root directory for the future program and run "git clone https://github.com/SaHaL1NeZ/RuStoreSAD".

Update pip just in case: "python -m pip install -U pip".

Install required libraries: "pip install requests tqdm pyinstaller".

Finally, build the program: "pyinstaller --onefile --icon=RuStoreSAD.ico --version-file=v.txt --clean --noconfirm RuStoreSAD.py".

Additionally, you can use UPX in the build by adding " --upx-dir="PATH_TO_UPX_FOLDER" " to the command.
###### RuStore is so SAD 😔
