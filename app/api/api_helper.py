def json_to_api_response(json_data):
    try:
        if json_data:
            return {
                "data": json_data,
                "error": None
            }
        else:
            return {
                "data": None,
                "error": {
                    "code": 404,
                    "data": "N/A",
                    "message": "Ressources not found",
                    "details": "The request could not be found."
                }
            }
    except Exception as e:
        return {
            "data": None,
            "error": {
                "code": 500,
                "message": "Internal Server Error",
                "details": str(e)
            }
        }
