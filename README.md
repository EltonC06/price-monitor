# Price Monitor: Scraper de preços online

![Badge de Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow) 

---

## 💻 Descrição do Projeto
O sistema coleta automaticamente os preços dos produtos cadastrados em intervalos regulares (ex: a cada 6 horas), sem necessidade de intervenção manual.

## ✨ Funcionalidades
### 1. 📊 Rastreamento Automático de Preços
**Descrição:** O sistema coleta automaticamente os preços dos produtos cadastrados em intervalos regulares (ex: a cada 6 horas), sem necessidade de intervenção manual.
Como funciona:

- Usuário cadastra URLs de produtos (iPhone no Mercado Livre, notebook na Amazon, etc.)
- Sistema usa web scraping para verificar preços periodicamente
- Armazena histórico completo de variações de preço no banco de dados
- Funciona 24/7 em segundo plano, mesmo com o site fechado
### 2. 🔔 Sistema de Alertas Inteligentes
**Descrição:** Notifica o usuário instantaneamente quando o preço de um produto cai abaixo de um valor definido por ele.
Como funciona:

- Usuário define "preço alvo" para cada produto (ex: "me avise se o iPhone ficar abaixo de R$ 4.500")
- Quando preço atual ≤ preço alvo, sistema dispara alerta automático
- Notificações via email com detalhes do produto e link direto
- Histórico de todos os alertas enviados

### 3. 📈 Dashboard com Análise Visual
**Descrição:** Interface web que exibe gráficos interativos mostrando a evolução dos preços ao longo do tempo e tendências de mercado.
Como funciona:

- Gráficos de linha mostrando variação de preços por período (semana, mês)
- Comparação de preços entre diferentes lojas para o mesmo produto
- Estatísticas úteis: menor preço registrado, maior desconto encontrado, preço médio
- Lista organizada de todos os produtos monitorados com status atual

## 🚀 Tecnologias Utilizadas

Liste as principais linguagens, frameworks, bibliotecas e outras ferramentas utilizadas no desenvolvimento.

* **Frontend:** React Js/Bootstrap.
* **Backend:**  Flask, Beautiful Soup, Celery.
* **Banco de Dados:** SQLite

## ⚙️ Instalação

### Pré-requisitos
Em andamento...

### Passos para Instalação
Em andamento...
## 💡 Como Usar
Em andamento...

## ✉️ Contato

* **Email:** [douglaswesley0407@gmail.com](mailto:douglaswesley0407@gmail.com)
* **LinkedIn:** [Meu Linkedin](https://www.linkedin.com/in/douglas-wesley/)

## Agradecimentos (Opcional)
* Gabriel Saraiva Sampaio - Por colaborar com o desenvolvimento criativo do projeto.
