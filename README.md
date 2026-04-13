# Secure Centralized EV Charging Payment Gateway
## BITS F463 Cryptography — Term Project 2025-26

---

## Team Members

- **Name:** Saniya Shahi | **ID:** 2022A8PS0810H  
- **Name:** Kumar Shivansh Sinha | **ID:** 2022B1AA1227H  
- **Name:** Surbhit Jain | **ID:** 2022B3A70868H  
- **Name:** Rickpoul Ghosh | **ID:** 2022AAPS1549H  
- **Name:** Gaurvi Khurana | **ID:** 2023A7PS0035H  

---

## Project Overview

A simulated end-to-end EV charging payment system integrating:
- **ASCON-128** (Lightweight Cryptography) — encrypts Franchise ID in QR codes
- **RSA + Shor's Algorithm** (Quantum Cryptography) — encrypts user credentials and demonstrates quantum vulnerability
- **SHA3-256 Blockchain** — immutable ledger of all charging transactions

### Entities
| Entity | Role |
|---|---|
| Grid Authority | Central server — registers users/franchises, processes payments, maintains blockchain |
| Franchise | Charging station operator — receives QR code, unlocks hardware on success |
| EV Owner | Initiates session by scanning QR, provides VMID + PIN + amount |
| Charging Kiosk | Encrypts FID → QR, relays transaction to Grid |

---

## Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Grid Authority server (in one terminal)
```bash
uvicorn backend.main:app --reload --port 8000
```

### 3. Run the simulation (in another terminal)
```bash
python main_flow.py
```

---

## Project Structure
```
ev-charging-gateway/
├── backend/
│   └── main.py           # FastAPI Grid Authority server
├── blockchain/
│   ├── block.py          # Block with SHA3-256 hash (json-canonical)
│   └── blockchain.py     # Chain with integrity verification
├── crypto/
│   ├── ascon.py          # ASCON-128 lightweight encryption (IoT/kiosk)
│   ├── rsa_sim.py        # RSA-2048 for credential transmission
│   ├── qiskit_shor.py    # Shor's Algorithm simulation (quantum attack demo)
│   └── sha3_hash.py      # SHA3-256 / Keccak-256 ID generation
├── kiosk/
│   └── kiosk.py          # VFID generation, ASCON encrypt/decrypt, QR
├── user/
│   └── user_app.py       # RSA-encrypted credential submission
├── utils/
│   ├── helpers.py        # VMID generation (UID + full mobile)
│   └── qr.py             # QR code image generation
├── main_flow.py          # Full simulation runner
└── requirements.txt
```

---

## Key Design Decisions & Assumptions

### Cryptography
- **ASCON-128** with a random 16-byte nonce per message (nonce prepended to ciphertext for recovery). Key stored as a constant for demo; production should use a KDF or HSM.
- **SHA3-256** used for UID/FID generation. True Keccak-256 (Ethereum-style) is available via `generate_id_keccak()` in `sha3_hash.py` if `pycryptodome` is installed.
- **RSA-2048** encrypts the VMID+PIN bundle before network transmission. The Shor's demo factors a smaller modulus (N=3233) to show the same attack scales.

### VMID
- VMID = UID (16 hex chars) + full mobile number. Using the full number (not just last 4 digits) ensures global uniqueness.

### PIN vs Password
- Registration password is used only to derive the UID. A separate PIN is stored for authorizing every charge transaction.

### Blockchain
- Block hash uses `json.dumps(sort_keys=True)` for deterministic serialization across Python versions.
- Transaction ID = SHA3-256(UID + FID + timestamp + amount) per spec §6.
- Every block includes a `dispute_flag` (bool). Refund/reverse blocks set it to `True`.

### Edge Cases Handled
- **Insufficient balance**: transaction rejected before any balance change.
- **Invalid FID**: rejected at Grid before processing.
- **Invalid PIN**: rejected at Grid.
- **Hardware failure after payment**: `hardware_failure` flag in `process_transaction()`. When `True`, balances are reversed and a refund block with `dispute_flag=True` is appended.
- **Account closure mid-session**: assumed not possible in current implementation (no account deletion endpoint). Documented as out of scope for demo.

### Grid Zones
- 3 providers: TataPower, Adani, ChargePoint
- 3 zones each: e.g. TP-NORTH, TP-SOUTH, TP-WEST
- Both users and franchises must register with a valid zone_code.

---

## Quantum Attack Summary

Shor's algorithm finds the period `r` of `f(x) = a^x mod N`, allowing factorization of RSA moduli in polynomial time on a quantum computer. The demo:
1. Sets up a small RSA key (N=3233, e=17)
2. Runs Shor's period-finding (classical simulation, or Qiskit circuit for N=15)
3. Recovers `p`, `q`, and reconstructs private key `d`
4. Concludes that RSA-encrypted EV credential transmissions are quantum-breakable