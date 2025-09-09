# Assignment 1 – Mini Weather Prediction (Socket Programming)

This project is a **mini weather prediction game** developed as part of the **Computer Networks** course.  
It demonstrates **client-server communication** using Python sockets with tolerance-based validation, disconnection handling, and continuous server listening.  

---

## 📖 Project Overview
The server loads weather data (city names and temperatures) from an Excel file and randomly selects one city.  
The client must **guess the temperature** of that city within a **10% tolerance margin**.  

- If the guess is correct → the server replies with **Success** 🎉  
- If the guess is wrong → the server gives hints (**Higher / Lower**)  
- If the client fails 3 times → the server reveals the correct answer  
- If the client types **END** → the connection is terminated safely  

After each session, the **server remains open** for new client connections.  

---

## ⚙️ Features

### 🔹 Server (server.py)
- Loads weather data from `weathers.xlsx`  
- Selects a random city and sends it to the client  
- Validates client guesses with 10% tolerance  
- Provides real-time feedback:  
  - ✅ *Success* (within tolerance)  
  - 🔼 *Higher* / 🔽 *Lower* hints  
- Ends the game after 3 failed attempts  
- Handles **END command** to terminate connection gracefully  
- Robust error handling with `traceback`  

### 🔹 Client (client.py)
- Connects to server at `localhost:8888`  
- Receives city name and sends temperature guesses  
- Displays feedback from server in real-time  
- Ends session on:  
  - Correct guess  
  - 3 failed attempts  
  - User entering `"END"`  

---

## 🖥️ How to Run

### 1. Install Requirements
Make sure you have **Python 3.8+** installed and install dependencies:
```bash
pip install openpyxl
```

### 2. Start the Server
```bash
python server.py
```

### 3. Start the Client
In another terminal:
```bash
python client.py
```

### 4. Gameplay
- The client receives a random city.  
- Enter your temperature guess (integer).  
- Receive feedback until you:  
  - Guess correctly ✅  
  - Fail 3 times ❌  
  - Enter `"END"` ⏹️  

---

## 📂 File Structure
```
Assignment1/
│── server.py         # Server-side logic
│── client.py         # Client-side logic
│── weathers.xlsx     # Dataset: Cities & temperatures
│── README.md         # Project documentation
```

---

## 📸 Example Outputs
- **Correct Guess:**  
  ```
  Success! The temperature is correct.
  ```
- **Incorrect Guess (Lower):**  
  ```
  Wrong guess. Try Higher.
  ```
- **Incorrect Guess (Higher):**  
  ```
  Wrong guess. Try Lower.
  ```
- **End Command:**  
  ```
  Connection closed by client.
  ```

---

## 🛠️ Technologies Used
- **Python** – Core programming language  
- **Sockets** – Client-server communication  
- **openpyxl** – Handling Excel data (`weathers.xlsx`)  

---

## 🎓 Note
This project was developed as part of **CMPE 472 – Computer Networks** course at university.  
It serves as a practical demonstration of socket programming concepts.  
