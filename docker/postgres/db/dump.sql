--
-- Structure de la table `dim_info`
--

CREATE TABLE IF NOT EXISTS dim_info (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "name" TEXT NOT NULL,
    "room" INT NOT NULL,
    "capacity" INT NOT NULL
);

--
-- Structure de la table `dim_adress`
--

CREATE TABLE IF NOT EXISTS dim_adress (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "adress" TEXT NOT NULL,
    "zip" TEXT NOT NULL,
    "city" TEXT NOT NULL,
    "concat" TEXT NOT NULL
);

--
-- Structure de la table `dim_location`
--

CREATE TABLE IF NOT EXISTS dim_location (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "latitude" DOUBLE PRECISION NOT NULL,
    "longitude" DOUBLE PRECISION NOT NULL,
    "x" DOUBLE PRECISION NOT NULL,
    "y" DOUBLE PRECISION NOT NULL
);

--
-- Structure de la table `dim_date`
--

CREATE TABLE IF NOT EXISTS dim_date (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "date" TEXT NOT NULL,
    "day" INT NOT NULL,
    "month" INT NOT NULL,
    "year" INT NOT NULL
);

--
-- Structure de la table `fact_hotel`
--

CREATE TABLE IF NOT EXISTS fact_hotel (
    "id" INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "info_id" INT NOT NULL REFERENCES dim_info("id") ON DELETE CASCADE,
    "adress_id" INT NOT NULL REFERENCES dim_adress("id") ON DELETE CASCADE,
    "location_id" INT NOT NULL REFERENCES dim_location("id") ON DELETE CASCADE,
    "date_id" INT NOT NULL REFERENCES dim_date("id") ON DELETE CASCADE,
    "star" INT NOT NULL
);
