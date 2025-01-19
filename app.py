from crewai import Crew, Process
from dotenv import load_dotenv

from tweetcrafter.agents import (
    editor_agent,
    researcher_agent,
    scraper_agent,
    writer_agent,
)
from tweetcrafter.config import Config
from tweetcrafter.models import create_model
from tweetcrafter.tasks import (
    edit_task,
    research_content_task,
    scrape_content_task,
    write_tweet_task,
)

load_dotenv()

Config.Path.AGENT_LOGS_DIR.mkdir(exist_ok=True, parents=True)
Config.Path.OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

llm = create_model(Config.MODEL)

scraper = scraper_agent(llm)
researcher = researcher_agent(llm)
writer = writer_agent(llm)
editor = editor_agent(llm)

scrape_content = scrape_content_task(scraper)
research_content = research_content_task(researcher)
write_tweet = write_tweet_task(writer, context=[research_content])
edit = edit_task(editor, context=[write_tweet, research_content])

crew = Crew(
    agents=[scraper, researcher, writer, editor],
    tasks=[scrape_content, research_content, write_tweet, edit],
    process=Process.sequential,
    verbose=2,
    memory=False,
    output_log_file=str(Config.Path.LOGS_DIR / "crew.log"),
)

inputs = {
    "topic": "Resumo das principais novas funcionalidades do Phi-3",
    "urls": [
        "https://learn.microsoft.com/pt-br/windows/ai/models/get-started-models-genai",
    ],
    "suggestion": "Foque no desempenho e em como utilizar o modelo.",
}

crew.kickoff(inputs=inputs)

print(crew.usage_metrics)
