# CrewAI-Multi-Agents-FinancialResearch

---

🇫🇷  
Ce projet utilise CrewAI pour orchestrer la collaboration entre des agents IA spécialisés dans la recherche financière. Le premier agent, le researcher, collecte et synthétise des informations détaillées sur une entreprise (performance, actualités, concurrents, perspectives). Le second, l’analyst, analyse ces données pour produire un rapport clair, structuré et accessible, adapté à une audience financière.  
Chaque agent utilise un modèle de langage (LLM) paramétrable, ce qui permet d’adapter facilement le système à différentes APIs et modèles selon vos préférences (ex : OpenAI, Gemini, Mistral...).

🇬🇧  
This project uses CrewAI to orchestrate collaboration between AI agents specialized in financial research. The researcher gathers and summarizes detailed data about a company (performance, news, competitors, outlook). The analyst then analyzes this data to produce a clear, structured, and accessible financial report.  
Each agent's LLM is fully customizable, letting you connect to any API or model you prefer (e.g., OpenAI, Gemini, Mistral...).

---

## Agents Configuration

The LLM used by each agent is fully configurable in `config/agents.yaml`. Example agents include:

- **researcher**: Senior financial researcher specializing in a given company. Gathers and synthesizes relevant information.
- **analyst**: Market analyst and report writer who analyzes research results and produces clear, engaging reports.

---

## Tasks

- **research_task**  
  Conducts thorough research on a company, focusing on current status, news, history, challenges, outlook, and competitors. Produces a detailed, structured report.

- **analysis_task**  
  Analyzes research findings, writing a comprehensive market analysis report including an executive summary, key insights, and a market outlook (not for trading decisions).

---

## Crew Configuration

The core crew is defined in `crew.py` and consists of:

- Two agents (`researcher` and `analyst`) instantiated with configurable LLMs and tools.
- Two tasks (`research_task` and `analysis_task`) performed sequentially.
- Use of `SerperDevTool` integrated in the researcher agent for enhanced web search capabilities.

---

## Installation

Make sure you have Python >=3.10 and <3.14 installed.

Install the dependency manager `uv` from Astral :  
https://docs.astral.sh/uv/getting-started/first-steps/

Then, install the dependencies:  
`uv sync`

---

## Usage

Run the project with:  
`crewai run`

This command will launch the sequential execution of the research and analysis tasks by the configured agents. The final report will be saved as `output/report.md`.

---

## Customization

- Add your `OPENAI_API_KEY` or other API keys in the `.env` file.
- Modify `config/agents.yaml` to change or add agents and their LLM configurations.
- Modify `config/tasks.yaml` to customize tasks.
- Adjust `crew.py` to extend logic, add tools, or change process flows.
- Modify `main.py` to provide custom inputs like the target company name.

---