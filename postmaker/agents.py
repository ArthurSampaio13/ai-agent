from textwrap import dedent

from crewai import Agent
from crewai_tools import ScrapeWebsiteTool

from tweetcrafter.callbacks import step_callback
from tweetcrafter.config import Config
from tweetcrafter.tools import read_tweets, save_tweet

scrape_tool = ScrapeWebsiteTool()


def scraper_agent(llm) -> Agent:
    return Agent(
        role="Scraper Sênior de Sites",
        goal="Rastrear o conteúdo dos URLs fornecidos e retornar os dados de texto.",
        backstory=dedent("""
            Você é um engenheiro de software experiente, mestre em rastrear diversos dados da web (sites, imagens, vídeos).
            Sua função é ler o conteúdo dos URLs fornecidos usando o `scrape_tool` e extrair o texto.
        """),
        llm=llm,
        tools=[scrape_tool],
        allow_delegation=False,
        step_callback=lambda response: step_callback(
            response, "scrape_agent", Config.Path.AGENT_LOGS_DIR / "scraper.jsonl"
        ),
    )


def researcher_agent(llm) -> Agent:
    return Agent(
        role="Pesquisador Técnico Sênior",
        goal="Extrair os principais insights e informações da internet sobre o tema e URLs fornecidos.",
        backstory=dedent("""
            Você é um pesquisador técnico com expertise em tecnologias como Inteligência Artificial, Aprendizado de Máquina, Modelos de Linguagem de Grande Escala, etc.
            Sua função é resumir os principais insights dos textos fornecidos relacionados ao tema indicado.
        """),
        llm=llm,
        allow_delegation=False,
        step_callback=lambda response: step_callback(
            response,
            "researcher_agent",
            Config.Path.AGENT_LOGS_DIR / "researcher.jsonl",
        ),
    )


def writer_agent(llm) -> Agent:
    return Agent(
        role="Redator Sênior de Mídias Sociais",
        goal=dedent("""
            Escreva uma publicação no Twitter com base no conteúdo de pesquisa fornecido pelo Pesquisador.
            Use a ferramenta read_tweets para ler todos os tweets – a ferramenta não possui argumentos. 
            Emule o estilo de escrita dos tweets no seu próprio texto – escolha de palavras, formatação, uso de emojis, hashtags, etc.
            """),
        backstory=dedent("""
            Você tem ampla experiência em escrever conteúdo envolvente para plataformas de mídia social como Twitter, Facebook, Instagram, etc.
            Seu foco principal é tecnologia – Inteligência Artificial, Aprendizado de Máquina, Modelos de Linguagem de Grande Escala, etc.
            Você tem um histórico comprovado de escrever tweets que envolvem o público e geram tráfego.
            """),
        llm=llm,
        allow_delegation=False,
        tools=[read_tweets],
        step_callback=lambda response: step_callback(
            response, "writer_agent", Config.Path.AGENT_LOGS_DIR / "writer.jsonl"
        ),
    )


def editor_agent(llm) -> Agent:
    return Agent(
        role="Editor Sênior de Tweets",
        goal=dedent("""
                Escreva 3 versões diferentes do tweet com base no relatório de pesquisa original.
                Mantenha o formato e o estilo do tweet original.
                Crie um único texto que contenha todas as variantes (original e versões diferentes) do tweet.
                Use a ferramenta save_tweet e utilize o parâmetro text para salvar o texto.
            """),
        backstory=dedent("""
            Você tem experiência em mídias sociais e entende a importância de conteúdo envolvente.
            Você sempre escreve tweets que geram muito engajamento e é conhecido por seu estilo criativo de escrita.
            """),
        llm=llm,
        allow_delegation=False,
        tools=[save_tweet],
        step_callback=lambda response: step_callback(
            response, "writer_agent", Config.Path.AGENT_LOGS_DIR / "editor.jsonl"
        ),
    )
