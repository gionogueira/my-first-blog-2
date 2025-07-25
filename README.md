# 📝 Django Girls Blog

Um blog moderno e responsivo desenvolvido com Django, criado durante o tutorial Django Girls com melhorias e funcionalidades extras.

![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Melhorias Implementadas](#melhorias-implementadas)
- [Capturas de Tela](#capturas-de-tela)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## 🎯 Sobre o Projeto

Este é um blog desenvolvido em Django como parte do tutorial Django Girls, mas com várias melhorias e funcionalidades adicionais implementadas. O projeto demonstra conceitos fundamentais do desenvolvimento web com Django, incluindo:

- Sistema de autenticação
- CRUD completo para posts
- Interface responsiva
- Paginação
- Sistema de comentários (planejado)
- Design moderno com Bootstrap

## ✨ Funcionalidades

### 🔄 Funcionalidades Atuais

- ✅ **Listagem de Posts**: Visualização de todos os posts publicados
- ✅ **Detalhamento de Posts**: Página individual para cada post
- ✅ **Criação de Posts**: Interface para criar novos posts
- ✅ **Edição de Posts**: Editar posts existentes
- ✅ **Sistema de Autenticação**: Login/logout para autores
- ✅ **Design Responsivo**: Interface adaptável para todos os dispositivos
- ✅ **Paginação**: Navegação eficiente entre posts
- ✅ **Data de Publicação**: Controle de quando os posts são publicados

### 🚀 Funcionalidades Planejadas

- 🔄 Sistema de comentários
- 🔄 Categorias e tags
- 🔄 Sistema de busca
- 🔄 Perfil de usuários
- 🔄 Upload de imagens
- 🔄 Editor de texto rico

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 4.2+** - Framework web Python
- **SQLite** - Banco de dados (desenvolvimento)
- **Python 3.8+** - Linguagem de programação

### Frontend
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização personalizada
- **Bootstrap 5.3** - Framework CSS responsivo
- **JavaScript** - Interatividade

### Ferramentas
- **Git** - Controle de versão
- **VS Code** - Editor de código
- **Virtual Environment** - Isolamento de dependências

## 📋 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git

```bash
# Verificar instalações
python --version
pip --version
git --version
```

## 🚀 Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/gionogueira/my-first-blog-2.git
cd my-first-blog-2
```

2. **Crie um ambiente virtual**
```bash
python -m venv myenv
```

3. **Ative o ambiente virtual**
```bash
# Linux/Mac
source myenv/bin/activate

# Windows
myenv\Scripts\activate
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Execute as migrações**
```bash
python manage.py migrate
```

6. **Crie um superusuário** (opcional)
```bash
python manage.py createsuperuser
```

7. **Colete arquivos estáticos**
```bash
python manage.py collectstatic
```

## 🎮 Como Usar

1. **Inicie o servidor de desenvolvimento**
```bash
python manage.py runserver
```

2. **Acesse o blog**
   - Blog: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

3. **Navegue pelas funcionalidades**
   - Visualize posts na página inicial
   - Clique em um post para ver os detalhes
   - Faça login para criar/editar posts

## 📁 Estrutura do Projeto

```
djangogirls/
├── blog/                   # App principal do blog
│   ├── migrations/         # Migrações do banco de dados
│   ├── static/            # Arquivos CSS customizados
│   ├── templates/         # Templates HTML
│   ├── admin.py           # Configuração do admin
│   ├── forms.py           # Formulários
│   ├── models.py          # Modelos de dados
│   ├── urls.py            # URLs do blog
│   └── views.py           # Views/controladores
├── mysite/                # Configurações do Django
│   ├── settings.py        # Configurações principais
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # Configuração WSGI
├── static/                # Arquivos estáticos coletados
├── db.sqlite3             # Banco de dados SQLite
├── manage.py              # Script de gerenciamento Django
├── requirements.txt       # Dependências Python
└── README.md              # Este arquivo
```

## 🌟 Melhorias Implementadas

Este projeto vai além do tutorial básico do Django Girls, incluindo:

### Design e Interface
- Layout moderno com Bootstrap 5
- Navbar responsiva com navegação intuitiva
- Cards para posts com efeitos hover
- Footer informativo
- Design totalmente responsivo

### Funcionalidades Técnicas
- Sistema de paginação
- Melhor organização de templates
- Formulários aprimorados
- Validações customizadas
- Meta informações para SEO

### Melhorias de Código
- Documentação completa
- Organização modular
- Boas práticas de Django
- Código limpo e comentado

## 📸 Capturas de Tela

*[Aqui você pode adicionar capturas de tela do seu blog]*

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👩‍💻 Autora

**Giovanna** - [GitHub](https://github.com/gionogueira)

## 🙏 Agradecimentos

- [Django Girls](https://djangogirls.org/) pelo excelente tutorial
- Comunidade Django pela documentação e suporte
- Bootstrap pela framework CSS
- Todos que contribuíram para este projeto

---

⭐ **Se este projeto te ajudou, não esqueça de dar uma estrela!** ⭐