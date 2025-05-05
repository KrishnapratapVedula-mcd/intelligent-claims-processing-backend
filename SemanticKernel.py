from semantic_kernel.kernel import Kernel
from semantic_kernel.agents import Agent
from IntakeAgent import IntakeAgent
from AssessmentAgent import AssessmentAgent
from FraudDetectionAgent import FraudDetectionAgent
from RiskAnalysisAgent import RiskAnalysisAgent
from DecisionAgent import DecisionAgent
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/SendIntakeAgent', methods=['POST'])
def get_Intake_Agent_data():
    # Check if the request has JSON data
    #if not request.is_json:
    #    return jsonify({'error': 'Invalid Content-Type. Expected application/json'}), 415
    
    # Initialize Kernel and IntakeAgent
    kernel = Kernel()
    intakeAgent = IntakeAgent(kernel)

    # Get the payload from the POST request
    payload = request.json  # Retrieve the entire JSON payload

    input_text = payload["key"]

    # Call the perform_task method and get the result
    result_a = intakeAgent.perform_task(input_text)    

    # Return the result as a JSON response
    return jsonify({'result': result_a[0]})

@app.route('/api/SendRiskAnalysisAgent', methods=['POST'])
def get_Risk_Analysis_Agent_data():
    # Check if the request has JSON data
    #if not request.is_json:
    #    return jsonify({'error': 'Invalid Content-Type. Expected application/json'}), 415
    
    # Initialize Kernel and IntakeAgent
    kernel = Kernel()
    risk_analysisAgent = RiskAnalysisAgent(kernel)

    # Get the payload from the POST request
    payload = request.json  # Retrieve the entire JSON payload

    input_text = payload["key"]

    # Call the perform_task method and get the result
    result_b = risk_analysisAgent.perform_task(input_text)

    # Return the result as a JSON response
    return jsonify({'result': result_b[0]})


@app.route('/api/SendFraudDetectionAgent', methods=['POST'])
def get_Fraud_Detection_Agent_data():
    # Check if the request has JSON data
    #if not request.is_json:
    #    return jsonify({'error': 'Invalid Content-Type. Expected application/json'}), 415
    
    # Initialize Kernel and IntakeAgent
    kernel = Kernel()
    fraudDetection_Agent = FraudDetectionAgent(kernel)

    # Get the payload from the POST request
    payload = request.json  # Retrieve the entire JSON payload    

    input_text = payload["key"]

    # Call the perform_task method and get the result
    result_c = fraudDetection_Agent.perform_task(input_text)

    # Return the result as a JSON response
    return jsonify({'result': result_c[0]})

@app.route('/api/SendAssessmentAgent', methods=['POST'])
def get_Assessment_Agent_data():
    # Check if the request has JSON data
    #if not request.is_json:
    #    return jsonify({'error': 'Invalid Content-Type. Expected application/json'}), 415
    
    # Initialize Kernel and IntakeAgent
    kernel = Kernel()
    assessment_Agent = AssessmentAgent(kernel)

    # Get the payload from the POST request
    payload = request.json  # Retrieve the entire JSON payload

    input_text = payload["key"]

    # Call the perform_task method and get the result
    result_d = assessment_Agent.perform_task(input_text)

    # Return the result as a JSON response
    return jsonify({'result': result_d[0]})

@app.route('/api/SendDecisionAgent', methods=['POST'])
def get_Decision_Agent_data():
    # Check if the request has JSON data
    #if not request.is_json:
    #    return jsonify({'error': 'Invalid Content-Type. Expected application/json'}), 415
    
    # Initialize Kernel and IntakeAgent
    kernel = Kernel()
    decision_Agent = DecisionAgent(kernel)

    # Get the payload from the POST request
    payload = request.json  # Retrieve the entire JSON payload

    input_text = payload["key"]

    # Call the perform_task method and get the result
    result_e = decision_Agent.perform_task(input_text)

    # Return the result as a JSON response
    return jsonify({'result': result_e[0]})

if __name__ == "__main__":
    app.run(debug=True)