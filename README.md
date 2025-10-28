# Futures Trading Bot // PLEASE READ

A Telegram bot for futures algorythmic trading. 

## Requirements

- Python 3.10.11 (recommended) or compatible version
- Git installed and configured

## For Developers

If you want to contribute to the bot's development:

1. Clone the repository into a new directory:
```bash
# Create a new directory for the project
mkdir futures_bot_dev
cd futures_bot_dev

# Clone the repository
git clone https://github.com/matviitertyshnyi/futures_trading_bot.git .
```

2. Create and activate a clean virtual environment (important: create it OUTSIDE the project folder):
```bash
# Windows
# Ensure you're using Python 3.10.11
python --version  # Should show Python 3.10.11
# Create venv in a separate location
python -m venv %USERPROFILE%\envs\futures_bot_env
# Activate it
%USERPROFILE%\envs\futures_bot_env\Scripts\activate

# Linux/MacOS
# Ensure you're using Python 3.10.11
python3 --version  # Should show Python 3.10.11
# Create venv in a separate location
python3 -m venv ~/envs/futures_bot_env
# Activate it
source ~/envs/futures_bot_env/bin/activate
```

3. Install dependencies (make sure your virtual environment is activated):
```bash
# Verify you're using the correct Python
which python  # Linux/MacOS
where python  # Windows
# Should show the python from your virtual environment

# Install requirements
pip install -r requirements.txt
```

4. Place the `.env` file in the project root directory (important!)

## Contributing

1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/your-feature-name
```
3. Make your changes and commit:
```bash
git add .
git commit -m "Add your feature description"
```
4. Push to your fork:
```bash
git push origin feature/your-feature-name
```
5. Create a Pull Request

## Important Notes

- Never commit your `.env` file - it contains sensitive information
- When commiting, name those commits accordingly e.g. "Confidence calculation added"
- Always test your changes in a development environment before pushing
- Keep the group chat ID private
- When adding new features, update this README accordingly