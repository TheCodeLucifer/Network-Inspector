# Network Inspector & Speed Checker 🌐⚡

An easy-to-use Python utility that automatically detects your connection type (Wi-Fi or Ethernet), retrieves your ISP details, tests download/upload speeds, calculates ping, checks for packet loss, and prints a beautiful formatted status table refreshed in real time.

---

## 📌 Features

- **Connection Type Detection:** Automatically checks whether you are connected via Wi-Fi or Ethernet cable (supports Windows & Linux).
- **ISP & IP Information:** Retrieves your ISP (Internet Service Provider), Public IP address, and Local IP address.
- **Speed Test:** Measures Download speed (Mbps), Upload speed (Mbps), and Ping latency (ms).
- **Packet Loss Test:** Performs a ping test to `8.8.8.8` to calculate packet loss percentage.
- **Live Auto-Refresh:** Automatically re-checks and refreshes the network status table every 10 seconds.
- **User-Friendly CLI Display:** Uses colored output and formatted ASCII tables for maximum readability.

---

## 📋 Prerequisites

Before installing, ensure you have Python installed on your system:

- **Python 3.8 or higher**
- **pip** (Python package installer)

> 💡 *Not sure if Python is installed?* Open your Command Prompt (Windows) or Terminal (macOS/Linux) and type:
> ```bash
> python --version
> ```
> or
> ```bash
> python3 --version
> ```

---

## 🚀 Installation Guide (Step-by-Step)

Follow these simple instructions to download and set up the project on your computer.

### Step 1: Clone or Download the Repository

**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/your-username/network-inspector.git
cd network-inspector
```

**Option B: Manual Download**
1. Click the green **Code** button at the top of this GitHub repository page.
2. Click **Download ZIP**.
3. Extract the downloaded ZIP file to any folder on your computer.
4. Open Command Prompt / Terminal and navigate into that extracted folder:
   ```bash
   cd path/to/extracted-folder
   ```

---

### Step 2: (Optional but Recommended) Create a Virtual Environment

Creating a virtual environment keeps your project dependencies organized and avoids conflicts with other Python projects.

- **On Windows:**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

- **On macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

---

### Step 3: Install Required Dependencies

Install all necessary packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 💻 How to Run

Once all dependencies are installed, run the script with:

```bash
python main.py
```
*(If `python` doesn't work on macOS/Linux, try `python3 main.py`)*

To stop the program at any time, press `Ctrl + C` in your terminal window.

---

## 📦 Project Structure

```text
network-inspector/
├── main.py             # Main script for network monitoring
├── requirements.txt    # List of required Python packages
└── README.md           # Project documentation and guide
```

---

## 📄 Dependencies (`requirements.txt`)

Here are the required external libraries used in this project:

- `colorama` — Adds colorized terminal output.
- `prettytable` — Formats network parameters into neat ASCII tables.
- `requests` — Handles HTTP requests to fetch public IP and ISP information.
- `speedtest-cli` — Performs internet upload/download speed and ping tests.

---

## 🛡️ License

This project is open source and available under the [MIT License](LICENSE).
