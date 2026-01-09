-- Create the genomic results table
CREATE TABLE genomic_analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sample_id VARCHAR(50) NOT NULL,
    data_source VARCHAR(100),
    organism VARCHAR(100),
    sequence_length INT,
    gc_content_pct DECIMAL(5, 2),
    mw_gmol DECIMAL(10, 2),
    sequence TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexing for performance (Standard practice in Data Analytics)
CREATE INDEX idx_organism ON genomic_analysis(organism);
CREATE INDEX idx_gc_content ON genomic_analysis(gc_content_pct);
̦̦