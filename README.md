# Skills for Coding Agents
A collection of [Agent Skills](https://agentskills.io/home) for several scopes in software development, computer science and engineering.

Skills are specialized instruction sets that extend the capabilities of coding agents for specific tasks, automatically activating when needed.

## Available skills

### Simulink Creator

**Name**: [simulink-creator](skills/simulink-creator)

**Description**: Simulink Creator is a tool that allows users to create and edit Simulink models programmatically using MATLAB code. It provides a set of functions and APIs that enable users to build Simulink models, add blocks, connect them, and configure their properties through code. This skill is useful for automating the creation of Simulink models, generating models from data or specifications, and integrating Simulink with other tools and workflows.

**Prompt Example**: 

```
Build a Simulink model that simulates a cruise control system. The vehicle dynamics are modeled as a transfer function 10 / (s^2 + 3s). Use a PID controller with P=2, I=0.5, D=0.1. Include a Step reference at t=1s with amplitude 25 (target speed in m/s), log the output to workspace, and display both the reference and output on the same Scope.
```

**License**: [MIT License](LICENSE)


## Installation & Usage

### Claude Code (CLI)

**Recommended**: Install all agent skills using the plugin marketplace:

```bash
# (Step 1) Add the marketplace to Claude Code
/plugin marketplace add HariSeldon86/skills

# (Step 2) Install all the MATLAB Agent Skills
/plugin install hariseldon86-skills@hariseldon86-skills
```

This installs all the skills in one command. Skills automatically activate when Claude detects relevant tasks.

### Manual installation

Agent Skills are supported by **Claude Code**, **Claude.ai**, **Cursor**, **VS Code**, **GitHub Copilot**, **Gemini CLI**, **Antigravity**, **OpenAI Codex**,  and many more.

Integration and connection may vary by plan and platform. Generally you should:

```bash
# Clone the repository
git clone https://github.com/HariSeldon86/skills.git

# Copy all skills to your skills directory (claude, vscode, antigravity, etc.)
cp -r skills/skills/* YOUR_PROJECT/.claude/skills/
cp -r skills/skills/* YOUR_PROJECT/.github/skills/
cp -r skills/skills/* YOUR_PROJECT/.agent/skills/

# Or copy one specific skill only
cp -r skills/skills/simulink-creator YOUR_PROJECT/.claude/skills/simulink-creator
cp -r skills/skills/simulink-creator YOUR_PROJECT/.github/skills/simulink-creator
cp -r skills/skills/simulink-creator YOUR_PROJECT/.agent/skills/simulink-creator

```

