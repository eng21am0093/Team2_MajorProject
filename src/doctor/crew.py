from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, MDXSearchTool, SerperDevTool, ScrapeWebsiteTool

@CrewBase
class Diagnosis():
    """Diagnosis crew"""
    # YAML configuration files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    # File paths for the data files - using absolute paths
    patient_history_path = "C:/Users/Ratan/Desktop/doctor/knowledge/data/patient_profile.txt"
    lab_history_path = "C:/Users/Ratan/Desktop/doctor/knowledge/data/lab_results.txt"
    imaging_data_path = "C:/Users/Ratan/Desktop/doctor/knowledge/data/imaging_results.txt"

    # Knowledge directory path and MDX file path
    knowledge_dir = "C:/Users/Ratan/Desktop/doctor/knowledge"
    mdx_file_path = "C:/Users/Ratan/Desktop/doctor/knowledge/overall.mdx"

    # SerperDev API key
    serper_api_key = "9d499852bca0a1bfda0f6365f4d05769b275f2b2"
    
    def __init__(self):
        # Initialize MDX search tool with the specific MDX file
        self.mdx_search_tool = MDXSearchTool(mdx=self.mdx_file_path)
        
        # Initialize file read tools
        self.patient_history_tool = FileReadTool(file_path=self.patient_history_path)
        self.lab_history_tool = FileReadTool(file_path=self.lab_history_path)
        self.imaging_data_tool = FileReadTool(file_path=self.imaging_data_path)
        
        # Set environment variable for SerperDev
        import os
        os.environ["SERPER_API_KEY"] = self.serper_api_key
        
        # Initialize SerperDev search tool
        self.serper_search_tool = SerperDevTool(api_key=self.serper_api_key)
        
        # Initialize website scraping tool
        self.scrape_website_tool = ScrapeWebsiteTool()
    
    @agent
    def ethics_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['ethics_advisor'],
            verbose=True,
            tools=[
                self.patient_history_tool,
                self.lab_history_tool,
                self.imaging_data_tool,
                self.mdx_search_tool
            ]
        )
    
    @agent
    def medical_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['medical_researcher'],
            verbose=True,
            tools=[
                self.patient_history_tool,
                self.lab_history_tool,
                self.imaging_data_tool,
                self.mdx_search_tool,
                self.serper_search_tool,
                self.scrape_website_tool
            ]
        )
    
    @agent
    def patient_historian(self) -> Agent:
        return Agent(
            config=self.agents_config['patient_historian'],
            verbose=True,
            tools=[
                self.patient_history_tool,
                self.mdx_search_tool
            ]
        )
    
    @agent
    def lab_interpreter(self) -> Agent:
        return Agent(
            config=self.agents_config['lab_interpreter'],
            verbose=True,
            tools=[
                self.lab_history_tool,
                self.imaging_data_tool,
                self.mdx_search_tool
            ]
        )
    
    @agent
    def case_data_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['case_data_extractor'],
            verbose=True,
            tools=[
                self.patient_history_tool,
                self.lab_history_tool,
                self.imaging_data_tool,
                self.mdx_search_tool
            ]
        )
    
    @agent
    def diagnostic_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['diagnostic_specialist'],
            verbose=True,
            tools=[
                self.patient_history_tool,
                self.lab_history_tool,
                self.imaging_data_tool,
                self.mdx_search_tool
            ]
        )
    
    @task
    def ethics_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['ethics_review_task']
        )
    
    @task
    def medical_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['medical_research_task']
        )
    
    @task
    def patient_history_task(self) -> Task:
        return Task(
            config=self.tasks_config['patient_history_task']
        )
    
    @task
    def lab_interpretation_task(self) -> Task:
        return Task(
            config=self.tasks_config['lab_interpretation_task']
        )
    
    @task
    def case_data_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['case_data_extraction_task']
        )
    
    @task
    def diagnostic_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config['diagnostic_assessment_task']
        )
    
    @task
    def treatment_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['treatment_recommendation_task']
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the Diagnosis crew"""
        return Crew(
            agents=[
                self.ethics_advisor(),
                self.medical_researcher(),
                self.patient_historian(),
                self.lab_interpreter(),
                self.case_data_extractor(),
                self.diagnostic_specialist()
            ],
            tasks=[
                self.ethics_review_task(),
                self.medical_research_task(),
                self.patient_history_task(),
                self.lab_interpretation_task(),
                self.case_data_extraction_task(),
                self.diagnostic_assessment_task(),
                self.treatment_recommendation_task()
            ],
            process=Process.sequential,
            verbose=True
        )