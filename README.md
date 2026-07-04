# 🎭 Mood Chatbot (CLI)

A simple command-line chatbot that adapts its personality based on your mood. Choose between **funny**, **sad**, or **angry** mode, and chat with an AI powered by **Mistral AI** through **LangChain**.

## Features

- 🎚️ Pick a mood at startup: funny, sad, or angry
- 🤖 AI responses tailored to the selected personality via a system prompt
- 💬 Multi-turn conversation with full message history maintained during the session
- 🔑 Simple `.env`-based API key configuration

## Tech Stack

- [LangChain](https://python.langchain.com/) — message handling and LLM orchestration
- [langchain-mistralai](https://pypi.org/project/langchain-mistralai/) — Mistral AI integration
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management

## Prerequisites

- Python 3.9+
- A [Mistral AI API key](https://console.mistral.ai/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API key:
   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

## Usage

Run the chatbot from the terminal:

```bash
python chatbot.py
```

You'll be prompted to select a mood:

```
According to your mood make a choice from below
choose 1 if want me to be funny
choose 2 if your mood is sad
choose 3 if your mood is angry
make a choice :
```

After selecting a mode, start chatting. Type `0` at any time to exit the conversation.

## Example

```
make a choice : 1
------------I am funny chatbot now-----------------
User: Tell me about your day
BOT: Oh, you know, just doing my usual thing—processing tokens and dodging existential crises. 10/10 day.
User: 0
```

## Project Structure

```
.
├── chatbot.py          # Main chatbot script
├── requirements.txt    # Python dependencies
├── .env                # API key (not committed to version control)
└── README.md
```

## Notes

- Add `.env` and `.venv/` to your `.gitignore` before pushing to GitHub, so your API key is never exposed.
- The model used is `mistral-small-latest`; you can change this in `chatbot.py` to any other supported Mistral model.

## License

This project is open source and available under the [MIT License](LICENSE).