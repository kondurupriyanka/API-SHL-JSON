from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    query = request.args.get('q', '')
    response_data = {
        "recommendations": [
            {
                "id": "1",
                "name": "SHL Assessment",
                "url": "https://shlassessment.netlify.app/",
                "description": "A sample assessment recommendation based on the provided query.",
                "remoteTestingSupport": True,
                "adaptiveSupport": False,
                "duration": "30 minutes",
                "testType": "Cognitive"
            }
        ],
        "query": query
    }
    return jsonify(response_data)

if __name__ == '__main__':
    # For local testing, use this
    app.run(host="0.0.0.0", port=5000, debug=True)
