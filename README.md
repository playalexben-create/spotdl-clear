# Spotify Downloader

[Русский](#русский) | [English](#english)

---

## Русский

Простой графический интерфейс (GUI) для скачивания музыки, альбомов и плейлистов со Spotify в формате MP3. Программа использует библиотеку `spotDL` и обходит блокировки YouTube с помощью файлов cookies.

### Требования
* Python 3.8 или выше
* Microsoft Edge или Google Chrome (для экспорта cookies)

### Быстрый запуск

1. **Установите зависимости:**
   Откройте терминал в папке с проектом и выполните:
   ```bash
   pip install -r requirements.txt
   ```

2. **Настройте FFmpeg:**
   Запустите программу:
   ```bash
   python main.py
   ```
   При первом запуске нажмите кнопку **"1. Install FFmpeg"** и дождитесь окончания процесса в логах. Это необходимо для конвертации аудио в MP3.

3. **Обойдите блокировку YouTube (Обязательно):**
   * Установите в Edge или Chrome расширение [Get cookies.txt LOCALLY](https://microsoftedge.microsoft.com/addons/detail/get-cookiestxt-locally/helblmgegdgppdaolonigpebdmdehada).
   * Зайдите на сайт [youtube.com](https://www.youtube.com) под своей учетной записью.
   * Нажмите на иконку расширения, выберите **Export** и сохраните файл `cookies.txt` на компьютер.
   * В интерфейсе программы нажмите кнопку **"Выбрать"** рядом с полем **Cookies.txt** и укажите этот файл.

4. **Скачивание:**
   * Вставьте ссылку на трек или плейлист Spotify.
   * Выберите папку для сохранения (кнопка **Browse**).
   * Нажмите **"2. Download Music"**.

---

## English

A simple desktop GUI application to download songs, albums, and playlists from Spotify in MP3 format. It uses `spotDL` under the hood and bypasses YouTube bot detection via a cookies file.

### Requirements
* Python 3.8 or higher
* Microsoft Edge or Google Chrome (to export cookies)

### Quick Start

1. **Install dependencies:**
   Open your terminal in the project directory and run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up FFmpeg:**
   Run the application:
   ```bash
   python main.py
   ```
   Click the **"1. Install FFmpeg"** button and wait for the process to finish in the logs. This is required for converting audio to MP3.

3. **Bypass YouTube bot detection **
   * Install the [Get cookies.txt LOCALLY](https://microsoftedge.microsoft.com/addons/detail/get-cookiestxt-locally/helblmgegdgppdaolonigpebdmdehada) extension in Edge or Chrome.
   * Open [youtube.com](https://www.youtube.com) and ensure you are logged in.
   * Click the extension icon, choose **Export**, and save the `cookies.txt` file.
   * In the app GUI, click **"Выбрать" (Browse)** next to the **Cookies.txt** field and select this file.

4. **Download:**
   * Paste your Spotify URL.
   * Choose your output folder (using the **Browse** button).
   * Click **"2. Download Music"**.
