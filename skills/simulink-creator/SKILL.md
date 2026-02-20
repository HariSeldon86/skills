---
name: simulink-creator
description: Simulink Creator is a tool that allows users to create and edit Simulink models programmatically using MATLAB code. It provides a set of functions and APIs that enable users to build Simulink models, add blocks, connect them, and configure their properties through code. This skill is useful for automating the creation of Simulink models, generating models from data or specifications, and integrating Simulink with other tools and workflows.
license: MIT License
---

# Simulink Creator Skill

## Overview

This skill enables AI model to generate complete, runnable MATLAB scripts that programmatically create and configure Simulink models. AI model should produce clean, well-commented MATLAB code that follows Simulink best practices and covers the full lifecycle of model creation: opening a new model, adding and configuring blocks, connecting signals, setting simulation parameters, and saving the model. If MATLAB is available, test the model creation.

---

## Core Responsibilities

When a user requests a Simulink model, AI model must:

1. **Understand the model's purpose** — identify inputs, outputs, processing logic, and any domain-specific requirements (control, signal processing, physical modeling, etc.)
2. **Identify required blocks** — determine which Simulink blocks are needed to implement the model based on the user's description (e.g., Step, Sum, PID Controller, Transfer Fcn, Scope), using the relevant `resources/simulink_blocks.md` and `resources/simulink_functions.md` files to confirm names, descriptions, and documentation links for blocks and API functions
3. **Look into documentation** — use `tools/web_crawler.py` to retrieve official documentation with blocks/functions doc links to confirm programmatic syntax, block names, library paths, ports, and `set_param`, if needed
4. **Generate a complete MATLAB script** — not just snippets, but a runnable `.m` file that creates the full model from scratch
5. **Explain the generated code** — briefly describe what each major section does, what blocks are used, and how to run the script
6. **Handle errors proactively** — anticipate common pitfalls (duplicate block names, unconnected ports, missing toolboxes) and write defensive code where appropriate
7. **Verify the model creation** — If MATLAB is available, test the script, using available `MCP` or `tools/run_matlab_command.*`, to ensure it creates the model without errors and simulates successfully, then iterate if any issues arise.


---

## Code Quality Standards

All generated scripts must:

- **Use a `modelName` variable** — never hardcode the model name in every `set_param` call
- **Use string concatenation consistently** — `[modelName '/SubSystem1/SubSystem2/BlockName']` 
- **Guard against existing models** — always call `close_system(modelName, 0)` before `new_system`
- **Comment each section** — use `%%` section headers in MATLAB style
- **Use workspace variables for numeric parameters** — define them at the top of the script for easy modification
- **Ensure clean layout** — combining `set_param` with `'Position'` and auto arrangement with `Simulink.BlockDiagram.arrangeSystem`, so the model isn't a jumbled mess when the user opens it
- **Encapsulate logic in subsystems** — if the model has multiple logical components, use `Subsystem` blocks to group them for readability, even in nested levels
- **Include a success message** — `disp(...)` at the end so the user knows it ran

---

## Error Prevention

AI model should proactively avoid these common mistakes:

| Mistake | Fix |
|---|---|
| Wrong `set_param` key name | **Look up the block's `.md` file** — use the exact `Block Parameter` string from the Programmatic Use section, never guess |
| Wrong library path | **Look up the block's `.md` file** — copy the library path from the Libraries section exactly |
| Wrong port count in `add_line` | **Look up the block's `.md` file** — check the Ports section to know how many in/out ports the block has |
| Duplicate block names | Use unique, descriptive names like `Gain_Plant`, `Gain_Controller` with `MakeNameUnique="on"` option to create a unique name for the new block.|
| Wrong port numbers | Verify port count for blocks like Sum, Mux before connecting |
| String vs number params | Simulink `set_param` always takes strings: `'2.5'` not `2.5` |
| Missing `close_system` | Always add it before `new_system` to prevent "model already exists" errors |
| Connecting wrong direction | Always `Source/outport → Destination/inport` |
| Forgetting feedback branch | Use `add_line` twice from the same output to split signals |

---

## Interaction Guidelines

- If the user's request is ambiguous (e.g., "make a control system"), ask one clarifying question: what is the plant/system being controlled, or what should the input/output be?
- If the user provides a block diagram sketch, description, or transfer function, extract all necessary information from it and generate the full script without further questions.
- If a required block belongs to a toolbox the user may not have (e.g., Control System Toolbox, DSP System Toolbox), add a comment warning at the top of the script.
- Always offer to extend the model (e.g., "I can also add data logging to workspace, or wrap the controller in a subsystem — just ask").

---

## Example Interaction

**User:** Create a simple PID control system for a second-order plant with transfer function 1/(s²+2s+1).

**AI model should:**
1. Identify the required blocks: e.g. `Step`, `Sum`, `PID Controller`, `Transfer Fcn`, `Scope`
2. Read both `resources/simulink_blocks.md` and `resources/simulink_functions.md` to get basic knowledge such name, description and doc hyperlink for library blocks and API functions
3. Look into the doc hyperlinks for each block and function to confirm the syntax, library path, ports, and parameters, using `tools/web_crawler.py` if necessary
4. Produce a complete `.m` script with Step reference, Sum (error), PID Controller, Transfer Function plant, feedback line, and Scope
5. Use correct `set_param` parameter key names sourced directly from the block documentation
6. Define tunable PID gains as variables at the top of the script
7. Set block positions so the layout is readable when opened in Simulink
8. Add a brief explanation of the closed-loop architecture and how to run the simulation
9. If MATLAB is available, test the script, using available `MCP` or `tools/run_matlab_command.*`, to ensure it creates the model without errors and simulates successfully, then iterate if any issues arise

---

## Output Format

Every response should include:

### 1. A complete MATLAB script

The script must follow this general structure:

```matlab
%% =========================================================
%% [Model Name] — Simulink Model Creator Script
%% Description: [short description]
%% Generated for MATLAB/Simulink R20XXa or later
%% =========================================================

%% 1. Setup — close any existing instance and create a new model
modelName = 'MyModel';
close_system(modelName, 0);   % close without saving if already open
new_system(modelName);
open_system(modelName);

%% 2. Add Blocks
% Use add_block('libraryPath/BlockType', 'modelName/BlockName')

%% 3. Set Block Parameters
% Use set_param('modelName/BlockName', 'ParameterName', 'Value')

%% 4. Connect Blocks
% Use add_line('modelName', 'SourceBlock/Port', 'DestBlock/Port')

%% 5. Arrange Layout (optional but recommended)
% Use automatic arrangement: Simulink.BlockDiagram.arrangeSystem(modelName);
% Or use set_param to set 'Position' [left top right bottom]

%% 6. Save the Model
save_system(modelName);
disp(['Model "' modelName '" created and saved successfully.']);

%% 7. Run the Simulation
sim(modelName);
```

### 2. A brief explanation

After the code block, include a short prose explanation covering:
- What the model does
- Key blocks used and why
- How to run the script (open MATLAB, run the `.m` file, then simulate)
- Any required toolboxes beyond core Simulink

---

## Resources and Tools
The matlab script shall be validated, if matlab is available, using either:
1. any installed **MCP** that can execute the script or command.
2. using `run_matlab_command.sh` or `run_matlab_command.bat` tool.

AI model can access useful **resources** from
```
resources/*.md
```

The resources have many hyperlink to official MathWorks documentation.

AI model can retrieve this documentation with **tool**:
```
tools/web_crawler.py
```

### Setup `web_crawler` tool
The tool requires `crawl4ai` python library.

If not already installed, install `crawl4ai` in a virtual environment `venv` and run `crawl4ai-setup`.

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install crawl4ai
crawl4ai-setup
```

For Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
pip install crawl4ai
crawl4ai-setup
```

---

## MATLAB / Simulink API Reference

AI model must use the correct Simulink programmatic API.

### Main Programmatic API functions

| Function | Purpose |
|---|---|
| `new_system('modelName')` | Create a new empty model |
| `open_system('modelName')` | Open a model or subsystem |
| `close_system('modelName', 0)` | Close without saving |
| `save_system('modelName')` | Save the model |
| `load_system('modelName')` | Load without opening the window |
| `add_block('libraryPath/BlockType', 'modelName/BlockName')` | Add a block to the model |
| `set_param('modelName/BlockName', 'ParameterName', 'Value')` | Set a parameter of a block |
| `add_line('modelName', 'SourceBlock/Port', 'DestBlock/Port')` | Add a line between two blocks |
| `sim(modelName)` | Run the simulation |
| `get_param('modelName/BlockName', 'ParameterName')` | Get a parameter of a block |
| `Simulink.SubSystem.deleteContents('modelName/SubSystemBlock')` | Delete all contents of a subsystem |
| `Simulink.BlockDiagram.arrangeSystem('path')` | Arrange the blocks in the model level |
| `Simulink.findBlocksOfType(modelName,'Subsystem')` | Find all blocks of a certain type |

### Function Resource File

**All function basic documentation is stored as individual Markdown files in:**
```
resources/simulink_functions.md
```

Each function:
- is categorised by category/scope
- has the name and hyperlink to official and detailed documentation
- has a brief description

#### When to look up the function's resource file

**Always read the function's `simulink_functions.md` file before using it in generated code** whenever you need to:
- Confirm the name of the function
- Understand the function's description

#### When to research further the function's info

**Extract detailed documentation** whenever you need to clarify:
- **Programmatic Use** — the exact API
- **Examples** — useful examples of how to apply the function 

The official documentation can be retrieved from the hyperlink in the function's `simulink_functions.md` file by using the [web_crawler.py](tools/web_crawler.py)

---

## Simulink Blocks

AI model must use the correct Simulink blocks, with the correct name, library path, ports, parameters.

### Commonly Used Blocks
| Name | Library Paths | Description |
|---|---|---|
| `In1` | simulink/Commonly Used Blocks/In1; simulink/Ports & Subsystems/In1; simulink/Sources/In1 | Provide an input port for a subsystem or model. |
| `Bus Creator` | simulink/Commonly Used Blocks/Bus Creator; simulink/Signal Routing/Bus Creator | This block creates a bus from its inputs. |
| `Bus Selector` | simulink/Commonly Used Blocks/Bus Selector; simulink/Signal Routing/Bus Selector | Select nested buses and signals from the input bus. |
| `Constant` | simulink/Commonly Used Blocks/Constant; simulink/Sources/Constant | Output the constant specified by the 'Constant value' parameter. |
| `Data Type Conversion` | simulink/Commonly Used Blocks/Data Type Conversion; simulink/Signal Attributes/Data Type Conversion | Convert the input to the data type and scaling of the output.  |
| `Delay` | simulink/Commonly Used Blocks/Delay; simulink/Discrete/Delay | Delay input signal by a specified number of samples. |
| `Demux` | simulink/Commonly Used Blocks/Demux; simulink/Signal Routing/Demux | Split vector signals into scalars or smaller vectors. |
| `Discrete-Time Integrator` | simulink/Commonly Used Blocks/Discrete-Time Integrator; simulink/Discrete/Discrete-Time Integrator | Discrete-time integration or accumulation of the input signal. |
| `Gain` | simulink/Commonly Used Blocks/Gain; simulink/Math Operations/Gain | Element-wise gain (y = K.*u) or matrix gain (y = K*u or y = u*K). |
| `Ground` | simulink/Commonly Used Blocks/Ground; simulink/Sources/Ground | Used to "ground" input signals.  (Prevents warnings about unconnected input ports.)  Outputs zero. |
| `Integrator` | simulink/Commonly Used Blocks/Integrator; simulink/Continuous/Integrator | Continuous-time integration of the input signal. |
| `Logical Operator` | simulink/Commonly Used Blocks/Logical Operator; simulink/Logic and Bit Operations/Logical Operator | Logical operators. |
| `Mux` | simulink/Commonly Used Blocks/Mux; simulink/Signal Routing/Mux | Combine scalar or vector signals of the same data type and complexity into a virtual vector. This block does not concatenate the signals. |
| `Product` | simulink/Commonly Used Blocks/Product; simulink/Math Operations/Product | Multiply or divide inputs. |
| `Relational Operator` | simulink/Commonly Used Blocks/Relational Operator; simulink/Logic and Bit Operations/Relational Operator | Applies the selected relational operator to the inputs and outputs the result. The top (or left) input corresponds to the first operand. |
| `Saturation` | simulink/Commonly Used Blocks/Saturation; simulink/Discontinuities/Saturation | Limit input signal to the upper and lower saturation values. |
| `Scope` | simulink/Commonly Used Blocks/Scope; simulink/Sinks/Scope | Displays input signals with respect to simulation time |
| `Subsystem` | simulink/Commonly Used Blocks/Subsystem; simulink/Ports & Subsystems/Subsystem | A subsystem block template containing an inport and outport block. |
| `Sum` | simulink/Commonly Used Blocks/Sum; simulink/Math Operations/Sum | Add or subtract inputs. |
| `Switch` | simulink/Commonly Used Blocks/Switch; simulink/Signal Routing/Switch | Pass through input 1 when input 2 satisfies the selected criterion; otherwise, pass through input 3. |
| `Terminator` | simulink/Commonly Used Blocks/Terminator; simulink/Sinks/Terminator | Used to "terminate" output signals.  (Prevents warnings about unconnected output ports.) |
| `Vector Concatenate` | simulink/Commonly Used Blocks/Vector Concatenate; simulink/Math Operations/Vector Concatenate; simulink/Signal Routing/Vector Concatenate | Concatenate input signals of the same data type to create a contiguous output signal. Select vector or multidimensional array mode. |
| `Out1` | simulink/Commonly Used Blocks/Out1; simulink/Ports & Subsystems/Out1; simulink/Sinks/Out1 | Provide an output port for a subsystem or model. |

### Block Resource File

**All block basic documentation is stored as individual Markdown files in:**
```
resources/simulink_blocks.md
```

Each block:
- is categorised by library category
- has the name and hyperlink to official and detailed documentation
- has a brief description

#### When to look up the block's resource file

**Always read the block's `simulink_blocks.md` file before using it in generated code** whenever you need to:
- Confirm the name of the block
- Understand the block's description

#### When to research further the block's info

**Extract detailed documentation** whenever you need to clarify:
- **Libraries** — the exact library path(s) to use with `add_block`
- **Ports** — input/output port count and data types
- **Parameters** — every configurable parameter with its `set_param` key name, valid values, and default
- **Programmatic Use** — the exact `Block Parameter` string to pass to `set_param`
- **Block Characteristics** — supported data types, direct feedthrough, etc.

The official documentation can be retrieved from the hyperlink in the block's `simulink_blocks.md` file by using the [web_crawler.py](tools/web_crawler.py)


#### Example lookup workflow

For a block named **Abs**:
```
Read: resources/simulink_blocks.md
→ Description: Output absolute value of input
→ Official Documentation: https://uk.mathworks.com/help/simulink/slref/abs.html
→ Use web_crawler.py to get more information about the block
→ Library path:  simulink/Math Operations   (use: 'simulink/Math Operations/Abs')
→ set_param key: ZeroCross        values: 'on' (default) | 'off'
→ set_param key: SaturateOnIntegerOverflow   values: 'off' (default) | 'on'
→ set_param key: SampleTime       values: '-1' (default) | scalar
→ Ports: 1 input (Port_1), 1 output (Port_1)
```

#### File not found

If a block name does not exist in `resources/simulink_blocks.md`, fall back to your general Simulink knowledge and add a code comment flagging that the parameters were not verified against the block reference:
```matlab
% NOTE: Block reference file not found for 'BlockName'.
% Parameters below are based on general Simulink knowledge — verify before use.
```

### Adding Blocks
```matlab
% Syntax: add_block('libraryPath/BlockName', 'modelName/InstanceName')
% Always confirm the library path from the block's .md file before using it
add_block('simulink/Sources/Sine Wave', [modelName '/SineInput']);
add_block('simulink/Math Operations/Gain', [modelName '/Gain1']);
add_block('simulink/Sinks/Scope', [modelName '/Scope']);
```

### Setting Block Parameters
```matlab
% Always use the exact Block Parameter key from the block's .md file
% General syntax:
set_param([modelName '/BlockName'], 'ParameterKey', 'Value');

% The parameter key comes from the "Programmatic Use" section in the block's .md file
% e.g., for Abs: ZeroCross, SaturateOnIntegerOverflow, SampleTime, OutDataTypeStr
set_param([modelName '/AbsVal'], 'ZeroCross', 'on');
set_param([modelName '/AbsVal'], 'SaturateOnIntegerOverflow', 'off');
```

### Connecting Blocks
```matlab
% Syntax: add_line('modelName', 'SrcBlock/OutPort#', 'DstBlock/InPort#')
add_line(modelName, 'SineInput/1', 'Gain1/1');
add_line(modelName, 'Gain1/1', 'Scope/1');

% Named signal lines (optional, for readability)
h = add_line(modelName, 'Gain1/1', 'Scope/1');
set_param(h, 'Name', 'gainedSignal');
```

### Block Positioning
Use auto arrangement for a quick layout.

At top level:
```matlab
Simulink.BlockDiagram.arrangeSystem(modelName);
```

For each nested level:
```matlab
allSubsys = Simulink.findBlocksOfType(modelName,"Subsystem");
for i = 1:numel(allSubsys)
    try
        Simulink.BlockDiagram.arrangeSystem(allSubsys(i));
    catch
    end
end
```

Furthermore, set positions manually to ensure a clean layout when the user opens the model. Positions are defined as `[left, top, right, bottom]` in pixels relative to the model window.
```matlab
% Position format: [left, top, right, bottom] in pixels
set_param([modelName '/SineInput'], 'Position', [50, 100, 150, 130]);
set_param([modelName '/Gain1'],     'Position', [250, 100, 350, 130]);
set_param([modelName '/Scope'],     'Position', [450, 100, 500, 130]);
```

### Simulation Parameters
```matlab
set_param(modelName, 'StopTime',        '10');
set_param(modelName, 'StartTime',       '0');
set_param(modelName, 'Solver',          'ode45');       % or 'FixedStepDiscrete'
set_param(modelName, 'SolverType',      'Variable-step');
set_param(modelName, 'MaxStep',         '0.01');
set_param(modelName, 'FixedStep',       '0.001');       % for fixed-step solvers
set_param(modelName, 'SimulationMode',  'normal');
```

### Subsystems
If the model requires hierarchical organization, use subsystems to group related blocks. Always confirm the library path for Subsystem blocks from the block reference file before adding.

```matlab
% Add a subsystem block
add_block('simulink/Ports & Subsystems/Subsystem', [modelName '/Controller']);

% Clean up the subsystem block, which usually comes with inport/outport blocks connected
Simulink.SubSystem.deleteContents([modelName '/Controller']);

% Add blocks inside the subsystem
add_block('simulink/Ports & Subsystems/In1', [modelName '/Controller/In1']);
add_block('simulink/Ports & Subsystems/Out1', [modelName '/Controller/Out1']);
add_block('simulink/Math Operations/Gain', [modelName '/Controller/InnerGain']);

% Connect inside the subsystem
add_line([modelName '/Controller'], 'In1/1', 'InnerGain/1');
add_line([modelName '/Controller'], 'InnerGain/1', 'Out1/1');
```

---

## Domain-Specific Patterns

### Control System (PID + Plant)
```matlab
% Typical closed-loop pattern
add_block('simulink/Sources/Step',                    [mdl '/Ref']);
add_block('simulink/Math Operations/Sum',             [mdl '/ErrorSum']);
add_block('simulink/Continuous/PID Controller',       [mdl '/PID']);
add_block('simulink/Continuous/Transfer Fcn',         [mdl '/Plant']);
add_block('simulink/Sinks/Scope',                     [mdl '/Scope']);

set_param([mdl '/ErrorSum'], 'Inputs', '+-');   % positive reference, negative feedback

add_line(mdl, 'Ref/1',      'ErrorSum/1');
add_line(mdl, 'ErrorSum/1', 'PID/1');
add_line(mdl, 'PID/1',      'Plant/1');
add_line(mdl, 'Plant/1',    'Scope/1');
add_line(mdl, 'Plant/1',    'ErrorSum/2');   % feedback path
```

### Signal Processing (Filter)
```matlab
% Using a discrete transfer function as a filter
add_block('simulink/Sources/Sine Wave',            [mdl '/Input']);
add_block('simulink/Discrete/Discrete Transfer Fcn', [mdl '/Filter']);
add_block('simulink/Sinks/Scope',                  [mdl '/Output']);

set_param([mdl '/Filter'], 'Numerator', 'num', 'Denominator', 'den');
% (define num/den as workspace variables before running)
```

### Data Logging
```matlab
add_block('simulink/Sinks/To Workspace', [mdl '/Logger']);
set_param([mdl '/Logger'], 'VariableName', 'simOut', 'SaveFormat', 'Array');
```

