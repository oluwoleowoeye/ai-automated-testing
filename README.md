# Automated Testing with AI

This project demonstrates automated testing of a login page

## Setup

1. Install Python 3.8+
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `source venv/Scripts/activate` (gitbash) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Running Tests

Execute:
```bash
pytest test_login.py -v

![test valid login Screenshot](test_valid_login_success_20250717_094243.png)
![test invalid login Screenshot](test_invalid_login_success_20250717_094248.png)

## AI Benefits in Testing
AI enhances test coverage by automatically generating additional test cases based on user behavior patterns. Machine learning algorithms can identify edge cases humans might miss and adapt tests as the application evolves. AI-powered tools like Testim.io use self-healing locators that automatically adjust when UI elements change, reducing maintenance overhead. Compared to manual testing, AI can execute thousands of test variations in the time it takes a human to complete one test cycle, while also providing intelligent analysis of results to identify potential issues.


