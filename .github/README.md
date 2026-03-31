# GitHub Configuration and Resources

This directory contains GitHub-specific configuration and resources for the Mergington High School API project.

## 📁 Directory Structure

### `/agents/` - Custom GitHub Copilot Agents
Custom agent configurations for specialized tasks:
- `refine-issue.agent.md` - Agent for refining GitHub issues with structured details
- `implementation-planner.agent.md` - Agent for planning implementations
- `readme-specialist.agent.md` - Agent for documentation work

### `/steps/` - Exercise Steps
Tutorial and exercise content:
- Step-by-step guides for learning GitHub Copilot
- Progressive exercises from basics to advanced features

### `/workflows/` - GitHub Actions Workflows
Automated workflows for CI/CD and course automation

## 📚 Issue Refinement Resources

### Quick Links
- **[Start Here](ISSUE_REFINEMENT_README.md)** - Overview and quick start
- **[Complete Guide](REFINE_ISSUE_GUIDE.md)** - Detailed usage instructions
- **[Process Flow](ISSUE_REFINEMENT_PROCESS.md)** - Visual diagram and workflow
- **[Template](ISSUE_REFINEMENT_TEMPLATE.md)** - Copy-paste template
- **[Example](ISSUE_REFINEMENT_EXAMPLE.md)** - See it in action

### What is Issue Refinement?

Issue refinement transforms basic GitHub issues into comprehensive, structured requirements with:

✅ Detailed context and background  
✅ Testable acceptance criteria  
✅ Technical implementation guidance  
✅ Edge cases and risk assessment  
✅ Non-functional requirements  
✅ Effort estimation and planning  

### How to Use

**Option 1: Use the Refine Issue Agent**
```
@refine-issue refine https://github.com/owner/repo/issues/NUMBER
```

**Option 2: Use the Template**
1. Open [ISSUE_REFINEMENT_TEMPLATE.md](ISSUE_REFINEMENT_TEMPLATE.md)
2. Copy the template
3. Fill in all sections
4. Update your GitHub issue

**Option 3: Programmatic Refinement**
```bash
python ../refine_issue_utility.py
```

## 🎯 Why Refine Issues?

### Benefits for Teams
- 📝 **Clarity**: Eliminate ambiguity in requirements
- ⏱️ **Efficiency**: Better estimates lead to better planning
- 🎯 **Quality**: Testable criteria ensure completeness
- 🔍 **Risk Management**: Identify issues before they occur

### Benefits for Individuals
- 🧭 **Direction**: Clear path from requirement to implementation
- ✅ **Confidence**: Know exactly what "done" means
- 📚 **Learning**: Understand the full context and implications
- 🤝 **Communication**: Share understanding across the team

## 📖 Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [ISSUE_REFINEMENT_README.md](ISSUE_REFINEMENT_README.md) | Quick start and overview | Everyone |
| [REFINE_ISSUE_GUIDE.md](REFINE_ISSUE_GUIDE.md) | Complete usage guide | All users |
| [ISSUE_REFINEMENT_PROCESS.md](ISSUE_REFINEMENT_PROCESS.md) | Visual process flow | Visual learners |
| [ISSUE_REFINEMENT_TEMPLATE.md](ISSUE_REFINEMENT_TEMPLATE.md) | Copy-paste template | Issue authors |
| [ISSUE_REFINEMENT_EXAMPLE.md](ISSUE_REFINEMENT_EXAMPLE.md) | Real-world example | Learners |

## 🛠️ Tools

- **refine_issue_utility.py** - Python script for programmatic issue refinement
  - Located in project root: `../refine_issue_utility.py`
  - Data classes for all refinement components
  - Example usage included

## 🚀 Getting Started

1. **Read**: Start with [ISSUE_REFINEMENT_README.md](ISSUE_REFINEMENT_README.md)
2. **Learn**: Review the [example](ISSUE_REFINEMENT_EXAMPLE.md)
3. **Practice**: Use the [template](ISSUE_REFINEMENT_TEMPLATE.md) on a real issue
4. **Automate**: Try the [refine-issue agent](agents/refine-issue.agent.md)

## 🤝 Contributing

To improve these resources:
1. Share feedback via GitHub issues
2. Submit examples of well-refined issues
3. Propose template enhancements
4. Contribute domain-specific variations

## 📞 Support

- Check the [Guide](REFINE_ISSUE_GUIDE.md) for detailed help
- Review the [Example](ISSUE_REFINEMENT_EXAMPLE.md) for reference
- Open an issue if you find problems

---

**Maintained By**: Development Team  
**Last Updated**: 2026-02-19  
**Version**: 1.0
