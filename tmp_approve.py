import asyncio
from temporalio.client import Client
from ag_exams.workflow import BuildScenarioWorkflow

async def approve_all():
    client = await Client.connect("localhost:7233")
    query = 'WorkflowType="BuildScenarioWorkflow" AND ExecutionStatus="Running"'
    async for wf in client.list_workflows(query):
        print(f"Found child workflow: {wf.id}")
        handle = client.get_workflow_handle(wf.id)
        await handle.signal(BuildScenarioWorkflow.approve_scenario, "")
        print(f"Approved {wf.id}")

asyncio.run(approve_all())
