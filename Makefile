# Makefile for python-console-snake
# Lightweight, configurable snake game running in the console

.PHONY: help run install clean test lint format docs

# Default target
help:
	@echo "Available targets:"
	@echo "  run          - Run the snake game"
	@echo "  run-size     - Run with specific size (s/m/l)"
	@echo "  run-theme    - Run with specific theme (classic/minimal/jungle)"
	@echo "  run-full     - Run in fullscreen mode"
	@echo "  install      - Install Python dependencies (if any)"
	@echo "  clean        - Clean Python cache files"
	@echo "  test         - Run tests (if available)"
	@echo "  lint         - Run linting (if available)"
	@echo "  format       - Format code (if available)"
	@echo "  docs         - Generate documentation (if available)"

# Run the game
run:
	python snake

# Run with specific size
run-size:
	@echo "Available sizes: s (small), m (medium), l (large)"
	@read -p "Enter size (s/m/l): " size; \
	python snake -s $$size

# Run with specific theme
run-theme:
	@echo "Available themes: classic, minimal, jungle, custom"
	@read -p "Enter theme: " theme; \
	python snake -t $$theme

# Run in fullscreen
run-full:
	python snake -f

# Install dependencies (placeholder - no requirements.txt found)
install:
	@echo "No requirements.txt found. This project appears to use only Python standard library."
	@echo "If you need to install additional dependencies, create a requirements.txt file first."

# Clean Python cache files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	@echo "Cleaned Python cache files"

# Run tests (placeholder - no test files found)
test:
	@echo "No test files found. Create tests/ directory with test files to enable testing."

# Run linting (placeholder - no linting tools configured)
lint:
	@echo "No linting tools configured. Consider installing flake8, pylint, or black."

# Format code (placeholder - no formatting tools configured)
format:
	@echo "No formatting tools configured. Consider installing black or autopep8."

# Generate documentation (placeholder - no doc generation tools configured)
docs:
	@echo "No documentation generation tools configured. Consider installing pydoc or sphinx."

# Development setup
dev-setup: install
	@echo "Development environment setup complete"

# Quick start - run game with default settings
start: run

# Show game help
help-game:
	python snake --help

# Show available themes
themes:
	@echo "Available themes:"
	@echo "  classic  - Default theme"
	@echo "  minimal  - Minimal theme"
	@echo "  jungle   - Jungle theme"
	@echo "  custom   - Custom theme" 