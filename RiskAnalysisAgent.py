# pip install azure-ai-projects~=1.0.0b7
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from semantic_kernel.agents import Agent

class RiskAnalysisAgent(Agent):
    def __init__(self, kernel):
        super().__init__()
        self.name = "RiskAnalysisAgent"
        self.kernel = kernel
        # Use object.__setattr__ to bypass Pydantic validation
        object.__setattr__(self, "project_client", AIProjectClient.from_connection_string(
            credential=DefaultAzureCredential(),
            conn_str="southindia.api.azureml.ms;609bbbac-377b-4a23-b9e6-6d76f678b5f8;intelligent-claim-processing-RG;ICP-AI-Agent"
        ))
        object.__setattr__(self, "agent", self.project_client.agents.get_agent("asst_yjIdV74j6hIP8vWedcHqrVkY"))
        object.__setattr__(self, "thread", self.project_client.agents.get_thread("thread_MhbFbI7WRtDsh5u56mkssSjI"))

    def perform_task(self, input_data):
        self.project_client.agents.create_message(
            thread_id=self.thread.id,
            role="user",
            content=input_data
        )
        self.project_client.agents.create_and_process_run(
            thread_id=self.thread.id,
            agent_id=self.agent.id
        )
        messages = self.project_client.agents.list_messages(thread_id=self.thread.id)
        return [msg.as_dict() for msg in messages.text_messages]

    def get_response(self, input_data):
        return self.perform_task(input_data)

    def invoke(self, input_data):
        return self.perform_task(input_data)

    def invoke_stream(self, input_data):
        yield f"RiskAnalysisAgent streaming response to {input_data}"