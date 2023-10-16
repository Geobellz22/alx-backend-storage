-- script that list all bands with Glam rock
-- ranked by their longevity

SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan from metal_bands,
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
