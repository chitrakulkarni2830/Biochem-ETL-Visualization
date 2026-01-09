# BioStream Analytics: End-to-End Genomic Data Pipeline



## 🧪 Project Overview
**BioStream Analytics** is a comprehensive data engineering and visualization workstation designed to bridge the gap between raw biochemistry research and actionable data insights. 

As a **MSc Biochemistry graduate**, I developed this project to demonstrate a complete **ETL (Extract, Transform, Load)** lifecycle using genomic data. The pipeline fetches real-time sequence data from the NCBI database, generates controlled synthetic datasets, stores them in a relational SQL database, and provides a GUI for instant biochemical analysis.

---

## 🚀 Key Features

### 1. Data Engineering (Python & API)
* **NCBI Integration:** Programmatically retrieves the Human Insulin (INS) gene sequence via the Entrez API to serve as a biological control.
* **Synthetic Data Generation:** Engineered a high-throughput generator to produce 99+ mock sequences with randomized but statistically relevant GC-content and molecular weights.
* **Biochemical Calculations:** Custom algorithms for $O(1)$ codon translation, Molecular Weight estimation, and GC-content percentage calculation.

### 2. Relational Database Management (SQL)
* **Structured Storage:** Automatically builds and populates an SQLite database (`BioResearch.db`).
* **Analytical Querying:** Includes a suite of SQL scripts for organism profiling, stability filtering, and quality control (QC) anomaly detection.

### 3. User Interface (CustomTkinter)
* **Modern GUI:** A dark-themed, industrial-grade workstation for manual DNA input and FASTA file parsing.
* **Automated Reporting:** Generates timestamped `.txt` laboratory reports for documentation and audit trails.

### 4. Visualization (Tableau)
* **Insights Dashboard:** Integrated CSV/SQL outputs with Tableau to visualize nucleotide distributions, sequence length histograms, and GC-stability scatter plots.

---

## 🧬 Scientific Methodology
The pipeline handles DNA sequences using the following monophosphate weight constants:
- **Adenine (A):** 313.21 g/mol
- **Thymine (T):** 304.19 g/mol
- **Cytosine (C):** 289.18 g/mol
- **Guanine (G):** 329.21 g/mol

$$MW = \sum (w_{base} \times n_{base}) + 79.0$$



---

## 🛠️ Tech Stack
* **Languages:** Python 3.10+, SQL (SQLite)
* **Libraries:** `Pandas` (Data Manipulation), `Requests` (API calls), `CustomTkinter` (GUI), `SQLite3` (Database)
* **Tools:** Tableau Public, VS Code, Git

---

## 📂 Repository Structure
```text
├── app/
│   └── biostream_pro.py        # Main GUI Application
├── scripts/
│   ├── data_generator.py       # API Fetching & Mock Data Logic
│   ├── db_loader.py            # CSV to SQL Database Migration
│   └── run_queries.py          # Analytical SQL Suite
├── data/
│   ├── genomic_batch_results.csv
│   └── BioResearch.db          # Relational Database File
├── README.md
└── requirements.txt            # Dependency list

---

## 📦 Installation & Usage
Clone the repo:
git clone [https://github.com/YourGitHubUsername/BioStream-Analytics.git](https://github.com/YourGitHubUsername/BioStream-Analytics.git)

Install dependencies:
pip install -r requirements.txt

Run the pipeline:
Run scripts/data_generator.py to fetch/generate data.
Run scripts/db_loader.py to create the SQL database.
Run app/biostream_pro.py to launch the GUI workstation.