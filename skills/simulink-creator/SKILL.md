---
name: simulink-creator
description: Generates complete, runnable MATLAB scripts that programmatically create and configure Simulink models.
license: MIT License
---

# Simulink Creator Skill

## Overview

This skill generates complete, runnable MATLAB `.m` scripts that build Simulink models programmatically. Scripts must cover the full lifecycle: creating the model, adding and configuring blocks, connecting signals, arranging layout, and saving. If MATLAB is available, validate the script using `MCP` or `scripts/run_matlab_command.*`.

---

## Workflow

For every Simulink model request:

1. **Understand the model** — identify inputs, outputs, processing logic, and domain (control, signal processing, physical modeling, etc.)
2. **Identify required blocks** — read `references/simulink_blocks.md` to confirm block names, descriptions, and doc links; read `references/simulink_functions.md` for API functions
3. **Retrieve detailed docs** — use `scripts/web_crawler.py` with the doc links from the resource files to confirm library paths, port counts, and exact `set_param` key names
4. **Generate a complete `.m` script** — not snippets; a full runnable file following the structure below
5. **Explain the code** — briefly describe blocks used, closed-loop architecture, and how to run
6. **Validate if MATLAB available** — run via `MCP` or `scripts/run_matlab_command.*`; iterate on errors

---

## Code Quality Standards

- Define `modelName` as a variable at the top; never hardcode it in API calls
- Use `[modelName '/BlockName']` string concatenation throughout
- Call `close_system(modelName, 0)` before `new_system` to prevent "already exists" errors
- Use `%%` section headers (MATLAB style)
- Define numeric parameters as workspace variables at the top for easy tuning
- All `set_param` values must be strings: `'2.5'` not `2.5`
- Use unique, descriptive block names (e.g., `Gain_Plant`, `Gain_Controller`); add `'MakeNameUnique', 'on'` option if needed
- Apply `Simulink.BlockDiagram.arrangeSystem` + manual `Position` for clean layout
- Use `Subsystem` blocks to encapsulate logical components
- End with `disp(...)` success message

---

## Script Template

```matlab
%% =========================================================
%% [Model Name] — Simulink Model Creator Script
%% Description: [short description]
%% Generated for MATLAB/Simulink R20XXa or later
%% =========================================================

%% 1. Setup
modelName = 'MyModel';
close_system(modelName, 0);
new_system(modelName);
open_system(modelName);

%% 2. Parameters
% Define tunable numeric parameters here

%% 3. Add Blocks
% add_block('libraryPath/BlockType', [modelName '/InstanceName'])

%% 4. Set Block Parameters
% set_param([modelName '/BlockName'], 'ParameterKey', 'Value')

%% 5. Connect Blocks
% add_line(modelName, 'SrcBlock/OutPort#', 'DstBlock/InPort#')

%% 6. Arrange Layout
Simulink.BlockDiagram.arrangeSystem(modelName);
% Also set Position [left top right bottom] manually for clarity

%% 7. Save
save_system(modelName);
disp(['Model "' modelName '" created and saved successfully.']);

%% 8. Simulate
sim(modelName);
```

---

## API Reference

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

Always look up `references/simulink_functions.md` to confirm function signatures and retrieve doc links for detailed usage.

---

## Block Reference

Always look up `references/simulink_blocks.md` before using a block to confirm name, description, and the doc link. Use `scripts/web_crawler.py` on that link to get the library path, port count, and exact `set_param` key names.

If a block is not found in the resource file, use general Simulink knowledge and add:
```matlab
% NOTE: Block reference not verified for 'BlockName' — confirm parameters before use.
```

### Commonly Used Blocks

| Name | Library Paths | Description |
|---|---|---|
| `In1` | simulink/Sources/In1 | Provide an input port for a subsystem or model. |
| `Out1` | simulink/Sinks/Out1 | Provide an output port for a subsystem or model. |
| `Constant` | simulink/Sources/Constant | Output the constant specified by the 'Constant value' parameter. |
| `Step` | simulink/Sources/Step | Output a step. |
| `Sine Wave` | simulink/Sources/Sine Wave | Output a sine wave. |
| `Ground` | simulink/Sources/Ground | Used to "ground" input signals.  (Prevents warnings about unconnected input ports.)  Outputs zero. |
| `Terminator` | simulink/Sinks/Terminator | Used to "terminate" output signals.  (Prevents warnings about unconnected output ports.) |
| `Scope` | simulink/Sinks/Scope | Displays input signals with respect to simulation time |
| `To Workspace` | simulink/Sinks/To Workspace | Write input to specified timeseries, array, or structure in a workspace. |
| `Sum` | simulink/Math Operations/Sum | Add or subtract inputs. |
| `Gain` | simulink/Math Operations/Gain | Element-wise gain (y = K.*u) or matrix gain (y = K*u or y = u*K). |
| `Product` | simulink/Math Operations/Product | Multiply or divide inputs. |
| `Abs` | simulink/Math Operations/Abs | Output the absolute value of the input signal. |
| `Mux` | simulink/Signal Routing/Mux | Combine scalar or vector signals of the same data type and complexity into a virtual vector. This block does not concatenate the signals. |
| `Demux` | simulink/Signal Routing/Demux | Split vector signals into scalars or smaller vectors. |
| `Bus Creator` | simulink/Signal Routing/Bus Creator | This block creates a bus from its inputs. |
| `Bus Selector` | simulink/Signal Routing/Bus Selector | Select nested buses and signals from the input bus. |
| `Vector Concatenate` | simulink/Math Operations/Vector Concatenate; simulink/Signal Routing/Vector Concatenate | Concatenate input signals of the same data type to create a contiguous output signal. Select vector or multidimensional array mode. |
| `Switch` | simulink/Signal Routing/Switch | Pass through input 1 when input 2 satisfies the selected criterion; otherwise, pass through input 3. |
| `Subsystem` | simulink/Ports & Subsystems/Subsystem | A subsystem block template containing an inport and outport block. |
| `Integrator` | simulink/Continuous/Integrator | Continuous-time integration of the input signal. |
| `Transfer Fcn` | simulink/Continuous/Transfer Fcn | The numerator coefficient can be a vector or matrix expression. The denominator coefficient must be a vector. The output width equals the number of rows in the numerator coefficient. You should specify the coefficients in descending order of powers of s. |
| `PID Controller` | simulink/Continuous/PID Controller | This block implements continuous- and discrete-time PID control algorithms and includes advanced features such as anti-windup, external reset, and signal tracking. |
| `Unit Delay` | simulink/Discrete/Unit Delay | Sample and hold with one sample period delay. |
| `Memory` | simulink/Discrete/Memory | Apply a one integration step delay. The output is the previous input value. |
| `Delay` | simulink/Discrete/Delay | Delay input signal by a specified number of samples. |
| `Discrete-Time Integrator` | simulink/Discrete/Discrete-Time Integrator | Discrete-time integration or accumulation of the input signal. |
| `Discrete Transfer Fcn` | simulink/Discrete/Discrete Transfer Fcn | Implement a z-transform transfer function. Specify the numerator and denominator coefficients in descending powers of z. |
| `Saturation` | simulink/Discontinuities/Saturation | Limit input signal to the upper and lower saturation values. |
| `Logical Operator` | simulink/Logic and Bit Operations/Logical Operator | Logical operators. |
| `Relational Operator` | simulink/Logic and Bit Operations/Relational Operator | Applies the selected relational operator to the inputs and outputs the result. The top (or left) input corresponds to the first operand. |
| `Data Type Conversion` | simulink/Signal Attributes/Data Type Conversion | Convert the input to the data type and scaling of the output.  |

---

## Code Patterns

### Adding and Configuring Blocks
```matlab
add_block('simulink/Sources/Sine Wave', [modelName '/SineInput']);
add_block('simulink/Math Operations/Gain', [modelName '/Gain1']);
add_block('simulink/Sinks/Scope', [modelName '/Scope']);

% Use exact key from block doc's "Programmatic Use" section
set_param([modelName '/Gain1'], 'Gain', '5');
set_param([modelName '/SineInput'], 'Frequency', '2*pi');
```

### Connecting Blocks
```matlab
% add_line(model, 'Source/OutPort#', 'Destination/InPort#')
add_line(modelName, 'SineInput/1', 'Gain1/1');
add_line(modelName, 'Gain1/1', 'Scope/1');

% Named signal (optional)
h = add_line(modelName, 'Gain1/1', 'Scope/1');
set_param(h, 'Name', 'gainedSignal');
```

### Layout
```matlab
% Auto-arrange top level
Simulink.BlockDiagram.arrangeSystem(modelName);

% Auto-arrange all nested subsystems
allSubsys = Simulink.findBlocksOfType(modelName, 'Subsystem');
for i = 1:numel(allSubsys)
    try; Simulink.BlockDiagram.arrangeSystem(allSubsys(i)); catch; end
end

% Manual positions [left, top, right, bottom]
set_param([modelName '/SineInput'], 'Position', [50,  100, 150, 130]);
set_param([modelName '/Gain1'],     'Position', [250, 100, 350, 130]);
set_param([modelName '/Scope'],     'Position', [450, 100, 500, 130]);
```

### Simulation Parameters
```matlab
set_param(modelName, 'StopTime',   '10');
set_param(modelName, 'Solver',     'ode45');
set_param(modelName, 'SolverType', 'Variable-step');
set_param(modelName, 'MaxStep',    '0.01');
```

### Subsystems
```matlab
add_block('simulink/Ports & Subsystems/Subsystem', [modelName '/Controller']);
Simulink.SubSystem.deleteContents([modelName '/Controller']);

add_block('simulink/Ports & Subsystems/In1',  [modelName '/Controller/In1']);
add_block('simulink/Math Operations/Gain',    [modelName '/Controller/InnerGain']);
add_block('simulink/Ports & Subsystems/Out1', [modelName '/Controller/Out1']);

add_line([modelName '/Controller'], 'In1/1',       'InnerGain/1');
add_line([modelName '/Controller'], 'InnerGain/1', 'Out1/1');
```

---

## Domain Patterns

### Closed-Loop Control (PID + Plant)
```matlab
add_block('simulink/Sources/Step',              [mdl '/Ref']);
add_block('simulink/Math Operations/Sum',        [mdl '/ErrorSum']);
add_block('simulink/Continuous/PID Controller',  [mdl '/PID']);
add_block('simulink/Continuous/Transfer Fcn',    [mdl '/Plant']);
add_block('simulink/Sinks/Scope',                [mdl '/Scope']);

set_param([mdl '/ErrorSum'], 'Inputs', '+-');

add_line(mdl, 'Ref/1',      'ErrorSum/1');
add_line(mdl, 'ErrorSum/1', 'PID/1');
add_line(mdl, 'PID/1',      'Plant/1');
add_line(mdl, 'Plant/1',    'Scope/1');
add_line(mdl, 'Plant/1',    'ErrorSum/2');  % feedback
```

### Discrete Filter
```matlab
add_block('simulink/Sources/Sine Wave',            [mdl '/Input']);
add_block('simulink/Discrete/Discrete Transfer Fcn', [mdl '/Filter']);
add_block('simulink/Sinks/Scope',                  [mdl '/Output']);

% num/den defined as workspace variables before running
set_param([mdl '/Filter'], 'Numerator', 'num', 'Denominator', 'den');
add_line(mdl, 'Input/1', 'Filter/1');
add_line(mdl, 'Filter/1', 'Output/1');
```

### Data Logging
```matlab
add_block('simulink/Sinks/To Workspace', [mdl '/Logger']);
set_param([mdl '/Logger'], 'VariableName', 'simOut', 'SaveFormat', 'Array');
```

---

## Error Prevention

| Mistake | Fix |
|---|---|
| Wrong `set_param` key | Look up the exact `Block Parameter` string from the block's official doc |
| Wrong library path | Look up the Libraries section in the block's official doc |
| Wrong port count in `add_line` | Check the Ports section in the block's official doc |
| Duplicate block names | Use descriptive names; add `'MakeNameUnique','on'` |
| String vs. number params | `set_param` always takes strings: `'2.5'` not `2.5` |
| "Model already exists" error | Always call `close_system(modelName, 0)` before `new_system` |
| Wrong connection direction | Always `Source/outport → Destination/inport` |
| Split signals | Call `add_line` twice from the same output port |

---

## Scripts & References

### References
```
references/simulink_blocks.md    — block names, descriptions, doc links
references/simulink_functions.md — API function names, descriptions, doc links
```

### Scripts

#### Web Crawler (for doc retrieval)
```
scripts/web_crawler.py
```

**Setup (run once):**
```bash
# Linux/Mac
python3 -m venv venv && source venv/bin/activate
pip install crawl4ai && crawl4ai-setup

# Windows
python -m venv venv && venv\Scripts\activate
pip install crawl4ai && crawl4ai-setup
```

**Usage:**
```bash
python scripts/web_crawler.py "https://uk.mathworks.com/help/simulink/slref/abs.html"
```

#### Run Matlab Command (for validation)
Run the generated script using any available method:
1. `MCP` that can execute MATLAB commands
2. `scripts/run_matlab_command.sh` (Linux/Mac) or `scripts/run_matlab_command.bat` (Windows)

---

## Interaction Guidelines

- If the request is ambiguous, ask **one** clarifying question (e.g., what is the plant / what are the I/O signals?)
- If the user provides a diagram, transfer function, or description, extract all info and generate without further questions
- Warn about optional toolbox requirements at the top of the script (e.g., Control System Toolbox, DSP System Toolbox)
- After delivering the model, offer one concrete extension (e.g., "I can add data logging to workspace or wrap the controller in a subsystem — just ask")