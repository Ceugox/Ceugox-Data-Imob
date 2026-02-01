CREATE OR REPLACE VIEW vw_real_estate_analysis AS
SELECT 
    city,
    CAST(
        REPLACE(
            REPLACE(
                SUBSTRING(raw_logs FROM 'R\$\s*([\d\.]+)'), 
            '.', ''), 
        ',', '.') 
    AS DECIMAL) AS price,
    CAST(SUBSTRING(raw_logs FROM '(\d+)\s*m²') AS INTEGER) AS area_sqm,
    CAST(SUBSTRING(raw_logs FROM '(\d+)\s*qt') AS INTEGER) AS bedrooms,
    TRIM(SPLIT_PART(raw_logs, '|', 1)) AS neighborhood_summary,
    raw_logs AS original_log
FROM staging_real_estate
WHERE raw_logs LIKE '%R$%';
