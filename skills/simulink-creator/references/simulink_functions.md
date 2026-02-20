# Simulink — Functions
- [Simulink — Functions](#simulink--functions)
  - [Simulink Environment Fundamentals](#simulink-environment-fundamentals)
    - [Programmatic Model Editing](#programmatic-model-editing)
      - [Get Handles and Paths](#get-handles-and-paths)
      - [Search](#search)
        - [Find Model Elements](#find-model-elements)
        - [Find Models](#find-models)
        - [Get Model Metadata](#get-model-metadata)
      - [Create Models](#create-models)
        - [Start Simulink](#start-simulink)
        - [Create, Load, Open, Save, and Close Models](#create-load-open-save-and-close-models)
        - [Add, Replace, and Delete Blocks](#add-replace-and-delete-blocks)
        - [Connect Blocks](#connect-blocks)
        - [Edit Parameters](#edit-parameters)
      - [Format Models](#format-models)
      - [Check Models](#check-models)
      - [Share Models](#share-models)
      - [Other](#other)
    - [Simulink Environment Customization](#simulink-environment-customization)
      - [Simulink Favorite Commands](#simulink-favorite-commands)
      - [Simulink Toolstrip](#simulink-toolstrip)
      - [Quick Insert Menu](#quick-insert-menu)
      - [Library Browser](#library-browser)
      - [Simulink Editor](#simulink-editor)
      - [Other](#other-1)
    - [Block Libraries](#block-libraries)
      - [Model-Wide Utilities](#model-wide-utilities)
  - [Modeling](#modeling)
    - [Design Model Architecture](#design-model-architecture)
      - [Subsystems](#subsystems)
      - [Libraries and Blocksets](#libraries-and-blocksets)
      - [Model References](#model-references)
      - [Variant Systems](#variant-systems)
      - [Data Stores](#data-stores)
      - [Composite Interfaces](#composite-interfaces)
    - [Manage Design Data](#manage-design-data)
      - [Manage Data Sources](#manage-data-sources)
      - [Manage Data Dictionary](#manage-data-dictionary)
      - [Manage External File Adapters](#manage-external-file-adapters)
      - [Manage Variables](#manage-variables)
      - [Data Sources](#data-sources)
      - [Model Workspace](#model-workspace)
      - [Data Dictionary](#data-dictionary)
      - [External File Adapters](#external-file-adapters)
      - [Objects and Variables](#objects-and-variables)
    - [Design Model Behavior](#design-model-behavior)
      - [Conditionally Executed Subsystems and Models](#conditionally-executed-subsystems-and-models)
      - [Schedule Model Components](#schedule-model-components)
      - [Nonlinearity](#nonlinearity)
      - [Multicore Processor Targets](#multicore-processor-targets)
    - [Configure Signals, States, and Parameters](#configure-signals-states-and-parameters)
      - [Blocks](#blocks)
      - [Signals](#signals)
      - [Units in Simulink](#units-in-simulink)
      - [Sample Time](#sample-time)
      - [Data Types](#data-types)
      - [Model, Block, and Port Callbacks](#model-block-and-port-callbacks)
      - [Model Configuration Sets](#model-configuration-sets)
    - [Analyze and Remodel Design](#analyze-and-remodel-design)
      - [Run Model Advisor Checks](#run-model-advisor-checks)
      - [Configure and View Diagnostics](#configure-and-view-diagnostics)
      - [Transform Models](#transform-models)
    - [Test Model Components](#test-model-components)
  - [Simulation](#simulation)
    - [Prepare Model Inputs and Outputs](#prepare-model-inputs-and-outputs)
      - [Create Signal Data for Simulation](#create-signal-data-for-simulation)
      - [Load Signal Data for Simulation](#load-signal-data-for-simulation)
      - [Save Run-Time Data from Simulation](#save-run-time-data-from-simulation)
    - [Configure Simulation Conditions](#configure-simulation-conditions)
    - [Run Simulations](#run-simulations)
      - [Run Individual Simulations](#run-individual-simulations)
      - [Run Multiple Simulations](#run-multiple-simulations)
    - [View and Analyze Simulation Results](#view-and-analyze-simulation-results)
      - [Control Simulations with Interactive Dashboards](#control-simulations-with-interactive-dashboards)
      - [View Data During Simulation](#view-data-during-simulation)
      - [Create Apps to Control Simulations](#create-apps-to-control-simulations)
      - [Analyze Simulation Results](#analyze-simulation-results)
      - [Save Simulation and Analysis Results](#save-simulation-and-analysis-results)
    - [Test and Debug Simulations](#test-and-debug-simulations)
      - [Debug Simulations Programmatically](#debug-simulations-programmatically)
      - [Diagnostics](#diagnostics)
    - [Optimize Performance](#optimize-performance)
      - [Acceleration](#acceleration)
      - [Manual Performance Optimization](#manual-performance-optimization)
  - [Project Management](#project-management)
    - [Using MATLAB Projects in Simulink](#using-matlab-projects-in-simulink)
  - [Block and Blockset Authoring](#block-and-blockset-authoring)
    - [Author Block Algorithms](#author-block-algorithms)
      - [Author Blocks Using MATLAB](#author-blocks-using-matlab)
      - [Author Blocks Using C/C++](#author-blocks-using-cc)
    - [Author Block Masks](#author-block-masks)
      - [Mask Parameters and Constraints](#mask-parameters-and-constraints)
      - [Dialog Control Elements](#dialog-control-elements)
  - [Simulation Integration](#simulation-integration)
    - [Create Large-Scale Model Components](#create-large-scale-model-components)
      - [Integrate Components from External Tools](#integrate-components-from-external-tools)
      - [Integrate External Code into Simulink](#integrate-external-code-into-simulink)
  - [References](#references)

## Simulink Environment Fundamentals
### Programmatic Model Editing
#### Get Handles and Paths
Name|Description
---|---
[bdroot](https://uk.mathworks.com/help/simulink/slref/bdroot.html) | Top-level model of current system  
[gcb](https://uk.mathworks.com/help/simulink/slref/gcb.html) | Get path name of current block  
[gcbh](https://uk.mathworks.com/help/simulink/slref/gcbh.html) | Get handle of current block  
[gcbp](https://uk.mathworks.com/help/simulink/slref/gcbp.html) | Get `Simulink.BlockPath` object for current block  
[gcs](https://uk.mathworks.com/help/simulink/slref/gcs.html) | Get path name of current system  
[get_param](https://uk.mathworks.com/help/simulink/slref/get_param.html) | Get parameter names and values  
[getCallbackAnnotation](https://uk.mathworks.com/help/simulink/slref/getcallbackannotation.html) | Get annotation executing callback  
[getCurrentAnnotation](https://uk.mathworks.com/help/simulink/slref/getcurrentannotation.html) | Get current annotation object  
[getfullname](https://uk.mathworks.com/help/simulink/slref/getfullname.html) | Get path that identifies block or line  
[getSimulinkBlockHandle](https://uk.mathworks.com/help/simulink/slref/getsimulinkblockhandle.html) | Get block handle from block path  
#### Search
##### Find Model Elements
Name|Description
---|---
[find_system](https://uk.mathworks.com/help/simulink/slref/find_system.html) | Find models, blocks, lines, ports, and annotations  
[hilite_system](https://uk.mathworks.com/help/simulink/slref/hilite_system.html) | Highlight block, signal line, port, or annotation  
[Simulink.findBlocks](https://uk.mathworks.com/help/simulink/slref/simulink.findblocks.html) | Find blocks in Simulink models  
[Simulink.findBlocksOfType](https://uk.mathworks.com/help/simulink/slref/simulink.findblocksoftype.html) | Find specified type of block in Simulink models  
[Simulink.FindOptions](https://uk.mathworks.com/help/simulink/slref/simulink.findoptions.html) | Specify options for finding blocks in models and subsystems  
##### Find Models
Name|Description
---|---
[find_system](https://uk.mathworks.com/help/simulink/slref/find_system.html) | Find models, blocks, lines, ports, and annotations  
[modelfinder](https://uk.mathworks.com/help/simulink/slref/modelfinder.html) | Search and open examples, models, and projects _(Since R2022a)_  
[modelfinder.createDatabase](https://uk.mathworks.com/help/simulink/slref/modelfinder.createdatabase.html) | Create new database to index models _(Since R2023b)_  
[modelfinder.deleteDatabase](https://uk.mathworks.com/help/simulink/slref/modelfinder.deletedatabase.html) | Remove database from Model Finder _(Since R2023b)_  
[modelfinder.importDatabase](https://uk.mathworks.com/help/simulink/slref/modelfinder.importdatabase.html) | Import database to Model Finder _(Since R2023b)_  
[modelfinder.registerFolder](https://uk.mathworks.com/help/simulink/slref/modelfinder.registerfolder.html) | Index models in Model Finder _(Since R2022a)_  
[modelfinder.searchFilter](https://uk.mathworks.com/help/simulink/slref/modelfinder.internal.modelfinderfilter.modelfinder.searchfilter.html) | Create Model Finder search filter _(Since R2025a)_  
[modelfinder.setDefaultDatabase](https://uk.mathworks.com/help/simulink/slref/modelfinder.setdefaultdatabase.html) | Set default database to index models _(Since R2023b)_  
[modelfinder.setSearchDatabase](https://uk.mathworks.com/help/simulink/slref/modelfinder.setsearchdatabase.html) | Set search scope to find models _(Since R2023b)_  
[modelfinder.unregisterFolder](https://uk.mathworks.com/help/simulink/slref/modelfinder.unregisterfolder.html) | Remove models from Model Finder _(Since R2022a)_  
[Simulink.allBlockDiagrams](https://uk.mathworks.com/help/simulink/slref/simulink.allblockdiagrams.html) | Find loaded Simulink models and libraries  
##### Get Model Metadata
Name|Description
---|---
[Simulink.MDLInfo](https://uk.mathworks.com/help/simulink/slref/simulink.mdlinfo.html) | Extract SLX, SLXP, or MDL file information without loading file  
[Simulink.MDLInfo.getDescription](https://uk.mathworks.com/help/simulink/slref/simulink.mdlinfo.getdescription.html) | Extract SLX, SLXP, or MDL file description without loading file  
[Simulink.MDLInfo.getMetadata](https://uk.mathworks.com/help/simulink/slref/simulink.mdlinfo.getmetadata.html) | Extract SLX, SLXP, or MDL file metadata without loading file  
#### Create Models
##### Start Simulink
Name|Description
---|---
[isSimulinkStarted](https://uk.mathworks.com/help/simulink/slref/issimulinkstarted.html) | Check whether Simulink is started  
[simulink](https://uk.mathworks.com/help/simulink/slref/simulink.html) | Open Simulink Start Page  
[slLibraryBrowser](https://uk.mathworks.com/help/simulink/slref/sllibrarybrowser.html) | Open, load, and close Simulink Library Browser, create and get handle of Library Browser object  
[start_simulink](https://uk.mathworks.com/help/simulink/slref/start_simulink.html) | Start Simulink without opening any windows  
##### Create, Load, Open, Save, and Close Models
Name|Description
---|---
[bdclose](https://uk.mathworks.com/help/simulink/slref/bdclose.html) | Close any or all Simulink model windows unconditionally  
[close_system](https://uk.mathworks.com/help/simulink/slref/close_system.html) | Close Simulink model window or block dialog box  
[load_system](https://uk.mathworks.com/help/simulink/slref/load_system.html) | Load Simulink model into memory  
[new_system](https://uk.mathworks.com/help/simulink/slref/new_system.html) | Create Simulink model or library in memory  
[open_system](https://uk.mathworks.com/help/simulink/slref/open_system.html) | Open model, library, subsystem, or block dialog box  
[save_system](https://uk.mathworks.com/help/simulink/slref/save_system.html) | Save Simulink model  
##### Add, Replace, and Delete Blocks
Name|Description
---|---
[add_block](https://uk.mathworks.com/help/simulink/slref/add_block.html) | Add block to model  
[addterms](https://uk.mathworks.com/help/simulink/slref/addterms.html) | Add terminators to unconnected ports in model  
[delete_block](https://uk.mathworks.com/help/simulink/slref/delete_block.html) | Delete blocks from Simulink system  
[replace_block](https://uk.mathworks.com/help/simulink/slref/replace_block.html) | Replace blocks in Simulink model  
[Simulink.BlockDiagram.deleteContents](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.deletecontents.html) | Delete graphical contents of model  
[Simulink.SubSystem.deleteContents](https://uk.mathworks.com/help/simulink/slref/simulink.subsystem.deletecontents.html) | Delete contents of subsystem  
##### Connect Blocks
Name|Description
---|---
[add_line](https://uk.mathworks.com/help/simulink/slref/add_line.html) | Add line to Simulink model  
[delete_line](https://uk.mathworks.com/help/simulink/slref/delete_line.html) | Delete line from Simulink model  
[Simulink.connectBlocks](https://uk.mathworks.com/help/simulink/slref/simulink.connectblocks.html) | Connect blocks with signal lines _(Since R2024b)_  
##### Edit Parameters
Name|Description
---|---
[add_param](https://uk.mathworks.com/help/simulink/slref/add_param.html) | Add parameter to Simulink model  
[delete_param](https://uk.mathworks.com/help/simulink/slref/delete_param.html) | Delete model parameter added with `add_param` function  
[docblock](https://uk.mathworks.com/help/simulink/slref/docblock_cmd.html) | Get or set editor invoked by Simulink DocBlock block  
[get_param](https://uk.mathworks.com/help/simulink/slref/get_param.html) | Get parameter names and values  
[set_param](https://uk.mathworks.com/help/simulink/slref/set_param.html) | Set Simulink parameter value  
#### Format Models
Name|Description
---|---
[bdIsSubsystem](https://uk.mathworks.com/help/simulink/slref/bdissubsystem.html) | Determine whether model is subsystem  
[Simulink.BlockDiagram.arrangeSystem](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.arrangesystem.html) | Improve layout of block diagram  
[Simulink.BlockDiagram.createSubsystem](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.createsubsystem.html) | Create subsystem containing specified set of blocks  
[Simulink.BlockDiagram.expandSubsystem](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.expandsubsystem.html) | Replace subsystem with subsystem contents  
[Simulink.BlockDiagram.resizeBlocksToFitContent](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.resizeblockstofitcontent.html) | Adjust block size to fit displayed value _(Since R2024b)_  
[Simulink.BlockDiagram.routeLine](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.routeline.html) | Route existing lines of model  
[Simulink.SubSystem.copyContentsToBlockDiagram](https://uk.mathworks.com/help/simulink/slref/simulink.subsystem.copycontentstoblockdiagram.html) | Copy graphical contents from subsystem to another model  
[Simulink.SubSystem.deleteContents](https://uk.mathworks.com/help/simulink/slref/simulink.subsystem.deletecontents.html) | Delete contents of subsystem  
#### Check Models
Name|Description
---|---
[bdIsDirty](https://uk.mathworks.com/help/simulink/slref/bdisdirty.html) | Determine whether model, subsystem, or library has unsaved changes  
[bdIsLibrary](https://uk.mathworks.com/help/simulink/slref/bdislibrary.html) | Determine whether model is library  
[bdIsLoaded](https://uk.mathworks.com/help/simulink/slref/bdisloaded.html) | Determine whether model, subsystem, or library is loaded  
[bdIsSubsystem](https://uk.mathworks.com/help/simulink/slref/bdissubsystem.html) | Determine whether model is subsystem  
[edittime.getDisplayIssues](https://uk.mathworks.com/help/simulink/slref/edittime.getdisplayissues.html) | Check whether model design warnings and errors are on  
[edittime.setDisplayIssues](https://uk.mathworks.com/help/simulink/slref/edittime.setdisplayissues.html) | Detect model design errors and warnings  
[isSimulinkStarted](https://uk.mathworks.com/help/simulink/slref/issimulinkstarted.html) | Check whether Simulink is started  
[slIsFileChangedOnDisk](https://uk.mathworks.com/help/simulink/slref/slisfilechangedondisk.html) | Determine whether model has changed since it was loaded  
#### Share Models
Name|Description
---|---
[frameedit](https://uk.mathworks.com/help/simulink/slref/frameedit.html) | Open PrintFrame Editor to edit print frames for Simulink and Stateflow block diagrams  
[orient](https://uk.mathworks.com/help/matlab/ref/orient.html) | Paper orientation for printing or saving  
[print](https://uk.mathworks.com/help/matlab/ref/print.html) | Print figure or save to specific file format  
[Simulink.createFromTemplate](https://uk.mathworks.com/help/simulink/slref/simulink.createfromtemplate.html) | Create model or project from template  
[Simulink.defaultModelTemplate](https://uk.mathworks.com/help/simulink/slref/simulink.defaultmodeltemplate.html) | Set or get default model template  
[Simulink.exportToTemplate](https://uk.mathworks.com/help/simulink/slref/simulink.exporttotemplate.html) | Create template from model or project  
[Simulink.exportToVersion](https://uk.mathworks.com/help/simulink/slref/simulink.exporttoversion.html) | Export model, library, or project for use in previous version of Simulink  
[Simulink.findTemplates](https://uk.mathworks.com/help/simulink/slref/simulink.findtemplates.html) | Find model or project templates with specified properties  
[Simulink.ModelReference.protect](https://uk.mathworks.com/help/ecoder/ref/simulink.modelreference.protect.html) | Obscure referenced model contents to hide intellectual property  
[slCharacterEncoding](https://uk.mathworks.com/help/simulink/slref/slcharacterencoding.html) | Specify encoding to use in code generated from Simulink models  
#### Other
Name|Description
---|---
[ModelFinderFilter](https://uk.mathworks.com/help/simulink/slref/modelfinder.internal.modelfinderfilter.html) | Model Finder search filter _(Since R2025a)_  
[Simulink.Annotation](https://uk.mathworks.com/help/simulink/slref/simulink.annotation.html) | Create and specify properties of text, image, and area annotations  
### Simulink Environment Customization
#### Simulink Favorite Commands
Name|Description
---|---
[slExportFavoriteCommands](https://uk.mathworks.com/help/simulink/slref/slexportfavoritecommands.html) | Export favorite commands from Simulink quick access toolbar _(Since R2021b)_  
[slImportFavoriteCommands](https://uk.mathworks.com/help/simulink/slref/slimportfavoritecommands.html) | Import favorite commands to Simulink quick access toolbar _(Since R2021b)_  
[slResetFavoriteCommands](https://uk.mathworks.com/help/simulink/slref/slresetfavoritecommands.html) | Reset Simulink Favorite Commands gallery _(Since R2021b)_  
#### Simulink Toolstrip
Name|Description
---|---
[sl_refresh_customizations](https://uk.mathworks.com/help/simulink/slref/sl_refresh_customizations.html) | Refresh customizations in the current MATLAB session _(Since R2022a)_  
[slConvertCustomMenus](https://uk.mathworks.com/help/simulink/slref/slconvertcustommenus.html) | Convert custom toolbar menu into toolstrip tab _(Since R2022a)_  
[slCreateToolstripComponent](https://uk.mathworks.com/help/simulink/slref/slcreatetoolstripcomponent.html) | Create custom Simulink Toolstrip component _(Since R2021b)_  
[slCreateToolstripTab](https://uk.mathworks.com/help/simulink/slref/slcreatetoolstriptab.html) | Create custom tab for Simulink Toolstrip _(Since R2021b)_  
[slDestroyToolstripComponent](https://uk.mathworks.com/help/simulink/slref/sldestroytoolstripcomponent.html) | Destroy Simulink Toolstrip component _(Since R2021b)_  
[slEditToolstripAction](https://uk.mathworks.com/help/simulink/slref/sledittoolstripaction.html) | Open file that defines custom Simulink Toolstrip action _(Since R2021b)_  
[slEditToolstripCommand](https://uk.mathworks.com/help/simulink/slref/sledittoolstripcommand.html) | Open file that defines custom Simulink Toolstrip command _(Since R2021b)_  
[slEditToolstripIcon](https://uk.mathworks.com/help/simulink/slref/sledittoolstripicon.html) | Open file that defines custom Simulink Toolstrip icon _(Since R2021b)_  
[slEditToolstripWidget](https://uk.mathworks.com/help/simulink/slref/sledittoolstripwidget.html) | Open file that defines custom Simulink Toolstrip tab, section, column, or control _(Since R2021b)_  
[slLoadedToolstripComponents](https://uk.mathworks.com/help/simulink/slref/slloadedtoolstripcomponents.html) | Find loaded custom Simulink Toolstrip components _(Since R2021b)_  
[slPersistToolstripComponent](https://uk.mathworks.com/help/simulink/slref/slpersisttoolstripcomponent.html) | Specify whether custom Simulink Toolstrip component persists across MATLAB sessions _(Since R2021b)_  
[slReloadToolstripConfig](https://uk.mathworks.com/help/simulink/slref/slreloadtoolstripconfig.html) | Reload Simulink Toolstrip configuration _(Since R2021b)_  
[slToolstripDeveloperMode](https://uk.mathworks.com/help/simulink/slref/sltoolstripdevelopermode.html) | Enable developer mode for Simulink Toolstrip _(Since R2021b)_  
[slUpdateToolstripComponent](https://uk.mathworks.com/help/simulink/slref/slupdatetoolstripcomponent.html) | Reload specific custom toolstrip component _(Since R2023b)_  
#### Quick Insert Menu
Name|Description
---|---
[slblocksearchdb.trainfrommodel](https://uk.mathworks.com/help/simulink/slref/slblocksearchdb.trainfrommodel.html) | Train suggestion engine to improve quick insert results based on one model  
[slblocksearchdb.trainfrommodelsindir](https://uk.mathworks.com/help/simulink/slref/slblocksearchdb.trainfrommodelsindir.html) | Train suggestion engine to improve quick insert results based on models in a folder  
[slblocksearchdb.untrainall](https://uk.mathworks.com/help/simulink/slref/slblocksearchdb.untrainall.html) | Remove the effects of all added models from the suggestion engine  
[slblocksearchdb.untrainmodel](https://uk.mathworks.com/help/simulink/slref/slblocksearchdb.untrainmodel.html) | Remove the effect of a model from the suggestion engine  
[slblocksearchdb.untrainmodelsindir](https://uk.mathworks.com/help/simulink/slref/slblocksearchdb.untrainmodelsindir.html) | Remove the effects of models from the suggestion engine  
#### Library Browser
Name|Description
---|---
[LibraryBrowser.LibraryBrowser2](https://uk.mathworks.com/help/simulink/slref/librarybrowser.librarybrowser2.html) | Get handle of Library Browser object  
[sl_refresh_customizations](https://uk.mathworks.com/help/simulink/slref/sl_refresh_customizations.html) | Refresh customizations in the current MATLAB session _(Since R2022a)_  
#### Simulink Editor
Name|Description
---|---
[Simulink.history.clear](https://uk.mathworks.com/help/simulink/slref/simulink.history.clear.html) | Clear the Simulink start page and editor history  
#### Other
Name|Description
---|---
[LibraryBrowser.LBStandalone](https://uk.mathworks.com/help/simulink/slref/librarybrowser.lbstandalone.html) | Display, hide, size, and position Simulink Library Browser  
### Block Libraries
#### Model-Wide Utilities
Name|Description
---|---
[showblockdatatypetable](https://uk.mathworks.com/help/simulink/slref/showblockdatatypetable.html) | Display HTML page of Simulink block data type support  
## Modeling
### Design Model Architecture
#### Subsystems
Name|Description
---|---
[Simulink.BlockDiagram.copyContentsToSubsystem](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.copycontentstosubsystem.html) | Copy graphical contents from system to empty subsystem  
[Simulink.BlockDiagram.createSubsystem](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.createsubsystem.html) | Create subsystem containing specified set of blocks  
[Simulink.BlockDiagram.expandSubsystem](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.expandsubsystem.html) | Replace subsystem with subsystem contents  
[Simulink.SubSystem.convertToModelReference](https://uk.mathworks.com/help/simulink/slref/simulink.subsystem.converttomodelreference.html) | Convert subsystems to models  
[Simulink.SubSystem.copyContentsToBlockDiagram](https://uk.mathworks.com/help/simulink/slref/simulink.subsystem.copycontentstoblockdiagram.html) | Copy graphical contents from subsystem to another model  
[Simulink.SubSystem.deleteContents](https://uk.mathworks.com/help/simulink/slref/simulink.subsystem.deletecontents.html) | Delete contents of subsystem  
[Simulink.SubsystemReference.convertAllSubsystemReferenceBlocksToSubsystem](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.convertallsubsystemreferenceblockstosubsystem.html) | Convert all Subsystem Reference blocks to Subsystem blocks _(Since R2022a)_  
[Simulink.SubsystemReference.convertSubsystemReferenceBlockToSubsystem](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.convertsubsystemreferenceblocktosubsystem.html) | Convert Subsystem Reference block to Subsystem block _(Since R2022a)_  
[Simulink.SubsystemReference.convertSubsystemToSubsystemReference](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.convertsubsystemtosubsystemreference.html) | Convert Subsystem block to Subsystem Reference block _(Since R2022a)_  
[Simulink.SubsystemReference.generateSignatures](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.generatesignatures.html) | Generate unit test signatures of subsystem file _(Since R2023a)_  
[Simulink.SubsystemReference.getActiveInstances](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.getactiveinstances.html) | Return active instances of subsystem reference _(Since R2022a)_  
[Simulink.SubsystemReference.getAllDirtyInstances](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.getalldirtyinstances.html) | Return subsystem files referenced in model that are currently being edited _(Since R2022a)_  
[Simulink.SubsystemReference.getAllInstances](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.getallinstances.html) | Return all Subsystem Reference blocks in model _(Since R2022a)_  
[Simulink.SubsystemReference.getAllReferencedSubsystemBlockDiagrams](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.getallreferencedsubsystemblockdiagrams.html) | Return all subsystem files referenced in model _(Since R2022a)_  
[Simulink.SubsystemReference.getNearestParentSubsystemReferenceBlock](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.getnearestparentsubsystemreferenceblock.html) | Return nearest parent Subsystem Reference block for specified block _(Since R2022a)_  
[Simulink.SubsystemReference.getSystemOwningTheLock](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.getsystemowningthelock.html) | Return subsystem reference instance that has acquired lock for editing _(Since R2022a)_  
[Simulink.SubsystemReference.getUnitTestNames](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.getunittestnames.html) | Return names of unit tests of subsystem file _(Since R2023a)_  
[Simulink.SubsystemReference.isSystemLocked](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.issystemlocked.html) |  Check if subsystem file is locked due to edit or update _(Since R2022a)_  
[Simulink.SubsystemReference.removeSignatures](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.removesignatures.html) | Remove previously generated unit test signatures of subsystem file _(Since R2023a)_  
[Simulink.SubsystemReference.showSignatureDiffDialogForSS](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.showsignaturediffdialogforss.html) | Display differences in signatures of two Subsystem blocks _(Since R2023a)_  
[Simulink.SubsystemReference.showSignatureDiffDialogForUnitTests](https://uk.mathworks.com/help/simulink/slref/simulink.subsystemreference.showsignaturediffdialogforunittests.html) | Display differences in signatures of Subsystem Reference block in model with unit test signatures of subsystem file _(Since R2023a)_  
#### Libraries and Blocksets
Name|Description
---|---
[libinfo](https://uk.mathworks.com/help/simulink/slref/libinfo.html) | Get information about library blocks referenced by model  
#### Model References
Name|Description
---|---
[depview](https://uk.mathworks.com/help/simulink/slref/depview.html) | Analyze and visualize model referencing dependencies with or without library dependencies  
[find_mdlrefs](https://uk.mathworks.com/help/simulink/slref/find_mdlrefs.html) | Find referenced models and Model blocks in model hierarchy  
[pathsToReferencedModel](https://uk.mathworks.com/help/simulink/slref/pathstoreferencedmodel.html) | Model hierarchy path composed of referenced models and Model blocks _(Since R2023b)_  
[Simulink.BlockDiagram.refreshBlocks](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.refreshblocks.html) | Update variants, linked blocks, and model references to reflect changes _(Since R2023a)_  
[Simulink.BlockPath](https://uk.mathworks.com/help/simulink/slref/simulink.blockpath.html) | Fully specified Simulink block path  
[Simulink.fileGenControl](https://uk.mathworks.com/help/simulink/slref/simulink.filegencontrol.html) | Specify root folders for files generated by diagram updates and model builds  
[Simulink.ModelReference.refresh](https://uk.mathworks.com/help/simulink/slref/simulink.modelreference.refresh.html) | Force update to Model block to reflect changes to referenced model  
[Simulink.ProtectedModel.createHarness](https://uk.mathworks.com/help/simulink/slref/simulink.protectedmodel.createharness.html) | Create harness model that provides isolated environment for testing protected model  
[Simulink.ProtectedModel.getPublisher](https://uk.mathworks.com/help/simulink/slref/simulink.protectedmodel.getpublisher.html) | Return information about publisher that signed the protected model  
[Simulink.ProtectedModel.suppressSignatureVerification](https://uk.mathworks.com/help/simulink/slref/simulink.protectedmodel.suppresssignatureverification.html) | Suppress digital signature verification of protected models  
[Simulink.ProtectedModel.verifySignature](https://uk.mathworks.com/help/simulink/slref/simulink.protectedmodel.verifysignature.html) | Verify digital signature on protected model  
[Simulink.SubSystem.convertToModelReference](https://uk.mathworks.com/help/simulink/slref/simulink.subsystem.converttomodelreference.html) | Convert subsystems to models  
[slbuild](https://uk.mathworks.com/help/simulink/slref/slbuild.html) | Build standalone executable file or model reference target for model  
[slxcinfo](https://uk.mathworks.com/help/simulink/slref/slxcinfo.html) | Query contents of Simulink cache files  
[slxcunpack](https://uk.mathworks.com/help/simulink/slref/slxcunpack.html) | Unpack simulation and code generation targets from Simulink cache file  
[slxpinfo](https://uk.mathworks.com/help/simulink/slref/slxpinfo.html) | High-level information about protected model _(Since R2024b)_  
#### Variant Systems
Name|Description
---|---
[addComponentConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.addcomponentconfiguration.html) |  Associate top-model variant configuration with variant configuration of referenced model _(Since R2022b)_  
[addConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.addconfiguration.html) | Add new variant configuration to variant configuration data object  
[addConstraint](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.addconstraint.html) | Add constraint to variant configuration data object  
[addControlVariables](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.addcontrolvariables.html) | Add variant control variables to named variant configuration in variant configuration data object  
[addCopyOfConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.addcopyofconfiguration.html) | Add copy of existing variant configuration to variant configuration data object  
[convertDefaultToPreferred](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.convertdefaulttopreferred.html) | Convert default variant configuration to preferred variant configuration _(Since R2022b)_  
[enumeration](https://uk.mathworks.com/help/matlab/ref/enumeration.html) | Class enumeration members and names  
[getComponentConfigurationName](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.getcomponentconfigurationname.html) | Get name of variant configuration used by referenced component in model hierarchy _(Since R2023b)_  
[getConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.getconfiguration.html) | Get specific variant configuration from variant configuration data object  
[getPreferredConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.getpreferredconfiguration.html) | Get name of preferred variant configuration for variant configuration data object _(Since R2022b)_  
[isConfigActive](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.isconfigactive.html) | Check if variant configuration is active _(Since R2025a)_  
[removeComponentConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.removecomponentconfiguration.html) | Remove association between variant configurations of top-level model and referenced model _(Since R2022b)_  
[removeConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.removeconfiguration.html) | Remove variant configuration from variant configuration data object  
[removeConstraint](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.removeconstraint.html) |  Remove constraint from variant configuration data object  
[removeControlVariable](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.removecontrolvariable.html) | Remove variant control variable from variant configuration  
[setPreferredConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.setpreferredconfiguration.html) |  Set name of preferred variant configuration for variant configuration data object _(Since R2022b)_  
[Simulink.Parameter](https://uk.mathworks.com/help/simulink/slref/simulink.parameter.html) | Store, share, and configure parameter values  
[Simulink.VariantBank](https://uk.mathworks.com/help/simulink/slref/simulink.variantbank-class.html) | Group all variant parameter values in structure array in generated code _(Since R2023a)_  
[Simulink.VariantBankCoderInfo](https://uk.mathworks.com/help/simulink/slref/simulink.variantbankcoderinfo-class.html) | Specify code generation properties for variant parameter bank _(Since R2023a)_  
[Simulink.VariantConfigurationAnalysis](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationanalysis-class.html) | Analyze variant configurations programmatically  
[Simulink.VariantConfigurationData](https://uk.mathworks.com/help/simulink/slref/simulink.variantconfigurationdata.html) | Create and store variant configurations and constraints  
[Simulink.VariantControl](https://uk.mathworks.com/help/simulink/slref/simulink.variantcontrol-class.html) | Create a variant control variable object _(Since R2021a)_  
[Simulink.VariantExpression](https://uk.mathworks.com/help/simulink/slref/simulink.variantexpression-class.html) | Specify conditions that control variant selection  
[Simulink.VariantManager.activateModel](https://uk.mathworks.com/help/simulink/slref/simulink.variantmanager.activatemodel.html) |  Validate and activate variant blocks in model hierarchy _(Since R2022b)_  
[Simulink.VariantManager.applyConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.variantmanager.applyconfiguration.html) | Apply specified variant configuration to model _(Since R2022b)_  
[Simulink.VariantManager.findVariantControlVars](https://uk.mathworks.com/help/simulink/slref/simulink.variantmanager.findvariantcontrolvars.html) |  Find variables used in variant control expressions  
[Simulink.VariantManager.generateConfigurations](https://uk.mathworks.com/help/simulink/slref/simulink.variantmanager.generateconfigurations.html) |  Generate variant configurations automatically _(Since R2022b)_  
[Simulink.VariantManager.getConfigurationData](https://uk.mathworks.com/help/simulink/slref/simulink.variantmanager.getconfigurationdata.html) | Get variant configuration data object associated with model _(Since R2022b)_  
[Simulink.VariantManager.getPreferredConfigurationName](https://uk.mathworks.com/help/simulink/slref/simulink.variantmanager.getpreferredconfigurationname.html) | Get name of preferred variant configuration for model _(Since R2022b)_  
[Simulink.VariantManager.reduceModel](https://uk.mathworks.com/help/simulink/slref/simulink.variantmanager.reducemodel.html) | Generate reduced model for specified variant configurations  
[Simulink.VariantManager.updateModel](https://uk.mathworks.com/help/simulink/slref/simulink.variantmanager.updatemodel.html) | Obtain model compilation information and activate variant blocks in model hierarchy _(Since R2024b)_  
[Simulink.VariantManager.validateConstraint](https://uk.mathworks.com/help/simulink/slref/simulink.variantmanager.validateconstraint.html) | Verify if variant constraint is satisfied by model hierarchy _(Since R2025a)_  
[Simulink.VariantUtils](https://uk.mathworks.com/help/simulink/slref/simulink.variantutils-class.html) | Utility methods to work with variant elements _(Since R2023b)_  
[Simulink.VariantVariable](https://uk.mathworks.com/help/simulink/slref/simulink.variantvariable-class.html) | Create variant parameter object _(Since R2021a)_  
[struct](https://uk.mathworks.com/help/matlab/ref/struct.html) | Structure array  
#### Data Stores
Name|Description
---|---
[Simulink.SimulationData.BlockPath](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.blockpath.html) | Fully specified block path  
[Simulink.SimulationData.Dataset](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.dataset.html) | Access logged simulation data or group simulation input data  
[Simulink.SimulationData.DataStoreMemory](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.datastorememory.html) | Container for data store logging information  
#### Composite Interfaces
Name|Description
---|---
[createBusPort](https://uk.mathworks.com/help/simulink/slref/createbusport.html) | Create bus element port from bus block connected to port block _(Since R2025a)_  
[getLeafBusElements](https://uk.mathworks.com/help/simulink/slref/simulink.bus.getleafbuselements.html) | Leaf elements in `Simulink.Bus` object  
[getNumLeafBusElements](https://uk.mathworks.com/help/simulink/slref/simulink.bus.getnumleafbuselements.html) | Number of leaf elements in `Simulink.Bus` object  
[simplifyInterfacesWithBusPorts](https://uk.mathworks.com/help/simulink/slref/simplifyinterfaceswithbusports.html) | Update model or subsystem file to use bus element ports for buses _(Since R2025a)_  
[Simulink.BlockDiagram.addBusToVector](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.addbustovector.html) | Convert virtual bus signals into vector signals by adding Bus to Vector blocks  
[Simulink.Bus](https://uk.mathworks.com/help/simulink/slref/simulink.bus.html) |  Specify properties of buses  
[Simulink.Bus.addElementToPort](https://uk.mathworks.com/help/simulink/slref/simulink.bus.addelementtoport.html) | Add element to input bus element port _(Since R2022b)_  
[Simulink.Bus.cellToObject](https://uk.mathworks.com/help/simulink/slref/simulink.bus.celltoobject.html) | Create `Simulink.Bus` objects from cell array of bus information  
[Simulink.Bus.createMATLABStruct](https://uk.mathworks.com/help/simulink/slref/simulink.bus.creatematlabstruct.html) | Create MATLAB structures that use same hierarchy and attributes as buses  
[Simulink.Bus.createObject](https://uk.mathworks.com/help/simulink/slref/simulink.bus.createobject.html) | Create `Simulink.Bus` objects from blocks or MATLAB structures  
[Simulink.Bus.objectToCell](https://uk.mathworks.com/help/simulink/slref/simulink.bus.objecttocell.html) | Create cell array of bus information from `Simulink.Bus` objects  
[Simulink.Bus.save](https://uk.mathworks.com/help/simulink/slref/simulink.bus.save.html) | Save `Simulink.Bus` object definitions in function  
[Simulink.BusElement](https://uk.mathworks.com/help/simulink/slref/simulink.buselement.html) |  Specify properties of elements of buses  
### Manage Design Data
#### Manage Data Sources
Name|Description
---|---
[Simulink.data.connect](https://uk.mathworks.com/help/simulink/slref/simulink.data.connect.html) | Create `Simulink.data.DataConnection` object for data source _(Since R2024a)_  
[Simulink.data.dataSource.addSource](https://uk.mathworks.com/help/simulink/slref/simulink.data.datasource.addsource.html) | Add external data source to model _(Since R2024b)_  
[Simulink.data.dataSource.getSourceNames](https://uk.mathworks.com/help/simulink/slref/simulink.data.datasource.getsourcenames.html) | Get list of all external data sources associated with model _(Since R2024b)_  
[Simulink.data.dataSource.hasSource](https://uk.mathworks.com/help/simulink/slref/simulink.data.datasource.hassource.html) | Determine if specified external data source is associated with model _(Since R2024b)_  
[Simulink.data.dataSource.removeSource](https://uk.mathworks.com/help/simulink/slref/simulink.data.datasource.removesource.html) | Remove external data source from model _(Since R2024b)_  
#### Manage Data Dictionary
Name|Description
---|---
[Simulink.data.dictionary.closeAll](https://uk.mathworks.com/help/simulink/slref/simulink.data.dictionary.closeall.html) | Close all connections to all open data dictionaries  
[Simulink.data.dictionary.create](https://uk.mathworks.com/help/simulink/slref/simulink.data.dictionary.create.html) | Create new data dictionary and create `Simulink.data.Dictionary` object  
[Simulink.data.dictionary.getOpenDictionaryPaths](https://uk.mathworks.com/help/simulink/slref/simulink.data.dictionary.getopendictionarypaths.html) | Return file names and paths of open data dictionaries  
[Simulink.data.dictionary.open](https://uk.mathworks.com/help/simulink/slref/simulink.data.dictionary.open.html) | Open data dictionary for editing  
[Simulink.dictionary.archdata.create](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.create.html) | Create Simulink data dictionary and Architectural Data object _(Since R2023b)_  
[Simulink.dictionary.archdata.open](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.open.html) | Create Architectural Data object representing architectural data of existing Simulink data dictionary _(Since R2023b)_  
[Simulink.LibraryDictionary.clear](https://uk.mathworks.com/help/simulink/slref/simulink.librarydictionary.clear.html) | Clear library dictionary dependency analysis _(Since R2021a)_  
[Simulink.LibraryDictionary.refresh](https://uk.mathworks.com/help/simulink/slref/simulink.librarydictionary.refresh.html) | Update library dictionary dependencies _(Since R2021a)_  
[Simulink.LibraryDictionary.resetLibraryLinks](https://uk.mathworks.com/help/simulink/slref/simulink.librarydictionary.resetlibrarylinks.html) | Clear cached information on library dictionary links _(Since R2022a)_  
#### Manage External File Adapters
Name|Description
---|---
[Simulink.data.adapters.catalog](https://uk.mathworks.com/help/simulink/slref/simulink.data.adapters.catalog.html) | List registered file adapters _(Since R2022b)_  
[Simulink.data.adapters.registerAdapter](https://uk.mathworks.com/help/simulink/slref/simulink.data.adapters.registeradapter.html) | Register custom file adapter _(Since R2022b)_  
[Simulink.data.adapters.unregisterAdapter](https://uk.mathworks.com/help/simulink/slref/simulink.data.adapters.unregisteradapter.html) | Unregister custom file adapter _(Since R2022b)_  
#### Manage Variables
Name|Description
---|---
[matlab.io.saveVariablesToScript](https://uk.mathworks.com/help/matlab/ref/matlab.io.savevariablestoscript.html) | Save workspace variables to MATLAB script  
[Simulink.data.assigninGlobal](https://uk.mathworks.com/help/simulink/slref/simulink.data.assigninglobal.html) | Modify variable values in context of Simulink model  
[Simulink.data.evalinGlobal](https://uk.mathworks.com/help/simulink/slref/simulink.data.evalinglobal.html) | Evaluate MATLAB expression in context of Simulink model  
[Simulink.data.existsInGlobal](https://uk.mathworks.com/help/simulink/slref/simulink.data.existsinglobal.html) | Determine if variable exists in context of Simulink model  
[Simulink.data.getVariableFromGlobal](https://uk.mathworks.com/help/simulink/slref/simulink.data.getvariablefromglobal.html) | Get variable defined in context of Simulink model _(Since R2024b)_  
[Simulink.data.resolveInGlobal](https://uk.mathworks.com/help/simulink/slref/simulink.data.resolveinglobal.html) | Resolve MATLAB expression in context of Simulink model _(Since R2024b)_  
[Simulink.findVars](https://uk.mathworks.com/help/simulink/slref/simulink.findvars.html) | Analyze relationship between variables and blocks in models  
#### Data Sources
Name|Description
---|---
[Simulink.data.DataConnection](https://uk.mathworks.com/help/simulink/slref/simulink.data.dataconnection.html) | Data source connection _(Since R2024a)_  
#### Model Workspace
Name|Description
---|---
[Simulink.ModelWorkspace](https://uk.mathworks.com/help/simulink/slref/simulink.modelworkspace.html) | Interact with the model workspace of a model programmatically  
#### Data Dictionary
Name|Description
---|---
[Simulink.data.Dictionary](https://uk.mathworks.com/help/simulink/slref/simulink.data.dictionary.html) | Configure data dictionary  
[Simulink.data.dictionary.Entry](https://uk.mathworks.com/help/simulink/slref/simulink.data.dictionary.entry.html) | Configure data dictionary entry  
[Simulink.data.dictionary.EnumTypeDefinition](https://uk.mathworks.com/help/simulink/slref/simulink.data.dictionary.enumtypedefinition.html) | Store enumerated type definition in data dictionary  
[Simulink.data.dictionary.Section](https://uk.mathworks.com/help/simulink/slref/simulink.data.dictionary.section.html) | Configure data dictionary section  
[Simulink.dictionary.archdata.AliasType](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.aliastype.html) | Edit Simulink alias types in Simulink data dictionary _(Since R2023b)_  
[Simulink.dictionary.archdata.Constant](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.constant.html) | Store constant values in Architectural Data section of data dictionaries _(Since R2023b)_  
[Simulink.dictionary.archdata.DataElement](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.dataelement.html) | Data element of data interface _(Since R2023b)_  
[Simulink.dictionary.archdata.DataInterface](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.datainterface.html) | Data interface in Architectural Data section of Simulink data dictionary _(Since R2023b)_  
[Simulink.dictionary.archdata.Enumeral](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.enumeral.html) | Enumeration member of enumerated data type stored in Architectural Data section _(Since R2023b)_  
[Simulink.dictionary.archdata.EnumType](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.enumtype.html) | Enumerated data type stored in Architectural Data section _(Since R2023b)_  
[Simulink.dictionary.archdata.FunctionArgument](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.functionargument.html) | Function argument in function element of client-server interface _(Since R2023b)_  
[Simulink.dictionary.archdata.FunctionElement](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.functionelement.html) | Function in client-server interface _(Since R2023b)_  
[Simulink.dictionary.archdata.NumericType](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.numerictype.html) | Edit Simulink numeric types in Simulink data dictionary _(Since R2023b)_  
[Simulink.dictionary.archdata.PhysicalElement](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.physicalelement.html) | Physical element of a physical interface _(Since R2023b)_  
[Simulink.dictionary.archdata.PhysicalInterface](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.physicalinterface.html) | Physical interface _(Since R2023b)_  
[Simulink.dictionary.archdata.ServiceInterface](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.serviceinterface.html) | Service interface _(Since R2023b)_  
[Simulink.dictionary.archdata.StructElement](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.structelement.html) | Struct element of a struct type _(Since R2023b)_  
[Simulink.dictionary.archdata.StructType](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.structtype.html) | Structure data type _(Since R2023b)_  
[Simulink.dictionary.archdata.ValueType](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.archdata.valuetype.html) | Specify common set of signal properties for reuse in Architectural Data section _(Since R2023b)_  
[Simulink.dictionary.ArchitecturalData](https://uk.mathworks.com/help/simulink/slref/simulink.dictionary.architecturaldata.html) | Edit architectural data in a Simulink data dictionary programmatically _(Since R2023b)_  
#### External File Adapters
Name|Description
---|---
[Simulink.data.adapters.AdapterDataTester](https://uk.mathworks.com/help/simulink/slref/simulink.data.adapters.adapterdatatester.html) | Test custom external file adapter _(Since R2022b)_  
[Simulink.data.adapters.BaseMatlabFileAdapter](https://uk.mathworks.com/help/simulink/slref/simulink.data.adapters.basematlabfileadapter-class.html) | Base class used to define file adapter for reading custom file formats _(Since R2022b)_  
[Simulink.data.DataSourceWorkspace](https://uk.mathworks.com/help/simulink/slref/simulink.data.datasourceworkspace.html) | Contains data for external data source _(Since R2022b)_  
#### Objects and Variables
Name|Description
---|---
[Simulink.CoderInfo](https://uk.mathworks.com/help/simulink/slref/simulink.coderinfo.html) | Specify information needed to generate code for signal, state, or parameter data  
[Simulink.VariableUsage](https://uk.mathworks.com/help/simulink/slref/simulink.variableusage.html) | Store information about the relationship between variables and blocks in models  
[Simulink.WorkspaceVar](https://uk.mathworks.com/help/simulink/slref/simulink.workspacevar.html) | Store information about workspace variables and blocks that use them  
### Design Model Behavior
#### Conditionally Executed Subsystems and Models
Name|Description
---|---
[Simulink.getOutportInheritsInitialValue](https://uk.mathworks.com/help/simulink/slref/simulink.getoutportinheritsinitialvalue.html) | Determine if conditional subsystem Outport block inherits initial output value _(Since R2021a)_  
#### Schedule Model Components
Name|Description
---|---
[Simulink.BlockDiagram.getExecutionOrder](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.getexecutionorder.html) | Open Execution Order pane _(Since R2022b)_  
[simulink.event.InputWrite](https://uk.mathworks.com/help/simulink/slref/simulink.event.inputwrite.html) | Trigger schedule event when input port value updates _(Since R2022b)_  
[simulink.event.InputWriteLost](https://uk.mathworks.com/help/simulink/slref/simulink.event.inputwritelost.html) | Trigger schedule event when update to input port value overwrites unprocessed data _(Since R2022b)_  
[simulink.event.InputWriteTimeout](https://uk.mathworks.com/help/simulink/slref/simulink.event.inputwritetimeout.html) | Trigger schedule event when input port value does not update within specified time _(Since R2022b)_  
[simulink.schedule.createSchedule](https://uk.mathworks.com/help/simulink/slref/simulink.schedule.createschedule.html) | Create a new schedule using provided schedule and ordering  
[simulink.schedule.OrderedSchedule](https://uk.mathworks.com/help/simulink/slref/simulink.schedule.orderedschedule-class.html) | Creates an `OrderedSchedule` object containing priority order of the partitions of a model  
#### Nonlinearity
Name|Description
---|---
[Simulink.Breakpoint](https://uk.mathworks.com/help/simulink/slref/simulink.breakpoint-class.html) | Store and share data for a breakpoint set, configure the data for ASAP2 and AUTOSAR code generation  
[Simulink.LookupTable](https://uk.mathworks.com/help/simulink/slref/simulink.lookuptable-class.html) | Store and share lookup table and breakpoint data, configure data for ASAP2 and AUTOSAR code generation  
[Simulink.lookuptable.Breakpoint](https://uk.mathworks.com/help/simulink/slref/simulink.lookuptable.breakpoint-class.html) | Configure breakpoint set data for lookup table object  
[Simulink.lookuptable.Evenspacing](https://uk.mathworks.com/help/simulink/slref/simulink.lookuptable.evenspacing-class.html) | Configure even spacing set data for lookup table object   
[Simulink.lookuptable.StructTypeInfo](https://uk.mathworks.com/help/simulink/slref/simulink.lookuptable.structtypeinfo-class.html) | Configure settings for structure type that lookup table object uses in the generated code  
[Simulink.lookuptable.Table](https://uk.mathworks.com/help/simulink/slref/simulink.lookuptable.table-class.html) | Configure table data for lookup table object  
#### Multicore Processor Targets
Name|Description
---|---
[Simulink.architecture.add](https://uk.mathworks.com/help/simulink/slref/simulink.architecture.add.html) | Add tasks or triggers to selected architecture of model  
[Simulink.architecture.config](https://uk.mathworks.com/help/simulink/slref/simulink.architecture.config.html) | Create or convert configuration for concurrent execution  
[Simulink.architecture.delete](https://uk.mathworks.com/help/simulink/slref/simulink.architecture.delete.html) | Delete triggers and tasks from selected architecture of model  
[Simulink.architecture.find_system](https://uk.mathworks.com/help/simulink/slref/simulink.architecture.find_system.html) | Find objects under architecture object  
[Simulink.architecture.get_param](https://uk.mathworks.com/help/simulink/slref/simulink.architecture.get_param.html) | Get configuration parameters of architecture objects  
[Simulink.architecture.importAndSelect](https://uk.mathworks.com/help/simulink/slref/simulink.architecture.importandselect.html) | Import and select target architecture for concurrent execution environment for model  
[Simulink.architecture.profile](https://uk.mathworks.com/help/simulink/slref/simulink.architecture.profile.html) | Generate profile report for model configured for concurrent execution  
[Simulink.architecture.register](https://uk.mathworks.com/help/simulink/slref/simulink.architecture.register.html) | Add custom target architecture to concurrent execution target architecture selector  
[Simulink.architecture.set_param](https://uk.mathworks.com/help/simulink/slref/simulink.architecture.set_param.html) | Set architecture object properties  
[Simulink.GlobalDataTransfer](https://uk.mathworks.com/help/simulink/slref/simulink.globaldatatransfer.html) | Configure concurrent execution data transfers  
### Configure Signals, States, and Parameters
#### Blocks
Name|Description
---|---
[get_param](https://uk.mathworks.com/help/simulink/slref/get_param.html) | Get parameter names and values  
[set_param](https://uk.mathworks.com/help/simulink/slref/set_param.html) | Set Simulink parameter value  
[Simulink.DualScaledParameter](https://uk.mathworks.com/help/simulink/slref/simulink.dualscaledparameter.html) | Specify name, value, units, and other properties of Simulink dual-scaled parameter  
[Simulink.Parameter](https://uk.mathworks.com/help/simulink/slref/simulink.parameter.html) | Store, share, and configure parameter values  
[Simulink.VariantControl](https://uk.mathworks.com/help/simulink/slref/simulink.variantcontrol-class.html) | Create a variant control variable object _(Since R2021a)_  
[Simulink.VariantVariable](https://uk.mathworks.com/help/simulink/slref/simulink.variantvariable-class.html) | Create variant parameter object _(Since R2021a)_  
[slexpr](https://uk.mathworks.com/help/simulink/slref/slexpr.html) | Generate expression to use in value of parameter object  
#### Signals
Name|Description
---|---
[disableimplicitsignalresolution](https://uk.mathworks.com/help/simulink/slref/disableimplicitsignalresolution.html) | Convert model to use only explicit signal resolution  
[highlight](https://uk.mathworks.com/help/simulink/slref/sltrace.graph.highlight.html) | Highlight path to signal sources or destinations in model _(Since R2021b)_  
[removehighlight](https://uk.mathworks.com/help/simulink/slref/sltrace.graph.removehighlight.html) | Remove highlighting for `sltrace.Graph` object from model _(Since R2021b)_  
[signalBuilderToSignalEditor](https://uk.mathworks.com/help/simulink/slref/signalbuildertosignaleditor.html) | Import signal data and properties from Signal Builder block to Signal Editor block  
[Simulink.Signal](https://uk.mathworks.com/help/simulink/slref/simulink.signal.html) | Specify instance-specific properties of signal or discrete state  
[Simulink.ValueType](https://uk.mathworks.com/help/simulink/slref/simulink.valuetype.html) | Specify common set of signal properties for reuse _(Since R2021b)_  
[sltrace](https://uk.mathworks.com/help/simulink/slref/sltrace.html) | Analyze structure of model by tracing signal sources and destinations _(Since R2021b)_  
[sltrace.Graph](https://uk.mathworks.com/help/simulink/slref/sltrace.graph.html) | Signal path traced using `sltrace` function _(Since R2021b)_  
#### Units in Simulink
Name|Description
---|---
[createCustomDBFromExcel](https://uk.mathworks.com/help/simulink/slref/createcustomdbfromexcel.html) | Create custom units database file from Microsoft Excel spreadsheet  
[rehashUnitDBs](https://uk.mathworks.com/help/simulink/slref/rehashunitdbs.html) | Refresh unit database files on MATLAB path  
[showunitslist](https://uk.mathworks.com/help/simulink/slref/showunitslist.html) | Show built-in units, physical quantities, and unit systems supported by Simulink  
#### Sample Time
Name|Description
---|---
[Simulink.Block.getSampleTimes](https://uk.mathworks.com/help/simulink/slref/simulink.block.getsampletimes.html) | Return sample time information for a block  
[Simulink.BlockDiagram.getSampleTimes](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.getsampletimes.html) | Return all sample times associated with model  
[Simulink.BlockPortData](https://uk.mathworks.com/help/simulink/slref/simulink.blockportdata.html) | Describe block input or output port  
[Simulink.SampleTime](https://uk.mathworks.com/help/simulink/slref/simulink.sampletime-class.html) | Object containing sample time information   
[simulink.sampletimecolors.applyPalette](https://uk.mathworks.com/help/simulink/slref/simulink.sampletimecolors.applypalette.html) | Apply sample time color palette to current MATLAB session _(Since R2024b)_  
[simulink.sampletimecolors.getPalette](https://uk.mathworks.com/help/simulink/slref/simulink.sampletimecolors.getpalette.html) | Get available `simulink.sampletimecolors.Palette` objects _(Since R2024b)_  
[simulink.sampletimecolors.Palette](https://uk.mathworks.com/help/simulink/slref/simulink.sampletimecolors.palette.html) | Create custom sample time color palette for Simulink model _(Since R2024b)_  
[simulink.sampletimecolors.removePalette](https://uk.mathworks.com/help/simulink/slref/simulink.sampletimecolors.removepalette.html) | Remove `simulink.sampletimecolors.Palette` object from preferences _(Since R2024b)_  
[simulink.sampletimecolors.storePalette](https://uk.mathworks.com/help/simulink/slref/simulink.sampletimecolors.storepalette.html) | Add new `simulink.sampletimecolors.Palette` object to preferences _(Since R2024b)_  
#### Data Types
Name|Description
---|---
[enumeration](https://uk.mathworks.com/help/matlab/ref/enumeration.html) | Class enumeration members and names  
[fixdt](https://uk.mathworks.com/help/simulink/slref/simulink.numerictype.fixdt.html) | Create `Simulink.NumericType` object describing a fixed-point or floating-point data type  
[fixpt_evenspace_cleanup](https://uk.mathworks.com/help/simulink/slref/fixpt_evenspace_cleanup.html) | Modify breakpoints of lookup table to have even spacing  
[fixpt_look1_func_approx](https://uk.mathworks.com/help/simulink/slref/fixpt_look1_func_approx.html) | Optimize fixed-point approximation of nonlinear function by interpolating lookup table data points  
[fixpt_look1_func_plot](https://uk.mathworks.com/help/simulink/slref/fixpt_look1_func_plot.html) | Plot fixed-point approximation function for lookup table  
[fixpt_set_all](https://uk.mathworks.com/help/simulink/slref/fixpt_set_all.html) | Set property for each fixed-point block in subsystem  
[fixptbestexp](https://uk.mathworks.com/help/simulink/slref/fixptbestexp.html) | Exponent that gives best precision for fixed-point representation of value  
[fixptbestprec](https://uk.mathworks.com/help/simulink/slref/fixptbestprec.html) | Determine maximum precision available for fixed-point representation of value  
[showblockdatatypetable](https://uk.mathworks.com/help/simulink/slref/showblockdatatypetable.html) | Display HTML page of Simulink block data type support  
[Simulink.AliasType](https://uk.mathworks.com/help/simulink/slref/simulink.aliastype.html) | Create alias for signal and parameter data type  
[Simulink.Block.getInternalDataType](https://uk.mathworks.com/help/simulink/slref/simulink.block.getinternaldatatype.html) | Get data type of block parameter _(Since R2023a)_  
[Simulink.clearIntEnumType](https://uk.mathworks.com/help/simulink/slref/simulink.clearintenumtype.html) | Delete enumeration classes defined by `Simulink.defineIntEnumType`  
[Simulink.data.getEnumTypeInfo](https://uk.mathworks.com/help/simulink/slref/simulink.data.getenumtypeinfo.html) | Get information about enumerated data type  
[Simulink.data.isSupportedEnumClass](https://uk.mathworks.com/help/simulink/slref/simulink.data.issupportedenumclass.html) | Determine whether an enumeration class is valid for Simulink  
[Simulink.data.isSupportedEnumObject](https://uk.mathworks.com/help/simulink/slref/simulink.data.issupportedenumobject.html) | Determine whether an enumeration object is valid for Simulink  
[Simulink.defineIntEnumType](https://uk.mathworks.com/help/simulink/slref/simulink.defineintenumtype.html) | Define enumerated data type   
[Simulink.findIntEnumType](https://uk.mathworks.com/help/simulink/slref/simulink.findintenumtype.html) | Find enumeration classes defined by `Simulink.defineIntEnumType`  
[Simulink.importExternalCTypes](https://uk.mathworks.com/help/simulink/slref/simulink.importexternalctypes.html) | Generate Simulink representations of custom data types defined by C or C++ code  
[Simulink.NumericType](https://uk.mathworks.com/help/simulink/slref/simulink.numerictype.html) | Specify floating-point, integer, or fixed-point data type  
[stringtype](https://uk.mathworks.com/help/simulink/slref/stringtype.html) | Create string data type  
[tunablevars2parameterobjects](https://uk.mathworks.com/help/simulink/slref/tunablevars2parameterobjects.html) | Create Simulink parameter objects from tunable parameters  
#### Model, Block, and Port Callbacks
Name|Description
---|---
[getCallbackAnnotation](https://uk.mathworks.com/help/simulink/slref/getcallbackannotation.html) | Get annotation executing callback  
[Simulink.Annotation](https://uk.mathworks.com/help/simulink/slref/simulink.annotation.html) | Create and specify properties of text, image, and area annotations  
#### Model Configuration Sets
Name|Description
---|---
[attachConfigSet](https://uk.mathworks.com/help/simulink/slref/attachconfigset.html) | Associate configuration set or configuration reference with model  
[attachConfigSetCopy](https://uk.mathworks.com/help/simulink/slref/attachconfigsetcopy.html) | Copy configuration set or configuration reference and associate it with model  
[configset.reference.getOverriddenParameters](https://uk.mathworks.com/help/simulink/slref/configset.reference.getoverriddenparameters.html) | Parameters that are overridden in a configuration reference _(Since R2021a)_  
[configset.reference.hasOverriddenParameters](https://uk.mathworks.com/help/simulink/slref/configset.reference.hasoverriddenparameters.html) | Determine if model configuration reference has overridden parameters _(Since R2021a)_  
[configset.reference.isParameterOverridden](https://uk.mathworks.com/help/simulink/slref/configset.reference.isparameteroverridden.html) | Determine if parameter is overridden in configuration reference of model _(Since R2021a)_  
[configset.reference.overrideParameter](https://uk.mathworks.com/help/simulink/slref/configset.reference.overrideparameter.html) | Change value of parameter in configuration reference _(Since R2021a)_  
[configset.reference.restoreAllOverriddenParameters](https://uk.mathworks.com/help/simulink/slref/configset.reference.restorealloverriddenparameters.html) | Restore all overridden parameters in configuration reference of model _(Since R2021a)_  
[configset.reference.restoreOverriddenParameter](https://uk.mathworks.com/help/simulink/slref/configset.reference.restoreoverriddenparameter.html) | Restore overridden parameter in configuration reference of model _(Since R2021a)_  
[detachConfigSet](https://uk.mathworks.com/help/simulink/slref/detachconfigset.html) | Dissociate configuration set or configuration reference from model  
[get_param](https://uk.mathworks.com/help/simulink/slref/get_param.html) | Get parameter names and values  
[getActiveConfigSet](https://uk.mathworks.com/help/simulink/slref/getactiveconfigset.html) | Get active configuration set or configuration reference of model  
[getConfigSet](https://uk.mathworks.com/help/simulink/slref/getconfigset.html) | Get configuration set or configuration reference from model  
[getConfigSets](https://uk.mathworks.com/help/simulink/slref/getconfigsets.html) | Get names of all of model's configuration sets or configuration references  
[getRefConfigSet](https://uk.mathworks.com/help/simulink/slref/simulink.configsetref.getrefconfigset.html) | Get configuration set from configuration reference  
[set_param](https://uk.mathworks.com/help/simulink/slref/set_param.html) | Set Simulink parameter value  
[setActiveConfigSet](https://uk.mathworks.com/help/simulink/slref/setactiveconfigset.html) | Specify active configuration set or configuration reference for model  
[Simulink.BlockDiagram.loadActiveConfigSet](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.loadactiveconfigset.html) | Load, associate, and activate configuration set with model  
[Simulink.BlockDiagram.propagateConfigSet](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.propagateconfigset.html) | Propagate top model configuration reference to referenced models  
[Simulink.BlockDiagram.restoreConfigSet](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.restoreconfigset.html) | Restore model configuration for converted models  
[Simulink.BlockDiagram.saveActiveConfigSet](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.saveactiveconfigset.html) | Save active configuration set of model  
[Simulink.ConfigSet](https://uk.mathworks.com/help/simulink/slref/simulink.configset.html) | Model configuration set  
[Simulink.ConfigSetRef](https://uk.mathworks.com/help/simulink/slref/simulink.configsetref.html) | Link model to freestanding configuration set  
### Analyze and Remodel Design
#### Run Model Advisor Checks
Name|Description
---|---
[modeladvisor](https://uk.mathworks.com/help/simulink/slref/modeladvisor.html) | Open Model Advisor  
[ModelAdvisor.Preferences](https://uk.mathworks.com/help/simulink/slref/modeladvisor.preferences-class.html) | Set Model Advisor window preferences by specifying which folders and tabs to display  
[Simulink.ModelAdvisor](https://uk.mathworks.com/help/simulink/slref/simulink.modeladvisor.html) |  Run Model Advisor from MATLAB file  
#### Configure and View Diagnostics
Name|Description
---|---
[Simulink.getSuppressedDiagnostics](https://uk.mathworks.com/help/simulink/slref/simulink.getsuppresseddiagnostics.html) |  Return `Simulink.SuppressedDiagnostic` objects associated with a block, subsystem, or model  
[Simulink.restoreDiagnostic](https://uk.mathworks.com/help/simulink/slref/simulink.restorediagnostic.html) | Restore diagnostic warnings to a specific block, subsystem, or model   
[Simulink.suppressDiagnostic](https://uk.mathworks.com/help/simulink/slref/simulink.suppressdiagnostic.html) | Suppress a diagnostic from a specific block  
[Simulink.SuppressedDiagnostic](https://uk.mathworks.com/help/simulink/slref/simulink.suppresseddiagnostic-class.html) | Suppress diagnostic messages from specific block  
[sldiagnostics](https://uk.mathworks.com/help/simulink/slref/sldiagnostics.html) | Display diagnostic information of Simulink system  
#### Transform Models
Name|Description
---|---
[dlinmod](https://uk.mathworks.com/help/simulink/slref/dlinmod.html) | Extract discrete-time linear state-space model around operating point  
[findop](https://uk.mathworks.com/help/slcontrol/ug/findop.html) | Steady-state operating point from specifications (trimming) or simulation  
[fixdt](https://uk.mathworks.com/help/simulink/slref/simulink.numerictype.fixdt.html) | Create `Simulink.NumericType` object describing a fixed-point or floating-point data type  
[fixpt_evenspace_cleanup](https://uk.mathworks.com/help/simulink/slref/fixpt_evenspace_cleanup.html) | Modify breakpoints of lookup table to have even spacing  
[fixpt_look1_func_approx](https://uk.mathworks.com/help/simulink/slref/fixpt_look1_func_approx.html) | Optimize fixed-point approximation of nonlinear function by interpolating lookup table data points  
[fixpt_look1_func_plot](https://uk.mathworks.com/help/simulink/slref/fixpt_look1_func_plot.html) | Plot fixed-point approximation function for lookup table  
[fixpt_set_all](https://uk.mathworks.com/help/simulink/slref/fixpt_set_all.html) | Set property for each fixed-point block in subsystem  
[fixptbestexp](https://uk.mathworks.com/help/simulink/slref/fixptbestexp.html) | Exponent that gives best precision for fixed-point representation of value  
[fixptbestprec](https://uk.mathworks.com/help/simulink/slref/fixptbestprec.html) | Determine maximum precision available for fixed-point representation of value  
[linearize](https://uk.mathworks.com/help/slcontrol/ug/linearize.html) | Linear approximation of Simulink model or subsystem  
[linmod](https://uk.mathworks.com/help/simulink/slref/linmod.html) | Extract continuous-time linear state-space model around operating point using block by block linearization algorithm  
[linmod2](https://uk.mathworks.com/help/simulink/slref/linmod2.html) | Extract continuous-time linear state-space model around operating point using algorithm that reduces truncation error  
[linmodv5](https://uk.mathworks.com/help/simulink/slref/linmodv5.html) | Extract continuous-time linear state-space model around operating point using full model perturbation algorithm  
[sldiscmdl](https://uk.mathworks.com/help/simulink/slref/sldiscmdl.html) | Discretize model that contains continuous blocks  
[slLinearizer](https://uk.mathworks.com/help/slcontrol/ug/sllinearizer.html) | Interface for batch linearization of Simulink models  
[slmdldiscui](https://uk.mathworks.com/help/simulink/slref/slmdldiscui.html) | Open Model Discretizer GUI  
[trim](https://uk.mathworks.com/help/simulink/slref/trim.html) | Find trim point of dynamic system  
### Test Model Components
Name|Description
---|---
[polyspaceArtifact](https://uk.mathworks.com/help/simulink/slref/polyspaceartifact.html) | Generate artifacts to run Polyspace analysis on code generated from Simulink model _(Since R2024a)_  
[polyspacePackNGo](https://uk.mathworks.com/help/simulink/slref/polyspacepackngo.html) | Generate and package options files to run Polyspace analysis on code generated from Simulink model  
[pslinkoptions](https://uk.mathworks.com/help/simulink/slref/pslinkoptions.html) | Create an options object to customize Polyspace analysis of generated code or custom code in Simulink model  
## Simulation
### Prepare Model Inputs and Outputs
#### Create Signal Data for Simulation
Name|Description
---|---
[signalbuilder](https://uk.mathworks.com/help/simulink/slref/signalbuilder_cmd.html) | (Not recommended) Create and access Signal Builder blocks  
[signalBuilderToSignalEditor](https://uk.mathworks.com/help/simulink/slref/signalbuildertosignaleditor.html) | Import signal data and properties from Signal Builder block to Signal Editor block  
[Simulink.io.BaseWorkspace](https://uk.mathworks.com/help/simulink/slref/simulink.io.baseworkspace-class.html) | Read data in format used by base workspace _(Since R2021a)_  
[Simulink.io.FileType](https://uk.mathworks.com/help/simulink/slref/simulink.io.filetype-class.html) | Base class for file type readers for Simulink interfaces such as Signal Editor  
[Simulink.io.getFileTypeDiagnostics](https://uk.mathworks.com/help/simulink/slref/simulink.io.getfiletypediagnostics.html) | Return structure with `NamespaceErrors` field for `Simulink.io.FileType` objects _(Since R2021a)_  
[Simulink.io.MatFile](https://uk.mathworks.com/help/simulink/slref/simulink.io.matfile-class.html) | Read data in MAT file format _(Since R2021a)_  
[Simulink.io.MDF](https://uk.mathworks.com/help/simulink/slref/simulink.io.mdf-class.html) | Read data in MDF-file format _(Since R2023b)_  
[Simulink.io.ModelWorkspace](https://uk.mathworks.com/help/simulink/slref/simulink.io.modelworkspace-class.html) | Read data in format used by model workspace _(Since R2021b)_  
[Simulink.io.PluggableNamespace](https://uk.mathworks.com/help/simulink/slref/simulink.io.pluggablenamespace-class.html) | Register `Simulink.io.FileType` objects from different name space _(Since R2021a)_  
[Simulink.io.SignalBuilderSpreadsheet](https://uk.mathworks.com/help/simulink/slref/simulink.io.signalbuilderspreadsheet-class.html) | Read spreadsheet in format used by Signal Builder  
[Simulink.io.SLDVMatFile](https://uk.mathworks.com/help/simulink/slref/simulink.io.sldvmatfile-class.html) | Read Simulink Design Verifier format data in MAT file _(Since R2022a)_  
#### Load Signal Data for Simulation
Name|Description
---|---
[convertToSLDataset](https://uk.mathworks.com/help/simulink/slref/converttosldataset.html) | Convert contents of MAT file to `Simulink.SimulationData.Dataset` object in another MAT file  
[createInputDataset](https://uk.mathworks.com/help/simulink/slref/createinputdataset.html) | Generate dataset object for root-level Inport or bus element ports in model  
[getInputString](https://uk.mathworks.com/help/simulink/slref/getinputstring.html) | Create comma-separated list of variables to map  
[getRootInportMap](https://uk.mathworks.com/help/simulink/slref/getrootinportmap.html) | Create custom object to map signals to top-level input ports  
[getSlRootInportMap](https://uk.mathworks.com/help/simulink/slref/getslrootinportmap.html) | Create custom object to map signals to root-level inports using Simulink mapping mode  
[getSupportedFileTypes](https://uk.mathworks.com/help/simulink/slref/getsupportedfiletypes.html) | Return file type of signals in spreadsheet file _(Since R2024b)_  
[loadScenarioToWorkspace](https://uk.mathworks.com/help/simulink/slref/loadscenariotoworkspace.html) | Load scenario to base workspace _(Since R2024b)_  
[mapDataToInport](https://uk.mathworks.com/help/simulink/slref/mapdatatoinport.html) | Map data to root input ports _(Since R2024b)_  
[matlab.io.datastore.SimulationDatastore](https://uk.mathworks.com/help/simulink/slref/matlab.io.datastore.simulationdatastore.html) | Datastore for inputs and outputs of Simulink models  
[signalBuilderToSignalEditor](https://uk.mathworks.com/help/simulink/slref/signalbuildertosignaleditor.html) | Import signal data and properties from Signal Builder block to Signal Editor block  
[Simulink.Bus.createMATLABStruct](https://uk.mathworks.com/help/simulink/slref/simulink.bus.creatematlabstruct.html) | Create MATLAB structures that use same hierarchy and attributes as buses  
[Simulink.playback.createSignals](https://uk.mathworks.com/help/simulink/slref/simulink.playback.createsignals.html) | Create `Simulink.playback.Signal` object to add to Playback block _(Since R2024a)_  
[Simulink.playback.Signal](https://uk.mathworks.com/help/simulink/slref/simulink.playback.signal.html) | Container for signals to add to Playback block _(Since R2024a)_  
[Simulink.SimulationData.createStructOfTimeseries](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.createstructoftimeseries.html) | Create structure of `timeseries` data to load as simulation input for bus  
[Simulink.SimulationData.Dataset](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.dataset.html) | Access logged simulation data or group simulation input data  
[Simulink.SimulationData.DatasetRef](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.datasetref.html) | Create `Simulink.SimulationData.DatasetRef` object  
#### Save Run-Time Data from Simulation
Name|Description
---|---
[extractTimetable](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.dataset.extracttimetable.html) | Extract data from `Simulink.SimulationData.Dataset` or `Simulink.SimulationData.Signal` objects into timetables _(Since R2021b)_  
[findSignal](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.modellogginginfo.findsignal.html) | Find index of signals in `Signals` property vector  
[getAsDatastore](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.datasetref.getasdatastore.html) | Get `matlab.io.datastore.SimulationDatastore` representation of element from referenced `Dataset` object  
[getLogAsSpecifiedInModel](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.modellogginginfo.getlogasspecifiedinmodel.html) | Determine whether model logs as specified in model or uses override settings  
[matlab.io.datastore.SimulationDatastore](https://uk.mathworks.com/help/simulink/slref/matlab.io.datastore.simulationdatastore.html) | Datastore for inputs and outputs of Simulink models  
[removeElement](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.dataset.removeelement.html) | Remove element from `Simulink.SimulationData.Dataset` object  
[setLogAsSpecifiedInModel](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.modellogginginfo.setlogasspecifiedinmodel.html) | Set logging mode for top model or top-level Model block  
[Simulink.sdi.getArchiveRunLimit](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getarchiverunlimit.html) | Get limit for number of runs to retain in Simulation Data Inspector archive  
[Simulink.sdi.getAutoArchiveMode](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getautoarchivemode.html) | Get Simulation Data Inspector run management mode  
[Simulink.sdi.getDeleteRunsOnLowSpace](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getdeleterunsonlowspace.html) | Get configured behavior when size of logged data approaches configured limits _(Since R2021a)_  
[Simulink.sdi.getMaxDiskUsage](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getmaxdiskusage.html) | Get configured maximum size for data logged to disk _(Since R2021a)_  
[Simulink.sdi.getRecordData](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getrecorddata.html) | Check record mode for logging _(Since R2021a)_  
[Simulink.sdi.getRequiredFreeSpace](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getrequiredfreespace.html) | Get configured minimum disk space requirement for logging _(Since R2021a)_  
[Simulink.sdi.getSignalInputProcessingMode](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getsignalinputprocessingmode.html) | Get value of Input Processing signal property  
[Simulink.sdi.getStorageLocation](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getstoragelocation.html) | Get path to custom storage location for data logged to disk _(Since R2021a)_  
[Simulink.sdi.getStorageMode](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getstoragemode.html) | Check if logging is configured to log data to disk or memory _(Since R2021a)_  
[Simulink.sdi.markSignalForStreaming](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.marksignalforstreaming.html) | Turn logging on or off for signal  
[Simulink.sdi.setArchiveRunLimit](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setarchiverunlimit.html) | Specify number of runs to retain in Simulation Data Inspector archive  
[Simulink.sdi.setAutoArchiveMode](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setautoarchivemode.html) | Specify how Simulation Data Inspector manages simulation runs  
[Simulink.sdi.setDeleteRunsOnLowSpace](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setdeleterunsonlowspace.html) | Specify behavior when logged data size approaches configured limits _(Since R2021a)_  
[Simulink.sdi.setMaxDiskUsage](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setmaxdiskusage.html) | Specify maximum size for data logged to disk _(Since R2021a)_  
[Simulink.sdi.setRecordData](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setrecorddata.html) | Specify record mode for logging _(Since R2021a)_  
[Simulink.sdi.setRequiredFreeSpace](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setrequiredfreespace.html) | Specify minimum disk space to leave free when logging data _(Since R2021a)_  
[Simulink.sdi.setSignalInputProcessingMode](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setsignalinputprocessingmode.html) | Specify value for Input Processing signal property  
[Simulink.sdi.setStorageLocation](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setstoragelocation.html) | Specify location for logged data on disk _(Since R2021a)_  
[Simulink.sdi.setStorageMode](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setstoragemode.html) | Specify whether to log data to disk or memory _(Since R2021a)_  
[Simulink.SimulationData.BlockPath](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.blockpath.html) | Fully specified block path  
[Simulink.SimulationData.createStructOfTimeseries](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.createstructoftimeseries.html) | Create structure of `timeseries` data to load as simulation input for bus  
[Simulink.SimulationData.Dataset](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.dataset.html) | Access logged simulation data or group simulation input data  
[Simulink.SimulationData.DatasetRef](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.datasetref.html) | Create `Simulink.SimulationData.DatasetRef` object  
[Simulink.SimulationData.DatasetRef.getDatasetVariableNames](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.datasetref.getdatasetvariablenames.html) | List names of variables in MAT file that contain `Simulink.SimulationData.Dataset` objects  
[Simulink.SimulationData.forEachTimeseries](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.foreachtimeseries.html) | Apply function to data contained in set of `timeseries` objects  
[Simulink.SimulationData.LoggingInfo](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.logginginfo.html) | Signal logging override settings  
[Simulink.SimulationData.ModelLoggingInfo](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.modellogginginfo.html) | Signal logging override settings for model  
[Simulink.SimulationData.ModelLoggingInfo.createFromModel](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.modellogginginfo.createfrommodel.html) | Create `Simulink.SimulationData.ModelLoggingInfo` object for top model with override settings for each logged signal in model  
[Simulink.SimulationData.Signal](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.signal.html) | Container for signal logging information  
[Simulink.SimulationData.SignalLoggingInfo](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.signallogginginfo.html) | Signal logging override settings for signal  
[Simulink.SimulationData.State](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.state.html) | Container for state logging information  
[Simulink.SimulationData.Unit](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.unit.html) | Container for units for simulation data  
[Simulink.SimulationMetadata](https://uk.mathworks.com/help/simulink/slref/simulink.simulationmetadata.html) | Information about model, environment, execution, and timing of simulation  
[Simulink.SimulationOutput](https://uk.mathworks.com/help/simulink/slref/simulink.simulationoutput.html) | Access simulation outputs and metadata  
[verifySignalAndModelPaths](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.modellogginginfo.verifysignalandmodelpaths.html) | Verify paths in `Simulink.SimulationData.ModelLoggingInfo` object  
### Configure Simulation Conditions
Name|Description
---|---
[closeDialog](https://uk.mathworks.com/help/simulink/slref/closedialog.html) | Close configuration parameters dialog  
[openDialog](https://uk.mathworks.com/help/simulink/slref/opendialog.html) | Open configuration parameters dialog  
[Simulink.BlockDiagram.getAlgebraicLoops](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.getalgebraicloops.html) | Identify and analyze algebraic loops in a model  
[solverprofiler.profileModel](https://uk.mathworks.com/help/simulink/slref/solverprofiler.profilemodel.html) | Programmatically analyze solver performance for model using Solver Profiler  
### Run Simulations
#### Run Individual Simulations
Name|Description
---|---
[find](https://uk.mathworks.com/help/simulink/slref/simulink.simulationoutput.find.html) | Query and access properties on `Simulink.SimulationOutput` object  
[get](https://uk.mathworks.com/help/simulink/slref/simulink.op.modeloperatingpoint.get.html) |  Get operating point information for Stateflow chart, MATLAB System block, or S-function  
[get](https://uk.mathworks.com/help/simulink/slref/simulink.simulationoutput.get.html) | Access simulation results in `Simulink.SimulationOutput` object  
[get_param](https://uk.mathworks.com/help/simulink/slref/get_param.html) | Get parameter names and values  
[getVariantConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.getvariantconfiguration.html) | Get name of variant configuration from `SimulationInput` object _(Since R2024a)_  
[initialize](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.initialize.html) | Initialize simulation represented by `Simulation` object _(Since R2024a)_  
[pause](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.pause.html) | Pause active simulation represented by `Simulation` object _(Since R2024a)_  
[removeProperty](https://uk.mathworks.com/help/simulink/slref/simulink.simulationoutput.removeproperty.html) | Remove property from `Simulink.SimulationOutput` object  
[resume](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.resume.html) | Continue paused simulation represented by `Simulation` object _(Since R2024a)_  
[set](https://uk.mathworks.com/help/simulink/slref/simulink.op.modeloperatingpoint.set.html) | Set operating point information for Stateflow chart, MATLAB System block, or S-function  
[set_param](https://uk.mathworks.com/help/simulink/slref/set_param.html) | Set Simulink parameter value  
[setBlockParameter](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setblockparameter.html) | Set block parameter values for simulation using `SimulationInput` or `Simulation` object  
[setExternalInput](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setexternalinput.html) | Specify external input data for top-level input ports using `SimulationInput` or `Simulation` object  
[setInitialState](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setinitialstate.html) | Specify initial state for simulation using `SimulationInput` or `Simulation` object  
[setModelParameter](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setmodelparameter.html) | Set model parameter values for simulation using `SimulationInput` or `Simulation` object  
[setPostSimFcn](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setpostsimfcn.html) |  Set MATLAB function to run after each simulation  
[setPreSimFcn](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setpresimfcn.html) | Specify MATLAB function to run before start of each simulation on `Simulink.SimulationInput` object  
[setUserData](https://uk.mathworks.com/help/simulink/slref/simulink.simulationoutput.setuserdata.html) | Add data to metadata in `Simulink.SimulationOutput` object  
[setUserString](https://uk.mathworks.com/help/simulink/slref/simulink.simulationoutput.setuserstring.html) | Add string to metadata in `Simulink.SimulationOutput` object  
[setVariable](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setvariable.html) | Set variable values for simulation using `SimulationInput` or `Simulation` object  
[setVariantConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setvariantconfiguration.html) | Set variant configuration for simulation using `SimulationInput` object _(Since R2024a)_  
[sim](https://uk.mathworks.com/help/simulink/slref/sim.html) | Run and script programmatic simulations of Simulink models  
[Simulation](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.html) | Control simulation execution and tune variable, block parameter, and model parameter values _(Since R2024a)_  
[Simulink.BlockDiagram.getInitialState](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.getinitialstate.html) | Get initial state data from block diagram  
[Simulink.op.ModelOperatingPoint](https://uk.mathworks.com/help/simulink/slref/simulink.op.modeloperatingpoint.html) | Complete information that represents model operating point in simulation  
[Simulink.SimulationInput](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.html) | Create `Simulink.SimulationInput` objects to make changes to model for multiple or individual simulations  
[Simulink.SimulationMetadata](https://uk.mathworks.com/help/simulink/slref/simulink.simulationmetadata.html) | Information about model, environment, execution, and timing of simulation  
[Simulink.SimulationOutput](https://uk.mathworks.com/help/simulink/slref/simulink.simulationoutput.html) | Access simulation outputs and metadata  
[slsim.allowedModelChanges](https://uk.mathworks.com/help/simulink/slref/slsim.allowedmodelchanges.html) | Determine changes you can make to model based on simulation status _(Since R2022b)_  
[start](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.start.html) | Start simulation represented by `Simulation` object _(Since R2024a)_  
[step](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.step.html) | Advance simulation represented by `Simulation` object by specified amount _(Since R2024a)_  
[stop](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.stop.html) | Stop simulation represented by `Simulation` object _(Since R2024a)_  
[terminate](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.terminate.html) | Terminate simulation represented by `Simulation` object _(Since R2024a)_  
[who](https://uk.mathworks.com/help/simulink/slref/simulink.simulationoutput.who.html) | Get names of editable properties on `Simulink.SimulationOutput` object  
#### Run Multiple Simulations
Name|Description
---|---
[applyToModel](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.applytomodel.html) | Apply configuration in `SimulationInput` object to model  
[batchsim](https://uk.mathworks.com/help/simulink/slref/batchsim.html) | Offload simulations to run on a compute cluster  
[getSimulationJobs](https://uk.mathworks.com/help/simulink/slref/getsimulationjobs.html) | Get all `Simulink.Simulation.Job` objects from cluster  
[getVariantConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.getvariantconfiguration.html) | Get name of variant configuration from `SimulationInput` object _(Since R2024a)_  
[loadVariablesFromExternalSource](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.loadvariablesfromexternalsource.html) | Load variables from a custom file into `Simulink.SimulationInput` object _(Since R2022b)_  
[loadVariablesFromMATFile](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.loadvariablesfrommatfile.html) | Load variables from MAT file into `Simulink.SimulationInput` object  
[parsim](https://uk.mathworks.com/help/simulink/slref/parsim.html) | Simulate dynamic system multiple times in parallel or serial  
[setBlockParameter](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setblockparameter.html) | Set block parameter values for simulation using `SimulationInput` or `Simulation` object  
[setExternalInput](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setexternalinput.html) | Specify external input data for top-level input ports using `SimulationInput` or `Simulation` object  
[setInitialState](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setinitialstate.html) | Specify initial state for simulation using `SimulationInput` or `Simulation` object  
[setModelParameter](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setmodelparameter.html) | Set model parameter values for simulation using `SimulationInput` or `Simulation` object  
[setPostSimFcn](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setpostsimfcn.html) |  Set MATLAB function to run after each simulation  
[setPreSimFcn](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setpresimfcn.html) | Specify MATLAB function to run before start of each simulation on `Simulink.SimulationInput` object  
[setVariable](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setvariable.html) | Set variable values for simulation using `SimulationInput` or `Simulation` object  
[setVariantConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setvariantconfiguration.html) | Set variant configuration for simulation using `SimulationInput` object _(Since R2024a)_  
[showContents](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.showcontents.html) | View summary of specification in `SimulationInput` or `Simulation` object  
[simulink.multisim.BlockParameter](https://uk.mathworks.com/help/simulink/slref/simulink.multisim.blockparameter.html) | Specify a range of block parameters _(Since R2024a)_  
[simulink.multisim.DesignStudy](https://uk.mathworks.com/help/simulink/slref/simulink.multisim.designstudy.html) | Create design study for multiple simulations _(Since R2024a)_  
[simulink.multisim.Exhaustive](https://uk.mathworks.com/help/simulink/slref/simulink.multisim.exhaustive.html) | Create an exhaustive parameter combination for specified parameter values _(Since R2024a)_  
[simulink.multisim.ExternalInput](https://uk.mathworks.com/help/simulink/slref/simulink.multisim.externalinput.html) | Specify a range of external inputs _(Since R2024a)_  
[simulink.multisim.ModelParameter](https://uk.mathworks.com/help/simulink/slref/simulink.multisim.modelparameter.html) | Specify a range of values for model parameters _(Since R2024a)_  
[simulink.multisim.MultisimDatastore](https://uk.mathworks.com/help/simulink/slref/simulink.multisim.multisimdatastore.html) | Create datastore for post-processing large-scale simulation results _(Since R2025a)_  
[simulink.multisim.Sequential](https://uk.mathworks.com/help/simulink/slref/simulink.multisim.sequential.html) | Create a sequential parameter combination for specified parameter values _(Since R2024a)_  
[simulink.multisim.Variable](https://uk.mathworks.com/help/simulink/slref/simulink.multisim.variable.html) | Specify a range of values for model variables _(Since R2024a)_  
[Simulink.Simulation.BlockParameter](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.blockparameter-class.html) | Block parameters in `Simulink.SimulationInput` objects  
[Simulink.Simulation.Future](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.future-class.html) |  Create `Future` object for simulation  
[Simulink.Simulation.Job](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.job-class.html) |  `Simulink.Simulation.Job` object for batch simulations  
[Simulink.Simulation.Variable](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.variable-class.html) | Variables in `Simulink.SimulationInput` objects  
[Simulink.SimulationInput](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.html) | Create `Simulink.SimulationInput` objects to make changes to model for multiple or individual simulations  
[validate](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.validate.html) | Validate contents of `SimulationInput` object  
### View and Analyze Simulation Results
#### Control Simulations with Interactive Dashboards
Name|Description
---|---
[Simulink.HMI.InstrumentedSignals](https://uk.mathworks.com/help/simulink/slref/simulink.hmi.instrumentedsignals.html) | Save and restore signal logging specification  
[Simulink.HMI.ParamSourceInfo](https://uk.mathworks.com/help/simulink/slref/simulink.hmi.paramsourceinfo.html) | Information about Dashboard block variable and parameter connections  
[Simulink.HMI.SignalSpecification](https://uk.mathworks.com/help/simulink/slref/simulink.hmi.signalspecification.html) | Programmatically connect a Dashboard block to a signal  
[Simulink.SimulationData.Parameter](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.parameter.html) | Stores logged parameter data and metadata  
#### View Data During Simulation
Name|Description
---|---
[TimeScopeConfiguration](https://uk.mathworks.com/help/simulink/slref/spbscopes.scope.timescopeconfiguration.html) | Control Scope block appearance and behavior  
#### Create Apps to Control Simulations
Name|Description
---|---
[bind](https://uk.mathworks.com/help/simulink/slref/bind.html) | Connect app components to simulation signals and variables _(Since R2024a)_  
[Binding](https://uk.mathworks.com/help/simulink/slref/matlab.lang.binding.html) | Connection between app components and simulation signals and variables _(Since R2024a)_  
[findbindings](https://uk.mathworks.com/help/simulink/slref/findbindings.html) | Find bindings between objects _(Since R2024a)_  
[initialize](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.initialize.html) | Initialize simulation represented by `Simulation` object _(Since R2024a)_  
[pause](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.pause.html) | Pause active simulation represented by `Simulation` object _(Since R2024a)_  
[resume](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.resume.html) | Continue paused simulation represented by `Simulation` object _(Since R2024a)_  
[setBlockParameter](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setblockparameter.html) | Set block parameter values for simulation using `SimulationInput` or `Simulation` object  
[setExternalInput](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setexternalinput.html) | Specify external input data for top-level input ports using `SimulationInput` or `Simulation` object  
[setInitialState](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setinitialstate.html) | Specify initial state for simulation using `SimulationInput` or `Simulation` object  
[setModelParameter](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setmodelparameter.html) | Set model parameter values for simulation using `SimulationInput` or `Simulation` object  
[setVariable](https://uk.mathworks.com/help/simulink/slref/simulink.simulationinput.setvariable.html) | Set variable values for simulation using `SimulationInput` or `Simulation` object  
[Simulation](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.html) | Control simulation execution and tune variable, block parameter, and model parameter values _(Since R2024a)_  
[start](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.start.html) | Start simulation represented by `Simulation` object _(Since R2024a)_  
[step](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.step.html) | Advance simulation represented by `Simulation` object by specified amount _(Since R2024a)_  
[stop](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.stop.html) | Stop simulation represented by `Simulation` object _(Since R2024a)_  
[terminate](https://uk.mathworks.com/help/simulink/slref/simulink.simulation.terminate.html) | Terminate simulation represented by `Simulation` object _(Since R2024a)_  
[uisimcontrols](https://uk.mathworks.com/help/simulink/slref/uisimcontrols.html) | Create simulation controls in app _(Since R2024a)_  
[uisimdatabutton](https://uk.mathworks.com/help/simulink/slref/uisimdatabutton.html) | Create buttons to save or load simulation data in app _(Since R2024a)_  
[uisimprogress](https://uk.mathworks.com/help/simulink/slref/uisimprogress.html) | Display simulation progress bar in app _(Since R2024a)_  
[uisimvartuner](https://uk.mathworks.com/help/simulink/slref/uisimvartuner.html) | Create a model variable tuner UI component in an app _(Since R2024a)_  
[uitimescope](https://uk.mathworks.com/help/simulink/slref/uitimescope.html) | Display time-domain signals in app _(Since R2024a)_  
#### Analyze Simulation Results
Name|Description
---|---
[add](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.add.html) | Import data into existing run in Simulation Data Inspector using `Simulink.sdi.Run` object  
[collapse](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.collapse.html) | Represent multidimensional signal as a single signal with nonscalar sample values _(Since R2021b)_  
[convertDataType](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.convertdatatype.html) | Convert data type for signal in Simulation Data Inspector _(Since R2022a)_  
[convertToFrames](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.converttoframes.html) | Remove buffering from frames of frame-based signal _(Since R2021b)_  
[convertUnits](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.convertunits.html) |  Convert units of `Simulink.sdi.Signal` object  
[expand](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.expand.html) | Represent multidimensional signal as group of signals with scalar sample values _(Since R2021b)_  
[export](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.export.html) |  Export data for signal in Simulation Data Inspector to workspace or file  
[getAllSignalIDs](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.getallsignalids.html) | Get all signal IDs for signals in `Simulink.sdi.Run` object  
[getAllSignals](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.getallsignals.html) | Get all signals in `Simulink.sdi.Run` object  
[getAsTall](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.getastall.html) |  Create tall timetable from `Simulink.sdi.Signal` object  
[getDatasetRef](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.getdatasetref.html) | Create a `Simulink.sdi.DatasetRef` object for a run  
[getResultByIndex](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.diffrunresult.getresultbyindex.html) | Return signal comparison result  
[getResultsByName](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.diffrunresult.getresultsbyname.html) | Return signal comparison results based on signal name _(Since R2022b)_  
[getSignalByIndex](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.getsignalbyindex.html) | Get signal in `Simulink.sdi.Run` object by index  
[getSignalIDByIndex](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.getsignalidbyindex.html) | Get signal ID for signal at specified index in `Simulink.sdi.Run` object  
[getSignalIDsByName](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.getsignalidsbyname.html) | Get signal IDs for signals inside `Simulink.sdi.Run` object using signal name  
[getSignalsByName](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.getsignalsbyname.html) | Access signals in a `Simulink.sdi.Run` object using signal name  
[io.reader](https://uk.mathworks.com/help/simulink/slref/io.reader-class.html) | Base class used to define custom variable or file reader for Simulation Data Inspector  
[isValidSignalID](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.isvalidsignalid.html) | Check whether signal ID corresponds to signal in `Simulink.sdi.Run` object  
[loadIntoMemory](https://uk.mathworks.com/help/simulink/slref/loadintomemory.html) | Load logged data into memory  
[matlab.io.datastore.sdidatastore](https://uk.mathworks.com/help/simulink/slref/matlab.io.datastore.sdidatastore.html) |  Datastore for Simulation Data Inspector signals  
[plotOnSubPlot](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.plotonsubplot.html) |  Plot `Simulink.sdi.Signal` object on Simulation Data Inspector subplot  
[saveResult](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.diffrunresult.saveresult.html) | Save comparison results to an MLDATX file  
[Simulink.HMI.InstrumentedSignals](https://uk.mathworks.com/help/simulink/slref/simulink.hmi.instrumentedsignals.html) | Save and restore signal logging specification  
[Simulink.HMI.SignalSpecification](https://uk.mathworks.com/help/simulink/slref/simulink.hmi.signalspecification.html) | Programmatically connect a Dashboard block to a signal  
[Simulink.sdi.addToRun](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.addtorun.html) | Import data into existing run in Simulation Data Inspector using run ID  
[Simulink.sdi.addTrigger](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.addtrigger.html) | Add trigger to signal to control display updates in the Simulation Data Inspector  
[Simulink.sdi.cleanupWorkerResources](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.cleanupworkerresources.html) | Clean up worker repositories  
[Simulink.sdi.clear](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.clear.html) | Clear all data from the Simulation Data Inspector  
[Simulink.sdi.clearAllSubPlots](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.clearallsubplots.html) | Clear plotted signals from all subplots in the Simulation Data Inspector  
[Simulink.sdi.clearPreferences](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.clearpreferences.html) | Restore Simulation Data Inspector preferences to default settings  
[Simulink.sdi.clearSubPlot](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.clearsubplot.html) | Clear plotted signals from single subplot in Simulation Data Inspector _(Since R2024b)_  
[Simulink.sdi.close](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.close.html) | Close the Simulation Data Inspector  
[Simulink.sdi.compareRuns](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.compareruns.html) | Compare data in two simulation runs  
[Simulink.sdi.compareSignals](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.comparesignals.html) | Compare data in two `Simulink.sdi.Signal` objects  
[Simulink.sdi.constraints.MatchesSignal](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.constraints.matchessignal-class.html) | Constraint that compares time series data with tolerances using the Simulation Data Inspector  
[Simulink.sdi.constraints.MatchesSignalOptions](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.constraints.matchessignaloptions-class.html) | Specify comparison options for `Simulink.sdi.MatchesSignal` constraint  
[Simulink.sdi.copyRun](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.copyrun.html) | Copy a Simulation Data Inspector run  
[Simulink.sdi.copyRunViewSettings](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.copyrunviewsettings.html) | Copy line style and color for signals from one run to another  
[Simulink.sdi.createRun](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.createrun.html) | Import data into new run in Simulation Data Inspector and return run ID  
[Simulink.sdi.createRunOrAddToStreamedRun](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.createrunoraddtostreamedrun.html) | Create a single run for all simulation outputs  
[Simulink.sdi.CustomSnapshot](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.customsnapshot.html) |  Specify settings for snapshot without opening or affecting the Simulation Data Inspector  
[Simulink.sdi.DatasetRef](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.datasetref.html) | Access data in Simulation Data Inspector repository  
[Simulink.sdi.deleteRun](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.deleterun.html) | Delete a run from the Simulation Data Inspector repository  
[Simulink.sdi.deleteSignal](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.deletesignal.html) | Delete signal in the Simulation Data Inspector  
[Simulink.sdi.DiffRunResult](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.diffrunresult.html) | Access run comparison results  
[Simulink.sdi.DiffRunResult.getLatest](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.diffrunresult.getlatest.html) | Access results from most recent comparison  
[Simulink.sdi.DiffSignalResult](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.diffsignalresult.html) | Access signal comparison results  
[Simulink.sdi.enablePCTSupport](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.enablepctsupport.html) | Control when to import data from parallel simulations into the Simulation Data Inspector  
[Simulink.sdi.getAllRunIDs](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getallrunids.html) | Get all Simulation Data Inspector run identifiers  
[Simulink.sdi.getAppendRunToTop](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getappendruntotop.html) | Get order in which Simulation Data Inspector appends run in work area or archive _(Since R2022b)_  
[Simulink.sdi.getArchiveRunLimit](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getarchiverunlimit.html) | Get limit for number of runs to retain in Simulation Data Inspector archive  
[Simulink.sdi.getAutoArchiveMode](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getautoarchivemode.html) | Get Simulation Data Inspector run management mode  
[Simulink.sdi.getAutoTimespan](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getautotimespan.html) | Get behavior of time span in Simulation Data Inspector _(Since R2022b)_  
[Simulink.sdi.getBorderOn](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getborderon.html) | Get border display setting for time plots  
[Simulink.sdi.getComparisonColor](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getcomparisoncolor.html) | Get line color in comparison plot _(Since R2021b)_  
[Simulink.sdi.getCurrentComparison](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getcurrentcomparison.html) | Access results from most recent comparison  
[Simulink.sdi.getCurrentSimulationRun](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getcurrentsimulationrun.html) | Access data for in-progress or most recently completed simulation  
[Simulink.sdi.getCursorOptions](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getcursoroptions.html) | Get current shading options for cursors in Simulation Data Inspector _(Since R2024a)_  
[Simulink.sdi.getCursorPositions](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getcursorpositions.html) | Get position for active cursors in the Simulation Data Inspector _(Since R2021a)_  
[Simulink.sdi.getGridOn](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getgridon.html) | Determine grid configuration for time plots  
[Simulink.sdi.getLegendPosition](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getlegendposition.html) | Get legend position in Simulation Data Inspector _(Since R2023b)_  
[Simulink.sdi.getMarkersOn](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getmarkerson.html) | Determine if data markers are shown in the Simulation Data Inspector  
[Simulink.sdi.getNumCursors](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getnumcursors.html) | Check number of cursors active in the Simulation Data Inspector _(Since R2021a)_  
[Simulink.sdi.getPosition](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getposition.html) | Get position and size of Simulation Data Inspector _(Since R2022b)_  
[Simulink.sdi.getRecordData](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getrecorddata.html) | Check record mode for logging _(Since R2021a)_  
[Simulink.sdi.getRun](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getrun.html) | Access data for a Simulation Data Inspector run  
[Simulink.sdi.getRunCount](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getruncount.html) | Get number of runs in Simulation Data Inspector repository  
[Simulink.sdi.getRunIDByIndex](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getrunidbyindex.html) | Use Simulation Data Inspector run index to get run ID  
[Simulink.sdi.getRunNamingRule](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getrunnamingrule.html) | Get the Simulation Data Inspector rule for naming runs  
[Simulink.sdi.getSignal](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getsignal.html) | Get Simulink.sdi.Signal object for a signal  
[Simulink.sdi.getSource](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getsource.html) | Get path of temporary file used to store Simulation Data Inspector data  
[Simulink.sdi.getSubPlotLayout](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getsubplotlayout.html) | Get subplot layout in Simulation Data Inspector _(Since R2023b)_  
[Simulink.sdi.getSubplotLimits](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getsubplotlimits.html) | Get _t_ - and _y_ -axis limits for time plot in the Simulation Data Inspector _(Since R2021a)_  
[Simulink.sdi.getTickLabelsDisplay](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getticklabelsdisplay.html) | Get tick mark label setting for time plots  
[Simulink.sdi.getTicksPosition](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getticksposition.html) | Get tick mark position setting for time plots  
[Simulink.sdi.getTrigger](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.gettrigger.html) | Get signal and trigger options for trigger configured in the Simulation Data Inspector  
[Simulink.sdi.getUnitSystem](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getunitsystem.html) | Get current unit system configured in Simulation Data Inspector preferences  
[Simulink.sdi.getVisualization](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getvisualization.html) | Get visualization type of subplot in Simulation Data Inspector _(Since R2024b)_  
[Simulink.sdi.isPCTSupportEnabled](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.ispctsupportenabled.html) | Determine status and mode for Parallel Computing Toolbox support  
[Simulink.sdi.isValidRunID](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.isvalidrunid.html) | Determine if run ID is valid  
[Simulink.sdi.isValidSignalID](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.isvalidsignalid.html) | Determine if signal ID is valid _(Since R2022b)_  
[Simulink.sdi.load](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.load.html) | Load a Simulation Data Inspector session or view  
[Simulink.sdi.loadView](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.loadview.html) | Load a view file to visualize data in the Simulation Data Inspector  
[Simulink.sdi.markSignalForStreaming](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.marksignalforstreaming.html) | Turn logging on or off for signal  
[Simulink.sdi.plot](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.plot.html) | Plot data in Simulation Data Inspector  
[Simulink.sdi.registerCursorCallback](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.registercursorcallback.html) | Register callback for cursor movements in the Simulation Data Inspector _(Since R2021a)_  
[Simulink.sdi.removeTrigger](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.removetrigger.html) | Remove trigger from signal in the Simulation Data Inspector  
[Simulink.sdi.resetRunNamingRule](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.resetrunnamingrule.html) | Revert the Simulation Data Inspector run naming rule to default  
[Simulink.sdi.Run](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.html) | Access run signals and metadata  
[Simulink.sdi.Run.create](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.create.html) | Import data into new run in Simulation Data Inspector and return `Simulink.sdi.Run` object  
[Simulink.sdi.Run.getLatest](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.getlatest.html) | Get the most recently created Simulation Data Inspector run  
[Simulink.sdi.saveView](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.saveview.html) | Save visualization settings to apply to other data  
[Simulink.sdi.sendWorkerRunToClient](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.sendworkerruntoclient.html) | Send run created on parallel workers to the Simulation Data Inspector  
[Simulink.sdi.setAppendRunToTop](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setappendruntotop.html) | Specify order in which Simulation Data Inspector appends new run in work area or archive _(Since R2022b)_  
[Simulink.sdi.setArchiveRunLimit](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setarchiverunlimit.html) | Specify number of runs to retain in Simulation Data Inspector archive  
[Simulink.sdi.setAutoArchiveMode](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setautoarchivemode.html) | Specify how Simulation Data Inspector manages simulation runs  
[Simulink.sdi.setAutoTimespan](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setautotimespan.html) | Specify behavior of time span in Simulation Data Inspector _(Since R2022b)_  
[Simulink.sdi.setBorderOn](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setborderon.html) | Display or hide border on time plots  
[Simulink.sdi.setComparisonColor](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setcomparisoncolor.html) | Set line color in comparison plot _(Since R2021b)_  
[Simulink.sdi.setCursorOptions](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setcursoroptions.html) | Configure shading options for cursors in Simulation Data Inspector  
[Simulink.sdi.setCursorPositions](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setcursorpositions.html) | Specify active cursor positions in the Simulation Data Inspector _(Since R2021a)_  
[Simulink.sdi.setGridOn](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setgridon.html) | Configure grid lines for time plots in the Simulation Data Inspector  
[Simulink.sdi.setLegendPosition](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setlegendposition.html) | Set legend position in Simulation Data Inspector _(Since R2023b)_  
[Simulink.sdi.setMarkersOn](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setmarkerson.html) | Show or hide markers for plotted signals  
[Simulink.sdi.setNumCursors](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setnumcursors.html) | Configure number of cursors active in Simulation Data Inspector _(Since R2021a)_  
[Simulink.sdi.setPosition](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setposition.html) | Set position and size of Simulation Data Inspector _(Since R2022b)_  
[Simulink.sdi.setRecordData](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setrecorddata.html) | Specify record mode for logging _(Since R2021a)_  
[Simulink.sdi.setRunNamingRule](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setrunnamingrule.html) | Specify the Simulation Data Inspector run naming rule  
[Simulink.sdi.setSubPlotLayout](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setsubplotlayout.html) | Set subplot layout in Simulation Data Inspector  
[Simulink.sdi.setSubplotLimits](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setsubplotlimits.html) | Specify subplot limits for time plots in the Simulation Data Inspector _(Since R2021a)_  
[Simulink.sdi.setTableGrouping](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.settablegrouping.html) | Change signal grouping hierarchy in Inspect pane  
[Simulink.sdi.setTickLabelsDisplay](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setticklabelsdisplay.html) | Configure tick label visibility for time plot axes  
[Simulink.sdi.setTicksPosition](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setticksposition.html) | Configure position for tick marks on time plots in the Simulation Data Inspector  
[Simulink.sdi.setUnitSystem](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setunitsystem.html) | Specify system of units to define signal display units in the Simulation Data Inspector  
[Simulink.sdi.setVisualization](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.setvisualization.html) | Set visualization type of subplot in Simulation Data Inspector _(Since R2024b)_  
[Simulink.sdi.Signal](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.html) |  Access signal data and metadata  
[Simulink.sdi.snapshot](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.snapshot.html) | Capture contents of Simulation Data Inspector plots  
[Simulink.sdi.unregisterCursorCallback](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.unregistercursorcallback.html) | Unregister cursor callback function _(Since R2021a)_  
[Simulink.sdi.useSignalColorForBaseline](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.usesignalcolorforbaseline.html) | Determine whether comparison plot uses baseline signal color and line style  
[Simulink.sdi.useSignalColorForCompareTo](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.usesignalcolorforcompareto.html) | Determine whether comparison plot uses comparison signal color and line style  
[Simulink.sdi.view](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.view.html) | Open the Simulation Data Inspector  
[Simulink.sdi.WorkerRun](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.workerrun.html) |  Access simulation data from parallel workers  
[Simulink.sdi.WorkerRun.getLatest](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.workerrun.getlatest.html) | Create worker run for latest run  
[Simulink.SimulationData.Parameter](https://uk.mathworks.com/help/simulink/slref/simulink.simulationdata.parameter.html) | Stores logged parameter data and metadata  
#### Save Simulation and Analysis Results
Name|Description
---|---
[export](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.run.export.html) | Export run to base workspace or file  
[export](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.signal.export.html) |  Export data for signal in Simulation Data Inspector to workspace or file  
[matlabshared.mldatx.getDescription](https://uk.mathworks.com/help/simulink/slref/matlabshared.mldatx.getdescription.html) | Get description of MLDATX file _(Since R2025a)_  
[matlabshared.mldatx.getType](https://uk.mathworks.com/help/simulink/slref/matlabshared.mldatx.gettype.html) | Get type of MLDATX file _(Since R2025a)_  
[Simulink.sdi.exportRun](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.exportrun.html) | Export Simulation Data Inspector run data to the workspace or a file  
[Simulink.sdi.getVersion](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.getversion.html) | Get Simulation Data Inspector session file version _(Since R2024b)_  
[Simulink.sdi.report](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.report.html) | Generate a Simulation Data Inspector report  
[Simulink.sdi.save](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.save.html) | Save Simulation Data Inspector session  
[Simulink.sdi.saveView](https://uk.mathworks.com/help/simulink/slref/simulink.sdi.saveview.html) | Save visualization settings to apply to other data  
### Test and Debug Simulations
#### Debug Simulations Programmatically
Name|Description
---|---
[ashow](https://uk.mathworks.com/help/simulink/slref/ashow.html) | Identify and highlight algebraic loops in simulation debugging session  
[atrace](https://uk.mathworks.com/help/simulink/slref/atrace.html) | Configure simulation debugging session to display information each time algebraic loop is solved  
[bafter](https://uk.mathworks.com/help/simulink/slref/bafter.html) | Insert breakpoint after specified method in simulation debugging session  
[break](https://uk.mathworks.com/help/simulink/slref/break.html) | Insert breakpoint before specified method in simulation debugging session  
[bshow](https://uk.mathworks.com/help/simulink/slref/bshow.html) | Highlight block in model with specified block ID during simulation debugging session  
[clear](https://uk.mathworks.com/help/simulink/slref/clear.html) | Clear breakpoint in simulation debugging session  
[continue](https://uk.mathworks.com/help/simulink/slref/continue.html) | Continue simulation debugging session  
[disp](https://uk.mathworks.com/help/simulink/slref/disp.html) | Display information about specified block when simulation debugging session pauses  
[ebreak](https://uk.mathworks.com/help/simulink/slref/ebreak.html) | Set or clear breakpoint to pause when solver error occurs in simulation debugging session  
[elist](https://uk.mathworks.com/help/simulink/slref/elist.html) | Display execution order in simulation debugging session  
[emode](https://uk.mathworks.com/help/simulink/slref/emode.html) | Switch between accelerator and normal mode during simulation debugging session  
[etrace](https://uk.mathworks.com/help/simulink/slref/etrace.html) | Configure simulation debugging session to display information when entering and exiting methods  
[help](https://uk.mathworks.com/help/simulink/slref/help.html) | Display help for Simulink debugging programmatic interface during simulation debugging session  
[nanbreak](https://uk.mathworks.com/help/simulink/slref/nanbreak.html) | Set or clear breakpoint to pause when `Inf` or `NaN` value occurs in simulation debugging session  
[next](https://uk.mathworks.com/help/simulink/slref/next.html) | Progress simulation debugging session to start of next method in model execution list  
[probe](https://uk.mathworks.com/help/simulink/slref/probe_cmd.html) | Display input, output, and state data for specified block in simulation debugging session  
[quit](https://uk.mathworks.com/help/simulink/slref/quit.html) | End simulation debugging session  
[rbreak](https://uk.mathworks.com/help/simulink/slref/rbreak.html) | Configure simulation debugging session to pause before solver reset  
[run](https://uk.mathworks.com/help/simulink/slref/run.html) | Run simulation debugging session from current point to end of simulation, ignoring breakpoints  
[sldebug](https://uk.mathworks.com/help/simulink/slref/sldebug.html) | Start simulation debugging session for Simulink model  
[slist](https://uk.mathworks.com/help/simulink/slref/slist.html) | Display sorted list of blocks in model during simulation debugging session  
[states](https://uk.mathworks.com/help/simulink/slref/states.html) | Display state values during simulation debugging session  
[status](https://uk.mathworks.com/help/simulink/slref/status.html) | Display options used in current simulation debugging session  
[step](https://uk.mathworks.com/help/simulink/slref/step_cmd.html) | Advance simulation by specified increment  
[stimes](https://uk.mathworks.com/help/simulink/slref/stimes.html) | Display information about sample times in model during simulation debugging session  
[stop](https://uk.mathworks.com/help/simulink/slref/stop.html) | Stop simulation debugging session  
[strace](https://uk.mathworks.com/help/simulink/slref/strace.html) | Display solver information in simulation debugging session  
[systems](https://uk.mathworks.com/help/simulink/slref/systems.html) | List nonvirtual subsystems in model or model hierarchy during simulation debugging session  
[tbreak](https://uk.mathworks.com/help/simulink/slref/tbreak.html) | Set or clear breakpoint that pauses simulation debugging session at specified time  
[trace](https://uk.mathworks.com/help/simulink/slref/trace.html) | Display information about specified block each time block executes in simulation debugging session  
[undisp](https://uk.mathworks.com/help/simulink/slref/undisp.html) | Remove display point in simulation debugging session  
[untrace](https://uk.mathworks.com/help/simulink/slref/untrace.html) | Remove trace point in simulation debugging session  
[where](https://uk.mathworks.com/help/simulink/slref/where.html) | Display current location within simulation loop during simulation debugging session  
[xbreak](https://uk.mathworks.com/help/simulink/slref/xbreak.html) | Set or clear breakpoint to pause when state limits step size in simulation debugging session  
[zcbreak](https://uk.mathworks.com/help/simulink/slref/zcbreak.html) | Configure simulation debugging session to pause when nonsampled zero-crossing events occur  
[zclist](https://uk.mathworks.com/help/simulink/slref/zclist.html) | List blocks that detect zero crossings in simulation debugging session  
#### Diagnostics
Name|Description
---|---
[modeladvisor](https://uk.mathworks.com/help/simulink/slref/modeladvisor.html) | Open Model Advisor  
[Simulink.BlockDiagram.getChecksum](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.getchecksum.html) | Return model checksum  
[Simulink.getSuppressedDiagnostics](https://uk.mathworks.com/help/simulink/slref/simulink.getsuppresseddiagnostics.html) |  Return `Simulink.SuppressedDiagnostic` objects associated with a block, subsystem, or model  
[Simulink.restoreDiagnostic](https://uk.mathworks.com/help/simulink/slref/simulink.restorediagnostic.html) | Restore diagnostic warnings to a specific block, subsystem, or model   
[Simulink.SubSystem.getChecksum](https://uk.mathworks.com/help/simulink/slref/simulink.subsystem.getchecksum.html) | Return checksum of nonvirtual subsystem  
[Simulink.suppressDiagnostic](https://uk.mathworks.com/help/simulink/slref/simulink.suppressdiagnostic.html) | Suppress a diagnostic from a specific block  
[Simulink.SuppressedDiagnostic](https://uk.mathworks.com/help/simulink/slref/simulink.suppresseddiagnostic-class.html) | Suppress diagnostic messages from specific block  
[sldiagnostics](https://uk.mathworks.com/help/simulink/slref/sldiagnostics.html) | Display diagnostic information of Simulink system  
[sldiagviewer.Comparator.compare](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.comparator.compare.html) | Compare diagnostic details between model operations _(Since R2025a)_  
[sldiagviewer.Comparator.compareWithBaseline](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.comparator.comparewithbaseline.html) | Compare diagnostic details with saved baseline _(Since R2025a)_  
[sldiagviewer.Comparator.convertToJson](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.comparator.converttojson.html) | Convert diagnostic details comparison to JSON format _(Since R2025a)_  
[sldiagviewer.Comparator.displayResult](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.comparator.displayresult.html) | Display differences in diagnostic details of model operations _(Since R2025a)_  
[sldiagviewer.createStage](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.createstage.html) | Create stage to display diagnostic messages  
[sldiagviewer.DiagnosticReceiver](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.diagnosticreceiver.html) | Create receiver to get diagnostic details of model operation _(Since R2025a)_  
[sldiagviewer.diary](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.diary.html) | Log diagnostic messages and build information in file  
[sldiagviewer.reportError](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.reporterror.html) | Report error messages in Diagnostic Viewer  
[sldiagviewer.reportInfo](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.reportinfo.html) | Report information messages in Diagnostic Viewer  
[sldiagviewer.reportSimulationMetadataDiagnostics](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.reportsimulationmetadatadiagnostics.html) | Display errors and warnings in `Simulink.SimulationOutput` object using Diagnostic Viewer  
[sldiagviewer.reportWarning](https://uk.mathworks.com/help/simulink/slref/sldiagviewer.reportwarning.html) | Report warning messages in Diagnostic Viewer  
### Optimize Performance
#### Acceleration
Name|Description
---|---
[set_param](https://uk.mathworks.com/help/simulink/slref/set_param.html) | Set Simulink parameter value  
[sim](https://uk.mathworks.com/help/simulink/slref/sim.html) | Run and script programmatic simulations of Simulink models  
[Simulink.BlockDiagram.buildRapidAcceleratorTarget](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.buildrapidacceleratortarget.html) | Build Rapid Accelerator target for model and return run-time parameter set  
[Simulink.BlockDiagram.getChecksum](https://uk.mathworks.com/help/simulink/slref/simulink.blockdiagram.getchecksum.html) | Return model checksum  
[Simulink.getFileChecksum](https://uk.mathworks.com/help/simulink/slref/simulink.getfilechecksum.html) | Checksum of file  
[Simulink.SubSystem.getChecksum](https://uk.mathworks.com/help/simulink/slref/simulink.subsystem.getchecksum.html) | Return checksum of nonvirtual subsystem  
[slbuild](https://uk.mathworks.com/help/simulink/slref/slbuild.html) | Build standalone executable file or model reference target for model  
#### Manual Performance Optimization
Name|Description
---|---
[generateReport](https://uk.mathworks.com/help/simulink/slref/generatereport.html) | Create report of data from profiling simulation run using Simulink Profiler _(Since R2023a)_  
[Simulink.profiler.Data](https://uk.mathworks.com/help/simulink/slref/simulink.profiler.data.html) | Access profiling information created using Simulink Profiler  
[sldiagnostics](https://uk.mathworks.com/help/simulink/slref/sldiagnostics.html) | Display diagnostic information of Simulink system  
## Project Management
### Using MATLAB Projects in Simulink
Name|Description
---|---
[addReference](https://uk.mathworks.com/help/matlab/ref/matlab.project.project.addreference.html) | Add referenced project to project  
[dependencies.fileDependencyAnalysis](https://uk.mathworks.com/help/simulink/slref/dependencies.filedependencyanalysis.html) | Find model file dependencies  
[dependencies.toolboxDependencyAnalysis](https://uk.mathworks.com/help/simulink/slref/dependencies.toolboxdependencyanalysis.html) | Find products required by file  
[listAllProjectReferences](https://uk.mathworks.com/help/matlab/ref/matlab.project.project.listallprojectreferences.html) | List all projects in reference hierarchy of current project _(Since R2021a)_  
[removeReference](https://uk.mathworks.com/help/matlab/ref/matlab.project.project.removereference.html) | Remove project reference  
[Simulink.createFromTemplate](https://uk.mathworks.com/help/simulink/slref/simulink.createfromtemplate.html) | Create model or project from template  
[Simulink.exportToTemplate](https://uk.mathworks.com/help/simulink/slref/simulink.exporttotemplate.html) | Create template from model or project  
[Simulink.findTemplates](https://uk.mathworks.com/help/simulink/slref/simulink.findtemplates.html) | Find model or project templates with specified properties  
[updateDependencies](https://uk.mathworks.com/help/matlab/ref/matlab.project.project.updatedependencies.html) | Update project dependencies  
## Block and Blockset Authoring
### Author Block Algorithms
#### Author Blocks Using MATLAB
Name|Description
---|---
[allowModelReferenceDiscreteSampleTimeInheritanceImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.allowmodelreferencediscretesampletimeinheritanceimpl.html) | Model reference sample time inheritance status for discrete sample times  
[CheckParameters](https://uk.mathworks.com/help/simulink/sfg/checkparameters.html) | Check the validity of a MATLAB S-Function's parameters  
[closeReport](https://uk.mathworks.com/help/simulink/slref/simulink.matlabfunctionconfiguration.closereport.html) | Close MATLAB function report _(Since R2021a)_  
[coder.allowpcode](https://uk.mathworks.com/help/simulink/slref/coder.allowpcode.html) | Control code generation from P-code files  
[coder.areUnboundedVariableSizedArraysSupported](https://uk.mathworks.com/help/simulink/slref/coder.areunboundedvariablesizedarrayssupported.html) | Check if current configuration settings allow unbounded variable-size arrays _(Since R2024a)_  
[coder.BuildConfig](https://uk.mathworks.com/help/simulink/slref/coder.buildconfig-class.html) | Build context during code generation  
[coder.ceval](https://uk.mathworks.com/help/simulink/slref/coder.ceval.html) | Call C/C++ function from generated code  
[coder.cinclude](https://uk.mathworks.com/help/simulink/slref/coder.cinclude.html) | Include header file in generated code  
[coder.columnMajor](https://uk.mathworks.com/help/simulink/slref/coder.columnmajor.html) | Specify column-major array layout for a function or class  
[coder.const](https://uk.mathworks.com/help/simulink/slref/coder.const.html) | Fold expressions into constants in generated code  
[coder.cstructname](https://uk.mathworks.com/help/simulink/slref/coder.cstructname.html) | Name C structure type in generated code  
[coder.ExternalDependency](https://uk.mathworks.com/help/simulink/slref/coder.externaldependency-class.html) | Interface to external code  
[coder.extrinsic](https://uk.mathworks.com/help/simulink/slref/coder.extrinsic.html) | Declare function as extrinsic and execute it in MATLAB  
[coder.ignoreConst](https://uk.mathworks.com/help/simulink/slref/coder.ignoreconst.html) | Prevent use of constant value of expression for function specializations  
[coder.ignoreSize](https://uk.mathworks.com/help/simulink/slref/coder.ignoresize.html) | Prevent code generator from creating function specializations for constant-size expressions  
[coder.inline](https://uk.mathworks.com/help/simulink/slref/coder.inline.html) | Control inlining of current function in generated code  
[coder.inlineCall](https://uk.mathworks.com/help/simulink/slref/coder.inlinecall.html) | Inline called function in generated code _(Since R2024a)_  
[coder.isColumnMajor](https://uk.mathworks.com/help/simulink/slref/coder.iscolumnmajor.html) | Determine whether the current function or variable uses column-major layout  
[coder.isRowMajor](https://uk.mathworks.com/help/simulink/slref/coder.isrowmajor.html) | Determine whether the current function or variable uses row-major layout  
[coder.load](https://uk.mathworks.com/help/simulink/slref/coder.load.html) | Load constants from MAT file or ASCII file at code generation time  
[coder.mustBeConst](https://uk.mathworks.com/help/simulink/slref/coder.mustbeconst.html) | Validate that value is a compile-time constant _(Since R2023b)_  
[coder.noImplicitExpansionInFunction](https://uk.mathworks.com/help/coder/ref/coder.noimplicitexpansioninfunction.html) | Disable implicit expansion within the specified function in the generated code _(Since R2021b)_  
[coder.nonInlineCall](https://uk.mathworks.com/help/simulink/slref/coder.noninlinecall.html) | Prevent inlining of called function in generated code _(Since R2024a)_  
[coder.nullcopy](https://uk.mathworks.com/help/simulink/slref/coder.nullcopy.html) | Declare uninitialized variables in generated code  
[coder.opaque](https://uk.mathworks.com/help/simulink/slref/coder.opaque.html) | Declare variable in generated code  
[coder.read](https://uk.mathworks.com/help/simulink/slref/coder.read.html) | Read data files at run time in generated code _(Since R2023a)_  
[coder.ref](https://uk.mathworks.com/help/simulink/slref/coder.ref.html) | Indicate data to pass by reference  
[coder.rowMajor](https://uk.mathworks.com/help/simulink/slref/coder.rowmajor.html) | Specify row-major array layout for a function or class  
[coder.rref](https://uk.mathworks.com/help/simulink/slref/coder.rref.html) | Indicate read-only data to pass by reference  
[coder.sameSizeBinaryOp](https://uk.mathworks.com/help/coder/ref/coder.samesizebinaryop.html) | Apply element-wise binary operations without implicit expansion _(Since R2021b)_  
[coder.screener](https://uk.mathworks.com/help/simulink/slref/coder.screener.html) | Determine if function is suitable for code generation  
[coder.target](https://uk.mathworks.com/help/simulink/slref/coder.target.html) | Determine if code generation target is specified target  
[coder.unroll](https://uk.mathworks.com/help/simulink/slref/coder.unroll.html) | Unroll `for`-loop by making a copy of the loop body for each loop iteration  
[coder.updateBuildInfo](https://uk.mathworks.com/help/simulink/slref/coder.updatebuildinfo.html) | Update `RTW.BuildInfo` build information object  
[coder.varsize](https://uk.mathworks.com/help/simulink/slref/coder.varsize.html) | Resolve size incompatibility errors and declare upper bounds  
[coder.wref](https://uk.mathworks.com/help/simulink/slref/coder.wref.html) | Indicate write-only data to pass by reference  
[coder.write](https://uk.mathworks.com/help/simulink/slref/coder.write.html) | Create data files that the generated code reads at run time _(Since R2023a)_  
[createSampleTime](https://uk.mathworks.com/help/simulink/slref/matlab.system.createsampletime.html) | Create sample time specification object  
[Derivatives](https://uk.mathworks.com/help/simulink/sfg/derivatives.html) | Compute a MATLAB S-Function's derivatives  
[Disable](https://uk.mathworks.com/help/simulink/sfg/disable.html) | Respond to disabling of an enabled system containing this MATLAB S-Function block  
[Enable](https://uk.mathworks.com/help/simulink/sfg/enable.html) | Respond to enabling of an enabled system containing this MATLAB S-Function block  
[getCurrentTime](https://uk.mathworks.com/help/simulink/slref/matlab.system.getcurrenttime.html) | Current simulation time in MATLAB System block  
[getDiscreteStateImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getdiscretestateimpl.html) | Discrete state property values  
[getDiscreteStateSpecificationImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getdiscretestatespecificationimpl.html) | Discrete state size, data type, and complexity  
[getGlobalNamesImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getglobalnamesimpl.html) | Global variable names for MATLAB System block  
[getHeaderImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getheaderimpl.html) | Header for System object display  
[getIconImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.geticonimpl.html) | Name to display as block icon  
[getInputNamesImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getinputnamesimpl.html) | Names of MATLAB System block input ports  
[getInterfaceImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getinterfaceimpl.html) | Set System object as message or data _(Since R2021a)_  
[GetOperatingPoint](https://uk.mathworks.com/help/simulink/sfg/getoperatingpoint.html) | Return operating point for MATLAB S-function as MATLAB data structure  
[getOutputDataTypeImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getoutputdatatypeimpl.html) | Data types of output ports  
[getOutputNamesImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getoutputnamesimpl.html) | Names of MATLAB System block output ports  
[getOutputSizeImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getoutputsizeimpl.html) | Sizes of output ports  
[getPropertyGroupsImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getpropertygroupsimpl.html) | Property groups for System object display  
[getReport](https://uk.mathworks.com/help/simulink/slref/simulink.matlabfunctionconfiguration.getreport.html) | Generate MATLAB function report _(Since R2021a)_  
[getSampleTime](https://uk.mathworks.com/help/simulink/slref/matlab.system.getsampletime.html) | Query sample time  
[getSampleTimeImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getsampletimeimpl.html) | Specify sample time type, offset time, and sample time   
[getSimulateUsingImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getsimulateusingimpl.html) | Specify value for Simulate using parameter  
[getSimulinkFunctionNamesImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.getsimulinkfunctionnamesimpl.html) | Register Simulink function names used in your System object  
[isInputDirectFeedthroughImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.isinputdirectfeedthroughimpl.html) | Direct feedthrough status of input  
[isOutputComplexImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.isoutputcompleximpl.html) | Complexity of output ports  
[isOutputFixedSizeImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.isoutputfixedsizeimpl.html) | Fixed- or variable-size output ports  
[matlab.system.display.Action](https://uk.mathworks.com/help/simulink/slref/matlab.system.display.action-class.html) | Create custom button in Block Parameters dialog box for MATLAB System block  
[matlab.system.display.Header](https://uk.mathworks.com/help/simulink/slref/matlab.system.display.header-class.html) | Specify header in Block Parameters dialog box for MATLAB System block  
[matlab.system.display.Icon](https://uk.mathworks.com/help/simulink/slref/matlab.system.display.icon-class.html) | Specify custom image as icon for MATLAB System block  
[matlab.system.display.Section](https://uk.mathworks.com/help/simulink/slref/matlab.system.display.section-class.html) | Create property group section in Block Parameters dialog box for MATLAB System block  
[matlab.system.display.SectionGroup](https://uk.mathworks.com/help/simulink/slref/matlab.system.display.sectiongroup-class.html) | Create nested groupings of properties in Block Parameters dialog box for MATLAB System block  
[MATLABFunctionConfiguration](https://uk.mathworks.com/help/simulink/slref/simulink.matlabfunctionconfiguration.html) |  MATLAB Function block property configuration  
[MATLABFunctionReport](https://uk.mathworks.com/help/simulink/slref/simulink.matlabfunctionreport.html) |  MATLAB function report _(Since R2021a)_  
[openReport](https://uk.mathworks.com/help/simulink/slref/simulink.matlabfunctionconfiguration.openreport.html) | Open MATLAB function report _(Since R2021a)_  
[outputImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.outputimpl.html) | Output calculation from input or internal state of System object  
[Outputs](https://uk.mathworks.com/help/simulink/sfg/outputs.html) | Compute the signals that this MATLAB S-function block emits  
[PostPropagationSetup](https://uk.mathworks.com/help/simulink/sfg/postpropagationsetup.html) | Specify the sizes of the work vectors and create the run-time parameters required by this MATLAB S-function  
[ProcessParameters](https://uk.mathworks.com/help/simulink/sfg/processparameters.html) | Process the MATLAB S-function's parameters  
[processTunedPropertiesImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.processtunedpropertiesimpl.html) | Action when tunable properties change  
[Projection](https://uk.mathworks.com/help/simulink/sfg/projection.html) | Perturb the solver's solution of a system's states to better satisfy time-invariant solution relationships  
[propagatedInputComplexity](https://uk.mathworks.com/help/simulink/slref/matlab.system.propagatedinputcomplexity.html) | Complexity of input during Simulink propagation  
[propagatedInputDataType](https://uk.mathworks.com/help/simulink/slref/matlab.system.propagatedinputdatatype.html) | Data type of input during Simulink propagation  
[propagatedInputFixedSize](https://uk.mathworks.com/help/simulink/slref/matlab.system.propagatedinputfixedsize.html) | Fixed-size status of input during Simulink propagation  
[propagatedInputSize](https://uk.mathworks.com/help/simulink/slref/matlab.system.propagatedinputsize.html) | Size of input during Simulink propagation  
[SetAllowConstantSampleTime](https://uk.mathworks.com/help/simulink/sfg/setallowconstantsampletime.html) | Specify sample time behavior and tunability for S-function blocks with port-based sample times  
[SetInputPortComplexSignal](https://uk.mathworks.com/help/simulink/sfg/setinputportcomplexsignal.html) | Set the numeric types (real, complex, or inherited) of the signals accepted by an input port  
[SetInputPortDataType](https://uk.mathworks.com/help/simulink/sfg/setinputportdatatype.html) | Set the data types of the signals accepted by an input port  
[SetInputPortDimensions](https://uk.mathworks.com/help/simulink/sfg/setinputportdimensions.html) | Set the dimensions of the signals accepted by an input port  
[SetInputPortSampleTime](https://uk.mathworks.com/help/simulink/sfg/setinputportsampletime.html) | Set the sample time of an input port that inherits its sample time from the port to which it is connected  
[setNumTicksUntilNextHit](https://uk.mathworks.com/help/simulink/slref/matlab.system.setnumticksuntilnexthit.html) | Set the number of ticks in Simulink sample time  
[SetOperatingPoint](https://uk.mathworks.com/help/simulink/sfg/setoperatingpoint.html) | Restore operating point of MATLAB S-function  
[SetOutputPortComplexSignal](https://uk.mathworks.com/help/simulink/sfg/setoutputportcomplexsignal.html) | Set the numeric types (real, complex, or inherited) of the signals accepted by an output port  
[SetOutputPortDataType](https://uk.mathworks.com/help/simulink/sfg/setoutputportdatatype.html) | Set the data type of the signals emitted by an output port  
[SetOutputPortDimensions](https://uk.mathworks.com/help/simulink/sfg/setoutputportdimensions.html) | Set the dimensions of the signals accepted by an output port  
[SetOutputPortSampleTime](https://uk.mathworks.com/help/simulink/sfg/setoutputportsampletime.html) | Set the sample time of an output port that inherits its sample time from the port to which it is connected  
[setup](https://uk.mathworks.com/help/simulink/sfg/setup.html) | Specify the number of inputs, outputs, states, parameters, and other characteristics of the MATLAB S-function  
[showFiSettingsImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.showfisettingsimpl.html) | Fixed point data type tab visibility for System objects  
[showSimulateUsingImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.showsimulateusingimpl.html) | Visibility of Simulate using parameter  
[SimStatusChange](https://uk.mathworks.com/help/simulink/sfg/simstatuschange.html) | Respond to a pause or resumption of the simulation of the model that contains this MATLAB S-function  
[Simulink.BlockCompDworkData](https://uk.mathworks.com/help/simulink/slref/simulink.blockcompdworkdata.html) | Provide post-compilation information about block `DWork` vector  
[Simulink.BlockCompInputPortData](https://uk.mathworks.com/help/simulink/slref/simulink.blockcompinputportdata.html) | Provide post-compilation information about block input port  
[Simulink.BlockCompOutputPortData](https://uk.mathworks.com/help/simulink/slref/simulink.blockcompoutputportdata.html) | Provide post-compilation information about block output port  
[Simulink.BlockData](https://uk.mathworks.com/help/simulink/slref/simulink.blockdata.html) | Provide runtime information about block-related data, such as block parameters  
[Simulink.BlockPortData](https://uk.mathworks.com/help/simulink/slref/simulink.blockportdata.html) | Describe block input or output port  
[Simulink.BlockPreCompInputPortData](https://uk.mathworks.com/help/simulink/slref/simulink.blockprecompinputportdata.html) | Provide precompilation information about block input port  
[Simulink.BlockPreCompOutputPortData](https://uk.mathworks.com/help/simulink/slref/simulink.blockprecompoutputportdata.html) | Provide precompilation information about block output port  
[Simulink.MSFcnRunTimeBlock](https://uk.mathworks.com/help/simulink/slref/simulink.msfcnruntimeblock.html) | Get run-time information about Level-2 MATLAB S-function block  
[Simulink.RunTimeBlock](https://uk.mathworks.com/help/simulink/slref/simulink.runtimeblock.html) | Allow Level-2 MATLAB S-function and other MATLAB programs to get information about block while simulation is running  
[Start](https://uk.mathworks.com/help/simulink/sfg/start.html) | Initialize the state vectors of this MATLAB S-function  
[Stateflow.EMChart](https://uk.mathworks.com/help/simulink/slref/stateflow.emchart.html) |  Stateflow interface to MATLAB Function block  
[supportsMultipleInstanceImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.supportsmultipleinstanceimpl.html) | Support System object in Simulink For Each subsystem  
[Terminate](https://uk.mathworks.com/help/simulink/sfg/terminate.html) | Perform any actions required at termination of the simulation  
[Update](https://uk.mathworks.com/help/simulink/sfg/update.html) | Update a block's states  
[updateImpl](https://uk.mathworks.com/help/simulink/slref/matlab.system.updateimpl.html) | Update object states based on inputs  
[WriteRTW](https://uk.mathworks.com/help/simulink/sfg/writertw.html) | Generate code generation data for the MATLAB S-function  
#### Author Blocks Using C/C++
Name|Description
---|---
[findSfunctions](https://uk.mathworks.com/help/simulink/slref/simulink.sfunction.analyzer.findsfunctions.html) | Find and return all eligible S-functions in a model  
[mdlInitializeConditions](https://uk.mathworks.com/help/simulink/sfg/mdlinitializeconditions.html) | Initialize the state vectors of this C MEX S-function  
[mdlSetInputPortDimensionInfo](https://uk.mathworks.com/help/simulink/sfg/mdlsetinputportdimensioninfo.html) | Set the dimensions of the signals accepted by an input port  
[Simulink.sfunction.Analyzer](https://uk.mathworks.com/help/simulink/slref/simulink.sfunction.analyzer-class.html) | Create S-function analyzer object  
[Simulink.sfunction.analyzer.BuildInfo](https://uk.mathworks.com/help/simulink/slref/simulink.sfunction.analyzer.buildinfo-class.html) |  Create an object to represent build information  
[Simulink.sfunction.analyzer.Options](https://uk.mathworks.com/help/simulink/slref/simulink.sfunction.analyzer.options-class.html) |  Create an object to specify options for running S-function checks  
[Simulink.SFunctionBuilder.add](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.add.html) | Add input, output, parameter, library item, or state to S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.build](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.build.html) | Build S-function and generate MEX file for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.delete](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.delete.html) | Remove input, output, parameter, library item, or state from S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.generateCodeOnly](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.generatecodeonly.html) | Build S-function without generating MEX file for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.generateFMU](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.generatefmu.html) | Generate FMU compatible with FMI 3.0 standards from C/C++ code using S-Function Builder block _(Since R2023b)_  
[Simulink.SFunctionBuilder.getBuildOptions](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.getbuildoptions.html) | Get build options for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.getSettings](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.getsettings.html) | Get settings for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.getSFunctionName](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.getsfunctionname.html) | Get name of S-function generated by S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.getTargetLanguage](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.gettargetlanguage.html) | Get language for S-function generated using S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.getUserCode](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.getusercode.html) | Get code for method of S-function generated using S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.list](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.list.html) | List inputs, outputs, parameters, library items, and states for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setBuildOptions](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.setbuildoptions.html) | Set build options for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setSettings](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.setsettings.html) | Set settings for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setSFunctionName](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.setsfunctionname.html) | Set name of S-function for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setTargetLanguage](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.settargetlanguage.html) | Set language for S-function generated using S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setUserCode](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.setusercode.html) | Set code for methods of S-function generated using S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.update](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.update.html) | Update attributes for input port, output port, or parameter of S-Function Builder block _(Since R2022a)_  
[ssSetControllableSampleTime](https://uk.mathworks.com/help/simulink/sfg/sssetcontrollablesampletime.html) | Register controllable sample time in a block  
[ssSetSupportedForCodeReuseAcrossModels](https://uk.mathworks.com/help/simulink/sfg/sssetsupportedforcodereuseacrossmodels.html) | Specify if S-function can be reused across models _(Since R2021a)_  
### Author Block Masks
#### Mask Parameters and Constraints
Name|Description
---|---
[Simulink.ConstraintManager](https://uk.mathworks.com/help/simulink/slref/simulink.constraintmanager-class.html) | Manage parameter and port constraints _(Since R2024b)_  
[Simulink.Mask](https://uk.mathworks.com/help/simulink/slref/simulink.mask-class.html) | Control masks programmatically  
[Simulink.Mask.Constraints](https://uk.mathworks.com/help/simulink/slref/simulink.mask.constraints-class.html) | Create mask parameter constraint  
[Simulink.Mask.CrossPortConstraint](https://uk.mathworks.com/help/simulink/slref/simulink.mask.crossportconstraint-class.html) | Creates cross-port constraint among ports of the same masked block _(Since R2023a)_  
[Simulink.Mask.CrossPortParameterConstraint](https://uk.mathworks.com/help/simulink/slref/simulink.mask.crossportparameterconstraint-class.html) | Cross port parameter constraint between ports and parameters of same masked block _(Since R2025a)_  
[Simulink.Mask.CrossPortParameterConstraintAssociation](https://uk.mathworks.com/help/simulink/slref/simulink.mask.crossportparameterassociation-class.html) | Cross port parameter constraint association between mask parameters and ports _(Since R2025a)_  
[Simulink.Mask.EnumerationBase](https://uk.mathworks.com/help/simulink/slref/simulink.mask.enumerationbase-class.html) | Derive enumeration class to hold numeric values of any data type _(Since R2021a)_  
[Simulink.Mask.EnumerationTypeOptions](https://uk.mathworks.com/help/simulink/slref/simulink.mask.enumerationtypeoptions-class.html) | Parse information from enumeration file derived from `Simulink.IntEnumType` and `Simulink.Mask.EnumerationBase`_(Since R2021a)_  
[Simulink.Mask.ParameterCondition](https://uk.mathworks.com/help/simulink/slref/simulink.mask.parametercondition-class.html) | Create mask parameter conditions _(Since R2022a)_  
[Simulink.Mask.PortConstraint](https://uk.mathworks.com/help/simulink/slref/simulink.mask.portconstraint-class.html) | Create mask port constraints programmatically _(Since R2022a)_  
[Simulink.Mask.PortConstraintRule](https://uk.mathworks.com/help/simulink/slref/simulink.mask.portconstraintrule-class.html) | Create instance of `Simulink.Mask.PortConstraintRule` to define rules of port constraint _(Since R2022a)_  
[Simulink.Mask.PortIdentifier](https://uk.mathworks.com/help/simulink/slref/simulink.mask.portidentifier-class.html) | Create port identifiers to identify ports of block in mask object _(Since R2022a)_  
[Simulink.Mask.SharedConstraintFile](https://uk.mathworks.com/help/simulink/slref/simulink.mask.sharedconstraintfile-class.html) | Constraints that needs to be saved in an XML file _(Since R2023a)_  
[Simulink.Mask.Workspace](https://uk.mathworks.com/help/simulink/slref/simulink.mask.workspace-class.html) | Mask workspace object _(Since R2025a)_  
[Simulink.MaskParameter](https://uk.mathworks.com/help/simulink/slref/simulink.maskparameter-class.html) | Control mask parameters programmatically  
#### Dialog Control Elements
Name|Description
---|---
[Simulink.dialog.Button](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.button-class.html) | Create instance of button dialog control  
[Simulink.dialog.Container](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.container-class.html) | Create instance of container dialog control  
[Simulink.dialog.Control](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.control-class.html) | Create instance of dialog control  
[Simulink.dialog.Group](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.group-class.html) | Create instance of group dialog control  
[Simulink.dialog.Hyperlink](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.hyperlink-class.html) | Create instance of hyperlink dialog control  
[Simulink.dialog.Image](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.image-class.html) | Manage image dialog control  
[Simulink.dialog.ListboxControl](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.listboxcontrol-class.html) | Control list box programmatically  
[Simulink.dialog.LookupTableControl](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.lookuptablecontrol-class.html) | Control mask lookup tables programmatically _(Since R2021b)_  
[Simulink.dialog.LookupTableControl.Breakpoints](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.lookuptablecontrol.breakpoints-class.html) | Control breakpoint data set for mask lookup table _(Since R2021b)_  
[Simulink.dialog.LookupTableControl.Table](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.lookuptablecontrol.table-class.html) | Control table data for mask lookup table _(Since R2021b)_  
[Simulink.dialog.MaskPartReference](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.maskpartreference-class.html) | Create and save parameters and dialog controls and reuse them across multiple masked blocks _(Since R2024b)_  
[Simulink.dialog.Panel](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.panel-class.html) | Create instance of panel dialog control  
[Simulink.dialog.parameter.Control](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.parameter.control.html) | Create a parameter dialog control  
[Simulink.dialog.parameter.CustomTable](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.parameter.customtable-class.html) | Create custom tables programmatically  
[Simulink.dialog.Tab](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.tab-class.html) | Create instance of tab dialog control  
[Simulink.dialog.TabContainer](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.tabcontainer-class.html) | Create instance of tab container dialog control  
[Simulink.dialog.Text](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.text-class.html) | Manage text dialog control  
[Simulink.dialog.TreeControl](https://uk.mathworks.com/help/simulink/slref/simulink.dialog.treecontrol-class.html) | Control Tree control programmatically  
## Simulation Integration
### Create Large-Scale Model Components
#### Integrate Components from External Tools
Name|Description
---|---
[fmudialog.compileFMUSources](https://uk.mathworks.com/help/simulink/slref/fmudialog.compilefmusources.html) | Generate binary for FMU with source code on current platform _(Since R2024a)_  
[fmudialog.createBusType](https://uk.mathworks.com/help/simulink/slref/fmudialog.createbustype.html) | Create all FMU bus objects required for structured input or output ports in workspace  
[fmudialog.createEnumType](https://uk.mathworks.com/help/simulink/slref/fmudialog.createenumtype.html) | Generate all enumeration classes required for FMU input or output ports  
[fmudialog.createTypeObject](https://uk.mathworks.com/help/simulink/slref/fmudialog.createtypeobject.html) | Generates enumeration and bus objects required for FMU input or output ports _(Since R2023b)_  
[shareMATLABForFMUCoSim](https://uk.mathworks.com/help/simulink/slref/sharematlabforfmucosim.html) | Share current MATLAB session for FMU tool-coupling co-simulation  
[Simulink.fmuexport.ExportSimulinkProjectToFMU](https://uk.mathworks.com/help/simulink/slref/simulink.fmuexport.exportsimulinkprojecttofmu.html) | Export project as Functional Mockup Unit (FMU)  
#### Integrate External Code into Simulink
Name|Description
---|---
[FunctionArgument](https://uk.mathworks.com/help/simulink/slref/simulink.customcode.functionargument.html) | Specify parameters of C Caller block inputs and outputs  
[FunctionPortSpecification](https://uk.mathworks.com/help/simulink/slref/simulink.customcode.functionportspecification.html) | Query and configure C Caller block properties  
[legacy_code](https://uk.mathworks.com/help/simulink/slref/legacy_code.html) | Integrate existing C/C++ code using Legacy Code Tool  
[Simulink.CodeImporter](https://uk.mathworks.com/help/simulink/slref/simulink.codeimporter-class.html) | Import custom C/C++ code into Simulink _(Since R2021a)_  
[Simulink.CodeImporter.CustomCode](https://uk.mathworks.com/help/simulink/slref/simulink.codeimporter.customcode-class.html) | Specify custom code settings for `Simulink.CodeImporter` and `sltest.CodeImporter` classes _(Since R2021a)_  
[Simulink.CodeImporter.Function](https://uk.mathworks.com/help/simulink/slref/simulink.codeimporter.function-class.html) | Access and configure detailed information about parsed custom code functions _(Since R2021a)_  
[Simulink.CodeImporter.Options](https://uk.mathworks.com/help/simulink/slref/simulink.codeimporter.options-class.html) | Specify additional import options for `Simulink.CodeImporter` and `sltest.CodeImporter` classes _(Since R2021a)_  
[Simulink.CodeImporter.ParseInfo](https://uk.mathworks.com/help/simulink/slref/simulink.codeimporter.parseinfo-class.html) | Information about parsed custom code _(Since R2021a)_  
[Simulink.CodeImporter.SimulinkPortSpecification](https://uk.mathworks.com/help/simulink/slref/simulink.codeimporter.simulinkportspecification-class.html) | Configure port specification for imported custom code _(Since R2021a)_  
[Simulink.SFunctionBuilder.add](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.add.html) | Add input, output, parameter, library item, or state to S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.build](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.build.html) | Build S-function and generate MEX file for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.delete](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.delete.html) | Remove input, output, parameter, library item, or state from S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.generateCodeOnly](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.generatecodeonly.html) | Build S-function without generating MEX file for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.generateFMU](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.generatefmu.html) | Generate FMU compatible with FMI 3.0 standards from C/C++ code using S-Function Builder block _(Since R2023b)_  
[Simulink.SFunctionBuilder.getBuildOptions](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.getbuildoptions.html) | Get build options for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.getSettings](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.getsettings.html) | Get settings for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.getSFunctionName](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.getsfunctionname.html) | Get name of S-function generated by S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.getTargetLanguage](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.gettargetlanguage.html) | Get language for S-function generated using S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.getUserCode](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.getusercode.html) | Get code for method of S-function generated using S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.list](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.list.html) | List inputs, outputs, parameters, library items, and states for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setBuildOptions](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.setbuildoptions.html) | Set build options for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setSettings](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.setsettings.html) | Set settings for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setSFunctionName](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.setsfunctionname.html) | Set name of S-function for S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setTargetLanguage](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.settargetlanguage.html) | Set language for S-function generated using S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.setUserCode](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.setusercode.html) | Set code for methods of S-function generated using S-Function Builder block _(Since R2022a)_  
[Simulink.SFunctionBuilder.update](https://uk.mathworks.com/help/simulink/slref/simulink.sfunctionbuilder.update.html) | Update attributes for input port, output port, or parameter of S-Function Builder block _(Since R2022a)_  
[Symbol](https://uk.mathworks.com/help/simulink/slref/simulink.cfunctionblock.symbol.html) | C Function block data symbol  
[SymbolSpec](https://uk.mathworks.com/help/simulink/slref/simulink.cfunctionblock.symbolspec.html) | Query and configure C Function block data symbols  
## References
* [Simulink Functions](https://uk.mathworks.com/help/simulink/referencelist.html?type=function&listtype=cat&category=index&blocktype=all&capability=&startrelease=&endrelease=)