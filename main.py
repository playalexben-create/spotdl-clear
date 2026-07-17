import customtkinter as ctk
import subprocess
import threading
import os
from tkinter import filedialog
from tkinter import messagebox

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Spotify Downloader")
        self.geometry("650x560")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # 1. URL Input
        self.url_label = ctk.CTkLabel(self, text="Spotify URL (Playlist, Track, Album):", font=ctk.CTkFont(size=14, weight="bold"))
        self.url_label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")
        
        self.url_entry = ctk.CTkEntry(self, placeholder_text="https://open.spotify.com/playlist/...", width=400)
        self.url_entry.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="ew")

        # 2. Output Directory Frame
        self.dir_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.dir_frame.grid(row=2, column=0, padx=20, pady=5, sticky="ew")
        self.dir_frame.grid_columnconfigure(0, weight=1)

        self.dir_entry = ctk.CTkEntry(self.dir_frame, placeholder_text="Download location...")
        self.dir_entry.grid(row=0, column=0, padx=(0, 10), pady=0, sticky="ew")
        
        # Set default directory to user's Music folder
        default_dir = os.path.join(os.path.expanduser("~"), "Music", "SpotifyDownloads")
        self.dir_entry.insert(0, default_dir)

        self.browse_btn = ctk.CTkButton(self.dir_frame, text="Browse", width=80, command=self.browse_directory)
        self.browse_btn.grid(row=0, column=1, padx=0, pady=0)

        # 2b. Cookies file
        self.cookies_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.cookies_frame.grid(row=3, column=0, padx=20, pady=(2, 5), sticky="ew")
        self.cookies_frame.grid_columnconfigure(1, weight=1)

        self.cookies_label = ctk.CTkLabel(self.cookies_frame, text="Cookies.txt:", font=ctk.CTkFont(size=13))
        self.cookies_label.grid(row=0, column=0, padx=(0, 10), pady=0, sticky="w")

        self.cookies_entry = ctk.CTkEntry(self.cookies_frame, placeholder_text="Путь к файлу cookies.txt (необязательно, но рекомендуется)")
        self.cookies_entry.grid(row=0, column=1, padx=(0, 10), pady=0, sticky="ew")

        self.cookies_browse_btn = ctk.CTkButton(self.cookies_frame, text="Выбрать", width=80, command=self.browse_cookies)
        self.cookies_browse_btn.grid(row=0, column=2, padx=0, pady=0)

        # 4. Log Text Box
        self.log_box = ctk.CTkTextbox(self, state="disabled", wrap="word", font=ctk.CTkFont(family="Consolas", size=12))
        self.log_box.grid(row=4, column=0, padx=20, pady=(10, 10), sticky="nsew")
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(3, weight=0)

        # 5. Action Buttons
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="ew")
        self.btn_frame.grid_columnconfigure((0,1), weight=1)

        self.download_ffmpeg_btn = ctk.CTkButton(self.btn_frame, text="1. Install FFmpeg (Required once)", command=self.download_ffmpeg, fg_color="#E07A5F", hover_color="#C0654D")
        self.download_ffmpeg_btn.grid(row=0, column=0, padx=(0, 10), sticky="ew")

        self.download_btn = ctk.CTkButton(self.btn_frame, text="2. Download Music", command=self.start_download, fg_color="#2A9D8F", hover_color="#21867A")
        self.download_btn.grid(row=0, column=1, padx=(10, 0), sticky="ew")

        self.append_log("Welcome to Spotify Downloader!\n")
        self.append_log("Для обхода блокировки YouTube нужен файл cookies.txt.\n")
        self.append_log("Как получить cookies.txt:\n")
        self.append_log("  1. Установите расширение 'Get cookies.txt LOCALLY' в Edge/Chrome\n")
        self.append_log("  2. Зайдите на youtube.com (убедитесь что вы залогинены)\n")
        self.append_log("  3. Нажмите на расширение → Export → сохраните файл cookies.txt\n")
        self.append_log("  4. Укажите путь к этому файлу в поле 'Cookies.txt' выше\n\n")

    def browse_directory(self):
        folder = filedialog.askdirectory()
        if folder:
            self.dir_entry.delete(0, 'end')
            self.dir_entry.insert(0, folder)

    def browse_cookies(self):
        filepath = filedialog.askopenfilename(
            title="Выберите файл cookies.txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filepath:
            self.cookies_entry.delete(0, 'end')
            self.cookies_entry.insert(0, filepath)

    def append_log(self, text):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", text)
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def run_command(self, command, cwd=None):
        try:
            # Use CREATE_NO_WINDOW on Windows to prevent console popup
            creationflags = subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                cwd=cwd,
                creationflags=creationflags,
                encoding='utf-8',
                errors='replace'
            )

            for line in process.stdout:
                self.after(0, self.append_log, line)
            
            process.wait()
            self.after(0, self.append_log, f"\n--- Process finished ---\n\n")
            
        except Exception as e:
            self.after(0, self.append_log, f"\nError: {str(e)}\n\n")
        finally:
            self.after(0, self.enable_buttons)

    def disable_buttons(self):
        self.download_btn.configure(state="disabled")
        self.download_ffmpeg_btn.configure(state="disabled")
        self.cookies_browse_btn.configure(state="disabled")

    def enable_buttons(self):
        self.download_btn.configure(state="normal")
        self.download_ffmpeg_btn.configure(state="normal")
        self.cookies_browse_btn.configure(state="normal")

    def download_ffmpeg(self):
        self.disable_buttons()
        self.append_log("Downloading FFmpeg... (This will download ffmpeg to spotDL's internal directory)\n")
        cmd = ["python", "-m", "spotdl", "--download-ffmpeg"]
        threading.Thread(target=self.run_command, args=(cmd,), daemon=True).start()

    def start_download(self):
        url = self.url_entry.get().strip()
        out_dir = self.dir_entry.get().strip()

        if not url:
            messagebox.showwarning("Warning", "Please enter a Spotify URL.")
            return
        
        if not out_dir:
            messagebox.showwarning("Warning", "Please select a download location.")
            return

        # Create output directory if it doesn't exist
        try:
            os.makedirs(out_dir, exist_ok=True)
        except Exception as e:
            messagebox.showerror("Error", f"Could not create directory:\n{str(e)}")
            return

        self.disable_buttons()
        self.append_log(f"Starting download for: {url}\nSaving to: {out_dir}\n")

        cookies_path = self.cookies_entry.get().strip()
        cmd = ["python", "-m", "spotdl", url, "--format", "mp3", "--audio", "youtube-music", "youtube"]

        if cookies_path and os.path.isfile(cookies_path):
            self.append_log(f"Используем cookies из файла: {cookies_path}\n")
            cmd += ["--cookie-file", cookies_path]
        else:
            self.append_log("⚠ Файл cookies.txt не указан — возможны ошибки блокировки от YouTube.\n")

        threading.Thread(target=self.run_command, args=(cmd, out_dir), daemon=True).start()

if __name__ == "__main__":
    app = App()
    app.mainloop()
