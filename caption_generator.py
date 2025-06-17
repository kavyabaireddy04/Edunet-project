import requests

# Replace these with your Azure details
subscription_key = "YOUR_COMPUTER_VISION_KEY"
endpoint = "YOUR_ENDPOINT_URL"

# Image to analyze
image_path = r"C:\Users\kotireddy81\OneDrive\Pictures\Screenshots\Screenshot 2025-05-16 231840.png"

# Open the image in binary format
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

analyze_url = f"{endpoint}/vision/v3.2/analyze?visualFeatures=Description"

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/octet-stream'
}

response = requests.post(analyze_url, headers=headers, data=image_data)
response.raise_for_status()

analysis = response.json()

# Extracting and printing caption
caption = analysis["description"]["captions"][0]["text"]
confidence = analysis["description"]["captions"][0]["confidence"]
print(f"Caption: {caption}")
print(f"Confidence: {confidence:.2f}")
