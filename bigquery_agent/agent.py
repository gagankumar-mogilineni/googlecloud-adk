from google.adk.agents import Agent
from google.adk.tools import google_search
import google.auth
from google.adk.tools.bigquery import BigQueryCredentialsConfig
from google.adk.tools.bigquery import BigQueryToolset
from google.adk.tools.bigquery.config import BigQueryToolConfig
from google.adk.tools.bigquery.config import WriteMode
from google.genai import types
tool_config = BigQueryToolConfig(write_mode=WriteMode.BLOCKED)

application_default_credentials,_ = google.auth.default()
credentials_config = BigQueryCredentialsConfig(
    credentials=application_default_credentials
)
 
bigquery_toolset = BigQueryToolset(
    credentials_config=credentials_config, bigquery_tool_config=tool_config
)

root_agent = Agent(
    name="bigquery_agent",
    model="gemini-2.0-flash",
    description="Agent answer question on Bigquery",
    instruction="""
    You are the data science agent with access to several bigquery tools.
    Make use of these tools to answer the users question.
    """,
    tools = [bigquery_toolset]
)