-- SQL Queries for Genomic Analysis Database


-- SQLite Query 1 
SELECT 
    organism,
    COUNT(*) AS sample_count,
    ROUND(AVG(gc_content_pct), 2) AS avg_gc_content,
    ROUND(MAX(sequence_length), 0) AS max_length
FROM genomic_analysis
GROUP BY organism
ORDER BY avg_gc_content DESC; 

-- SQLite Query 2
SELECT sample_id, organism, gc_content_pct
FROM genomic_analysis
WHERE gc_content_pct > 50.0 
AND sequence_length BETWEEN 200 AND 800
ORDER BY gc_content_pct DESC;

-- SQLite Query 3
SELECT 
    data_source, 
    AVG(mw_gmol) AS average_molecular_weight
FROM genomic_analysis
GROUP BY data_source;

-- SQLite Query 4
SELECT sample_id, organism, mw_gmol, sequence_length
FROM genomic_analysis
ORDER BY mw_gmol DESC
LIMIT 5;

-- SQLite Query 5
SELECT sample_id, organism, gc_content_pct
FROM genomic_analysis
WHERE gc_content_pct < (SELECT AVG(gc_content_pct) FROM genomic_analysis)
ORDER BY gc_content_pct ASC
LIMIT 10;
