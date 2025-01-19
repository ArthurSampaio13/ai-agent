from textwrap import dedent
from typing import List

from crewai import Agent, Task


def scrape_content_task(agent: Agent) -> Task:
    return Task(
        description=("Extraia o texto dos URLs fornecidos {urls}."),
        expected_output="Lista do texto extraído dos URLs.",
        agent=agent,
    )


def research_content_task(agent: Agent) -> Task:
    return Task(
        description=(
            dedent("""
            Use o conteúdo extraído para escrever um relatório de pesquisa sobre o tema {topic}.
            """)
        ),
        expected_output="Relatório com conteúdo bem estruturado e preciso sobre o tema.",
        agent=agent,
    )


def write_tweet_task(agent: Agent, context: List[Task] = []) -> Task:
    return Task(
        description=dedent("""
            Escreva um tweet com base no relatório de pesquisa e no estilo de escrita dos tweets.
            Destaque os principais detalhes técnicos em uma lista com marcadores que seja envolvente e fácil de entender.
            Use até 240 caracteres. Inclua hashtags e emojis relevantes.
        """),
        expected_output="Texto do tweet.",
        agent=agent,
        context=context,
    )


def edit_task(agent: Agent, context: List[Task] = []) -> Task:
    return Task(
        description=dedent("""
            Crie 3 versões diferentes do tweet com base em sua crítica, no relatório de pesquisa original,
            e na sugestão {suggestion}. Salve o tweet original e as 3 versões do tweet.
        """),
        expected_output="Tweet original e 3 versões salvas em um arquivo de texto.",
        agent=agent,
        context=context,
    )
