print("Hello, Saba! Python is working.")

# Read URLs from a file
with open("urls.txt", "r") as file:
    urls = [line.strip() for line in file.readlines()]

# List of trusted domains
trusted_domains = ["google.com", "facebook.com", "microsoft.com"]

# Open results file for writing
with open("results.txt", "w") as output:
    for url in urls:
        result = f"\nChecking: {url}\n"
        if "@" in url:
            result += "Suspicious: URL contains '@' symbol.\n"
        elif len(url) > 150:
            result += "Suspicious: URL is too long.\n"
        elif url.count(".") > 3:
            result += "Suspicious: URL has too many subdomains.\n"
        elif not any(domain in url for domain in trusted_domains):
            result += "Suspicious: Domain may be misspelled or untrusted.\n"
        else:
            result += "Safe: No obvious issues found.\n"

        # Print to terminal
        print(result)
        # Save to file
        output.write(result)
