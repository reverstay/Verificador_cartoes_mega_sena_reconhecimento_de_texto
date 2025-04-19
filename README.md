# Verificador_cartoes_mega_sena_reconhecimento_de_texto# Mega‑Sena OCR

Sistema Dockerizado em Python para:

- Extrair números de cartões da Mega‑Sena via OCR
- Armazenar resultados em um banco SQLite
- Exibir jogos capturados por uma interface web em Flask

---

## 🛠️ Pré‑requisitos

Antes de começar, certifique‑se de ter instalado:

- **Git**: para clonar o repositório
- **Docker** (>= 20.10): para buildar e rodar o ambiente isolado

---

## 🚀 Clonando o repositório

1. Em um terminal, clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/mega-sena-ocr.git
   ```
2. Navegue até o diretório da aplicação:
   ```bash
   cd mega-sena-ocr/app
   ```

---

## 📂 Estrutura de diretórios

```plaintext
mega-sena-ocr/
├─ app/                # Código-fonte da aplicação
│  ├─ Dockerfile       # Configuração da imagem Docker
│  ├─ requirements.txt # Dependências Python
│  ├─ ocr.py           # Módulo de reconhecimento de números
│  ├─ models.py        # Definição do banco com SQLAlchemy
│  ├─ app.py           # Aplicação Flask
│  └─ templates/       # Views HTML
│     └─ jogos.html    # Página para listar jogos
├─ data/               # Imagens de cartões (bind mount do container)
└─ db/                 # Banco SQLite (bind mount do container)
```

---

## 🐳 Build da imagem Docker

No diretório `app/`, execute:

```bash
docker build -t mega-sena-ocr .
```

---

## ▶️ Executando o container

Ainda em `app/`, rode:

```bash
docker run --rm -p 5000:5000 \
  -v $(pwd)/../data:/usr/src/app/data \
  -v $(pwd)/../db:/usr/src/app/../db \
  mega-sena-ocr
```

- A opção `-p 5000:5000` expõe a porta 5000 do container
- Os volumes `data` e `db` garantem persistência de imagens e jogos

---

## 🌐 Acessando a aplicação

Abra o navegador e acesse:

```
http://localhost:5000
```

- **Envie** uma imagem de cartão pelo formulário
- **Veja** os jogos listados logo abaixo

---

## 📝 Como usar

1. Clique em **"Escolher arquivo"** e selecione uma foto do cartão
2. Clique em **"Processar"**
3. O OCR vai reconhecer os números e salvar no SQLite
4. A lista de **jogos capturados** permanece visível na página

---

## 🤝 Contribuição

Pull requests são bem‑vindos! Para contribuições maiores:

1. Crie um _fork_
2. Abra uma _branch_ com a feature/fix (`git checkout -b feature/alguma-coisa`)
3. Faça commits claros e descritivos
4. Envie um _pull request_

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License].

