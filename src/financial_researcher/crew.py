from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List


@CrewBase
class FinancialResearcher():
    """FinancialResearcher crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> BaseAgent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()],
        )
    
    @agent
    def analyst(self) -> BaseAgent:
        return Agent(
            config=self.agents_config['analyst'], # type: ignore[index]
            verbose=True
        )
    
    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_task'], # type: ignore[index]
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the research crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
