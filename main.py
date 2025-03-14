import functions_framework
from flask import jsonify, request

@functions_framework.http
def hello_http(request):
    """Handles HTTP requests with different methods."""

    # Check HTTP method
    method = request.method

    if method == "GET":
        # Handle GET request
        request_args = request.args
        name = request_args.get("name", "World")
        return jsonify({"message": f"Hello {name}!", "method": "GET"})

    elif method == "POST":
        # Handle POST request
        request_json = request.get_json(silent=True)
        if request_json:
            return jsonify({"message": "Received POST data", "data": request_json})
        return jsonify({"error": "No JSON data received"}), 400

    elif method == "PUT":
        # Handle PUT request
        return jsonify({"message": "PUT request successful", "status": "Updated"})

    elif method == "DELETE":
        # Handle DELETE request
        return jsonify({"message": "DELETE request successful", "status": "Deleted"})

    else:
        return jsonify({"error": "Method not allowed"}), 405

    