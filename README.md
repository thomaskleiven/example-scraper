# Selenium Based Scraper

## Getting Started

Before you can use the scraper, make sure you have the following prerequisites installed on your system:

- Python 3.6+
- Chrome Browser
- Chrome Driver

### Setting up the virtual environment

To ensure a clean and isolated environment, it is recommended to set up a virtual environment. Follow these steps:

```bash
python -m venv venv
source venv/bin/activate
```

### Installation

Install the required packages using the following command (the dot in the end is important):

```bash
pip install -e .
```

If the installation command fails, please try setting the following environment variable and then retry the installation:

```bash
export PBR_VERSION=0.0.1
```

### Usage

To start using the scraper, simply execute the following command:

```bash
python scraper/main.py
```
