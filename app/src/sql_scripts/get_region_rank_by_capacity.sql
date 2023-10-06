WITH region AS (
    SELECT
        id,
        LEFT(zip, 2) AS num
    FROM dim_adress
),
region_capacity AS (
    SELECT
        region.num AS region_num,
        SUM(di.capacity) AS capacity_nb,
        DENSE_RANK() OVER (ORDER BY SUM(di.capacity) DESC) AS capacity_rank
    FROM fact_hotel AS fh
    JOIN region ON fh.adress_id = region.id
    JOIN dim_info AS di ON fh.info_id = di.id
    GROUP BY region.num
)
SELECT
    region_num,
    capacity_nb
FROM region_capacity
WHERE capacity_rank <= %(rank)s;
