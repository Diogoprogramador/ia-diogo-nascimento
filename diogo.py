#!/usr/bin/env python3
"""
IA Diogo Nascimento - Assistente de conversação offline
Similar ao Ollama, roda localmente na sua máquina
"""

import ollama
import sys


class DiogoAI:
    # Ajustado o padrão para "llama3.1:8b" que já está baixado no seu Arch
    def __init__(self, model="llama3.1:8b"):
        """
        Inicializa a IA Diogo Nascimento
        
        Args:
            model: Nome do modelo a ser usado (default: llama3.1:8b)
                   Outras opções: llama3:latest, qwen2.5-coder:latest, etc.
        """
        self.model = model
        self.conversation_history = []
        
    def chat(self, message):
        """
        Envia uma mensagem para a IA e obtém a resposta
        
        Args:
            message: Mensagem do usuário
            
        Returns:
            Resposta da IA
        """
        try:
            response = ollama.chat(
                model=self.model,
                messages=self.conversation_history + [{"role": "user", "content": message}]
            )
            
            # Atualiza histórico da conversa
            self.conversation_history.append({"role": "user", "content": message})
            self.conversation_history.append({"role": "assistant", "content": response['message']['content']})
            
            return response['message']['content']
            
        except Exception as e:
            return f"Erro ao comunicar com a IA: {str(e)}"
    
    def clear_history(self):
        """Limpa o histórico da conversa"""
        self.conversation_history = []
        print("Histórico de conversa limpo.")
    
    def interactive_mode(self):
        """Inicia o modo interativo de conversação"""
        # Ajustado o alinhamento visual da tabela dinâmica para o novo nome do modelo
        print(f"""
╔══════════════════════════════════════╗
║          IA Diogo Nascimento         ║
║         Modelo: {self.model:<21}║
╚══════════════════════════════════════╝

Digite suas mensagens para conversar comigo.
Comandos especiais:
  /clear - Limpar histórico da conversa
  /exit  - Sair
""")
        
        while True:
            try:
                user_input = input("\nVocê: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == '/exit':
                    print("\nAté logo! 👋")
                    break
                
                if user_input.lower() == '/clear':
                    self.clear_history()
                    continue
                
                print("Diogo Nascimento: ", end='', flush=True)
                response = self.chat(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\nAté logo! 👋")
                break
            except EOFError:
                print("\n\nAté logo! 👋")
                break


def main():
    """Função principal"""
    # Se você passar um argumento no terminal, ele usa. 
    # Se não passar nada, usa o "llama3.1:8b" por padrão sem quebrar.
    if len(sys.argv) > 1:
        model = sys.argv[1]
    else:
        model = "llama3.1:8b"
    
    # Cria a instância da IA Diogo Nascimento
    diogo = DiogoAI(model=model)
    
    # Inicia o modo interativo
    diogo.interactive_mode()


if __name__ == "__main__":
    main()
