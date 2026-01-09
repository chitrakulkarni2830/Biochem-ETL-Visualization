# BioStream Analytics: End-to-End Genomic Data Pipeline

![Genomic Dashboard Preview](https://via.placeholder.com/800x400.png?text=Place+Your+Dashboard+Screenshot+Here)


## 🧪 Project Overview
**BioStream Analytics** is a high-performance data engineering and visualization workstation. As a **MSc Biochemistry graduate** transitioning into **Data Analytics**, I developed this project to demonstrate a complete **ETL (Extract, Transform, Load)** lifecycle using complex biological data.

The pipeline automates the journey from raw genetic code to laboratory insights by integrating real-time API fetching, synthetic data engineering, relational database management, and interactive visual analytics.

---

## 🚀 Key Features

### 1. Data Engineering (Python & API)
* **NCBI Integration:** Programmatically retrieves the **Human Insulin (INS) gene** sequence via the Entrez API to serve as a biological gold-standard control.
* **Synthetic Data Generation:** A high-throughput generator produces 99+ mock sequences with randomized but statistically relevant GC-content and molecular weights.
* **Biochemical Engine:** Custom algorithms perform $O(1)$ codon translation, Molecular Weight ($MW$) estimation, and GC-content percentage calculation.

### 2. Relational Database Management (SQL)
* **Structured Storage:** Automatically builds and populates a local SQLite database (`BioResearch.db`) from processed sequence data.
* **Analytical Suite:** Includes optimized SQL queries for organism profiling, stability filtering, and quality control (QC) anomaly detection.

### 3. User Interface (CustomTkinter)
* **Genomic Workstation:** A modern, dark-themed GUI built for laboratory environments to allow manual DNA input, FASTA file parsing, and instant metric calculation.
* **Automated Reporting:** Generates timestamped `.txt` reports for professional documentation and audit trails.

### 4. Visual Analytics (Tableau)
* **QC Dashboard:** A 4-panel interactive dashboard visualizing species distribution, fragment length histograms, and GC-stability clusters.

---

## 🧬 Scientific Methodology
The pipeline calculates the molecular mass of single-stranded DNA using monophosphate weight constants:
- **Adenine (A):** 313.21 g/mol
- **Thine (T):** 304.19 g/mol
- **Cytosine (C):** 289.18 g/mol
- **Guanine (G):** 329.21 g/mol

The formula applied is:
$$MW = \sum (w_{base} \times n_{base}) + 79.0$$
*Where 79.0 accounts for the terminal phosphate/water adjustment.*

---

## 🛠️ Tech Stack
* **Languages:** Python 3.10+, SQL (SQLite)
* **Libraries:** `Pandas` (Data Processing), `Requests` (API calls), `CustomTkinter` (GUI), `SQLite3` (Database)
* **Visualization:** Tableau Public
* **Environment:** VS Code, Git

---

## 📂 Repository Structure
```text
├── app/
│   └── biostream_pro.py        # Main GUI Application Workstation
├── scripts/
│   ├── data_generator.py       # API Fetching & Mock Data Logic
│   ├── db_loader.py            # CSV to SQL Database Migration
│   └── run_queries.py          # Analytical SQL Suite (5 Queries)
├── data/
│   ├── genomic_batch_results.csv
│   └── BioResearch.db          # Relational Database File
├── README.md
└── requirements.txt            # Project dependencies