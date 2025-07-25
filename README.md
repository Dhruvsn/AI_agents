
# 🧠 AI Agents Collection

This repository is a growing collection of simple and useful AI agents built using [Google's Gemini API](https://ai.google.dev/) and interactive Python tools like `ipywidgets`.

Each agent serves a unique purpose — from generating tweets to assisting with health-related queries. The goal is to build a modular and extensible framework for creating smart assistants using natural language capabilities.

---

## 🔧 Current Agents

### 1. 🚀 Tweet Generator Agent
> Create tweets in seconds based on your topic, tone, audience, and hashtags!

**Features:**
- Custom tweet generation using Gemini AI
- Choose from multiple tones: Professional, Casual, Motivational, Informative
- Designed for social media marketers, creators, or anyone who needs content fast

**Usage:**
- Open the `tweet_generater_agent.py` file in a Jupyter Notebook environment
- Fill in the form inputs (Topic, Tone, Audience, Hashtags)
- Click **Generate Tweet** — your tweet appears instantly below

---

### 2. 💬 Health Consultation Agent (coming soon)
> A basic AI agent that assists users with general health-related questions and advice.

This is under development and will be expanded further.

---

## 🚀 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Dhruvsn/AI_agents.git
cd AI_agents
```

### 2. Install required packages

Here’s a full pip install command for all dependencies:

```bash
pip install google-generativeai ipywidgets IPython langgraph langchain langchain_community nest_asyncio python-dotenv
```

If you're using Jupyter Notebook, install it as well:

```bash
pip install notebook
```

---

## 📦 Required Python Packages

| Package | Purpose |
|---------|---------|
| `google-generativeai` | Access Gemini models via Google Generative AI |
| `ipywidgets` | Create interactive UI in notebooks |
| `IPython` (`IPython.display`) | Render markdown and rich outputs |
| `langgraph` | Build LLM agent flows |
| `langchain` | Framework for chaining LLM tasks |
| `langchain_community` | Community tools for LangChain |
| `nest_asyncio` | Enable async execution in Jupyter |
| `python-dotenv` | Load secrets like API keys from `.env` file |

---

## 🛠️ Planned Features

- [x] Tweet generation agent
- [ ] Health assistant AI
- [ ] Blog content generator
- [ ] Resume builder agent
- [ ] Travel planner assistant

---

## 🧑‍💻 Author

Made with ❤️ by Dhruv Sundan  
Feel free to connect or contribute!
