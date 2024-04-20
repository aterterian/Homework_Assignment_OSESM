# Code Review for Homework_Assignment_OSESM Repository

## Repository Overview
- [x] **Purpose and Functionality**
  - The repository is for the homework assignment from the second lecture of Open-Source Energy System Modelling in 2024.
  - It includes functions that print shapes like a Christmas tree and a diamond, with customizable sizes and appearances.

- [x] **Structure and Contents**
  - Contains `.github/workflows` for CI workflows, `utils.py` with main functions, `test_utils.py` for tests, `.gitignore`, `LICENSE`, and `README.md`.
  - The `utils.py` file has functions for printing shapes and a subtract function. The `test_utils.py` file contains tests for these functions.

- [x] **Usage and Contribution**
  - Developers can use the repository to learn about implementing and testing shape-printing functions.
  - Contributions to enhance functions or add new features are encouraged.

## Testing Procedures
- [x] **License Verification**
  - A `LICENSE` file is present, providing legal clarity for use and contribution: Apache License 2.0.

- [x] **Pytests Execution**
  - Pytests check the functionality of the subtract function and the input types for the print-functions.
  - Tests are expected to pass with correct inputs and fail otherwise, ensuring function robustness.

- [x] **Ruff Linter Checks**
  - The Ruff Linter is set up to check code style and formatting.
  - Expected to fail if the code does not meet style guidelines, prompting review and correction.

## Conducting the Code Review
- [x] **Code Style and Readability**
  - Code follows a consistent style and is well-commented for readability.
  - Variable names are descriptive, and logic is clear.

- [x] **Functionality**
  - Functions in `utils.py` perform as described, printing shapes based on given parameters.
  - The subtract function performs arithmetic subtraction correctly.

- [x] **Tests and Error Handling**
  - Tests in `test_utils.py` cover input types and function outputs.
  - Error handling is present, with appropriate messages for invalid inputs.
