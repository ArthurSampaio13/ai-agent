# PostMaker

Crie posts e tweets otimizados com Agentes de IA (CrewAI)

![img](/imgs/image.png)

---

## Objetivo

O **PostMaker** é uma ferramenta projetada para automatizar e otimizar a criação de posts para redes sociais, como Twitter. Ele utiliza agentes de Inteligência Artificial para executar tarefas específicas, como a coleta de informações, pesquisa, redação e edição, garantindo que o conteúdo gerado seja atraente, preciso e dentro das melhores práticas para engajamento.

Seja para empresas, criadores de conteúdo ou entusiastas, o PostMaker fornece um fluxo de trabalho completo e personalizável, reduzindo o esforço manual e aumentando a eficiência na produção de conteúdo de qualidade.

---

## O que são AI Agents?

Os AI Agents (Agentes de Inteligência Artificial) são sistemas projetados para realizar tarefas específicas de forma autônoma, simulando o raciocínio humano. Esses agentes integram habilidades como percepção, aprendizado, planejamento e ação, conectando-se ao ambiente por meio de entradas (inputs) e saídas (outputs). Eles podem interagir com usuários, tomar decisões baseadas em dados, e executar ações, como chamar APIs ou controlar ferramentas físicas, sendo fundamentais para automação e eficiência em diversos contextos.


![Screenshot 2024-04-07 at 2.53.23 PM.png](/imgs/agent.png)
> Legenda da Imagem:
> A imagem ilustra o funcionamento de um AI Agent, mostrando como ele interage com o ambiente (Environment), processa informações (Perception), armazena e utiliza conhecimento (Brain) e executa ações (Action). Os agentes recebem entradas do ambiente, como texto, áudio ou imagens, processam essas informações em seu "cérebro" usando memória e conhecimento acumulado, e tomam decisões ou realizam ações, como chamar APIs ou operar ferramentas físicas. Este ciclo reflete como os agentes de inteligência artificial combinam percepção, planejamento e ação para resolver problemas de forma autônoma.

## Requisitos

- **Python**: É **obrigatório** utilizar a versão **3.12.3** do Python. Outras versões não são suportadas.
- **Poetry**: Gerenciador de dependências utilizado pelo projeto.

---

## Instalação

1. Certifique-se de que possui o **Python 3.12.3** instalado no seu sistema. Para verificar a versão, execute:

   ```sh
   python --version
   ```

   Se não estiver na versão correta, faça o download e instale a versão **3.12.3** do Python em [python.org](https://www.python.org/downloads/release/python-3123/).

2. Crie um ambiente virtual utilizando a versão **3.12.3**:

   ```sh
   python -m venv venv
   ```

3. Ative o ambiente virtual:

   - **Windows**:
     ```sh
     venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```sh
     source venv/bin/activate
     ```

4. Clone o repositório:

   ```sh
   git clone https://github.com/ArthurSampaio13/ai-agent.git
   cd ai-agent
   ```

5. Instale as dependências com o Poetry:

   ```sh
   poetry install
   ```

---

## Adicione as chaves de API

Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API da Groq e/ou OpenAI:

```env
GROQ_API_KEY=<GROQ_API_KEY>
OPENAI_API_KEY=<OPENAI_API_KEY>
```

---

## Modelos de LLM Suportados

O **PostMaker** suporta as seguintes LLMs, permitindo flexibilidade entre serviços online e locais:

1. **Groq (LLama-3.3-70b)**  
   Um modelo avançado e versátil, ótimo para gerar conteúdo complexo.

2. **ChatGPT (GPT-4o-mini)**  
   Modelo baseado em nuvem da OpenAI, focado em tarefas que exigem conectividade.

3. **Ollama (Local: gemma2:9b)**  
   Um modelo executado localmente, ideal para quem prefere não depender de serviços online.

Para configurar o modelo desejado, edite a linha correspondente na classe `Config` (localizada em `postmaker/config.py`):

```py
from postmaker.config import Config, Model

Config.MODEL = Model.LLAMA_3  # Para usar o modelo Groq LLama-3.3-70b
Config.MODEL = Model.GPT_4o  # Para usar o modelo GPT-4o-mini (OpenAI)
Config.MODEL = Model.LOCAL  # Para usar o modelo local Ollama gemma2:9b
```

---

## Uso

### Configuração Inicial

Edite os inputs no arquivo `app.py`:

```py
inputs = {
    "topic": "Resumo das principais novas funcionalidades do Phi-3",
    "urls": [
        "https://learn.microsoft.com/pt-br/windows/ai/models/get-started-models-genai",
    ],
    "suggestion": "Foque no desempenho e em como utilizar o modelo.",
}
```

Adicione tweets ou conteúdos de exemplo no arquivo `data/tweets.md` para análise de estilo:

Um exemplo:
```md
# Tweet

Já se perguntou como reproduzir o GPT-2 (124M) de forma eficiente?  
@karpathy com o llm.c tem a resposta!  

- 90 minutos, $20 em 8x A100 80GB SXM  
- Dataset FineWeb: 10 bilhões de tokens  
- MFU: 49-60%, 178K tokens/seg  
```

### Execução

Execute o aplicativo:

```sh
poetry run python app.py
```

### Saída

Os resultados da execução serão salvos em `output/tweet.md` e exibidos no console. Exemplo:

```py
{
  'total_tokens': 25207, 
  'prompt_tokens': 19783, 
  'completion_tokens': 5424, 
  'successful_requests': 10
}
```

---

## Resultado

Os posts gerados pela equipe (salvos em `output/tweet.md`):

```md
Post original:  
Descubra o Phi-3! 🚀 Modelo de linguagem de grande escala para geração, transformação e tradução de texto. 🤖 Aprenda mais sobre suas funcionalidades e como integrá-lo em aplicativos do Windows. #Phi3 #IA #MachineLearning  

Versão 1:  
Descubra o Phi-3! 🚀 Modelo de linguagem de grande escala para geração, transformação e tradução de texto. 🤖 Aprenda mais sobre suas funcionalidades e como integrá-lo em aplicativos do Windows para melhorar o desempenho.  
#Phi3 #IA #MachineLearning  

Versão 2:  
O Phi-3 chegou! 🚀 Aprenda a utilizar o modelo de linguagem de grande escala para gerar texto, responder a perguntas e realizar outras tarefas de processamento de linguagem natural em aplicativos do Windows. 🤖  
#Phi3 #IA #MachineLearning  

Versão 3:  
Melhore o desempenho dos seus aplicativos do Windows com o Phi-3! 🚀 Modelo de linguagem de grande escala para geração, transformação e tradução de texto. 🤖 Aprenda mais sobre como integrá-lo e aproveitar suas funcionalidades.  
#Phi3 #IA #MachineLearning  
```
