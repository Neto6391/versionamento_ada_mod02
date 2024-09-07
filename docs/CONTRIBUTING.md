# Guia de Contribuição

Bem-vindo ao nosso projeto! Estamos felizes em receber sua contribuição. Este guia foi elaborado para ajudá-lo a entender como você pode participar efetivamente do desenvolvimento do projeto.

## Script user_data_ec2 para Provisionamento

Nosso projeto utiliza um script user_data_ec2 personalizado para provisionar instâncias EC2 da Amazon. Este script é crucial para garantir que todas as instâncias sejam configuradas de maneira consistente e eficiente. Ao contribuir com alterações relacionadas ao provisionamento, considere as seguintes diretrizes:

### Estrutura e Componentes do Script

1. **Atualização Inicial**: O script deve começar com uma atualização completa do sistema para garantir que estamos trabalhando com as versões mais recentes dos pacotes.

2. **Instalação de Dependências**: Liste e instale todas as dependências necessárias para o projeto. Mantenha esta lista atualizada conforme o projeto evolui.

3. **Configurações Personalizadas**: Implemente configurações específicas do projeto de forma clara e modular.

4. **Configuração de Rede**: Inclua as configurações de rede necessárias para o ambiente AWS.

5. **Sistema de Logs**: Implemente um sistema de logs robusto para facilitar o diagnóstico de problemas.

### Exemplo de Estrutura do Script

```bash
#!/bin/bash
# Script de Provisionamento EC2

# Atualização do Sistema
echo "Iniciando atualização do sistema..."
yum update -y

# Instalação de Dependências
echo "Instalando dependências..."
yum install -y docker git nginx

# Configurações Personalizadas
echo "Aplicando configurações personalizadas..."
# Adicione aqui suas configurações específicas

# Configuração de Rede
echo "Configurando rede..."
# Implemente aqui as configurações de rede necessárias

# Sistema de Logs
echo "Configurando sistema de logs..."
# Configure aqui o sistema de logging

echo "Provisionamento concluído com sucesso!"
```

## Processo de Contribuição

1. **Faça um Fork**: Comece criando uma cópia do repositório em sua conta GitHub.

2. **Crie uma Branch**: Desenvolva suas alterações em uma nova branch. Use um nome descritivo, por exemplo:
   ```
   git checkout -b feat/validacao-formulario
   ```

3. **Desenvolva e Commit**: Faça suas alterações e commit seguindo nossas convenções de mensagens (detalhadas abaixo).

4. **Push e Pull Request**: Envie suas alterações para o seu fork e abra um Pull Request no repositório original.

5. **Revisão**: Aguarde a revisão do encarregado do repositório. Esteja preparado para fazer ajustes se necessário.

## Convenções de Mensagens de Commit

Adotamos uma versão simplificada do Conventional Commits. Use os seguintes prefixos em suas mensagens:

- `feat:` para novas funcionalidades
- `fix:` para correções de bugs
- `docs:` para atualizações na documentação
- `style:` para mudanças de formatação
- `refactor:` para refatorações de código
- `test:` para adição ou modificação de testes
- `chore:` para alterações em configurações e dependências

Exemplos:
- `feat: implementa validação no formulário de cadastro`
- `fix: trata erro na inserção de dados`
- `docs: atualiza instruções de instalação no README`

## Diretrizes para Pull Requests

1. **Descreva claramente**: Explique o propósito e o impacto das suas mudanças.
2. **Mantenha-se focado**: Cada PR deve abordar uma única funcionalidade ou correção.
3. **Testes**: Inclua testes para novas funcionalidades ou correções, quando aplicável.
4. **Estilo de Código**: Siga os padrões de estilo existentes no projeto.

## Processo de Revisão

- O encarregado do repositório revisará seu PR assim que possível.
- Comentários e sugestões podem ser feitos para melhorar o código.
- Esteja aberto a fazer ajustes conforme solicitado.

## Licença

Ao contribuir, você concorda que seu trabalho será licenciado sob a mesma licença do projeto.

Agradecemos sua dedicação em melhorar este projeto! Sua contribuição é muito valiosa.
