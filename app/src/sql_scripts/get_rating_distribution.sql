SELECT
    star,
    count(*) AS frequency
FROM fact_hotel
GROUP BY star
ORDER BY star;
