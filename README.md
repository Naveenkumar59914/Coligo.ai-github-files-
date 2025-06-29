# Coligo AI Design Challenge 2025 – Phase 2
## Project Title: Energy Leakage Detection in Industrial Plants Using OPC UA and AI

### Overview
This project simulates real-time energy usage from an industrial environment using a Python-based OPC UA server. The generated data is then visualized using Matrikon OPC UA Explorer and prepared for anomaly detection through the Coligo AI platform.

### Contents
- `energy_opcua_server.py` – Python OPC UA server that generates random energy values
- `energy_log_sample.csv` – Sample CSV format to be uploaded to Coligo
- `screenshots/` – Images showing simulation output and Matrikon validation

### How to Run
1. Install required package:
```bash
pip install opcua
```
2. Run the simulation:
```bash
python energy_opcua_server.py
```
3. Observe output in terminal and verify in Matrikon.
4. Use the generated CSV file to upload to Coligo.ai for AI-based analysis.

### Status
✅ Phase 2 Simulation Complete  
⏳ Coligo AI Upload & ML Model – To be demonstrated in Phase 3

### License
MIT
