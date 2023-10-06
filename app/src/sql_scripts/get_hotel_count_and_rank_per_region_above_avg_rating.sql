WITH region AS (
    SELECT
        id,
        LEFT(zip, 2) AS num
    FROM dim_adress
),
avg_star AS (
    SELECT
        ROUND(AVG(star), 2) AS value
    FROM fact_hotel
),
hotel_data AS (
    SELECT
        region.num AS region_num,
        COUNT(CASE WHEN fh.star > avg_star.value THEN 1 END) as hotel_count,
        DENSE_RANK() OVER (ORDER BY COUNT(CASE WHEN fh.star > avg_star.value THEN 1 END) DESC) AS region_rank
    FROM fact_hotel AS fh
    JOIN region ON fh.adress_id = region.id,
        avg_star
    GROUP BY region.num
)
SELECT
    region_num,
    hotel_count,
    region_rank
FROM hotel_data
WHERE region_rank <= %(rank)s;
