SELECT
    di.name AS name,
    da.city AS city,
    fh.star,
    DENSE_RANK() OVER (PARTITION BY da.city ORDER BY fh.star DESC) AS star_rank
FROM fact_hotel AS fh
JOIN dim_info AS di ON fh.info_id = di.id
JOIN dim_adress AS da ON fh.adress_id = da.id
WHERE da.city = %(city)s;
