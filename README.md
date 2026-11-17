# QA Automation Framework

[![QA Automation CI](https://github.com/HMD91/qa-automation-framework/actions/workflows/ci.yml/badge.svg)](https://github.com/HMD91/qa-automation-framework/actions/workflows/ci.yml)

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange)
![Requests](https://img.shields.io/badge/Requests-API%20Testing-brightgreen)
![Allure](https://img.shields.io/badge/Allure-Reporting-ff6c37?logo=allure)

A professional test automation framework built with Python, Pytest, Playwright and Requests, covering both UI and API testing.

## Overview

This project is a test automation framework designed to validate both web application user journeys and REST API endpoints.

It combines two complementary automation approaches:

- **UI Testing:** Browser automation using Playwright and Pytest, following the Page Object Model (POM) design pattern.
- **API Testing:** REST API validation using Python Requests and Pytest, with a reusable API client and automated checks for successful responses and error handling.

The framework aims to provide reliable, maintainable and reusable automated tests across different application layers.

## Tech Stack

- **Python 3.12+** — Programming language
- **Playwright** — Browser automation
- **Pytest** — Test framework and test execution
- **pytest-playwright** — Playwright integration with Pytest
- **pytest-html** — HTML test reporting
- **Allure** — Detailed test reporting and visualization
- **Requests** — HTTP requests and REST API testing
- **python-dotenv** — Environment variable management
- **Ruff** — Code quality and linting
- **Git & GitHub** — Version control and source code hosting
- **GitHub Actions** — Continuous Integration (CI)

## Project Structure

```text
qa-automation-framework/
│
├── config/
│
├── framework/
│   ├── api/
│   │   ├── __init__.py
│   │   └── client.py
│   │
│   ├── ui/
│   │   ├── cart_page.py
│   │   ├── checkout_complete_page.py
│   │   ├── checkout_overview_page.py
│   │   ├── checkout_page.py
│   │   ├── inventory_page.py
│   │   └── login_page.py
│   │
│   ├── utils/
│   └── config.py
│
├── tests/
│   ├── api/
│   │   ├── test_api_client.py
│   │   ├── test_api_errors.py
│   │   └── test_post.py
│   │
│   ├── ui/
│   │   ├── test_cart.py
│   │   └── test_login.py
│   │
│   └── conftest.py
│
├── test_data/
│   └── users/
│       └── login_cases.json
│
├── docs/
│   └── images/
│       ├── inventory.png
│       └── report.png
│
├── .env.example
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── pyproject.toml
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/HMD91/qa-automation-framework.git
cd qa-automation-framework
```

### 2. Create a virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 3. Install project dependencies

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### 4. Configure environment variables

Create a local `.env` file from the example:

```bash
cp .env.example .env
```

The API base URL is configured as follows:

```env
API_BASE_URL=https://jsonplaceholder.typicode.com
```

The `.env` file is excluded from version control. The `.env.example` file provides the configuration template required to run the API tests.

### 5. Install Playwright browser

```bash
playwright install --with-deps chromium
```

## Running Tests

### Run all tests

```bash
pytest
```

### Run UI tests only

```bash
pytest tests/ui/
```

### Run API tests only

```bash
pytest tests/api/
```

### Run a specific test file

```bash
pytest tests/ui/test_login.py
```

```bash
pytest tests/api/test_api_client.py
```

### Run tests with detailed output

```bash
pytest -v
```

## Automated Test Scenarios

The current test suite includes **44 automated tests**, covering UI and API functionality.

### UI Testing — 15 tests

UI tests validate the main user journeys of the web application using Playwright and Chromium.

**Authentication**
- Successful login
- Login with an incorrect password
- Login with a locked user account

**Shopping Cart**
- Select an available product
- Add a product to the cart
- Verify cart counter increment
- Remove a product from the cart
- Verify cart counter after removal
- Navigate to and from the cart

**Checkout**
- Start the checkout process
- Fill in customer information
- Verify the order summary
- Complete an order
- Verify order confirmation

### API Testing — 29 tests

API tests validate REST API operations using Python Requests and Pytest.

**HTTP Methods**
- GET — Retrieve resources
- POST — Create resources
- PUT — Update resources
- PATCH — Partially update resources
- DELETE — Delete resources

**Error Handling and Reliability**
- Validate HTTP error responses
- Handle connection errors
- Handle request timeouts
- Verify server error handling
- Validate request execution and expected arguments

The API tests use a reusable API client to centralize HTTP communication and response handling.

## Test Reports

After test execution, an HTML report is automatically generated at:

```text
reports/report.html
```

The report provides a detailed overview of test execution results and can be opened directly in a web browser.
### Allure Reports

Allure generates detailed test reports with test descriptions, execution steps, features and results.

To generate and open the report locally:

```bash
npx allure generate reports/allure-results --clean
npx allure open


A screenshot of the report is available in:

```text
docs/images/report.png
```

## Continuous Integration (CI)

The project uses **GitHub Actions** to automatically validate code quality and execute automated tests.

The CI pipeline is triggered on:

- Push events to the `main` branch
- Pull requests targeting the `main` branch

### Pipeline Jobs

**1. Code Quality - Ruff**

- Install project dependencies
- Run Ruff to check code quality

**2. Automated Tests - Pytest**

- Install project dependencies
- Configure the API base URL
- Install Chromium and its system dependencies
- Execute the automated test suite
- Generate Pytest HTML and Allure reports
- Upload both reports as GitHub Actions artifacts

The HTML report is available for download for **7 days** after each workflow execution.

### Latest Test Results

The latest successful CI execution validated:

| Test Category | Tests |
|---|---:|
| UI Tests | 15 |
| API Tests | 29 |
| **Total** | **44** |

Both the Ruff code quality checks and the Pytest test suite passed successfully.

## Screenshots

### Inventory Page

![Inventory Page](docs/images/inventory.png)

### Pytest HTML Report

![Pytest HTML Report](docs/images/report.png)

## Project Goals

This project demonstrates practical skills in:

- UI test automation with Playwright
- REST API testing with Python Requests
- Test automation architecture and maintainability
- Page Object Model (POM)
- Pytest fixtures and parametrization
- Error handling and negative testing
- Environment configuration
- Code quality with Ruff
- Continuous Integration with GitHub Actions

---

**Author:** Ahmed Beggache

**Repository:** [HMD91/qa-automation-framework](https://github.com/HMD91/qa-automation-framework)