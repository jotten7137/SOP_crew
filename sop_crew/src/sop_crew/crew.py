from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from sop_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class SOPCrew():
	"""SOP crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

# Agents
	@agent
	def process_owner(self) -> Agent:
		return Agent(
			config=self.agents_config['process_owner'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def documentation_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['documentation_specialist'],
			verbose=True
		)
	
	@agent
	def quality_assurance(self) -> Agent:
		return Agent(
			config=self.agents_config['quality_assurance'],
			verbose=True
		)
	
	@agent
	def graphic_designer(self) -> Agent:
		return Agent(
			config=self.agents_config['graphic_designer'],
			verbose=True
		)
	
	@agent
	def conversion_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['conversion_specialist'],
			verbose=True
		)


# Tasks
	@task
	def step_task(self) -> Task:
		return Task(
			config=self.tasks_config['step_task'],
			agent=self.process_owner(),
			output_file='markdown/process_owner_steps.md'
		)

	@task
	def document_task(self) -> Task:
		return Task(
			config=self.tasks_config['document_task'],
			agent=self.documentation_specialist(),
			output_file='markdown/SOP_draft.md'
		)
	
	@task
	def quality_task(self) -> Task:
		return Task(
			config=self.tasks_config['quality_task'],
			agent=self.quality_assurance(),
			output_file='markdown/SOP_revised.md'
		)
	
	@task
	def visual_task(self) -> Task:
		return Task(
			config=self.tasks_config['visual_task'],
			agent=self.graphic_designer(),
			output_file='markdown/visual.md'
		)
	
	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			agent=self.conversion_specialist(),
			output_file='markdown/SOP.md'
		)


# Crew
	@crew
	def crew(self) -> Crew:
		"""Creates the SOP Crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=2,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)