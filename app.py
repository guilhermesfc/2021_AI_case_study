from flask import Flask, request, jsonify
import numpy as np
import onnxruntime as rt
import os
from loguru import logger

# Load the ONNX model
model_name = os.environ.get("MODEL_NAME", "calibrated_classifier")
onnx_model_path = os.path.join(model_name + ".onnx")
logger.info(f"Loading the model {onnx_model_path}")
session = rt.InferenceSession(onnx_model_path)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict() -> jsonify:
    try:
        features_data = request.get_json()
        input_data = np.array([features_data], dtype=np.float32)
        input_name = session.get_inputs()[0].name
        prediction = session.run(None, {input_name: input_data.astype(np.float32)})
        return jsonify({'prediction': prediction[1][0][1]}) # return probability of positive outcome
    except Exception as e:
        logger.error(f"Prediction API error: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)
