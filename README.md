# AutoGen Agents

Hands-on examples of building AI agents with [Microsoft AutoGen](https://github.com/microsoft/autogen) (AgentChat API). Runs on a local **Ollama** model by default, or **OpenAI** if you prefer.

## What's inside

| File | What it shows |
|------|---------------|
| `examples/01_single_agent.py` | A single assistant agent |
| `examples/02_tool_agent.py` | An agent that calls Python tools |
| `examples/03_team_writer_critic.py` | A two-agent team (writer + critic) with termination conditions |
| `src/config.py` | Model client factory (Ollama / OpenAI via `.env`) |
| `src/tools.py` | Reusable tools: current time, calculator |

## Project structure

```
autogen-agents/
├── examples/
│   ├── 01_single_agent.py
│   ├── 02_tool_agent.py
│   └── 03_team_writer_critic.py
├── src/
│   ├── config.py
│   └── tools.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
copy .env.example .env
```

### Option A: Ollama (local, free)

```bash
ollama pull llama3.1
ollama serve
```

Keep `LLM_PROVIDER=ollama` in `.env`.

### Option B: OpenAI

Set `LLM_PROVIDER=openai` and add your `OPENAI_API_KEY` in `.env`.

## Run

```bash
python examples/01_single_agent.py
python examples/02_tool_agent.py
python examples/03_team_writer_critic.py
```

## Key concepts

- **AssistantAgent**: an LLM-backed agent with a system message and optional tools.
- **Tools**: plain Python functions the agent can call (function calling).
- **Team**: several agents collaborating, e.g. `RoundRobinGroupChat`.
- **Termination conditions**: rules that stop a run (`TextMentionTermination`, `MaxMessageTermination`), combinable with `|`.
- **Model client**: the abstraction over the LLM provider.

## Next steps

- Add a web-search or file-reading tool
- Try `SelectorGroupChat` for dynamic speaker selection
- Add a human-in-the-loop agent with `UserProxyAgent`

## Author

Subrata Mondal - [LinkedIn](https://www.linkedin.com/in/subrata-mondal-3a57ab154/) | [GitHub](https://github.com/subbuworkspace)
