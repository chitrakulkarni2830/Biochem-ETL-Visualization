import pandas as pd
import sqlite3
import os

def create_and_load_db():
    csv_file = "genomic_batch_results.csv"
    db_file = "BioResearch.db"

    # 1. Check if the CSV exists
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found. Run your data generator script first!")
        return

    # 2. Load the CSV into a Pandas DataFrame
    df = pd.DataFrame()
    df = pd.read_csv(csv_file)
    
    # Rename CSV columns to match table schema
    df.rename(columns={
        'Sample_ID': 'sample_id',
        'Source': 'data_source',
        'Organism': 'organism',
        'Sequence_Length': 'sequence_length',
        'GC_Content_Pct': 'gc_content_pct',
        'MW_gMol': 'mw_gmol',
        'Sequence': 'sequence'
    }, inplace=True)

    # 3. Connect to SQLite (This creates the .db file automatically)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # 4. Create the Table with proper Bio-Data types
    cursor.execute("DROP TABLE IF EXISTS genomic_analysis")
    create_table_sql = """
    CREATE TABLE genomic_analysis (
        sample_id TEXT PRIMARY KEY,
        data_source TEXT,
        organism TEXT,
        sequence_length INTEGER,
        gc_content_pct REAL,
        mw_gmol REAL,
        sequence TEXT
    );
    """
    cursor.execute(create_table_sql)

    # 5. Load the DataFrame into the SQL Table
    df.to_sql("genomic_analysis", conn, if_exists="append", index=False)

    # 6. Verify the data
    cursor.execute("SELECT COUNT(*) FROM genomic_analysis")
    count = cursor.fetchone()[0]

    conn.close()
    print(f"✅ Success! Created {db_file}")
    print(f"📊 {count} genomic records have been loaded into the SQL table.")

if __name__ == "__main__":
    create_and_load_db()
    