import json

def load_json_data(file_path):
    """Load and validate JSON data from file"""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON data should be a dictionary")
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise Exception(f"Data loading failed: {str(e)}")

def validate_fruit_data(data):
    """Validate the structure of city data"""
    required_keys = ['item', 'price']
    if 'fruits' not in data:
        raise ValueError("Missing 'fruits' key in data")
    
    for fruit in data['fruits']:
        if not all(key in fruit for key in required_keys):
            raise ValueError(f"Fruit missing required keys: {required_keys}")