def handleError(e):
    print("Error", e)
    return {
        "status": "error",
        "message": str(e)
    }