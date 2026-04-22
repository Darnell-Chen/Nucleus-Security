from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def format_number(value):
    """Format a number similar to iPhone calculator display"""
    if not isinstance(value, (int, float)) or (isinstance(value, float) and not value == value):
        return "Error"
    
    # For very large or very small numbers, use exponential notation
    if abs(value) >= 1e12 or (abs(value) < 1e-6 and value != 0):
        return f"{value:.6e}"
    
    # For regular numbers, format with commas for thousands
    if isinstance(value, int):
        return f"{value:,}"
    else:
        # Round to reasonable decimal places to avoid floating point errors
        rounded = round(value, 10)
        formatted = f"{rounded:,}"
        return formatted


def calculate(a, b, operator):
    """Perform calculation based on operator"""
    try:
        a = float(a)
        b = float(b)

        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                return "DIV_ZERO"
            return a / b
        else:
            return None
    except (TypeError, ValueError, ZeroDivisionError):
        return None


@app.route('/calculate', methods=['POST'])
def calculate_endpoint():
    """Handle calculation requests"""
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON payload"}), 400

    try:
        a = data.get('a')
        b = data.get('b')
        operator = data.get('operator')

        if a is None or b is None or operator is None:
            return jsonify({"error": "Missing parameters"}), 400

        result = calculate(a, b, operator)

        if result == "DIV_ZERO":
            return jsonify({"error": "Division by zero", "display": "Error"}), 400

        if result is None:
            return jsonify({"error": "Invalid operator or operands"}), 400

        formatted_result = format_number(result)
        if formatted_result == "Error":
            return jsonify({"error": "Calculation error", "display": "Error"}), 400

        return jsonify({"result": result, "display": formatted_result})

    except Exception:
        return jsonify({"error": "Internal server error"}), 500


@app.route('/format', methods=['POST'])
def format_endpoint():
    """Format a number for display"""
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON payload"}), 400

    try:
        value = data.get('value')

        if value is None:
            return jsonify({"error": "Missing value"}), 400

        value = float(value)
        formatted_result = format_number(value)
        if formatted_result == "Error":
            return jsonify({"error": "Invalid value"}), 400

        return jsonify({"display": formatted_result})

    except (TypeError, ValueError):
        return jsonify({"error": "Invalid value"}), 400
    except Exception:
        return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
