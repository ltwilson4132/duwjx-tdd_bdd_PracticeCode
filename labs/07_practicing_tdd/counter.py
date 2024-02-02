from flask import Flask
import status

app = Flask(__name__)

COUNTERS = {}

@app.route("/counters/<name>", methods=["POST"])
def create_counter(name):
    """Creates a counter"""
    app.logger.info(f"Request to create counter: {name}")
    global COUNTERS

    if name in COUNTERS:
        return {"message":f"Counter {name} already exists"}, status.HTTP_409_CONFLICT

    COUNTERS[name] = 0
    return { name: COUNTERS[name] }, status.HTTP_201_CREATED

@app.route("/counters/<name>", methods=["PUT"])
def update_counter(name):
    """Update a counter"""
    app.logger.info(f"Request to update counter: {name}")
    global COUNTERS

    if name not in COUNTERS:
        return {"message":f"Counter does not exist"}, status.HTTP_204_NO_CONTENT
    
    COUNTERS[name] += 1

    app.logger.info(f"Counter {name} was successfully updated to {COUNTERS[name]}")
    return { name: COUNTERS[name] }, status.HTTP_200_OK

@app.route("/counters/<name>", methods=["GET"])
def read_counter(name):
    """Read a counter"""
    app.logger.info(f"Request to read counter: {name}")
    global COUNTERS

    if name not in COUNTERS:
        return {"message":f"Counter does not exist"}, status.HTTP_204_NO_CONTENT

    app.logger.info(f"Counter: {name} is {COUNTERS[name]}")
    return { name: COUNTERS[name] }, status.HTTP_200_OK

@app.route("/counters/<name>", methods=["DELETE"])
def delete_counter(name):
    """Delete a counter"""
    app.logger.info(f"Request to delete counter: {name}")
    global COUNTERS

    if name not in COUNTERS:
        return {"message":f"Counter does not exist"}, status.HTTP_204_NO_CONTENT

    del(COUNTERS[name])

    app.logger.info(f"Counter {name} has been deleted")
    return '', status.HTTP_204_NO_CONTENT
    