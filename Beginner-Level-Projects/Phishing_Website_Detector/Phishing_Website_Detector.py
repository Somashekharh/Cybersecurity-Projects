import requests
import re
import os

# Load VirusTotal API key from environment variable
API_KEY = os.getenv("VIRUSTOTAL_API_KEY", "YOUR_VIRUSTOTAL_API_KEY")

def check_virustotal(url):
    """Checks the URL on VirusTotal for phishing reputation."""
    print(f"\nChecking VirusTotal for: {url}...")
    headers = {"x-apikey": API_KEY}
    params = {"url": url}
    
    try:
        # Submit URL for analysis
        response = requests.post("https://www.virustotal.com/api/v3/urls", headers=headers, data=params)
        response.raise_for_status()  # Raise an error for bad status codes
        
        result = response.json()
        if result.get("data"):
            analysis_id = result["data"]["id"]
            # Retrieve analysis report
            analysis_result = requests.get(f"https://www.virustotal.com/api/v3/analyses/{analysis_id}", headers=headers)
            analysis_result.raise_for_status()
            
            report = analysis_result.json()
            malicious_count = report["data"]["attributes"]["stats"]["malicious"]
            if malicious_count > 0:
                return f"⚠️ WARNING: {malicious_count} security vendors flagged this URL as malicious!"
            else:
                return "✅ Safe: No security vendors flagged this URL."
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return "⚠️ Unable to check URL reputation."

def detect_suspicious_url(url):
    """Checks for suspicious patterns in the URL."""
    phishing_patterns = [
        r"(login|verify|update|secure|account|bank|paypal)",  # Fake login attempts
        r"(free|bonus|win|lottery|prize)",  # Scam giveaways
        r"(\.xyz|\.tk|\.cf|\.ml|\.ga)",  # Suspicious domain extensions
        r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"  # Direct IP usage
    ]
    
    for pattern in phishing_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            return "⚠️ WARNING: Suspicious patterns detected in the URL!"
    
    return "✅ No obvious phishing patterns found."

# Example Usage
if __name__ == "__main__":
    url_to_check = input("Enter the URL to check: ")
    print(detect_suspicious_url(url_to_check))
    print(check_virustotal(url_to_check))