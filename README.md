# IA Diogo Nascimento - Assistente Offline

Assistente de IA offline desenvolvido em Python que utiliza o Ollama para executar modelos de linguagem (LLMs) localmente, garantindo conversas privadas, rápidas e sem necessidade de conexão com a internet.

---

## 🚀 Características do Sistema

- **100% Offline**: Todo o processamento é feito localmente na sua máquina.
- **Privacidade Total**: Seus dados e conversas nunca saem do seu computador.
- **Memória de Contexto**: Mantém o histórico da conversa atual para respostas coerentes.
- **Multi-modelo**: Suporta qualquer modelo disponível na biblioteca do Ollama (como Llama 3.2, Llama 3.1, Qwen, etc.).
- **Interface CLI Limpa**: Visual simples, direto e fácil de operar no terminal.

## 📋 Pré-requisitos

1. **Python 3.8 ou superior** instalado.
2. **Ollama** instalado e com o serviço ativo no sistema.

## 🔧 Instalação e Configuração

### 1. Instalar o Ollama

#### No Linux (Arch Linux, Ubuntu, Debian, etc.):
```bash
curl -fsSL https://ollama.com | sh
```
*Após a instalação no Arch Linux, certifique-se de inicializar o serviço do sistema:*
```bash
sudo systemctl start ollama
```

#### No Windows ou macOS:
Baixe e execute o instalador oficial em [https://ollama.com](https://ollama.com).

### 2. Baixar o Modelo Recomendado (Llama 3.2)

O **Llama 3.2 (3B)** é o modelo ideal para notebooks por ser leve e rápido. Baixe-o executando:

```bash
ollama pull llama3.2
```
*Nota: Se o seu terminal interceptar o comando acima e abrir um chat em inglês, use o método alternativo via API:*
```bash
curl http://localhost:11434/api/pull -d '{"name": "llama3.2"}'
```

### 3. Configurar o Ambiente Python

Na pasta do projeto, crie e ative o seu ambiente virtual, depois instale a biblioteca necessária:

```bash
# Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate

# Instalar a biblioteca do Ollama
pip install -r requirements.txt
```

## 💻 Como Usar

### Inicialização Padrão
Execute o script principal dentro do seu ambiente virtual ativado:

```bash
python diogo.py
```
Isso iniciará o assistente carregando o modelo padrão configurado (`llama3.1:8b`).

### Escolher Outro Modelo pelo Terminal
Você pode forçar o bot a iniciar com qualquer outro modelo que já tenha baixado (como o Llama 3.2 que você baixou no passo anterior), passando o nome dele como argumento:

```bash
python diogo.py llama3.2
```

### Comandos Especiais no Chat
Durante a conversa, você pode digitar estes comandos diretamente no campo de texto:
- `/clear` - Limpa todo o histórico da conversa atual (útil se a IA começar a se confundir).
- `/exit` - Encerra o programa com segurança.

## 🎮 Exemplo de Interação


Ao iniciar o assistente no terminal, a interface gerencia o histórico de forma limpa e responde mantendo o contexto das mensagens anteriores:

```text
\$ python diogo.py llama3.2

[Sistema] Carregando modelo 'llama3.2'...
[Sistema] Assistente iniciado com sucesso!
[Sistema] Digite /clear para limpar o histórico ou /exit para sair.

Você: Olá, meu nome é Diogo e sou desenvolvedor Python.
IA: Olá, Diogo! É um prazer conversar com você. Como desenvolvedor Python, no que posso te ajudar hoje? Deseja debugar algum código ou estruturar um novo projeto?

Você: Qual é o meu nome e o que eu faço?
IA: Seu nome é Diogo e você é um desenvolvedor Python!

Você: /clear
[Sistema] Histórico de conversa limpo com sucesso!

Você: Qual é o meu nome?
IA: Peço desculpas, mas como o histórico foi limpo, eu não sei o seu nome. Como posso ajudar você agora?

Você: /exit
[Sistema] Encerrando o assistente offline de forma segura. Até mais!
```

