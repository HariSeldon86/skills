# Skills for Coding Agents
My collection of [Agent Skills](https://agentskills.io/home) for several scopes.

Skills are specialized instruction sets that extend the capabilities of coding agents for specific tasks, automatically activating when needed.

## Available skills

### Simulink Creator

**Name**: `simulink-creator`

**Description**: Simulink Creator is a tool that allows users to create and edit Simulink models programmatically using MATLAB code. It provides a set of functions and APIs that enable users to build Simulink models, add blocks, connect them, and configure their properties through code. This skill is useful for automating the creation of Simulink models, generating models from data or specifications, and integrating Simulink with other tools and workflows.

**Prompt Example**: 

```
Build a Simulink model that simulates a cruise control system. The vehicle dynamics are modeled as a transfer function 10 / (s^2 + 3s). Use a PID controller with P=2, I=0.5, D=0.1. Include a Step reference at t=1s with amplitude 25 (target speed in m/s), log the output to workspace, and display both the reference and output on the same Scope.
```

**License**: MIT License


## Installation & Usage

### Manual installation

```bash
# Clone the repository
git clone https://github.com/matlab/skills.git

# Copy all skills to your skills directory (claude, vscode, antigravity, etc.)
cp -r skills/skills/* YOUR_PROJECT/.claude/skills/
cp -r skills/skills/* YOUR_PROJECT/.github/skills/
cp -r skills/skills/* YOUR_PROJECT/.agent/skills/

# Or copy one specific skill only
cp -r skills/skills/simulink-creator YOUR_PROJECT/.claude/skills/simulink-creator
cp -r skills/skills/simulink-creator YOUR_PROJECT/.github/skills/simulink-creator
cp -r skills/skills/simulink-creator YOUR_PROJECT/.agent/skills/simulink-creator

```

