import pandas as pd
import random
import requests
import io

def get_ncbi_control():
    """Fetches the Human Insulin (INS) gene sequence from NCBI as a control."""
    print("Fetching real control data from NCBI (Human Insulin Gene)...")
    # NCBI E-utils URL for Human Insulin (NM_000207)
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NM_000207&rettype=fasta&retmode=text"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            lines = response.text.splitlines()
            sequence = "".join([line.strip() for line in lines if not line.startswith(">")])
            return sequence
    except Exception as e:
        print(f"Connection failed: {e}. Using hardcoded control.")
    
    # Fallback sequence if API is down
    return "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACT"

def calculate_metrics(sequence):
    """Standard biochemical calculations."""
    length = len(sequence)
    gc_content = (sequence.count('G') + sequence.count('C')) / length * 100
    mw = (sequence.count('A') * 313.2) + (sequence.count('T') * 304.2) + \
         (sequence.count('C') * 289.2) + (sequence.count('G') * 329.2) + 79.0
    return length, round(gc_content, 2), round(mw, 2)

def generate_dataset():
    data = []
    
    # 1. ADD THE CONTROL (Real Data)
    control_seq = get_ncbi_control()
    length, gc, mw = calculate_metrics(control_seq)
    data.append({
        "Sample_ID": "CONTROL-INS-01",
        "Source": "NCBI (NM_000207)",
        "Organism": "H. sapiens",
        "Sequence_Length": length,
        "GC_Content_Pct": gc,
        "MW_gMol": mw,
        "Sequence": control_seq
    })

    # 2. ADD THE MOCK SAMPLES (99 Synthetic)
    bases = ['A', 'T', 'C', 'G']
    organisms = ['E. coli', 'S. cerevisiae', 'B. subtilis', 'D. rerio']
    
    for i in range(1, 100):
        mock_len = random.randint(100, 1000)
        mock_seq = "".join(random.choices(bases, k=mock_len))
        length, gc, mw = calculate_metrics(mock_seq)
        
        data.append({
            "Sample_ID": f"MOCK-{i:03d}",
            "Source": "Synthetic_Generator",
            "Organism": random.choice(organisms),
            "Sequence_Length": length,
            "GC_Content_Pct": gc,
            "MW_gMol": mw,
            "Sequence": mock_seq
        })

    # 3. CONVERT AND SAVE
    df = pd.DataFrame(data)
    df.to_csv("genomic_batch_results.csv", index=False)
    print(f"\nSuccessfully generated 'genomic_batch_results.csv'")
    print(f"Total Records: {len(df)}")
    print(f"Control Entry: {df.iloc[0]['Sample_ID']} is ready for Tableau.")

if __name__ == "__main__":
    # Ensure requests is installed: pip install requests pandas
    generate_dataset()