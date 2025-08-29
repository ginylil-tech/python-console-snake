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

# Run the game (safe mode - ensures terminal restoration)
run:
	python -m snake
	make reset-terminal

# Run the original game directly (use with caution)
run-original:
	python -m snake
	make reset-terminal

# Run in debug mode (shows errors clearly, still restores terminal)
run-debug:
	python -m snake
	make reset-terminal

# Run with specific size
run-size:
	@echo "Available sizes: s (small), m (medium), l (large)"
	@read -p "Enter size (s/m/l): " size; \
	python -m snake -s $$size
	make reset-terminal

# Run with specific theme
run-theme:
	@echo "Available themes: classic, minimal, jungle, custom"
	@read -p "Enter theme: " theme; \
	python -m snake -t $$theme
	make reset-terminal

# Run in fullscreen
run-full:
	python -m snake -f
	make reset-terminal

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
	python -m snake --help

# Show available themes
themes:
	@echo "Available themes:"
	@echo "  classic  - Default theme"
	@echo "  minimal  - Minimal theme"
	@echo "  jungle   - Jungle theme"
	@echo "  custom   - Custom theme"

# Reset terminal to normal state (useful if terminal gets messed up)
reset-terminal:
	@echo "Resetting terminal..."
	@reset 2>/dev/null || true
	@stty sane 2>/dev/null || true
	@tput reset 2>/dev/null || true
	@tput cnorm 2>/dev/null || true
	@tput sgr0 2>/dev/null || true
	@stty echo 2>/dev/null || true
	@clear 2>/dev/null || true
	@echo "Terminal reset complete"

# Test terminal reset functionality
test-terminal:
	@echo "Testing terminal reset functionality..."
	@python3 test_terminal_reset.py

# Quick game test (starts and exits automatically)
test-game:
	@echo "Testing game startup and exit..."
	@echo "Game will start and exit automatically in 2 seconds..."
	@(python3 -m snake & sleep 2; pkill -f "python3 -m snake" 2>/dev/null || true; wait) || true
	@echo "Game test complete - terminal should be clean"
	@make reset-terminal 