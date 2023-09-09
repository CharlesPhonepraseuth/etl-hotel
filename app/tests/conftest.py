# Third party imports
import pytest
import polars as pl


###                    ###
### Relative to places ###
###                    ###
@pytest.fixture
def places_df():
    data = {
        "id":                           ["05168_l211jp", "06103_0668"],
        "nom_lieu_dit":                 ["Le Village", "Avenue de Verdun"],
        "code_postal":                  ["05130", "06450"],
        "code_insee":                   ["05168", "06130"],
        "nom_commune":                  ["Sigoyer", "Roquebillière"],
        "code_insee_ancienne_commune":  ["05168", "06130"],
        "nom_ancienne_commune":         ["Sigoyer", "Roquebillière"],
        "x":                            [936688.03, 1045428.48],
        "y":                            [6379851.51, 6334210.96],
        "lon":                          [5.97663, 7.310561],
        "lat":                          [44.477565, 44.022023],
        "source_position":              ["bal", "bal"],
        "source_nom_voie":              ["bal", "bal"]
    }
    return pl.DataFrame(data).lazy()


@pytest.fixture
def processed_places_df():
    data = {
        "id":                           ["05168_l211jp", "06103_0668"],
        "nom_lieu_dit":                 ["Le Village", "Avenue de Verdun"],
        "code_postal":                  ["05130", "06450"],
        "code_insee":                   ["05168", "06130"],
        "nom_commune":                  ["Sigoyer", "Roquebillière"],
        "code_insee_ancienne_commune":  ["05168", "06130"],
        "nom_ancienne_commune":         ["Sigoyer", "Roquebillière"],
        "x":                            [936688.03, 1045428.48],
        "y":                            [6379851.51, 6334210.96],
        "lon":                          [5.97663, 7.310561],
        "lat":                          [44.477565, 44.022023],
        "source_position":              ["bal", "bal"],
        "source_nom_voie":              ["bal", "bal"],
        "concat":                       ["le+village+05130+sigoyer", "avenue+de+verdun+06450+roquebillière"]
    }
    return pl.DataFrame(data)


@pytest.fixture
def invalid_processed_places_df():
    data = {
        "id":                           ["05168_l211jp", "06103_0668"],
        "nom_lieu_dit":                 ["Le Village", "Avenue de Verdun"],
        "code_postal":                  ["05130", "06450"],
        "code_insee":                   ["05168", "06130"],
        "nom_commune":                  ["Sigoyer", "Roquebillière"],
        "code_insee_ancienne_commune":  ["05168", "06130"],
        "nom_ancienne_commune":         ["Sigoyer", "Roquebillière"],
        "x":                            [936688.03, 1045428.48],
        "y":                            [6379851.51, 6334210.96],
        "lon":                          [5.97663, 7.310561],
        "lat":                          [44.477565, 44.022023],
        "source_position":              ["bal", "bal"],
        "source_nom_voie":              ["bal", "bal"],
        "concat":                       ["levillage05130sigoyer", None] # wrong concat
    }
    return pl.DataFrame(data)


###                     ###
### Relative to streets ###
###                     ###
@pytest.fixture
def streets_df():
    data = {
        "id":                           ["06088_6770_00091", "06088_6223_00006"],
        "id_fantoir":                   ["06088_6770", "06088_6223"],
        "numero":                       ["91", "6"],
        "rep":                          ["", ""],
        "nom_voie":                     ["Voie Romaine", "Rue du Sicou"],
        "code_postal":                  ["06000", "06300"],
        "code_insee":                   ["06088", "06088"],
        "nom_commune":                  ["Nice", "Nice"],
        "code_insee_ancienne_commune":  ["", ""],
        "nom_ancienne_commune":         ["", ""],
        "x":                            [1044787.64, 046142.8],
        "y":                            [6300795.35, 6302984.86],
        "lon":                          [7.28, 7.298267],
        "lat":                          [43.722067, 43.741078],
        "type_position":                ["entrée", "entrée"],
        "alias":                        ["", ""],
        "nom_ld":                       ["", ""],
        "libelle_acheminement":         ["NICE", "NICE"],
        "nom_afnor":                    ["VOIE ROMAINE", "RUE DU SICOU"],
        "source_position":              ["commune", "commune"],
        "source_nom_voie":              ["commune1", "commune1"],
        "certification_commune":        [1, 1],
        "cad_parcelles":                ["", ""]
    }
    return pl.DataFrame(data).lazy()


@pytest.fixture
def processed_streets_df():
    data = {
        "id":                           ["06088_6770_00091", "06088_6223_00006"],
        "id_fantoir":                   ["06088_6770", "06088_6223"],
        "numero":                       ["91", "6"],
        "rep":                          ["", ""],
        "nom_voie":                     ["Voie Romaine", "Rue du Sicou"],
        "code_postal":                  ["06000", "06300"],
        "code_insee":                   ["06088", "06088"],
        "nom_commune":                  ["Nice", "Nice"],
        "code_insee_ancienne_commune":  ["", ""],
        "nom_ancienne_commune":         ["", ""],
        "x":                            [1044787.64, 046142.8],
        "y":                            [6300795.35, 6302984.86],
        "lon":                          [7.28, 7.298267],
        "lat":                          [43.722067, 43.741078],
        "type_position":                ["entrée", "entrée"],
        "alias":                        ["", ""],
        "nom_ld":                       ["", ""],
        "libelle_acheminement":         ["NICE", "NICE"],
        "nom_afnor":                    ["VOIE ROMAINE", "RUE DU SICOU"],
        "source_position":              ["commune", "commune"],
        "source_nom_voie":              ["commune1", "commune1"],
        "certification_commune":        [1, 1],
        "cad_parcelles":                ["", ""],
        "concat":                       ["91+voie+romaine+06000+nice", "6+rue+du+sicou+06300+nice"]
    }
    return pl.DataFrame(data)


@pytest.fixture
def invalid_processed_streets_df():
    data = {
        "id":                           ["06088_6770_00091", "06088_6223_00006"],
        "id_fantoir":                   ["06088_6770", "06088_6223"],
        "numero":                       ["91", "6"],
        "rep":                          ["", ""],
        "nom_voie":                     ["Voie Romaine", "Rue du Sicou"],
        "code_postal":                  ["06000", "06300"],
        "code_insee":                   ["06088", "06088"],
        "nom_commune":                  ["Nice", "Nice"],
        "code_insee_ancienne_commune":  ["", ""],
        "nom_ancienne_commune":         ["", ""],
        "x":                            [1044787.64, 046142.8],
        "y":                            [6300795.35, 6302984.86],
        "lon":                          [7.28, 7.298267],
        "lat":                          [43.722067, 43.741078],
        "type_position":                ["entrée", "entrée"],
        "alias":                        ["", ""],
        "nom_ld":                       ["", ""],
        "libelle_acheminement":         ["NICE", "NICE"],
        "nom_afnor":                    ["VOIE ROMAINE", "RUE DU SICOU"],
        "source_position":              ["commune", "commune"],
        "source_nom_voie":              ["commune1", "commune1"],
        "certification_commune":        [1, 1],
        "cad_parcelles":                ["", ""],
        "concat":                       ["91voieromaine06000", None] # wrong concat
    }
    return pl.DataFrame(data)


###                          ###
### Relative to accommodation ###
###                          ###
@pytest.fixture
def accommodation_df():
    data = {
        "DATE DE CLASSEMENT":                       ["18/11/2014", "12/07/2016"],
        "DATE DE PUBLICATION DE L'ÉTABLISSEMENT":   ["18/11/2014", None],
        "TYPE D'HÉBERGEMENT":                       ["HÔTEL DE TOURISME", "CAMPING"],
        "CLASSEMENT":                               ["2 étoiles", "4 étoiles"],
        "CATÉGORIE":                                ["TOURISME", "LOISIRS"],
        "MENTION":                                  ["HÔTEL", "CAMPING"],
        "NOM COMMERCIAL":                           ["HÔTEL CHRISTIN", "O2 CAMPING"],
        "ADRESSE":                                  ["la lilette", "Lieu Dit La Bretonnière"],
        "CODE POSTAL":                              ["73390", "50290"],
        "COMMUNE":                                  ["CHAMOUSSET", "LONGUEVILLE"],
        "TÉLÉPHONE":                                ["04 79 36 42 06", "06 84 98 33 74"],
        "COURRIEL":                                 ["hotel.christin@wanadoo.fr", "contact@o2camping.fr"],
        "SITE INTERNET":                            [None, "www.o2camping.fr"],
        "TYPE DE SÉJOUR":                           ["HÔTEL", "CAMPING"],
        "CAPACITÉ D'ACCUEIL (PERSONNES)":           [32, 360],
        "NOMBRE DE CHAMBRES":                       [16, None],
        "NOMBRE D'EMPLACEMENTS":                    [None, 90],
        "NOMBRE D'UNITÉS D'HABITATION":             [0, None],
        "NOMBRE DE LOGEMENTS":                      [None, 0]
    }
    return pl.DataFrame(data)


@pytest.fixture
def invalid_accommodation_df():
    data = {
        # missing "CLASSEMENT" column
        "DATE DE CLASSEMENT":                       ["18/11/2014", "08/06/1900"], # outside range
        "TYPE D'HÉBERGEMENT":                       ["HÔTEL DE TOURISME", "CAMPING"],
        "CATÉGORIE":                                ["TOURISME", "LOISIRS"],
        "MENTION":                                  ["HÔTEL", "CAMPING"],
        "NOM COMMERCIAL":                           ["HÔTEL CHRISTIN", "O2 CAMPING"],
        "ADRESSE":                                  ["la lilette", "Lieu Dit La Bretonnière"],
        "CODE POSTAL":                              [73390, 50290], # wrong datatype
        "COMMUNE":                                  ["CHAMOUSSET", "LONGUEVILLE"],
        "TÉLÉPHONE":                                ["04 79 36 42 06", "06 84 98 33 74"],
        "COURRIEL":                                 ["hotel.christin@wanadoo.fr", "contact@o2camping.fr"],
        "SITE INTERNET":                            [None, "www.o2camping.fr"],
        "TYPE DE SÉJOUR":                           ["HÔTEL", "CAMPING"],
        "CAPACITÉ D'ACCUEIL (PERSONNES)":           [32, 360],
        "NOMBRE DE CHAMBRES":                       [16, None],
        "NOMBRE D'EMPLACEMENTS":                    [None, 90],
        "NOMBRE D'UNITÉS D'HABITATION":             [0, None],
        "NOMBRE DE LOGEMENTS":                      [None, 0]
    }
    return pl.DataFrame(data)


@pytest.fixture
def processed_accommodation_df():
    data = {
        "DATE DE CLASSEMENT":                       ["18/11/2014"],
        "DATE DE PUBLICATION DE L'ÉTABLISSEMENT":   ["18/11/2014"],
        "TYPE D'HÉBERGEMENT":                       ["HÔTEL DE TOURISME"],
        "CLASSEMENT":                               [2],
        "CATÉGORIE":                                ["TOURISME"],
        "MENTION":                                  ["HÔTEL"],
        "NOM COMMERCIAL":                           ["hôtel christin"],
        "ADRESSE":                                  ["la lilette"],
        "CODE POSTAL":                              ["73390"],
        "COMMUNE":                                  ["chamousset"],
        "TÉLÉPHONE":                                ["04 79 36 42 06"],
        "COURRIEL":                                 ["hotel.christin@wanadoo.fr"],
        "SITE INTERNET":                            [""],
        "TYPE DE SÉJOUR":                           ["HÔTEL"],
        "CAPACITÉ D'ACCUEIL (PERSONNES)":           [32],
        "NOMBRE DE CHAMBRES":                       [16],
        "NOMBRE D'EMPLACEMENTS":                    [None],
        "NOMBRE D'UNITÉS D'HABITATION":             [0],
        "NOMBRE DE LOGEMENTS":                      [None],
        "date":                                     ["2014-11-18"],
        "day":                                      [18],
        "month":                                    [11],
        "year":                                     [2014],
        "concat":                                   ["la+lilette+73390+chamousset"]

    }
    return pl.DataFrame(data)


@pytest.fixture
def invalid_processed_accommodation_df():
    data = {
        # missing "year" column
        "DATE DE CLASSEMENT":                       ["18/11/2014"],
        "DATE DE PUBLICATION DE L'ÉTABLISSEMENT":   ["18/11/2014"],
        "TYPE D'HÉBERGEMENT":                       ["HÔTEL DE TOURISME"],
        "CLASSEMENT":                               [2],
        "CATÉGORIE":                                ["TOURISME"],
        "MENTION":                                  ["HÔTEL"],
        "NOM COMMERCIAL":                           ["hôtel christin"],
        "ADRESSE":                                  ["la lilette"],
        "CODE POSTAL":                              ["73390"],
        "COMMUNE":                                  ["chamousset"],
        "TÉLÉPHONE":                                ["04 79 36 42 06"],
        "COURRIEL":                                 ["hotel.christin@wanadoo.fr"],
        "SITE INTERNET":                            [""],
        "TYPE DE SÉJOUR":                           ["HÔTEL"],
        "CAPACITÉ D'ACCUEIL (PERSONNES)":           [32],
        "NOMBRE DE CHAMBRES":                       [16],
        "NOMBRE D'EMPLACEMENTS":                    [None],
        "NOMBRE D'UNITÉS D'HABITATION":             [0],
        "NOMBRE DE LOGEMENTS":                      [None],
        "date":                                     ["2014-11-18"],
        "day":                                      [11], # wrong day
        "month":                                    [11],
        "concat":                                   ["lalilette73390"] # wrong concat

    }
    return pl.DataFrame(data)


###                                      ###
### Relative to processed/transformation ###
###                                      ###
@pytest.fixture
def processed_df():
    data = {
        "name":         ["hôtel muret", "hôtel saint sébastien"],
        "room":         [19, 20],
        "capacity":     [42, 43],
        "adress":       ["le village", "avenue de verdun"],
        "zip":          ["05130", "06450"],
        "city":         ["sigoye", "roquebillière"],
        "star":         [3, 2],
        "date":         ["2017-06-20", "2017-06-08"],
        "day":          [20, 8],
        "month":        [6, 6],
        "year":         [2017, 2017],
        "latitude":     [4.477565, 44.022023],
        "longitude":    [5.97663, 7.310561],
        "x":            [ 936688.03, 1045428.48],
        "y":            [.51, 6334210.96],
        "concat":       ["le+village+05130+sigoyer", "avenue+de+verdun+06450+roquebillière"]
    }
    return pl.DataFrame(data)


@pytest.fixture
def invalid_processed_df():
    data = {
        # missing "name" column
        "room":         [19, 20],
        "capacity":     [42, 43],
        "adress":       ["le village", "avenue de verdun"],
        "zip":          [5130, 6450], # wrong datatype
        "city":         ["sigoye", "roquebillière"],
        "star":         [3, 2],
        "date":         ["2017-06-20", "1900-06-08"], # outside range
        "day":          [20, 13],       # date cross field error 
        "month":        [6, 6],         # date cross field error 
        "year":         [2017, 2017],   # date cross field error 
        "latitude":     [44.477565, 44.022023],
        "longitude":    [35.97663, 7.310561],
        "x":            [936688.03, 1045428.48],
        "y":            [6379851.51, 6334210.96],
        "concat":       ["le+village+05130+sigoyer", None] # missing value
    }
    return pl.DataFrame(data)
