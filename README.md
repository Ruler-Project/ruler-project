# The RULER Project

The Really Useful Logging and Event Repository Project - [https://ruler-project.github.io/ruler-project/](https://ruler-project.github.io/ruler-project/)

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setting up a Virtual Environment](#setting-up-a-virtual-environment)
  - [Installing Dependencies](#installing-dependencies)
- [Running the Website](#running-the-website)
- [Contributing](#contributing)
  - [Creating a Pull Request](#creating-a-pull-request)

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python3
- pip

### Setting up a Virtual Environment

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Ruler-Project/ruler-project.git
   ```

2. Create a Python virtual environment.

   ```bash
   python3 -m venv ruler-project-web
   ```

3. Activate the virtual environment:

   On Windows:

   ```bash
   ruler-project-web\Scripts\activate
   ```

   On macOS and Linux:

   ```bash
   source ruler-project-web/bin/activate
   ```

### Installing Dependencies

1. While in the virtual environment, install the project dependencies using pip:

   ```bash
   pip3 install -r requirements.txt
   ```

## Running the Website

1. Make sure you're in the virtual environment with the project dependencies installed.

2. Run the MkDocs development server:

   ```bash
   mkdocs serve
   ```

3. Access the website locally by opening a web browser and navigating to http://localhost:8000.

## Adding content

The pages are stored in `docs\RULER\<folder name>\<file>.md` and then need to be referenced within the `mkdocs.yml` file.

## Contributing

We welcome contributions to improve The RULER Project. To contribute please fork the "Develop" branch of the repository and then create a pull request with any changes.

Upon review, the changes will be merged into the project. We will then do a pull request to "Main" which *should* automatically build the gh pages (If the action works...testing in progress...)

Thank you for contributing to The RULER Project!

### Contributors

* Phill Moore
* Andrew Skatoff
* Zach Stanford