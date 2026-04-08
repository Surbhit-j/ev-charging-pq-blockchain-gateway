# Secure Centralized EV Charging Payment Gateway using Post-Quantum and Lightweight Cryptography

---

## Project Overview

This project implements a **secure, centralized EV charging payment system** that simulates real-world smart grid transactions. It integrates **Blockchain**, **Lightweight Cryptography (LWC)**, and **Post-Quantum Cryptography concepts** to ensure secure, verifiable, and tamper-resistant energy transactions.

The system models three key entities:

* **EV Owner (User Device)**
* **Charging Kiosk**
* **Grid Authority (Central Server)**

Each entity is implemented as a separate module and interacts through a structured transaction flow.

---

## Key Features

* **SHA-3 (Keccak-256) based UID & FID generation**
* **Lightweight Cryptography (ASCON – simulated)** for QR encryption
* **QR Code-based payment initiation**
* **Blockchain ledger** for immutable transaction storage
* **Secure transaction validation** (VMID, PIN, balance)
* **Quantum attack simulation (Shor’s Algorithm)** to demonstrate RSA vulnerability
* **Refund handling and edge case support**

---

## System Architecture

```
User Device → Charging Kiosk → Grid Authority → Blockchain
```

### Entity Responsibilities

* **User Device (`user/user_app.py`)**

  * Inputs VMID, PIN, amount
  * Initiates transaction

* **Charging Kiosk (`kiosk/kiosk.py`)**

  * Generates encrypted QR (VFID)
  * Decrypts scanned data

* **Grid Authority (`backend/main.py`)**

  * Registers users & franchises
  * Validates transactions
  * Updates balances
  * Maintains blockchain ledger

* **Blockchain (`blockchain/`)**

  * Stores immutable transaction records

---

## Cryptographic Components

### 1. SHA-3 Hashing

Used for:

* User ID (UID)
* Franchise ID (FID)
* Transaction ID

### 2. Lightweight Cryptography (ASCON)

* Used to encrypt Franchise ID into QR codes
* **Note:** ASCON is simulated using XOR-based encryption for simplicity

### 3. Quantum Cryptography (Simulation)

* Demonstrates vulnerability of RSA using **Shor’s Algorithm (simulated)**

---

## Blockchain Structure

Each block contains:

* Transaction ID (SHA-3 hash)
* VMID, FID, Amount
* Timestamp
* Status (success/refund)
* Previous Block Hash
* Current Hash

Ensures:

* Immutability
* Transparency
* Tamper-resistance

---

## How to Run the Project

### 1️. Activate Virtual Environment

```bash
evcrypto_env\Scripts\activate   # Windows
```

---

### 2️. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Start Backend Server

```bash
uvicorn backend.main:app --reload
```

---

### 4️. Run Simulation

Open a new terminal and run:

```bash
python main_flow.py
```

---

## Sample Flow

1. User & Franchise are registered
2. Kiosk generates encrypted QR
3. User enters VMID, PIN, amount
4. Kiosk decodes QR → sends to Grid
5. Grid validates and processes transaction
6. Blockchain records transaction
7. Quantum vulnerability demonstration shown

---

## Assumptions & Simplifications

* ASCON is **simulated** using XOR-based encryption due to implementation complexity
* PIN is transmitted in plain form for simplicity (can be hashed in real systems)
* Blockchain is **centralized and in-memory**
* Quantum attack is demonstrated via simulation, not full implementation

---

## Learning Outcomes

* Understanding of **modern cryptographic systems**
* Integration of **blockchain with real-world applications**
* Exposure to **post-quantum cryptography concepts**
* Designing **secure distributed system simulations**

---

## Team Details

- **Name:** Saniya Shahi | **ID:** 2022A8PS0810H  
- **Name:** Kumar Shivansh Sinha | **ID:** 2022B1AA1227H  
- **Name:** Surbhit Jain | **ID:** 2022B3A70868H  
- **Name:** Rickpoul Ghosh | **ID:** 2022AAPS1549H  
- **Name:** Gaurvi Khurana | **ID:** 2023A7PS0035H  

---

## Conclusion

This project successfully demonstrates a **secure EV charging payment ecosystem** integrating cryptographic primitives, blockchain technology, and quantum-aware security considerations, aligned with modern smart-grid requirements.

