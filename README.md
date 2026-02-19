# Skills: Getting Started with GitHub Copilot

Welcome to the GitHub Copilot Skills repository! This repository contains a learning course for GitHub Copilot along with a sample FastAPI application.

## 🎓 What's in This Repository

### 1. GitHub Copilot Learning Course
Progressive exercises to master GitHub Copilot features:
- **Step 1**: Preparing your environment
- **Step 2**: First introduction to Copilot
- **Step 3**: Copilot edits and suggestions
- **Step 4**: Copilot agent mode
- **Step 5**: Copilot on GitHub

### 2. Sample Application
**Mergington High School Activities API** - A FastAPI application for managing student activity signups:
- View extracurricular activities
- Sign up for activities
- Unregister from activities
- See [src/README.md](src/README.md) for details

### 3. Issue Refinement Resources
Tools and templates for creating comprehensive, structured GitHub issues:
- **[Quick Start Guide](.github/ISSUE_REFINEMENT_README.md)**
- **[Complete Guide](.github/REFINE_ISSUE_GUIDE.md)**
- **[Template](.github/ISSUE_REFINEMENT_TEMPLATE.md)**
- **[Example](.github/ISSUE_REFINEMENT_EXAMPLE.md)**

## 🚀 Quick Start

### Running the Application

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   ```bash
   cd src
   python app.py
   ```

3. **Access the API:**
   - API documentation: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc
   - Web interface: http://localhost:8000/

### Running Tests

```bash
pytest
```

## 🎯 Using Issue Refinement

Transform basic issues into comprehensive requirements:

### Option 1: Use the Agent
```
@refine-issue refine https://github.com/owner/repo/issues/NUMBER
```

### Option 2: Use the Template
1. Copy from [.github/ISSUE_REFINEMENT_TEMPLATE.md](.github/ISSUE_REFINEMENT_TEMPLATE.md)
2. Fill in all sections
3. Update your issue

### Option 3: Use the Python Utility
```bash
python refine_issue_utility.py
```

## 📚 Documentation

### Application Documentation
- [Application README](src/README.md) - API details and data model
- [API Endpoints](src/README.md#api-endpoints) - Available endpoints

### Issue Refinement Documentation
- [Overview](.github/ISSUE_REFINEMENT_README.md) - Quick start
- [Complete Guide](.github/REFINE_ISSUE_GUIDE.md) - Detailed instructions
- [Template](.github/ISSUE_REFINEMENT_TEMPLATE.md) - Copy-paste template
- [Example](.github/ISSUE_REFINEMENT_EXAMPLE.md) - See it in action

### GitHub Copilot Agents
- [Refine Issue Agent](.github/agents/refine-issue.agent.md) - Issue refinement
- [Implementation Planner](.github/agents/implementation-planner.agent.md) - Planning
- [README Specialist](.github/agents/readme-specialist.agent.md) - Documentation

## 🛠️ Technology Stack

- **Backend**: FastAPI
- **Testing**: pytest
- **Development**: Python 3.x
- **AI Assistant**: GitHub Copilot

## 📁 Project Structure

```
.
├── .github/              # GitHub configuration and resources
│   ├── agents/          # Custom Copilot agents
│   ├── steps/           # Course exercise steps
│   ├── workflows/       # GitHub Actions
│   └── *.md            # Issue refinement documentation
├── src/                 # Application source code
│   ├── app.py          # FastAPI application
│   ├── static/         # Static web files
│   └── README.md       # Application documentation
├── tests/              # Test suite
│   └── test_api.py    # API tests
├── refine_issue_utility.py  # Issue refinement tool
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎓 Learning Path

1. **Start with basics**: Follow the course exercises in `.github/steps/`
2. **Practice with the app**: Modify the FastAPI application
3. **Refine issues**: Use the issue refinement tools
4. **Explore agents**: Try different Copilot agents

## 🤝 Contributing

Contributions welcome! Here's how:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Submit a pull request

### Issue Creation

When creating issues, consider using the [Issue Refinement Template](.github/ISSUE_REFINEMENT_TEMPLATE.md) for comprehensive requirements.

## 📊 What You'll Learn

### GitHub Copilot Skills
- ✅ Code completion and suggestions
- ✅ Chat-based assistance
- ✅ Edit mode for targeted changes
- ✅ Agent mode for complex tasks
- ✅ Custom agents for specialized workflows

### Issue Management
- ✅ Writing clear acceptance criteria
- ✅ Identifying technical considerations
- ✅ Assessing risks and edge cases
- ✅ Defining non-functional requirements
- ✅ Estimating effort accurately

### Development Best Practices
- ✅ Test-driven development
- ✅ API design
- ✅ Documentation
- ✅ Code review
- ✅ CI/CD workflows

## 🔗 Useful Links

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [pytest Documentation](https://docs.pytest.org/)

## 📄 License

See [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: Use GitHub Issues for bugs and features
- **Questions**: Check the documentation or open a discussion
- **Course Help**: Follow the steps in `.github/steps/`

---

**Last Updated**: 2026-02-19  
**Version**: 1.0  
**Maintained By**: Development Team

Happy coding with GitHub Copilot! 🚀
