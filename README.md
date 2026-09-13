# Phishing URL Detector

A simple Python-based cybersecurity project that checks URLs for common signs of phishing or suspicious activity.

## Features

The detector currently checks for:

* `@` symbols in URLs, which can be used to make a misleading URL appear trustworthy
* Excessive subdomains, which can be a suspicious indicator
* Potentially misspelled or untrusted domain names
* Legitimate URLs that do not trigger the implemented checks

## Example

The program can identify URLs such as:

```text
http://example.com@phishing.com
```

as suspicious because they contain an `@` symbol.

It can also flag URLs with an unusually large number of subdomains, such as:

```text
http://secure.login.bank.verify.example.com
```

A legitimate URL such as:

```text
https://google.com
```

can pass the implemented checks.

## Technologies Used

* Python
* URL and domain analysis
* Basic cybersecurity concepts

## How to Run

1. Make sure Python is installed.
2. Open a terminal in the project directory.
3. Run:

```bash
python check_url.py
```

## Project Purpose

This project was created to practice Python programming and understand basic techniques used to identify potentially suspicious phishing URLs.

## Limitations

This is a beginner-level rule-based detector. It does **not** guarantee that a URL is safe or malicious.

A real-world phishing detection system would use additional techniques, databases, threat intelligence, and more advanced analysis.

## Author

Saba Noor
# phishing-detector
Beginner‑friendly Python tool to detect suspicious URLs and flag potential phishing attempts.
