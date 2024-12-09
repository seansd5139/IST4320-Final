# pip install speedtest-cli

import speedtest
import tkinter as tk
import tkinter.ttk as ttk

def run_speed_test():
    s = speedtest.Speedtest(secure=True)
    s.get_best_server()
    s.download()
    s.upload()

    results_dict = s.results.dict()

    download_speed_mbps = round(results_dict['download'] / 1024 / 1024, 2)
    upload_speed_mbps = round(results_dict['upload'] / 1024 / 1024, 2)
    ping_ms = round(results_dict['ping'])

    print("Download Speed:", download_speed_mbps, "Mb/s")
    print("Upload Speed:", upload_speed_mbps, "Mb/s")
    print("Ping:", ping_ms, "ms")

    return {
        'download': download_speed_mbps,
        'upload': upload_speed_mbps,
        'ping': ping_ms
    }

class SpeedTestGUI:

    def __init__(self):
        self.root = tk.Tk()
        # self.root.geometry("600x400")
        self.root.resizable(False, False)

        style = ttk.Style(self.root)
        style.configure("TLabel", font=('Comic Sans MS', 16)) 
        style.configure("TButton", font=('Comic Sans MS', 20)) 
        
        self.title_label = ttk.Label(self.root, text='Speed Test', font=('Comic Sans MS', 32, 'bold'))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(10, 10))
        
        self.download_speed_label = ttk.Label(self.root, text='Download Speed', anchor="e")
        self.download_speed_label.grid(row=1, column=0, sticky="nsew", padx=(40, 20))

        self.download_speed_number = ttk.Label(self.root, text="-- Mb/s")
        self.download_speed_number.grid(row=1, column=1, padx=(0, 40))

        self.upload_speed_label = ttk.Label(self.root, text='Upload Speed', anchor="e")
        self.upload_speed_label.grid(row=2, column=0, sticky="nsew", padx=(40, 20))

        self.upload_speed_number = ttk.Label(self.root, text="-- Mb/s")
        self.upload_speed_number.grid(row=2, column=1, padx=(0, 40))

        self.ping_label = ttk.Label(self.root, text='Ping', anchor="e")
        self.ping_label.grid(row=3, column=0, sticky="nsew", padx=(40, 20))

        self.ping_number = ttk.Label(self.root, text="-- ms")
        self.ping_number.grid(row=3, column=1, padx=(0, 40))

        self.test_button = ttk.Button(self.root, text='Run Test', command=self.test_button_clicked)
        self.test_button.grid(row=4, column=0, columnspan=2, pady=(20, 30))

        self.root.mainloop()


    def test_button_clicked(self):
        print("Running speed test...")
        self.test_button.config(text="Running...")
        self.test_button.config(state="disabled")
        self.root.update()

        results = run_speed_test()

        self.download_speed_number.config(text=str(results['download']) + " Mb/s")
        self.upload_speed_number.config(text=str(results['upload']) + " Mb/s")
        self.ping_number.config(text=str(results['ping']) + " ms")

        self.test_button.config(text="Run Test")
        self.test_button.config(state="enabled")
        self.root.update()


gui = SpeedTestGUI()