import tkinter as tk
from tkinter import messagebox

class RocketShipInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rocket Ship Interface")
        self.geometry("400x600")
        self.configure(bg="black")

        self.status = tk.StringVar(value="Idle")
        self.fuel_level = tk.IntVar(value=100)
        self.altitude = tk.IntVar(value=0)
        self.speed = tk.IntVar(value=0)
        self.engine_on = False
        self.launched = False

        self.create_widgets()
        self.update_status()

    def create_widgets(self):
        title = tk.Label(self, text="🚀 Rocket Ship Control Panel", font=("Arial", 20, "bold"), fg="white", bg="black")
        title.pack(pady=10)

        # Status display
        status_frame = tk.Frame(self, bg="black")
        status_frame.pack(pady=10)

        tk.Label(status_frame, text="Status:", font=("Arial", 14), fg="white", bg="black").grid(row=0, column=0, sticky="w")
        tk.Label(status_frame, textvariable=self.status, font=("Arial", 14), fg="yellow", bg="black").grid(row=0, column=1, sticky="w")

        tk.Label(status_frame, text="Fuel Level:", font=("Arial", 14), fg="white", bg="black").grid(row=1, column=0, sticky="w")
        self.fuel_label = tk.Label(status_frame, text=f"{self.fuel_level.get()}%", font=("Arial", 14), fg="lime", bg="black")
        self.fuel_label.grid(row=1, column=1, sticky="w")

        tk.Label(status_frame, text="Altitude:", font=("Arial", 14), fg="white", bg="black").grid(row=2, column=0, sticky="w")
        self.altitude_label = tk.Label(status_frame, text=f"{self.altitude.get()} m", font=("Arial", 14), fg="cyan", bg="black")
        self.altitude_label.grid(row=2, column=1, sticky="w")

        tk.Label(status_frame, text="Speed:", font=("Arial", 14), fg="white", bg="black").grid(row=3, column=0, sticky="w")
        self.speed_label = tk.Label(status_frame, text=f"{self.speed.get()} m/s", font=("Arial", 14), fg="orange", bg="black")
        self.speed_label.grid(row=3, column=1, sticky="w")

        # Controls
        controls_frame = tk.Frame(self, bg="black")
        controls_frame.pack(pady=20)

        self.engine_button = tk.Button(controls_frame, text="Start Engine", font=("Arial", 14), width=15, command=self.toggle_engine)
        self.engine_button.grid(row=0, column=0, padx=10, pady=5)

        self.launch_button = tk.Button(controls_frame, text="Launch", font=("Arial", 14), width=15, command=self.launch)
        self.launch_button.grid(row=1, column=0, padx=10, pady=5)

        self.abort_button = tk.Button(controls_frame, text="Abort Mission", font=("Arial", 14), width=15, command=self.abort_mission, state="disabled")
        self.abort_button.grid(row=2, column=0, padx=10, pady=5)

        self.land_button = tk.Button(controls_frame, text="Land", font=("Arial", 14), width=15, command=self.land, state="disabled")
        self.land_button.grid(row=3, column=0, padx=10, pady=5)

        # Log box
        log_frame = tk.Frame(self, bg="black")
        log_frame.pack(pady=10, fill="both", expand=True)

        tk.Label(log_frame, text="Mission Log:", font=("Arial", 14), fg="white", bg="black").pack(anchor="w")

        self.log_text = tk.Text(log_frame, height=10, bg="black", fg="white", font=("Courier", 10), state="disabled")
        self.log_text.pack(fill="both", expand=True)

    def log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def toggle_engine(self):
        if not self.engine_on:
            if self.fuel_level.get() <= 0:
                messagebox.showwarning("Fuel Empty", "Cannot start engine. Fuel tank is empty!")
                return
            self.engine_on = True
            self.status.set("Engine On")
            self.engine_button.config(text="Stop Engine")
            self.log("Engine started.")
            self.launch_button.config(state="normal")
        else:
            self.engine_on = False
            self.status.set("Engine Off")
            self.engine_button.config(text="Start Engine")
            self.log("Engine stopped.")
            self.launch_button.config(state="disabled")

    def launch(self):
        if not self.engine_on:
            messagebox.showwarning("Engine Off", "Start the engine before launching!")
            return
        if self.launched:
            messagebox.showinfo("Already Launched", "Rocket is already launched!")
            return
        if self.fuel_level.get() <= 0:
            messagebox.showwarning("Fuel Empty", "Cannot launch. Fuel tank is empty!")
            return
        self.launched = True
        self.status.set("Launched")
        self.launch_button.config(state="disabled")
        self.abort_button.config(state="normal")
        self.land_button.config(state="normal")
        self.log("Rocket launched!")
        self.after(1000, self.update_flight)

    def abort_mission(self):
        if not self.launched:
            messagebox.showinfo("Not Launched", "Rocket has not launched yet.")
            return
        self.status.set("Mission Aborted")
        self.log("Mission aborted! Returning to base.")
        self.launched = False
        self.altitude.set(0)
        self.speed.set(0)
        self.abort_button.config(state="disabled")
        self.land_button.config(state="disabled")
        self.launch_button.config(state="normal")
        self.engine_on = False
        self.engine_button.config(text="Start Engine")
        self.update_status()

    def land(self):
        if not self.launched:
            messagebox.showinfo("Not Launched", "Rocket is already on the ground.")
            return
        self.status.set("Landing")
        self.log("Initiating landing sequence.")
        self.after(1000, self.perform_landing)

    def perform_landing(self):
        if self.altitude.get() > 0:
            new_altitude = max(0, self.altitude.get() - 50)
            self.altitude.set(new_altitude)
            self.speed.set(max(0, self.speed.get() - 5))
            self.consume_fuel(2)
            self.update_status()
            self.after(500, self.perform_landing)
        else:
            self.status.set("Landed")
            self.log("Rocket has landed safely.")
            self.launched = False
            self.abort_button.config(state="disabled")
            self.land_button.config(state="disabled")
            self.launch_button.config(state="normal")
            self.engine_on = False
            self.engine_button.config(text="Start Engine")

    def consume_fuel(self, amount):
        new_fuel = max(0, self.fuel_level.get() - amount)
        self.fuel_level.set(new_fuel)
        if new_fuel == 0:
            self.status.set("Out of Fuel")
            self.log("Fuel depleted!")
            self.engine_on = False
            self.engine_button.config(text="Start Engine")
            self.launch_button.config(state="disabled")
            self.abort_button.config(state="disabled")
            self.land_button.config(state="disabled")

    def update_flight(self):
        if not self.launched or not self.engine_on or self.fuel_level.get() <= 0:
            return
        # Increase altitude and speed
        self.altitude.set(self.altitude.get() + 100)
        self.speed.set(self.speed.get() + 20)
        self.consume_fuel(5)
        self.update_status()
        self.log(f"Altitude: {self.altitude.get()} m, Speed: {self.speed.get()} m/s, Fuel: {self.fuel_level.get()}%")
        if self.fuel_level.get() > 0:
            self.after(1000, self.update_flight)
        else:
            self.status.set("Out of Fuel - Freefall")
            self.log("Fuel exhausted during flight! Freefall initiated.")
            self.after(1000, self.freefall)

    def freefall(self):
        if self.altitude.get() > 0:
            new_altitude = max(0, self.altitude.get() - 150)
            self.altitude.set(new_altitude)
            self.speed.set(max(0, self.speed.get() + 30))
            self.update_status()
            self.log(f"Freefall Altitude: {self.altitude.get()} m, Speed: {self.speed.get()} m/s")
            self.after(500, self.freefall)
        else:
            self.status.set("Crashed")
            self.log("Rocket has crashed due to fuel exhaustion!")
            self.launched = False
            self.abort_button.config(state="disabled")
            self.land_button.config(state="disabled")
            self.launch_button.config(state="normal")

    def update_status(self):
            self.fuel_label.config(text=f"{self.fuel_level.get()}%")
            self.altitude_label.config(text=f"{self.altitude.get()} m")
            self.speed_label.config(text=f"{self.speed.get()} m/s")
            
if __name__ == "__main__":
    app = RocketShipInterface()
    app.mainloop()
            