# Third party imports
from fastapi import FastAPI

# Local application imports
from controllers import hotel_controller


app = FastAPI(
    title = 'Hotel API',
    description = 'API to fetch data',
    version = '1.0.0',
    openapi_tags=[
        {
            'name': 'status',
            'description': 'functions to check if we can connect to the API'
        },
        {
            'name': 'hotel',
            'description': 'functions relative to hotels'
        },
    ]
)


###
### CHECK API STATUS
###
@app.get("/api/status", tags = ['status'])
def read_status():
    """Check API status
    """
    return {"status": 200}


###
### HOTEL API ROUTE
###
@app.get("/api/hotel/count", tags = ["hotel"])
def read_hotel_count():
    result = hotel_controller.get_hotel_count()
    return result

@app.get("/api/hotel/city/{name:str}", tags = ["hotel"])
def read_hotel_rank_by_city(name):
    result = hotel_controller.get_hotel_rank_by_city(name)
    return result


###
### CITY API ROUTE
###
@app.get("/api/city", tags = ["city"])
def read_rating_distribution():
    result = hotel_controller.get_all_cities()
    return result


###
### RATIN API ROUTE
###
@app.get("/api/rating/average", tags = ["rating"])
def read_rating_avg():
    result = hotel_controller.get_rating_average()
    return result

@app.get("/api/rating/median", tags = ["rating"])
def read_rating_median():
    result = hotel_controller.get_rating_median()
    return result

@app.get("/api/rating/distribution", tags = ["rating"])
def read_rating_distribution():
    result = hotel_controller.get_rating_distribution()
    return result


###
### REGION API ROUTE
###
@app.get("/api/region/rank", tags = ["region"])
def read_hotel_rank_by_capacity(nb):
    result = hotel_controller.get_hotel_rank_by_capacity(nb)
    return result

@app.get("/api/region/rating/above-average/rank", tags = ['region'])
def read_hotel_rank_by_capacity(nb):
    result = hotel_controller.get_hotel_count_and_rank_per_region_above_avg_rating(nb)
    return result





