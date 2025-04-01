from data_loader import load_json_data, validate_fruit_data

def main():
    try:
        # Load and validate data
        data = load_json_data('data/data.json')
        validate_fruit_data(data)
        print("Data loaded and validated successfully.")
        print("Data:", data)
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()