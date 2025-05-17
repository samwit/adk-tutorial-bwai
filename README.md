# Google Agent Development Kit (ADK) Tutorial

This repository contains the code and resources for learning about Google's Agent Development Kit (ADK), a powerful framework for building AI agents and assistants. It was give as a live tutorial on May 17th. Please see the notebooks for the full code with runners and sessions etc.

## Overview

The Google Agent Development Kit (ADK) is a framework that enables developers to create sophisticated AI agents that can interact with users, understand context, and perform tasks autonomously. This tutorial project demonstrates key concepts and best practices for building agents using ADK.

## Prerequisites

- Python 3.12 or higher
- `uv` package manager (for virtual environment management)

## Setup

1. Clone this repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Create and activate a virtual environment using `uv`:
```bash
uv venv --python 3.12
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies using `uv sync`:
```bash
uv sync
```

This will install all required dependencies from the `pyproject.toml` file, including:
- google-adk (>=0.5.0)
- pydantic (>=2.11.4)
- yfinance (>=0.2.61)

## Getting Started

To run the ADK web interface:
```bash
uv run adk web
```

This will start the web interface where you can interact with the agents.

## Features

- [List key features of your ADK implementation]
- [Add any specific capabilities or integrations]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add appropriate license information]

## Resources

- [Google ADK Documentation](https://developers.google.com/agent-development-kit)
- [Additional resources and links]

## Contact

[Add contact information or ways to reach out for help]

uv venv --python 3.12