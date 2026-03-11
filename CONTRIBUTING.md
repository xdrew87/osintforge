# Contributing to OSINTForge

Thank you for your interest in contributing to OSINTForge! We welcome contributions from developers, researchers, and security professionals.

## Ways to Contribute

1. **Report Bugs** - Found an issue? Let us know!
2. **Suggest Features** - Have an idea? We'd love to hear it
3. **Improve Documentation** - Help clarify or improve docs
4. **Add Modules** - Create new OSINT reconnaissance modules
5. **Fix Issues** - Submit pull requests for open issues
6. **Improve Code Quality** - Refactor, optimize, or improve existing code

## Code of Conduct

- Be respectful and professional
- No harassment, discrimination, or hate speech
- Use constructive feedback
- Report violations to maintainers

## Getting Started

### 1. Fork the Repository

```bash
# Click "Fork" on GitHub
git clone https://github.com/xdrew87/osintforge.git
cd osintforge
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install development tools (optional)
pip install black flake8 pytest
```

### 3. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

## Development Guidelines

### Code Style

- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions
- Keep functions small and focused

### Module Development

When creating new OSINT modules:

```python
# modules/new_module.py
from core.banner import module_banner, output_banner, console
from core.history import add_to_history
from core.settings import get_theme
from rich.table import Table
from rich.panel import Panel

def run_new_module():
    """Description of what this module does."""
    # Display banner
    module_banner("Module Title")
    
    # Get user input
    target = input("Enter target > ").strip()
    
    if not target:
        console.print("[red]❌ Error: Target cannot be empty[/red]")
        return
    
    # Show processing message
    console.print("[cyan]🔍 Processing...[/cyan]")
    
    try:
        # Perform analysis
        results = analyze_target(target)
        
        # Display results
        output_banner("Results")
        
        table = Table(
            title="[bold cyan]Analysis Results[/bold cyan]",
            border_style="cyan",
            show_header=True,
            header_style="bold green",
            padding=(0, 1),
            pad_edge=True
        )
        
        table.add_column("Field", style="bold yellow")
        table.add_column("Value", style="green")
        
        for key, value in results.items():
            table.add_row(key, str(value))
        
        console.print(table)
        
        # Add to history
        add_to_history("module_name", target)
        
    except Exception as e:
        console.print(f"\n[bold red]❌ Error:[/bold red] {str(e)}\n")
```

### Adding to Menu

1. Update `core/menu.py`:
```python
# In display_main_menu()
table.add_row("XX", "Module Name", "[dim]Category[/dim]")
```

2. Update `main.py`:
```python
from modules.new_module import run_new_module

# In menu() function
elif choice == "XX":
    run_new_module()
```

### Testing Your Module

- Test with valid inputs
- Test with empty inputs
- Test with invalid inputs
- Verify error handling
- Check output formatting

## Submission Process

### 1. Commit Your Changes

```bash
git add .
git commit -m "Add: Description of changes"
```

Use conventional commit messages:
- `Add:` for new features
- `Fix:` for bug fixes
- `Improve:` for improvements
- `Refactor:` for code refactoring
- `Docs:` for documentation

### 2. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request

- Go to https://github.com/xdrew87/osintforge
- Click "Pull requests" → "New pull request"
- Select your branch
- Fill in PR template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] New module
- [ ] Documentation update
- [ ] Code improvement

## Testing
Describe how you tested these changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Testing performed
```

## Bug Reports

When reporting bugs, include:

```markdown
## Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. etc.

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: Windows/Linux/Mac
- Python version: 3.X
- OSINTForge version: X.X.X

## Error Message
```
Paste full error traceback
```

## Additional Context
Any other relevant info
```

## Feature Requests

When suggesting features, include:

```markdown
## Feature Description
Clear description of the feature

## Use Case
Why is this feature needed?

## Example Usage
How would users interact with this feature?

## Possible Implementation
Optional: How might this be implemented?
```

## Review Process

1. **Code Review** - Maintainers review for quality, style, and functionality
2. **Testing** - Changes are tested
3. **Feedback** - Comments may be requested
4. **Approval** - PR is approved and merged
5. **Release** - Changes included in next release

## Coding Standards

### Required
- No syntax errors
- Follows PEP 8
- Docstrings on functions
- Error handling

### Recommended
- Type hints
- Unit tests
- Meaningful variable names
- Comments for complex logic

### Performance
- No infinite loops
- Reasonable timeout handling
- Efficient algorithms
- Resource cleanup

## Documentation

Any new features must include:

1. **In-code documentation** - Docstrings and comments
2. **README updates** - Add to feature list
3. **Module documentation** - Module description and examples
4. **Setup guide** - Any new dependencies or setup

## Licensing

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

- Check existing issues for answers
- Review documentation
- Open a new issue with your question

## Recognition

Contributors are recognized in:
- Commit history
- GitHub contributors graph
- Release notes for major contributions

---

**Thank you for contributing to OSINTForge!** 🙌

Together we're building better OSINT tools for the security community.
