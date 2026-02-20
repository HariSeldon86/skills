# Simulink — Blocks
- [Simulink — Blocks](#simulink--blocks)
  - [Simulink Environment Fundamentals](#simulink-environment-fundamentals)
    - [Block Libraries](#block-libraries)
      - [Continuous](#continuous)
      - [Dashboard](#dashboard)
      - [Customizable Blocks](#customizable-blocks)
      - [Discontinuities](#discontinuities)
      - [Discrete](#discrete)
      - [Logic and Bit Operations](#logic-and-bit-operations)
      - [Lookup Tables](#lookup-tables)
      - [Math Operations](#math-operations)
      - [Matrix Operations](#matrix-operations)
      - [Messages \& Events](#messages--events)
      - [Model Verification](#model-verification)
      - [Model-Wide Utilities](#model-wide-utilities)
      - [Ports and Subsystems](#ports-and-subsystems)
      - [Signal Attributes](#signal-attributes)
      - [Signal Routing](#signal-routing)
      - [Sinks](#sinks)
      - [Sources](#sources)
      - [String](#string)
      - [User-Defined Functions](#user-defined-functions)
      - [Additional Math and Discrete](#additional-math-and-discrete)
  - [Modeling](#modeling)
    - [Design Model Architecture](#design-model-architecture)
      - [Component-Based Modeling](#component-based-modeling)
      - [Subsystems](#subsystems)
      - [Model References](#model-references)
      - [Variant Systems](#variant-systems)
      - [Data Stores](#data-stores)
      - [Composite Interfaces](#composite-interfaces)
    - [Design Model Behavior](#design-model-behavior)
      - [Conditionally Executed Subsystems and Models](#conditionally-executed-subsystems-and-models)
      - [Iterator Subsystems](#iterator-subsystems)
      - [Simulink Functions](#simulink-functions)
      - [Event Functions](#event-functions)
      - [Messages](#messages)
      - [Schedule Model Components](#schedule-model-components)
      - [Nonlinearity](#nonlinearity)
    - [Configure Signals, States, and Parameters](#configure-signals-states-and-parameters)
      - [Signals](#signals)
      - [Units in Simulink](#units-in-simulink)
      - [Data Types](#data-types)
      - [Model, Block, and Port Callbacks](#model-block-and-port-callbacks)
    - [Analyze and Remodel Design](#analyze-and-remodel-design)
      - [Transform Models](#transform-models)
    - [Test Model Components](#test-model-components)
  - [Simulation](#simulation)
    - [Prepare Model Inputs and Outputs](#prepare-model-inputs-and-outputs)
      - [Create Signal Data for Simulation](#create-signal-data-for-simulation)
      - [Load Signal Data for Simulation](#load-signal-data-for-simulation)
      - [Save Run-Time Data from Simulation](#save-run-time-data-from-simulation)
    - [View and Analyze Simulation Results](#view-and-analyze-simulation-results)
      - [Control Simulations with Interactive Dashboards](#control-simulations-with-interactive-dashboards)
      - [View Data During Simulation](#view-data-during-simulation)
  - [Block and Blockset Authoring](#block-and-blockset-authoring)
    - [Author Block Algorithms](#author-block-algorithms)
      - [Block Authoring Basics](#block-authoring-basics)
      - [Author Blocks Using MATLAB](#author-blocks-using-matlab)
      - [Author Blocks Using C/C++](#author-blocks-using-cc)
  - [Simulation Integration](#simulation-integration)
    - [Create Large-Scale Model Components](#create-large-scale-model-components)
      - [Integrate Components from External Tools](#integrate-components-from-external-tools)
      - [Integrate External Code into Simulink](#integrate-external-code-into-simulink)
  - [References](#references)

## Simulink Environment Fundamentals
### Block Libraries
#### Continuous
Name|Description
---|---
[Derivative](https://uk.mathworks.com/help/simulink/slref/derivative.html) | Compute approximate continuous derivative of continuous input signal with respect to time  
[Descriptor State-Space](https://uk.mathworks.com/help/simulink/slref/descriptorstatespace.html) | Model linear implicit system  
[Entity Transport Delay](https://uk.mathworks.com/help/simulink/slref/entitytransportdelay.html) | Introduce a delay in propagation of a SimEvents message  
[First Order Hold](https://uk.mathworks.com/help/simulink/slref/firstorderhold.html) | Implement linearly extrapolated first order hold on input signal  
[Integrator](https://uk.mathworks.com/help/simulink/slref/integrator.html) | Integrate signal  
[Integrator Limited](https://uk.mathworks.com/help/simulink/slref/integratorlimited.html) | Integrate signal  
[PID Controller](https://uk.mathworks.com/help/simulink/slref/pidcontroller.html) | Continuous-time or discrete-time PID controller  
[PID Controller (2DOF)](https://uk.mathworks.com/help/simulink/slref/pidcontroller2dof.html) | Continuous-time or discrete-time two-degree-of-freedom PID controller  
[Second-Order Integrator](https://uk.mathworks.com/help/simulink/slref/secondorderintegrator.html) | Second-order integration of input signal  
[Second-Order Integrator Limited](https://uk.mathworks.com/help/simulink/slref/secondorderintegratorlimited.html) | Second-order integration of input signal  
[State-Space](https://uk.mathworks.com/help/simulink/slref/statespace.html) | Implement linear state-space system  
[Transfer Fcn](https://uk.mathworks.com/help/simulink/slref/transferfcn.html) | Model linear system as transfer function  
[Transport Delay](https://uk.mathworks.com/help/simulink/slref/transportdelay.html) | Delay input by given amount of time  
[Variable Time Delay](https://uk.mathworks.com/help/simulink/slref/variabletimedelay.html) | Delay input by variable amount of time  
[Variable Transport Delay](https://uk.mathworks.com/help/simulink/slref/variabletransportdelay.html) | Delay input by variable amount of time  
[Zero-Pole](https://uk.mathworks.com/help/simulink/slref/zeropole.html) | Model system using zero-pole-gain transfer function  
#### Dashboard
Name|Description
---|---
[Callback Button](https://uk.mathworks.com/help/simulink/slref/callbackbutton.html) | Execute MATLAB code using button  
[Check Box](https://uk.mathworks.com/help/simulink/slref/checkbox.html) | Select parameter or variable value  
[Combo Box](https://uk.mathworks.com/help/simulink/slref/combobox.html) | Select parameter value from drop-down menu  
[Dashboard Scope](https://uk.mathworks.com/help/simulink/slref/dashboardscope.html) | Trace signals on scope display during simulation  
[Display](https://uk.mathworks.com/help/simulink/slref/dashboarddisplay.html) | Display signal value during simulation  
[Edit](https://uk.mathworks.com/help/simulink/slref/edit.html) | Enter new value for parameter  
[Gauge](https://uk.mathworks.com/help/simulink/slref/gauge.html) | Display signal value on circular scale  
[Half Gauge](https://uk.mathworks.com/help/simulink/slref/halfgauge.html) | Display input value on semicircular scale  
[Knob](https://uk.mathworks.com/help/simulink/slref/knob.html) | Tune parameter value with dial  
[Lamp](https://uk.mathworks.com/help/simulink/slref/lamp.html) | Display color that reflects signal value on lamp  
[Linear Gauge](https://uk.mathworks.com/help/simulink/slref/lineargauge.html) | Display input value on linear scale  
[MultiStateImage](https://uk.mathworks.com/help/simulink/slref/multistateimage.html) | Display image reflecting input value  
[Push Button](https://uk.mathworks.com/help/simulink/slref/pushbutton.html) | Change parameter or variable value using button  
[Quarter Gauge](https://uk.mathworks.com/help/simulink/slref/quartergauge.html) | Display input value on quadrant scale  
[Radio Button](https://uk.mathworks.com/help/simulink/slref/radiobutton.html) | Select parameter value  
[Rocker Switch](https://uk.mathworks.com/help/simulink/slref/rockerswitch.html) | Toggle parameter between two values  
[Rotary Switch](https://uk.mathworks.com/help/simulink/slref/rotaryswitch.html) | Switch parameter to set values on dial  
[Slider](https://uk.mathworks.com/help/simulink/slref/slider.html) | Tune parameter value with sliding scale  
[Slider Switch](https://uk.mathworks.com/help/simulink/slref/sliderswitch.html) | Toggle parameter between two values  
[Toggle Switch](https://uk.mathworks.com/help/simulink/slref/toggleswitch.html) | Toggle parameter between two values  
#### Customizable Blocks
Name|Description
---|---
[Callback Button](https://uk.mathworks.com/help/simulink/slref/customcallbackbutton.html) | Execute MATLAB code using button with customizable appearance _(Since R2021b)_  
[Check Box](https://uk.mathworks.com/help/simulink/slref/customcheckbox.html) | Change parameter or variable value during simulation using check box with customizable appearance _(Since R2024b)_  
[Circular Gauge](https://uk.mathworks.com/help/simulink/slref/circulargauge.html) | Display signal value during simulation on circular gauge with customizable appearance  
[Combo Box](https://uk.mathworks.com/help/simulink/slref/customcombobox.html) | Change parameter or variable value during simulation using combo box with customizable appearance _(Since R2025a)_  
[Display](https://uk.mathworks.com/help/simulink/slref/customdisplay.html) | Display signal value during simulation with customizable appearance _(Since R2023b)_  
[Half Gauge](https://uk.mathworks.com/help/simulink/slref/customhalfgauge.html) | Display signal value during simulation on gauge shaped as half-circle with customizable appearance _(Since R2024a)_  
[Horizontal Gauge](https://uk.mathworks.com/help/simulink/slref/horizontalgauge.html) | Display signal value during simulation on horizontal gauge with customizable appearance  
[Horizontal Slider](https://uk.mathworks.com/help/simulink/slref/horizontalslider.html) | Change parameter or variable value using horizontal slider with customizable appearance _(Since R2021a)_  
[Knob](https://uk.mathworks.com/help/simulink/slref/customknob.html) |  Change parameter or variable value using knob with customizable appearance _(Since R2021a)_  
[Lamp](https://uk.mathworks.com/help/simulink/slref/customlamp.html) | Display color that reflects signal value on lamp with customizable appearance _(Since R2021b)_  
[Push Button](https://uk.mathworks.com/help/simulink/slref/custompushbutton.html) | Change parameter or variable value using button with customizable appearance _(Since R2021b)_  
[Quarter Gauge](https://uk.mathworks.com/help/simulink/slref/customquartergauge.html) | Display signal value during simulation on gauge shaped as quarter-circle with customizable appearance _(Since R2024a)_  
[Radio Button](https://uk.mathworks.com/help/simulink/slref/customradiobutton.html) | Change parameter or variable value during simulation using radio button with customizable appearance _(Since R2025a)_  
[Rocker Switch](https://uk.mathworks.com/help/simulink/slref/customrockerswitch.html) | Change parameter or variable value using switch with customizable appearance _(Since R2021b)_  
[Rotary Switch](https://uk.mathworks.com/help/simulink/slref/customrotaryswitch.html) | Change parameter or variable value using rotary switch with customizable appearance _(Since R2021b)_  
[Slider Switch](https://uk.mathworks.com/help/simulink/slref/customsliderswitch.html) | Change parameter or variable value using switch with customizable appearance _(Since R2021b)_  
[Toggle Switch](https://uk.mathworks.com/help/simulink/slref/customtoggleswitch.html) | Change parameter or variable value using switch with customizable appearance _(Since R2021b)_  
[Vertical Gauge](https://uk.mathworks.com/help/simulink/slref/verticalgauge.html) | Display signal value during simulation on vertical gauge with customizable appearance  
[Vertical Slider](https://uk.mathworks.com/help/simulink/slref/verticalslider.html) | Change parameter or variable value using vertical slider with customizable appearance _(Since R2021a)_  
#### Discontinuities
Name|Description
---|---
[Backlash](https://uk.mathworks.com/help/simulink/slref/backlash.html) | Model behavior of system with play  
[Coulomb and Viscous Friction](https://uk.mathworks.com/help/simulink/slref/coulombandviscousfriction.html) | Model discontinuity at zero, with linear gain elsewhere  
[Dead Zone](https://uk.mathworks.com/help/simulink/slref/deadzone.html) | Provide region of zero output  
[Dead Zone Dynamic](https://uk.mathworks.com/help/simulink/slref/deadzonedynamic.html) | Provide dynamic region of zero output  
[Hit Crossing](https://uk.mathworks.com/help/simulink/slref/hitcrossing.html) | Detect crossing point  
[PWM](https://uk.mathworks.com/help/simulink/slref/pwm.html) | Generate ideal pulse width modulated signal corresponding to input duty cycle  
[Quantizer](https://uk.mathworks.com/help/simulink/slref/quantizer.html) | Discretize input at given interval  
[Rate Limiter](https://uk.mathworks.com/help/simulink/slref/ratelimiter.html) | Limit rate of change of signal  
[Rate Limiter Dynamic](https://uk.mathworks.com/help/simulink/slref/ratelimiterdynamic.html) | Limit rate of change of signal  
[Relay](https://uk.mathworks.com/help/simulink/slref/relay.html) | Switch output between two constants  
[Saturation](https://uk.mathworks.com/help/simulink/slref/saturation.html) | Limit input signal to the upper and lower saturation values  
[Saturation Dynamic](https://uk.mathworks.com/help/simulink/slref/saturationdynamic.html) | Limit input signal to dynamic upper and lower saturation values  
[Variable Pulse Generator](https://uk.mathworks.com/help/simulink/slref/variablepulsegenerator.html) | Generate ideal, time varying pulse signal  
[Wrap To Zero](https://uk.mathworks.com/help/simulink/slref/wraptozero.html) | Set output to zero if input is above threshold  
#### Discrete
Name|Description
---|---
[Delay](https://uk.mathworks.com/help/simulink/slref/delay.html) | Delay input signal by fixed or variable sample periods  
[Difference](https://uk.mathworks.com/help/simulink/slref/difference.html) | Calculate change in signal over one time step  
[Discrete Derivative](https://uk.mathworks.com/help/simulink/slref/discretederivative.html) | Compute discrete-time derivative  
[Discrete Filter](https://uk.mathworks.com/help/simulink/slref/discretefilter.html) | Model Infinite Impulse Response (IIR) filters  
[Discrete FIR Filter](https://uk.mathworks.com/help/simulink/slref/discretefirfilter.html) | Model FIR filters  
[Discrete PID Controller](https://uk.mathworks.com/help/simulink/slref/discretepidcontroller.html) | Discrete-time or continuous-time PID controller  
[Discrete PID Controller (2DOF)](https://uk.mathworks.com/help/simulink/slref/discretepidcontroller2dof.html) | Discrete-time or continuous-time two-degree-of-freedom PID controller  
[Discrete State-Space](https://uk.mathworks.com/help/simulink/slref/discretestatespace.html) | Implement discrete state-space system  
[Discrete Transfer Fcn](https://uk.mathworks.com/help/simulink/slref/discretetransferfcn.html) | Implement discrete transfer function  
[Discrete Zero-Pole](https://uk.mathworks.com/help/simulink/slref/discretezeropole.html) | Model system defined by zeros and poles of discrete transfer function  
[Discrete-Time Integrator](https://uk.mathworks.com/help/simulink/slref/discretetimeintegrator.html) | Perform discrete-time integration or accumulation of signal  
[Memory](https://uk.mathworks.com/help/simulink/slref/memory.html) | Output input from previous time step  
[Propagation Delay](https://uk.mathworks.com/help/simulink/slref/propagationdelay.html) | Model loop delay, latency, pulse delay _(Since R2022b)_  
[Resettable Delay](https://uk.mathworks.com/help/simulink/slref/resettabledelay.html) | Delay input signal by variable sample period and reset with external signal  
[Tapped Delay](https://uk.mathworks.com/help/simulink/slref/tappeddelay.html) | Delay scalar signal multiple sample periods and output all delayed versions  
[Transfer Fcn First Order](https://uk.mathworks.com/help/simulink/slref/transferfcnfirstorder.html) | Implement discrete-time first order transfer function  
[Transfer Fcn Lead or Lag](https://uk.mathworks.com/help/simulink/slref/transferfcnleadorlag.html) | Implement discrete-time lead or lag compensator  
[Transfer Fcn Real Zero](https://uk.mathworks.com/help/simulink/slref/transferfcnrealzero.html) | Implement discrete-time transfer function that has real zero and no pole  
[Unit Delay](https://uk.mathworks.com/help/simulink/slref/unitdelay.html) | Delay signal one sample period  
[Variable Integer Delay](https://uk.mathworks.com/help/simulink/slref/variableintegerdelay.html) | Delay input signal by variable sample period  
[Zero-Order Hold](https://uk.mathworks.com/help/simulink/slref/zeroorderhold.html) | Implement zero-order hold sample period  
#### Logic and Bit Operations
Name|Description
---|---
[Bit Clear](https://uk.mathworks.com/help/simulink/slref/bitclear.html) | Set specified bit of stored integer to zero  
[Bit Set](https://uk.mathworks.com/help/simulink/slref/bitset.html) | Set specified bit of stored integer to one  
[Bit to Integer Converter](https://uk.mathworks.com/help/simulink/slref/bittointegerconverter.html) | Map vector of bits to corresponding vector of integers  
[Bitwise Operator](https://uk.mathworks.com/help/simulink/slref/bitwiseoperator.html) | Specified bitwise operation on inputs  
[Combinatorial Logic](https://uk.mathworks.com/help/simulink/slref/combinatoriallogic.html) | Implement truth table  
[Compare To Constant](https://uk.mathworks.com/help/simulink/slref/comparetoconstant.html) | Determine how signal compares to specified constant  
[Compare To Zero](https://uk.mathworks.com/help/simulink/slref/comparetozero.html) | Determine how signal compares to zero  
[Detect Change](https://uk.mathworks.com/help/simulink/slref/detectchange.html) | Detect change in signal value  
[Detect Decrease](https://uk.mathworks.com/help/simulink/slref/detectdecrease.html) | Detect decrease in signal value  
[Detect Fall Negative](https://uk.mathworks.com/help/simulink/slref/detectfallnegative.html) | Detect falling edge when signal value decreases to strictly negative value, and its previous value was nonnegative  
[Detect Fall Nonpositive](https://uk.mathworks.com/help/simulink/slref/detectfallnonpositive.html) | Detect falling edge when signal value decreases to nonpositive value, and its previous value was strictly positive  
[Detect Increase](https://uk.mathworks.com/help/simulink/slref/detectincrease.html) | Detect increase in signal value  
[Detect Rise Nonnegative](https://uk.mathworks.com/help/simulink/slref/detectrisenonnegative.html) | Detect rising edge when signal value increases to nonnegative value, and its previous value was strictly negative  
[Detect Rise Positive](https://uk.mathworks.com/help/simulink/slref/detectrisepositive.html) | Detect rising edge when signal value increases to strictly positive value, and its previous value was nonpositive  
[Extract Bits](https://uk.mathworks.com/help/simulink/slref/extractbits.html) | Output selection of contiguous bits from input signal  
[Float Extract Bits](https://uk.mathworks.com/help/simulink/slref/floatextractbits.html) | Extract bits from floating-point input samples _(Since R2023a)_  
[Integer to Bit Converter](https://uk.mathworks.com/help/simulink/slref/integertobitconverter.html) | Map vector of integers to vector of bits  
[Interval Test](https://uk.mathworks.com/help/simulink/slref/intervaltest.html) | Determine if signal is in specified interval  
[Interval Test Dynamic](https://uk.mathworks.com/help/simulink/slref/intervaltestdynamic.html) | Determine if signal is in specified interval  
[Logical Operator](https://uk.mathworks.com/help/simulink/slref/logicaloperator.html) | Perform specified logical operation on input  
[Relational Operator](https://uk.mathworks.com/help/simulink/slref/relationaloperator.html) | Perform specified relational operation on inputs  
[Shift Arithmetic](https://uk.mathworks.com/help/simulink/slref/shiftarithmetic.html) | Shift bits or binary point of signal  
#### Lookup Tables
Name|Description
---|---
[1-D Lookup Table](https://uk.mathworks.com/help/simulink/slref/1dlookuptable.html) | Approximate one-dimensional function  
[2-D Lookup Table](https://uk.mathworks.com/help/simulink/slref/2dlookuptable.html) | Approximate two-dimensional function  
[Direct Lookup Table (n-D)](https://uk.mathworks.com/help/simulink/slref/directlookuptablend.html) | Index into n-dimensional table to retrieve element, vector, or 2-D matrix  
[Interpolation Using Prelookup](https://uk.mathworks.com/help/simulink/slref/interpolationusingprelookup.html) | Use precalculated index and fraction values to accelerate approximation of N-dimensional function  
[Lookup Table Dynamic](https://uk.mathworks.com/help/simulink/slref/lookuptabledynamic.html) | Approximate a one-dimensional function using dynamic table  
[n-D Lookup Table](https://uk.mathworks.com/help/simulink/slref/ndlookuptable.html) | Approximate n-dimensional function  
[Prelookup](https://uk.mathworks.com/help/simulink/slref/prelookup.html) | Compute index and fraction for Interpolation Using Prelookup block  
[Sine](https://uk.mathworks.com/help/simulink/slref/sine.html) | Implement fixed-point sine or cosine wave using lookup table approach that exploits quarter wave symmetry  
#### Math Operations
Name|Description
---|---
[Abs](https://uk.mathworks.com/help/simulink/slref/abs.html) | Output absolute value of input  
[Algebraic Constraint](https://uk.mathworks.com/help/simulink/slref/algebraicconstraint.html) | Constrain input signal  
[Assignment](https://uk.mathworks.com/help/simulink/slref/assignment.html) | Assign values to specified elements of signal  
[Bias](https://uk.mathworks.com/help/simulink/slref/bias.html) | Add bias to input  
[Complex to Magnitude-Angle](https://uk.mathworks.com/help/simulink/slref/complextomagnitudeangle.html) | Compute magnitude and/or phase angle of complex signal  
[Complex to Real-Imag](https://uk.mathworks.com/help/simulink/slref/complextorealimag.html) | Output real and imaginary parts of complex input signal  
[Divide](https://uk.mathworks.com/help/simulink/slref/divide.html) | Divide one input by another  
[Dot Product](https://uk.mathworks.com/help/simulink/slref/dotproduct.html) | Generate dot product of two vectors  
[Find Nonzero Elements](https://uk.mathworks.com/help/simulink/slref/findnonzeroelements.html) | Find nonzero elements in array  
[Gain](https://uk.mathworks.com/help/simulink/slref/gain.html) | Multiply input by constant  
[Magnitude-Angle to Complex](https://uk.mathworks.com/help/simulink/slref/magnitudeangletocomplex.html) | Convert magnitude and/or a phase angle signal to complex signal  
[Math Function](https://uk.mathworks.com/help/simulink/slref/mathfunction.html) | Perform mathematical function  
[Matrix Concatenate](https://uk.mathworks.com/help/simulink/slref/matrixconcatenate.html) | Concatenate input matrices of same data type for iterative processing  
[MinMax](https://uk.mathworks.com/help/simulink/slref/minmax.html) | Output minimum or maximum input value  
[MinMax Running Resettable](https://uk.mathworks.com/help/simulink/slref/minmaxrunningresettable.html) | Determine minimum or maximum of signal over time  
[Permute Dimensions](https://uk.mathworks.com/help/simulink/slref/permutedimensions.html) | Rearrange dimensions of multidimensional array dimensions  
[Polynomial](https://uk.mathworks.com/help/simulink/slref/polynomial.html) | Perform evaluation of polynomial coefficients on input values  
[Product of Elements](https://uk.mathworks.com/help/simulink/slref/productofelements.html) | Copy or invert one scalar input, or collapse one nonscalar input  
[Product, Matrix Multiply](https://uk.mathworks.com/help/simulink/slref/product.html) | Multiply and divide scalars and nonscalars or multiply and invert matrices  
[Real-Imag to Complex](https://uk.mathworks.com/help/simulink/slref/realimagtocomplex.html) | Convert real and/or imaginary inputs to complex signal  
[Reshape](https://uk.mathworks.com/help/simulink/slref/reshape.html) | Change dimensionality of signal  
[Rounding Function](https://uk.mathworks.com/help/simulink/slref/roundingfunction.html) | Apply rounding function to signal  
[Sign](https://uk.mathworks.com/help/simulink/slref/sign.html) | Indicate sign of input  
[Sine Wave Function](https://uk.mathworks.com/help/simulink/slref/sinewavefunction.html) | Generate sine wave, using external signal as time source  
[Slider Gain](https://uk.mathworks.com/help/simulink/slref/slidergain.html) | Vary scalar gain using slider  
[Sqrt](https://uk.mathworks.com/help/simulink/slref/sqrt.html) | Calculate square root, signed square root, or reciprocal of square root  
[Squeeze](https://uk.mathworks.com/help/simulink/slref/squeeze.html) | Remove singleton dimensions from multidimensional signal  
[Sum](https://uk.mathworks.com/help/simulink/slref/sum.html) | Add or subtract inputs  
[Trigonometric Function](https://uk.mathworks.com/help/simulink/slref/trigonometricfunction.html) | Specified trigonometric function on input  
[Unary Minus](https://uk.mathworks.com/help/simulink/slref/unaryminus.html) | Negate input  
[Vector Concatenate](https://uk.mathworks.com/help/simulink/slref/vectorconcatenate.html) | Concatenate input vectors of same data type for iterative processing  
[Weighted Sample Time Math](https://uk.mathworks.com/help/simulink/slref/weightedsampletimemath.html) | Support calculations involving sample time  
#### Matrix Operations
Name|Description
---|---
[Array Processing Subsystem](https://uk.mathworks.com/help/simulink/slref/arrayprocessingsubsystem.html) | Apply algorithm to each element of a matrix _(Since R2024a)_  
[Create Diagonal Matrix](https://uk.mathworks.com/help/simulink/slref/creatediagonalmatrix.html) | Create square diagonal matrix from diagonal elements  
[Cross Product](https://uk.mathworks.com/help/simulink/slref/crossproduct.html) | Cross product of two vectors _(Since R2021b)_  
[Expand Scalar](https://uk.mathworks.com/help/simulink/slref/expandscalar.html) | Create matrix from scalar using scalar expansion _(Since R2024a)_  
[Extract Diagonal](https://uk.mathworks.com/help/simulink/slref/extractdiagonal.html) | Extract main diagonal of input matrix  
[Hermitian Transpose](https://uk.mathworks.com/help/simulink/slref/hermitiantranspose.html) | Compute hermitian transpose of matrix _(Since R2021b)_  
[Identity Matrix](https://uk.mathworks.com/help/simulink/slref/identitymatrix.html) | Generate matrix with ones on main diagonal and ground values elsewhere _(Since R2021b)_  
[IsHermitian](https://uk.mathworks.com/help/simulink/slref/ishermitian.html) | Check if matrix is Hermitian or skew-Hermitian _(Since R2022a)_  
[IsSymmetric](https://uk.mathworks.com/help/simulink/slref/issymmetric.html) | Check if matrix is symmetric or skew-symmetric _(Since R2021b)_  
[IsTriangular](https://uk.mathworks.com/help/simulink/slref/istriangular.html) | Check if matrix is upper or lower triangular _(Since R2021b)_  
[Matrix Concatenate](https://uk.mathworks.com/help/simulink/slref/matrixconcatenate.html) | Concatenate input matrices of same data type for iterative processing  
[Matrix Square](https://uk.mathworks.com/help/simulink/slref/matrixsquare.html) | Compute square of input matrix  
[Neighborhood Processing Subsystem](https://uk.mathworks.com/help/simulink/slref/neighborhoodprocessingsubsystem.html) | Create algorithm that follows the neighborhood pattern _(Since R2022b)_  
[Permute Matrix](https://uk.mathworks.com/help/simulink/slref/permutematrix.html) | Reorder matrix rows or columns  
[Pixel Processing Subsystem](https://uk.mathworks.com/help/simulink/slref/pixelprocessingsubsystem.html) | Create algorithm that converts multichannel image data to single-channel _(Since R2024a)_  
[Product, Matrix Multiply](https://uk.mathworks.com/help/simulink/slref/product.html) | Multiply and divide scalars and nonscalars or multiply and invert matrices  
[Submatrix](https://uk.mathworks.com/help/simulink/slref/submatrix.html) | Select subset of elements (submatrix) from matrix input  
[Transpose](https://uk.mathworks.com/help/simulink/slref/transpose.html) | Compute transpose of matrix _(Since R2021b)_  
#### Messages & Events
Name|Description
---|---
[Hit Crossing](https://uk.mathworks.com/help/simulink/slref/hitcrossing.html) | Detect crossing point  
[Hit Scheduler](https://uk.mathworks.com/help/simulink/slref/hitscheduler.html) | Schedule major time steps for variable-step solver _(Since R2022b)_  
[Message Merge](https://uk.mathworks.com/help/simulink/slref/messagemerge.html) | Combine message paths _(Since R2021a)_  
[Message Triggered Subsystem](https://uk.mathworks.com/help/simulink/slref/messagetriggeredsubsystem.html) | Subsystem whose execution is controlled by message input _(Since R2022a)_  
[Queue](https://uk.mathworks.com/help/simulink/slref/queue.html) | Enqueue messages and entities  
[Receive](https://uk.mathworks.com/help/simulink/slref/receive.html) | Receive messages  
[Send](https://uk.mathworks.com/help/simulink/slref/send.html) | Create and send message  
[Sequence Viewer](https://uk.mathworks.com/help/simulink/slref/sequenceviewer.html) | Display messages, events, states, transitions, and functions between blocks during simulation  
#### Model Verification
Name|Description
---|---
[Assertion](https://uk.mathworks.com/help/simulink/slref/assertion.html) | Check whether signal is zero  
[Check Discrete Gradient](https://uk.mathworks.com/help/simulink/slref/checkdiscretegradient.html) | Check that absolute value of difference between successive samples of discrete signal is less than specified value  
[Check Dynamic Gap](https://uk.mathworks.com/help/simulink/slref/checkdynamicgap.html) | Check that gap of possibly varying width occurs in range of signal's amplitudes  
[Check Dynamic Lower Bound](https://uk.mathworks.com/help/simulink/slref/checkdynamiclowerbound.html) | Check that one signal is always less than another signal  
[Check Dynamic Range](https://uk.mathworks.com/help/simulink/slref/checkdynamicrange.html) | Check that signal falls inside range of amplitudes that varies from time step to time step  
[Check Dynamic Upper Bound](https://uk.mathworks.com/help/simulink/slref/checkdynamicupperbound.html) | Check that one signal is always greater than another signal  
[Check Input Resolution](https://uk.mathworks.com/help/simulink/slref/checkinputresolution.html) | Check that input signal has specified resolution  
[Check Static Gap](https://uk.mathworks.com/help/simulink/slref/checkstaticgap.html) | Check that gap exists in signal's range of amplitudes  
[Check Static Lower Bound](https://uk.mathworks.com/help/simulink/slref/checkstaticlowerbound.html) | Check that signal is greater than (or optionally equal to) static lower bound  
[Check Static Range](https://uk.mathworks.com/help/simulink/slref/checkstaticrange.html) | Check that signal falls inside fixed range of amplitudes  
[Check Static Upper Bound](https://uk.mathworks.com/help/simulink/slref/checkstaticupperbound.html) | Check that signal is less than (or optionally equal to) static upper bound  
#### Model-Wide Utilities
Name|Description
---|---
[Block Support Table](https://uk.mathworks.com/help/simulink/slref/blocksupporttable.html) | View data type support for Simulink blocks  
[DocBlock](https://uk.mathworks.com/help/simulink/slref/docblock.html) | Create text that documents model and save text with model  
[Model Info](https://uk.mathworks.com/help/simulink/slref/modelinfo.html) | Display model properties and text in model  
[Timed-Based Linearization](https://uk.mathworks.com/help/simulink/slref/timedbasedlinearization.html) | Generate linear models in base workspace at specific times  
[Trigger-Based Linearization](https://uk.mathworks.com/help/simulink/slref/triggerbasedlinearization.html) | Generate linear models in base workspace when triggered  
#### Ports and Subsystems
Name|Description
---|---
[Enable](https://uk.mathworks.com/help/simulink/slref/enable.html) | Add enable port to subsystem or model  
[Enabled and Triggered Subsystem](https://uk.mathworks.com/help/simulink/slref/enabledandtriggeredsubsystem.html) | Subsystem whose execution is enabled and triggered by external inputs  
[Enabled Subsystem](https://uk.mathworks.com/help/simulink/slref/enabledsubsystem.html) | Subsystem whose execution is enabled by external input  
[For Each Subsystem](https://uk.mathworks.com/help/simulink/slref/foreachsubsystem.html) | Apply algorithm to individual elements or subarrays of input signals or mask parameters  
[For Iterator Subsystem](https://uk.mathworks.com/help/simulink/slref/foriteratorsubsystem.html) |  Repeat subsystem execution during simulation time step for specified number of iterations  
[Function Element](https://uk.mathworks.com/help/simulink/slref/functionelement.html) | Specify function to be called via exporting function port _(Since R2022a)_  
[Function Element Call](https://uk.mathworks.com/help/simulink/slref/functionelementcall.html) | Specify function call to be issued via invoking function port _(Since R2022a)_  
[Function-Call Feedback Latch](https://uk.mathworks.com/help/simulink/slref/functioncallfeedbacklatch.html) | Break feedback loop involving data signals between function-call blocks  
[Function-Call Generator](https://uk.mathworks.com/help/simulink/slref/functioncallgenerator.html) | Provide function-call events to control execution of subsystem or model  
[Function-Call Split](https://uk.mathworks.com/help/simulink/slref/functioncallsplit.html) | Provide junction for splitting function-call line  
[Function-Call Subsystem](https://uk.mathworks.com/help/simulink/slref/functioncallsubsystem.html) | Subsystem whose execution is controlled by external function-call input  
[If](https://uk.mathworks.com/help/simulink/slref/if.html) | Select subsystem execution using logic similar to `if-else` statement  
[If Action Subsystem](https://uk.mathworks.com/help/simulink/slref/ifactionsubsystem.html) | Subsystem whose execution is enabled by If block  
[In Bus Element](https://uk.mathworks.com/help/simulink/slref/inbuselement.html) | Select input from external port  
[Inport](https://uk.mathworks.com/help/simulink/slref/inport.html) | Create input port for subsystem or external input  
[Model](https://uk.mathworks.com/help/simulink/slref/model.html) | Reference another model to create model hierarchy  
[Out Bus Element](https://uk.mathworks.com/help/simulink/slref/outbuselement.html) | Specify output of external port  
[Outport](https://uk.mathworks.com/help/simulink/slref/outport.html) | Create output port for subsystem or external output  
[Resettable Subsystem](https://uk.mathworks.com/help/simulink/slref/resettablesubsystem.html) |  Subsystem whose block states reset with external trigger  
[Subsystem](https://uk.mathworks.com/help/simulink/slref/subsystem.html) | Group blocks to create model hierarchy  
[Switch Case](https://uk.mathworks.com/help/simulink/slref/switchcase.html) | Select subsystem execution using logic similar to `switch` statement  
[Switch Case Action Subsystem](https://uk.mathworks.com/help/simulink/slref/switchcaseactionsubsystem.html) | Subsystem whose execution is enabled by Switch Case block  
[Trigger](https://uk.mathworks.com/help/simulink/slref/trigger.html) | Add trigger or function port to subsystem or model  
[Triggered Subsystem](https://uk.mathworks.com/help/simulink/slref/triggeredsubsystem.html) | Subsystem whose execution is triggered by external input  
[Unit System Configuration](https://uk.mathworks.com/help/simulink/slref/unitsystemconfiguration.html) | Restrict units to specified allowed unit systems  
[Variant Subsystem](https://uk.mathworks.com/help/simulink/slref/variantsubsystem.html) | Template subsystem containing Subsystem blocks as variant choices  
[While Iterator Subsystem](https://uk.mathworks.com/help/simulink/slref/whileiteratorsubsystem.html) |  Repeat subsystem execution during simulation time step while logical expression is true  
#### Signal Attributes
Name|Description
---|---
[Bus to Vector](https://uk.mathworks.com/help/simulink/slref/bustovector.html) | Convert virtual bus to vector  
[Data Type Conversion](https://uk.mathworks.com/help/simulink/slref/datatypeconversion.html) | Convert input signal to specified data type  
[Data Type Conversion Inherited](https://uk.mathworks.com/help/simulink/slref/datatypeconversioninherited.html) | Convert from one data type to another using inherited data type and scaling  
[Data Type Duplicate](https://uk.mathworks.com/help/simulink/slref/datatypeduplicate.html) | Force all inputs to same data type  
[Data Type Propagation](https://uk.mathworks.com/help/simulink/slref/datatypepropagation.html) | Set data type and scaling of propagated signal based on information from reference signals  
[Data Type Scaling Strip](https://uk.mathworks.com/help/simulink/slref/datatypescalingstrip.html) | Remove scaling and map to built in integer  
[IC](https://uk.mathworks.com/help/simulink/slref/ic.html) | Set initial value of signal  
[Probe](https://uk.mathworks.com/help/simulink/slref/probe.html) | Output signal attributes, including width, dimensionality, sample time, and complex signal flag  
[Rate Transition](https://uk.mathworks.com/help/simulink/slref/ratetransition.html) | Handle transfer of data between blocks operating at different rates  
[Signal Conversion](https://uk.mathworks.com/help/simulink/slref/signalconversion.html) | Convert signal to new type without altering signal values  
[Signal Specification](https://uk.mathworks.com/help/simulink/slref/signalspecification.html) | Specify desired dimensions, sample time, data type, numeric type, and other attributes of signal  
[Unit Conversion](https://uk.mathworks.com/help/simulink/slref/unitconversion.html) | Convert units  
[Weighted Sample Time](https://uk.mathworks.com/help/simulink/slref/weightedsampletime.html) | Support calculations involving sample time  
[Width](https://uk.mathworks.com/help/simulink/slref/width.html) | Output width of input vector  
#### Signal Routing
Name|Description
---|---
[Bus Assignment](https://uk.mathworks.com/help/simulink/slref/busassignment.html) | Assign new values to specified bus elements  
[Bus Creator](https://uk.mathworks.com/help/simulink/slref/buscreator.html) | Group input signals, buses, or messages into bus  
[Bus Selector](https://uk.mathworks.com/help/simulink/slref/busselector.html) | Select elements from input bus  
[Data Store Memory](https://uk.mathworks.com/help/simulink/slref/datastorememory.html) | Define data store  
[Data Store Read](https://uk.mathworks.com/help/simulink/slref/datastoreread.html) | Read data from data store  
[Data Store Write](https://uk.mathworks.com/help/simulink/slref/datastorewrite.html) | Write data to data store  
[Demux](https://uk.mathworks.com/help/simulink/slref/demux.html) | Extract and output elements of virtual vector signal  
[Environment Controller](https://uk.mathworks.com/help/simulink/slref/environmentcontroller.html) | (Removed) Create branches of block diagram that apply only to simulation or only to code generation  
[From](https://uk.mathworks.com/help/simulink/slref/from.html) | Accept input from Goto block  
[Goto](https://uk.mathworks.com/help/simulink/slref/goto.html) | Pass block input to From blocks  
[Goto Tag Visibility](https://uk.mathworks.com/help/simulink/slref/gototagvisibility.html) | Define scope of Goto block tag  
[Index Vector](https://uk.mathworks.com/help/simulink/slref/indexvector.html) | Switch output between different inputs based on value of first input  
[Manual Switch](https://uk.mathworks.com/help/simulink/slref/manualswitch.html) | Switch between two inputs  
[Manual Variant Sink](https://uk.mathworks.com/help/simulink/slref/manualvariantsink.html) | Switch between multiple variant choices at output  
[Manual Variant Source](https://uk.mathworks.com/help/simulink/slref/manualvariantsource.html) | Switch between multiple variant choices at input  
[Merge](https://uk.mathworks.com/help/simulink/slref/merge.html) | Combine multiple signals into single signal  
[Multiport Switch](https://uk.mathworks.com/help/simulink/slref/multiportswitch.html) | Select output signal based on control signal  
[Mux](https://uk.mathworks.com/help/simulink/slref/mux.html) | Combine input signals of same data type and complexity into virtual vector  
[Parameter Writer](https://uk.mathworks.com/help/simulink/slref/parameterwriter.html) | Write to block parameter or variable  
[Selector](https://uk.mathworks.com/help/simulink/slref/selector.html) | Select input elements from vector, matrix, or multidimensional signal  
[State Reader](https://uk.mathworks.com/help/simulink/slref/statereader.html) | Read a block state  
[State Writer](https://uk.mathworks.com/help/simulink/slref/statewriter.html) | Write to a block state  
[Switch](https://uk.mathworks.com/help/simulink/slref/switch.html) | Switch output between first input and third input based on value of second input  
[Variant End](https://uk.mathworks.com/help/simulink/slref/variantend.html) | Define end of bounded region _(Since R2024a)_  
[Variant Sink](https://uk.mathworks.com/help/simulink/slref/variantsink.html) | Route amongst multiple outputs using variants  
[Variant Source](https://uk.mathworks.com/help/simulink/slref/variantsource.html) | Route among multiple inputs using variants  
[Variant Start](https://uk.mathworks.com/help/simulink/slref/variantstart.html) | Define start of bounded region _(Since R2024a)_  
[Vector Concatenate](https://uk.mathworks.com/help/simulink/slref/vectorconcatenate.html) | Concatenate input vectors of same data type for iterative processing  
#### Sinks
Name|Description
---|---
[Display](https://uk.mathworks.com/help/simulink/slref/display.html) | Show value of input  
[Floating Scope and Scope Viewer](https://uk.mathworks.com/help/simulink/slref/scopeviewer.html) | Display signals generated during simulation without signal lines  
[Out Bus Element](https://uk.mathworks.com/help/simulink/slref/outbuselement.html) | Specify output of external port  
[Outport](https://uk.mathworks.com/help/simulink/slref/outport.html) | Create output port for subsystem or external output  
[Record](https://uk.mathworks.com/help/simulink/slref/record.html) | View and log data to the workspace, a file, or both _(Since R2021a)_  
[Scope](https://uk.mathworks.com/help/simulink/slref/scope.html) | Display signals generated during simulation  
[Stop Simulation](https://uk.mathworks.com/help/simulink/slref/stopsimulation.html) | Stop simulation when input is nonzero  
[Terminator](https://uk.mathworks.com/help/simulink/slref/terminator.html) | Terminate unconnected output port  
[To File](https://uk.mathworks.com/help/simulink/slref/tofile.html) | Write data to file  
[To Workspace](https://uk.mathworks.com/help/simulink/slref/toworkspace.html) | Log data to workspace from Simulink model  
#### Sources
Name|Description
---|---
[Band-Limited White Noise](https://uk.mathworks.com/help/simulink/slref/bandlimitedwhitenoise.html) | Introduce white noise into continuous system  
[Chirp Signal](https://uk.mathworks.com/help/simulink/slref/chirpsignal.html) | Generate sine wave with increasing frequency  
[Clock](https://uk.mathworks.com/help/simulink/slref/clock.html) | Display and provide simulation time  
[Constant](https://uk.mathworks.com/help/simulink/slref/constant.html) | Constant value  
[Counter Free-Running](https://uk.mathworks.com/help/simulink/slref/counterfreerunning.html) | Count up and overflow back to zero after reaching maximum value for specified number of bits  
[Counter Limited](https://uk.mathworks.com/help/simulink/slref/counterlimited.html) | Count up and wrap to zero after specified upper limit  
[Digital Clock](https://uk.mathworks.com/help/simulink/slref/digitalclock.html) | Output simulation time at specified sampling interval  
[Enumerated Constant](https://uk.mathworks.com/help/simulink/slref/enumeratedconstant.html) | Generate enumerated constant value  
[From File](https://uk.mathworks.com/help/simulink/slref/fromfile.html) | Load data from MAT file into Simulink model  
[From Spreadsheet](https://uk.mathworks.com/help/simulink/slref/fromspreadsheet.html) | Read data from spreadsheet  
[From Workspace](https://uk.mathworks.com/help/simulink/slref/fromworkspace.html) | Load signal data from workspace into Simulink model  
[Ground](https://uk.mathworks.com/help/simulink/slref/ground.html) | Ground unconnected input port  
[In Bus Element](https://uk.mathworks.com/help/simulink/slref/inbuselement.html) | Select input from external port  
[Inport](https://uk.mathworks.com/help/simulink/slref/inport.html) | Create input port for subsystem or external input  
[Playback](https://uk.mathworks.com/help/simulink/slref/playback.html) | Load data from workspace, file, or Simulation Data Inspector _(Since R2022b)_  
[Pulse Generator](https://uk.mathworks.com/help/simulink/slref/pulsegenerator.html) | Generate square wave pulses at regular intervals  
[Ramp](https://uk.mathworks.com/help/simulink/slref/ramp.html) | Generate constantly increasing or decreasing signal  
[Random Number](https://uk.mathworks.com/help/simulink/slref/randomnumber.html) | Generate normally distributed random numbers  
[Repeating Sequence](https://uk.mathworks.com/help/simulink/slref/repeatingsequence.html) | Generate arbitrarily shaped periodic signal  
[Repeating Sequence Interpolated](https://uk.mathworks.com/help/simulink/slref/repeatingsequenceinterpolated.html) | Output discrete-time sequence and repeat, interpolating between data points  
[Repeating Sequence Stair](https://uk.mathworks.com/help/simulink/slref/repeatingsequencestair.html) | Output and repeat discrete time sequence  
[Signal Editor](https://uk.mathworks.com/help/simulink/slref/signaleditorblock.html) | Display, create, edit, and switch interchangeable scenarios  
[Signal Generator](https://uk.mathworks.com/help/simulink/slref/signalgenerator.html) | Generate various waveforms  
[Sine Wave](https://uk.mathworks.com/help/simulink/slref/sinewave.html) | Generate sine wave, using simulation time as time source  
[Step](https://uk.mathworks.com/help/simulink/slref/step.html) | Generate step function  
[Uniform Random Number](https://uk.mathworks.com/help/simulink/slref/uniformrandomnumber.html) | Generate uniformly distributed random numbers  
[Waveform Generator](https://uk.mathworks.com/help/simulink/slref/waveformgenerator.html) | Output waveforms using signal notations  
#### String
Name|Description
---|---
[ASCII to String](https://uk.mathworks.com/help/simulink/slref/asciitostring.html) | Uint8 vector signal to string signal  
[Compose String](https://uk.mathworks.com/help/simulink/slref/composestring.html) | Compose output string signal based on specified format and input signals  
[Scan String](https://uk.mathworks.com/help/simulink/slref/scanstring.html) | Scan input string and convert to signals per specified format  
[String Compare](https://uk.mathworks.com/help/simulink/slref/stringcompare.html) | Compare two input strings  
[String Concatenate](https://uk.mathworks.com/help/simulink/slref/stringconcatenate.html) | Concatenate input strings to form one output string  
[String Constant](https://uk.mathworks.com/help/simulink/slref/stringconstant.html) | Output specified string  
[String Contains](https://uk.mathworks.com/help/simulink/slref/stringcontains.html) | Determine if string contains, starts with, or ends with pattern  
[String Count](https://uk.mathworks.com/help/simulink/slref/stringcount.html) | Count occurrences of pattern in string  
[String Find](https://uk.mathworks.com/help/simulink/slref/stringfind.html) | Return index of first occurrence of pattern string  
[String Length](https://uk.mathworks.com/help/simulink/slref/stringlength.html) | Output number of characters in input string  
[String to ASCII](https://uk.mathworks.com/help/simulink/slref/stringtoascii.html) | Convert string signal to uint8 vector  
[String to Double](https://uk.mathworks.com/help/simulink/slref/stringtodouble.html) | Convert string signal to double signal  
[String to Enum](https://uk.mathworks.com/help/simulink/slref/stringtoenum.html) | Input string signal to enumerated signal  
[String to Single](https://uk.mathworks.com/help/simulink/slref/stringtosingle.html) | Convert string signal to single signal  
[Substring](https://uk.mathworks.com/help/simulink/slref/substring.html) | Extract substring from input string signal  
[To String](https://uk.mathworks.com/help/simulink/slref/tostring.html) | Convert input signal to string signal  
#### User-Defined Functions
Name|Description
---|---
[C Caller](https://uk.mathworks.com/help/simulink/slref/ccaller.html) | Integrate C code in Simulink  
[C Function](https://uk.mathworks.com/help/simulink/slref/cfunction.html) | Integrate and call external C/C++ code from a Simulink model  
[Fcn](https://uk.mathworks.com/help/simulink/slref/fcn.html) | Apply specified expression to input  
[Function Caller](https://uk.mathworks.com/help/simulink/slref/functioncaller.html) | Call a Simulink function  
[Initialize Function](https://uk.mathworks.com/help/simulink/slref/initializefunction.html) | Execute subsystem on model initialize event  
[Interpreted MATLAB Function](https://uk.mathworks.com/help/simulink/slref/interpretedmatlabfunction.html) | (To be removed) Apply MATLAB function or expression to input  
[Level-2 MATLAB S-Function](https://uk.mathworks.com/help/simulink/slref/level2matlabsfunction.html) | Use Level-2 MATLAB S-function in model  
[MATLAB Function](https://uk.mathworks.com/help/simulink/slref/matlabfunction.html) | Include MATLAB code in Simulink models  
[MATLAB System](https://uk.mathworks.com/help/simulink/slref/matlabsystem.html) | Include System object in model  
[Python Code](https://uk.mathworks.com/help/simulink/ref_extras/pythoncode.html) | Integrate native Python code into a Simulink model _(Since R2025a)_  
[Reinitialize Function](https://uk.mathworks.com/help/simulink/slref/reinitializefunction.html) | Execute subsystem on model or subsystem reinitialize event _(Since R2022a)_  
[Reset Function](https://uk.mathworks.com/help/simulink/slref/resetfunction.html) | Execute subsystem on model reset event  
[S-Function](https://uk.mathworks.com/help/simulink/slref/sfunction.html) | Include S-function in model  
[S-Function Builder](https://uk.mathworks.com/help/simulink/slref/sfunctionbuilder.html) | Integrate C or C++ code to create S-functions  
[Simulink Function](https://uk.mathworks.com/help/simulink/slref/simulinkfunction.html) | Define a function using Simulink blocks  
[Terminate Function](https://uk.mathworks.com/help/simulink/slref/terminatefunction.html) | Execute subsystem on model terminate event  
#### Additional Math and Discrete
Name|Description
---|---
[Decrement Real World](https://uk.mathworks.com/help/simulink/slref/decrementrealworld.html) | Decrease real-world value of signal by one  
[Decrement Stored Integer](https://uk.mathworks.com/help/simulink/slref/decrementstoredinteger.html) | Decrease stored integer value of signal by one  
[Decrement Time To Zero](https://uk.mathworks.com/help/simulink/slref/decrementtimetozero.html) | Decrease real-world value of signal by sample time, but only to zero  
[Decrement To Zero](https://uk.mathworks.com/help/simulink/slref/decrementtozero.html) | Decrease real-world value of signal by one, but only to zero  
[Fixed-Point State-Space](https://uk.mathworks.com/help/simulink/slref/fixedpointstatespace.html) | Implement discrete-time state space  
[Increment Real World](https://uk.mathworks.com/help/simulink/slref/incrementrealworld.html) | Increase real-world value of signal by one  
[Increment Stored Integer](https://uk.mathworks.com/help/simulink/slref/incrementstoredinteger.html) | Increase stored integer value of signal by one  
[Transfer Fcn Direct Form II](https://uk.mathworks.com/help/simulink/slref/transferfcndirectformii.html) | Implement Direct Form II realization of transfer function  
[Transfer Fcn Direct Form II Time Varying](https://uk.mathworks.com/help/simulink/slref/transferfcndirectformiitimevarying.html) | Implement time varying Direct Form II realization of transfer function  
## Modeling
### Design Model Architecture
#### Component-Based Modeling
Name|Description
---|---
[In Bus Element](https://uk.mathworks.com/help/simulink/slref/inbuselement.html) | Select input from external port  
[Model](https://uk.mathworks.com/help/simulink/slref/model.html) | Reference another model to create model hierarchy  
[Out Bus Element](https://uk.mathworks.com/help/simulink/slref/outbuselement.html) | Specify output of external port  
[Subsystem](https://uk.mathworks.com/help/simulink/slref/subsystem.html) | Group blocks to create model hierarchy  
[Variant Subsystem](https://uk.mathworks.com/help/simulink/slref/variantsubsystem.html) | Template subsystem containing Subsystem blocks as variant choices  
#### Subsystems
Name|Description
---|---
[Subsystem](https://uk.mathworks.com/help/simulink/slref/subsystem.html) | Group blocks to create model hierarchy  
#### Model References
Name|Description
---|---
[Model](https://uk.mathworks.com/help/simulink/slref/model.html) | Reference another model to create model hierarchy  
[Variant Subsystem](https://uk.mathworks.com/help/simulink/slref/variantsubsystem.html) | Template subsystem containing Subsystem blocks as variant choices  
#### Variant Systems
Name|Description
---|---
[Initialize Function](https://uk.mathworks.com/help/simulink/slref/initializefunction.html) | Execute subsystem on model initialize event  
[Manual Variant Sink](https://uk.mathworks.com/help/simulink/slref/manualvariantsink.html) | Switch between multiple variant choices at output  
[Manual Variant Source](https://uk.mathworks.com/help/simulink/slref/manualvariantsource.html) | Switch between multiple variant choices at input  
[Reset Function](https://uk.mathworks.com/help/simulink/slref/resetfunction.html) | Execute subsystem on model reset event  
[Simulink Function](https://uk.mathworks.com/help/simulink/slref/simulinkfunction.html) | Define a function using Simulink blocks  
[Terminate Function](https://uk.mathworks.com/help/simulink/slref/terminatefunction.html) | Execute subsystem on model terminate event  
[Variant End](https://uk.mathworks.com/help/simulink/slref/variantend.html) | Define end of bounded region _(Since R2024a)_  
[Variant Sink](https://uk.mathworks.com/help/simulink/slref/variantsink.html) | Route amongst multiple outputs using variants  
[Variant Source](https://uk.mathworks.com/help/simulink/slref/variantsource.html) | Route among multiple inputs using variants  
[Variant Start](https://uk.mathworks.com/help/simulink/slref/variantstart.html) | Define start of bounded region _(Since R2024a)_  
[Variant Subsystem, Variant Model, Variant Assembly Subsystem](https://uk.mathworks.com/help/simulink/slref/variantsubsystem.html) | Template subsystem containing Subsystem blocks as variant choices  
#### Data Stores
Name|Description
---|---
[Data Store Memory](https://uk.mathworks.com/help/simulink/slref/datastorememory.html) | Define data store  
[Data Store Read](https://uk.mathworks.com/help/simulink/slref/datastoreread.html) | Read data from data store  
[Data Store Write](https://uk.mathworks.com/help/simulink/slref/datastorewrite.html) | Write data to data store  
#### Composite Interfaces
Name|Description
---|---
[Bus Assignment](https://uk.mathworks.com/help/simulink/slref/busassignment.html) | Assign new values to specified bus elements  
[Bus Creator](https://uk.mathworks.com/help/simulink/slref/buscreator.html) | Group input signals, buses, or messages into bus  
[Bus Selector](https://uk.mathworks.com/help/simulink/slref/busselector.html) | Select elements from input bus  
[Bus to Vector](https://uk.mathworks.com/help/simulink/slref/bustovector.html) | Convert virtual bus to vector  
[Demux](https://uk.mathworks.com/help/simulink/slref/demux.html) | Extract and output elements of virtual vector signal  
[In Bus Element](https://uk.mathworks.com/help/simulink/slref/inbuselement.html) | Select input from external port  
[Matrix Concatenate](https://uk.mathworks.com/help/simulink/slref/matrixconcatenate.html) | Concatenate input matrices of same data type for iterative processing  
[Mux](https://uk.mathworks.com/help/simulink/slref/mux.html) | Combine input signals of same data type and complexity into virtual vector  
[Out Bus Element](https://uk.mathworks.com/help/simulink/slref/outbuselement.html) | Specify output of external port  
[Selector](https://uk.mathworks.com/help/simulink/slref/selector.html) | Select input elements from vector, matrix, or multidimensional signal  
[Signal Conversion](https://uk.mathworks.com/help/simulink/slref/signalconversion.html) | Convert signal to new type without altering signal values  
[Vector Concatenate](https://uk.mathworks.com/help/simulink/slref/vectorconcatenate.html) | Concatenate input vectors of same data type for iterative processing  
### Design Model Behavior
#### Conditionally Executed Subsystems and Models
Name|Description
---|---
[Enable](https://uk.mathworks.com/help/simulink/slref/enable.html) | Add enable port to subsystem or model  
[Enabled and Triggered Subsystem](https://uk.mathworks.com/help/simulink/slref/enabledandtriggeredsubsystem.html) | Subsystem whose execution is enabled and triggered by external inputs  
[Enabled Subsystem](https://uk.mathworks.com/help/simulink/slref/enabledsubsystem.html) | Subsystem whose execution is enabled by external input  
[Function-Call Feedback Latch](https://uk.mathworks.com/help/simulink/slref/functioncallfeedbacklatch.html) | Break feedback loop involving data signals between function-call blocks  
[Function-Call Generator](https://uk.mathworks.com/help/simulink/slref/functioncallgenerator.html) | Provide function-call events to control execution of subsystem or model  
[Function-Call Split](https://uk.mathworks.com/help/simulink/slref/functioncallsplit.html) | Provide junction for splitting function-call line  
[Function-Call Subsystem](https://uk.mathworks.com/help/simulink/slref/functioncallsubsystem.html) | Subsystem whose execution is controlled by external function-call input  
[If](https://uk.mathworks.com/help/simulink/slref/if.html) | Select subsystem execution using logic similar to `if-else` statement  
[If Action Subsystem](https://uk.mathworks.com/help/simulink/slref/ifactionsubsystem.html) | Subsystem whose execution is enabled by If block  
[Message Triggered Subsystem](https://uk.mathworks.com/help/simulink/slref/messagetriggeredsubsystem.html) | Subsystem whose execution is controlled by message input _(Since R2022a)_  
[Resettable Subsystem](https://uk.mathworks.com/help/simulink/slref/resettablesubsystem.html) |  Subsystem whose block states reset with external trigger  
[Switch Case](https://uk.mathworks.com/help/simulink/slref/switchcase.html) | Select subsystem execution using logic similar to `switch` statement  
[Switch Case Action Subsystem](https://uk.mathworks.com/help/simulink/slref/switchcaseactionsubsystem.html) | Subsystem whose execution is enabled by Switch Case block  
[Trigger](https://uk.mathworks.com/help/simulink/slref/trigger.html) | Add trigger or function port to subsystem or model  
[Triggered Subsystem](https://uk.mathworks.com/help/simulink/slref/triggeredsubsystem.html) | Subsystem whose execution is triggered by external input  
#### Iterator Subsystems
Name|Description
---|---
[Array Processing Subsystem](https://uk.mathworks.com/help/simulink/slref/arrayprocessingsubsystem.html) | Apply algorithm to each element of a matrix _(Since R2024a)_  
[For Each Subsystem](https://uk.mathworks.com/help/simulink/slref/foreachsubsystem.html) | Apply algorithm to individual elements or subarrays of input signals or mask parameters  
[For Iterator Subsystem](https://uk.mathworks.com/help/simulink/slref/foriteratorsubsystem.html) |  Repeat subsystem execution during simulation time step for specified number of iterations  
[Neighborhood Processing Subsystem](https://uk.mathworks.com/help/simulink/slref/neighborhoodprocessingsubsystem.html) | Create algorithm that follows the neighborhood pattern _(Since R2022b)_  
[Pixel Processing Subsystem](https://uk.mathworks.com/help/simulink/slref/pixelprocessingsubsystem.html) | Create algorithm that converts multichannel image data to single-channel _(Since R2024a)_  
[While Iterator Subsystem](https://uk.mathworks.com/help/simulink/slref/whileiteratorsubsystem.html) |  Repeat subsystem execution during simulation time step while logical expression is true  
#### Simulink Functions
Name|Description
---|---
[Chart](https://uk.mathworks.com/help/stateflow/ref/chart.html) | Implement control logic with finite state machine  
[Function Caller](https://uk.mathworks.com/help/simulink/slref/functioncaller.html) | Call a Simulink function  
[Function Element](https://uk.mathworks.com/help/simulink/slref/functionelement.html) | Specify function to be called via exporting function port _(Since R2022a)_  
[Function Element Call](https://uk.mathworks.com/help/simulink/slref/functionelementcall.html) | Specify function call to be issued via invoking function port _(Since R2022a)_  
[Inport](https://uk.mathworks.com/help/simulink/slref/inport.html) | Create input port for subsystem or external input  
[MATLAB Function](https://uk.mathworks.com/help/simulink/slref/matlabfunction.html) | Include MATLAB code in Simulink models  
[Outport](https://uk.mathworks.com/help/simulink/slref/outport.html) | Create output port for subsystem or external output  
[Simulink Function](https://uk.mathworks.com/help/simulink/slref/simulinkfunction.html) | Define a function using Simulink blocks  
#### Event Functions
Name|Description
---|---
[Data Store Read](https://uk.mathworks.com/help/simulink/slref/datastoreread.html) | Read data from data store  
[Data Store Write](https://uk.mathworks.com/help/simulink/slref/datastorewrite.html) | Write data to data store  
[Initialize Function](https://uk.mathworks.com/help/simulink/slref/initializefunction.html) | Execute subsystem on model initialize event  
[Parameter Writer](https://uk.mathworks.com/help/simulink/slref/parameterwriter.html) | Write to block parameter or variable  
[Reinitialize Function](https://uk.mathworks.com/help/simulink/slref/reinitializefunction.html) | Execute subsystem on model or subsystem reinitialize event _(Since R2022a)_  
[Reset Function](https://uk.mathworks.com/help/simulink/slref/resetfunction.html) | Execute subsystem on model reset event  
[State Reader](https://uk.mathworks.com/help/simulink/slref/statereader.html) | Read a block state  
[State Writer](https://uk.mathworks.com/help/simulink/slref/statewriter.html) | Write to a block state  
[Terminate Function](https://uk.mathworks.com/help/simulink/slref/terminatefunction.html) | Execute subsystem on model terminate event  
#### Messages
Name|Description
---|---
[Hit Crossing Probe](https://uk.mathworks.com/help/simulink/slref/hitcrossing.html) | Detect crossing point  
[Message Merge](https://uk.mathworks.com/help/simulink/slref/messagemerge.html) | Combine message paths _(Since R2021a)_  
[Message Triggered Subsystem](https://uk.mathworks.com/help/simulink/slref/messagetriggeredsubsystem.html) | Subsystem whose execution is controlled by message input _(Since R2022a)_  
[Queue, Entity Queue](https://uk.mathworks.com/help/simulink/slref/queue.html) | Enqueue messages and entities  
[Receive](https://uk.mathworks.com/help/simulink/slref/receive.html) | Receive messages  
[Send](https://uk.mathworks.com/help/simulink/slref/send.html) | Create and send message  
[Sequence Viewer](https://uk.mathworks.com/help/simulink/slref/sequenceviewer.html) | Display messages, events, states, transitions, and functions between blocks during simulation  
#### Schedule Model Components
Name|Description
---|---
[Function-Call Feedback Latch](https://uk.mathworks.com/help/simulink/slref/functioncallfeedbacklatch.html) | Break feedback loop involving data signals between function-call blocks  
[Function-Call Generator](https://uk.mathworks.com/help/simulink/slref/functioncallgenerator.html) | Provide function-call events to control execution of subsystem or model  
[Function-Call Split](https://uk.mathworks.com/help/simulink/slref/functioncallsplit.html) | Provide junction for splitting function-call line  
[Function-Call Subsystem](https://uk.mathworks.com/help/simulink/slref/functioncallsubsystem.html) | Subsystem whose execution is controlled by external function-call input  
[Inport](https://uk.mathworks.com/help/simulink/slref/inport.html) | Create input port for subsystem or external input  
[Subsystem](https://uk.mathworks.com/help/simulink/slref/subsystem.html) | Group blocks to create model hierarchy  
[Trigger](https://uk.mathworks.com/help/simulink/slref/trigger.html) | Add trigger or function port to subsystem or model  
#### Nonlinearity
Name|Description
---|---
[1-D Lookup Table](https://uk.mathworks.com/help/simulink/slref/1dlookuptable.html) | Approximate one-dimensional function  
[2-D Lookup Table](https://uk.mathworks.com/help/simulink/slref/2dlookuptable.html) | Approximate two-dimensional function  
[Direct Lookup Table (n-D)](https://uk.mathworks.com/help/simulink/slref/directlookuptablend.html) | Index into n-dimensional table to retrieve element, vector, or 2-D matrix  
[Interpolation Using Prelookup](https://uk.mathworks.com/help/simulink/slref/interpolationusingprelookup.html) | Use precalculated index and fraction values to accelerate approximation of N-dimensional function  
[Lookup Table Dynamic](https://uk.mathworks.com/help/simulink/slref/lookuptabledynamic.html) | Approximate a one-dimensional function using dynamic table  
[n-D Lookup Table](https://uk.mathworks.com/help/simulink/slref/ndlookuptable.html) | Approximate n-dimensional function  
[Prelookup](https://uk.mathworks.com/help/simulink/slref/prelookup.html) | Compute index and fraction for Interpolation Using Prelookup block  
[Sine, Cosine](https://uk.mathworks.com/help/simulink/slref/sine.html) | Implement fixed-point sine or cosine wave using lookup table approach that exploits quarter wave symmetry  
### Configure Signals, States, and Parameters
#### Signals
Name|Description
---|---
[Bus to Vector](https://uk.mathworks.com/help/simulink/slref/bustovector.html) | Convert virtual bus to vector  
[IC](https://uk.mathworks.com/help/simulink/slref/ic.html) | Set initial value of signal  
[Probe](https://uk.mathworks.com/help/simulink/slref/probe.html) | Output signal attributes, including width, dimensionality, sample time, and complex signal flag  
[Rate Transition](https://uk.mathworks.com/help/simulink/slref/ratetransition.html) | Handle transfer of data between blocks operating at different rates  
[Signal Conversion](https://uk.mathworks.com/help/simulink/slref/signalconversion.html) | Convert signal to new type without altering signal values  
[Signal Editor](https://uk.mathworks.com/help/simulink/slref/signaleditorblock.html) | Display, create, edit, and switch interchangeable scenarios  
[Signal Specification](https://uk.mathworks.com/help/simulink/slref/signalspecification.html) | Specify desired dimensions, sample time, data type, numeric type, and other attributes of signal  
[Weighted Sample Time](https://uk.mathworks.com/help/simulink/slref/weightedsampletime.html) | Support calculations involving sample time  
[Width](https://uk.mathworks.com/help/simulink/slref/width.html) | Output width of input vector  
#### Units in Simulink
Name|Description
---|---
[Inport](https://uk.mathworks.com/help/simulink/slref/inport.html) | Create input port for subsystem or external input  
[Outport](https://uk.mathworks.com/help/simulink/slref/outport.html) | Create output port for subsystem or external output  
[Signal Specification](https://uk.mathworks.com/help/simulink/slref/signalspecification.html) | Specify desired dimensions, sample time, data type, numeric type, and other attributes of signal  
[Unit Conversion](https://uk.mathworks.com/help/simulink/slref/unitconversion.html) | Convert units  
[Unit System Configuration](https://uk.mathworks.com/help/simulink/slref/unitsystemconfiguration.html) | Restrict units to specified allowed unit systems  
#### Data Types
Name|Description
---|---
[ASCII to String](https://uk.mathworks.com/help/simulink/slref/asciitostring.html) | Uint8 vector signal to string signal  
[Block Support Table](https://uk.mathworks.com/help/simulink/slref/blocksupporttable.html) | View data type support for Simulink blocks  
[Compose String](https://uk.mathworks.com/help/simulink/slref/composestring.html) | Compose output string signal based on specified format and input signals  
[Data Type Conversion](https://uk.mathworks.com/help/simulink/slref/datatypeconversion.html) | Convert input signal to specified data type  
[Data Type Conversion Inherited](https://uk.mathworks.com/help/simulink/slref/datatypeconversioninherited.html) | Convert from one data type to another using inherited data type and scaling  
[Data Type Duplicate](https://uk.mathworks.com/help/simulink/slref/datatypeduplicate.html) | Force all inputs to same data type  
[Data Type Propagation](https://uk.mathworks.com/help/simulink/slref/datatypepropagation.html) | Set data type and scaling of propagated signal based on information from reference signals  
[Data Type Scaling Strip](https://uk.mathworks.com/help/simulink/slref/datatypescalingstrip.html) | Remove scaling and map to built in integer  
[Scan String](https://uk.mathworks.com/help/simulink/slref/scanstring.html) | Scan input string and convert to signals per specified format  
[String Compare](https://uk.mathworks.com/help/simulink/slref/stringcompare.html) | Compare two input strings  
[String Concatenate](https://uk.mathworks.com/help/simulink/slref/stringconcatenate.html) | Concatenate input strings to form one output string  
[String Constant](https://uk.mathworks.com/help/simulink/slref/stringconstant.html) | Output specified string  
[String Contains](https://uk.mathworks.com/help/simulink/slref/stringcontains.html) | Determine if string contains, starts with, or ends with pattern  
[String Count](https://uk.mathworks.com/help/simulink/slref/stringcount.html) | Count occurrences of pattern in string  
[String Find](https://uk.mathworks.com/help/simulink/slref/stringfind.html) | Return index of first occurrence of pattern string  
[String Length](https://uk.mathworks.com/help/simulink/slref/stringlength.html) | Output number of characters in input string  
[String to ASCII](https://uk.mathworks.com/help/simulink/slref/stringtoascii.html) | Convert string signal to uint8 vector  
[String to Double](https://uk.mathworks.com/help/simulink/slref/stringtodouble.html) | Convert string signal to double signal  
[String to Enum](https://uk.mathworks.com/help/simulink/slref/stringtoenum.html) | Input string signal to enumerated signal  
[String to Single](https://uk.mathworks.com/help/simulink/slref/stringtosingle.html) | Convert string signal to single signal  
[Substring](https://uk.mathworks.com/help/simulink/slref/substring.html) | Extract substring from input string signal  
[To String](https://uk.mathworks.com/help/simulink/slref/tostring.html) | Convert input signal to string signal  
#### Model, Block, and Port Callbacks
Name|Description
---|---
[Callback Button](https://uk.mathworks.com/help/simulink/slref/callbackbutton.html) | Execute MATLAB code using button  
### Analyze and Remodel Design
#### Transform Models
Name|Description
---|---
[Timed-Based Linearization](https://uk.mathworks.com/help/simulink/slref/timedbasedlinearization.html) | Generate linear models in base workspace at specific times  
[Trigger-Based Linearization](https://uk.mathworks.com/help/simulink/slref/triggerbasedlinearization.html) | Generate linear models in base workspace when triggered  
[Trigger-Based Operating Point Snapshot](https://uk.mathworks.com/help/slcontrol/ug/triggerbasedoperatingpointsnapshot.html) | Generate operating points at triggered events  
### Test Model Components
Name|Description
---|---
[Assertion](https://uk.mathworks.com/help/simulink/slref/assertion.html) | Check whether signal is zero  
[Check Discrete Gradient](https://uk.mathworks.com/help/simulink/slref/checkdiscretegradient.html) | Check that absolute value of difference between successive samples of discrete signal is less than specified value  
[Check Dynamic Gap](https://uk.mathworks.com/help/simulink/slref/checkdynamicgap.html) | Check that gap of possibly varying width occurs in range of signal's amplitudes  
[Check Dynamic Lower Bound](https://uk.mathworks.com/help/simulink/slref/checkdynamiclowerbound.html) | Check that one signal is always less than another signal  
[Check Dynamic Range](https://uk.mathworks.com/help/simulink/slref/checkdynamicrange.html) | Check that signal falls inside range of amplitudes that varies from time step to time step  
[Check Dynamic Upper Bound](https://uk.mathworks.com/help/simulink/slref/checkdynamicupperbound.html) | Check that one signal is always greater than another signal  
[Check Input Resolution](https://uk.mathworks.com/help/simulink/slref/checkinputresolution.html) | Check that input signal has specified resolution  
[Check Static Gap](https://uk.mathworks.com/help/simulink/slref/checkstaticgap.html) | Check that gap exists in signal's range of amplitudes  
[Check Static Lower Bound](https://uk.mathworks.com/help/simulink/slref/checkstaticlowerbound.html) | Check that signal is greater than (or optionally equal to) static lower bound  
[Check Static Range](https://uk.mathworks.com/help/simulink/slref/checkstaticrange.html) | Check that signal falls inside fixed range of amplitudes  
[Check Static Upper Bound](https://uk.mathworks.com/help/simulink/slref/checkstaticupperbound.html) | Check that signal is less than (or optionally equal to) static upper bound  
## Simulation
### Prepare Model Inputs and Outputs
#### Create Signal Data for Simulation
Name|Description
---|---
[Signal Editor](https://uk.mathworks.com/help/simulink/slref/signaleditorblock.html) | Display, create, edit, and switch interchangeable scenarios  
#### Load Signal Data for Simulation
Name|Description
---|---
[Enable](https://uk.mathworks.com/help/simulink/slref/enable.html) | Add enable port to subsystem or model  
[From File](https://uk.mathworks.com/help/simulink/slref/fromfile.html) | Load data from MAT file into Simulink model  
[From Spreadsheet](https://uk.mathworks.com/help/simulink/slref/fromspreadsheet.html) | Read data from spreadsheet  
[From Workspace](https://uk.mathworks.com/help/simulink/slref/fromworkspace.html) | Load signal data from workspace into Simulink model  
[In Bus Element, Bus Element In](https://uk.mathworks.com/help/simulink/slref/inbuselement.html) | Select input from external port  
[Inport](https://uk.mathworks.com/help/simulink/slref/inport.html) | Create input port for subsystem or external input  
[Playback](https://uk.mathworks.com/help/simulink/slref/playback.html) | Load data from workspace, file, or Simulation Data Inspector _(Since R2022b)_  
[Signal Editor](https://uk.mathworks.com/help/simulink/slref/signaleditorblock.html) | Display, create, edit, and switch interchangeable scenarios  
[Trigger](https://uk.mathworks.com/help/simulink/slref/trigger.html) | Add trigger or function port to subsystem or model  
#### Save Run-Time Data from Simulation
Name|Description
---|---
[Outport](https://uk.mathworks.com/help/simulink/slref/outport.html) | Create output port for subsystem or external output  
[Record](https://uk.mathworks.com/help/simulink/slref/record.html) | View and log data to the workspace, a file, or both _(Since R2021a)_  
[To File](https://uk.mathworks.com/help/simulink/slref/tofile.html) | Write data to file  
[To Workspace](https://uk.mathworks.com/help/simulink/slref/toworkspace.html) | Log data to workspace from Simulink model  
### View and Analyze Simulation Results
#### Control Simulations with Interactive Dashboards
Name|Description
---|---
[Callback Button](https://uk.mathworks.com/help/simulink/slref/callbackbutton.html) | Execute MATLAB code using button  
[Callback Button](https://uk.mathworks.com/help/simulink/slref/customcallbackbutton.html) | Execute MATLAB code using button with customizable appearance _(Since R2021b)_  
[Check Box](https://uk.mathworks.com/help/simulink/slref/checkbox.html) | Select parameter or variable value  
[Check Box](https://uk.mathworks.com/help/simulink/slref/customcheckbox.html) | Change parameter or variable value during simulation using check box with customizable appearance _(Since R2024b)_  
[Circular Gauge](https://uk.mathworks.com/help/simulink/slref/circulargauge.html) | Display signal value during simulation on circular gauge with customizable appearance  
[Combo Box](https://uk.mathworks.com/help/simulink/slref/combobox.html) | Select parameter value from drop-down menu  
[Combo Box](https://uk.mathworks.com/help/simulink/slref/customcombobox.html) | Change parameter or variable value during simulation using combo box with customizable appearance _(Since R2025a)_  
[Dashboard Scope](https://uk.mathworks.com/help/simulink/slref/dashboardscope.html) | Trace signals on scope display during simulation  
[Display](https://uk.mathworks.com/help/simulink/slref/dashboarddisplay.html) | Display signal value during simulation  
[Display](https://uk.mathworks.com/help/simulink/slref/customdisplay.html) | Display signal value during simulation with customizable appearance _(Since R2023b)_  
[Edit](https://uk.mathworks.com/help/simulink/slref/edit.html) | Enter new value for parameter  
[Gauge](https://uk.mathworks.com/help/simulink/slref/gauge.html) | Display signal value on circular scale  
[Half Gauge](https://uk.mathworks.com/help/simulink/slref/halfgauge.html) | Display input value on semicircular scale  
[Half Gauge](https://uk.mathworks.com/help/simulink/slref/customhalfgauge.html) | Display signal value during simulation on gauge shaped as half-circle with customizable appearance _(Since R2024a)_  
[Horizontal Gauge](https://uk.mathworks.com/help/simulink/slref/horizontalgauge.html) | Display signal value during simulation on horizontal gauge with customizable appearance  
[Horizontal Slider](https://uk.mathworks.com/help/simulink/slref/horizontalslider.html) | Change parameter or variable value using horizontal slider with customizable appearance _(Since R2021a)_  
[Knob](https://uk.mathworks.com/help/simulink/slref/knob.html) | Tune parameter value with dial  
[Knob](https://uk.mathworks.com/help/simulink/slref/customknob.html) |  Change parameter or variable value using knob with customizable appearance _(Since R2021a)_  
[Lamp](https://uk.mathworks.com/help/simulink/slref/lamp.html) | Display color that reflects signal value on lamp  
[Lamp](https://uk.mathworks.com/help/simulink/slref/customlamp.html) | Display color that reflects signal value on lamp with customizable appearance _(Since R2021b)_  
[Linear Gauge](https://uk.mathworks.com/help/simulink/slref/lineargauge.html) | Display input value on linear scale  
[MultiStateImage](https://uk.mathworks.com/help/simulink/slref/multistateimage.html) | Display image reflecting input value  
[Push Button](https://uk.mathworks.com/help/simulink/slref/pushbutton.html) | Change parameter or variable value using button  
[Push Button](https://uk.mathworks.com/help/simulink/slref/custompushbutton.html) | Change parameter or variable value using button with customizable appearance _(Since R2021b)_  
[Quarter Gauge](https://uk.mathworks.com/help/simulink/slref/quartergauge.html) | Display input value on quadrant scale  
[Quarter Gauge](https://uk.mathworks.com/help/simulink/slref/customquartergauge.html) | Display signal value during simulation on gauge shaped as quarter-circle with customizable appearance _(Since R2024a)_  
[Radio Button](https://uk.mathworks.com/help/simulink/slref/radiobutton.html) | Select parameter value  
[Radio Button](https://uk.mathworks.com/help/simulink/slref/customradiobutton.html) | Change parameter or variable value during simulation using radio button with customizable appearance _(Since R2025a)_  
[Rocker Switch](https://uk.mathworks.com/help/simulink/slref/rockerswitch.html) | Toggle parameter between two values  
[Rocker Switch](https://uk.mathworks.com/help/simulink/slref/customrockerswitch.html) | Change parameter or variable value using switch with customizable appearance _(Since R2021b)_  
[Rotary Switch](https://uk.mathworks.com/help/simulink/slref/rotaryswitch.html) | Switch parameter to set values on dial  
[Rotary Switch](https://uk.mathworks.com/help/simulink/slref/customrotaryswitch.html) | Change parameter or variable value using rotary switch with customizable appearance _(Since R2021b)_  
[Slider](https://uk.mathworks.com/help/simulink/slref/slider.html) | Tune parameter value with sliding scale  
[Slider Switch](https://uk.mathworks.com/help/simulink/slref/sliderswitch.html) | Toggle parameter between two values  
[Slider Switch](https://uk.mathworks.com/help/simulink/slref/customsliderswitch.html) | Change parameter or variable value using switch with customizable appearance _(Since R2021b)_  
[Toggle Switch](https://uk.mathworks.com/help/simulink/slref/toggleswitch.html) | Toggle parameter between two values  
[Toggle Switch](https://uk.mathworks.com/help/simulink/slref/customtoggleswitch.html) | Change parameter or variable value using switch with customizable appearance _(Since R2021b)_  
[Vertical Gauge](https://uk.mathworks.com/help/simulink/slref/verticalgauge.html) | Display signal value during simulation on vertical gauge with customizable appearance  
[Vertical Slider](https://uk.mathworks.com/help/simulink/slref/verticalslider.html) | Change parameter or variable value using vertical slider with customizable appearance _(Since R2021a)_  
#### View Data During Simulation
Name|Description
---|---
[Floating Scope and Scope Viewer](https://uk.mathworks.com/help/simulink/slref/scopeviewer.html) | Display signals generated during simulation without signal lines  
[Record](https://uk.mathworks.com/help/simulink/slref/record.html) | View and log data to the workspace, a file, or both _(Since R2021a)_  
[Scope](https://uk.mathworks.com/help/simulink/slref/scope.html) | Display signals generated during simulation  
## Block and Blockset Authoring
### Author Block Algorithms
#### Block Authoring Basics
Name|Description
---|---
[Fcn](https://uk.mathworks.com/help/simulink/slref/fcn.html) | Apply specified expression to input  
[Function Caller](https://uk.mathworks.com/help/simulink/slref/functioncaller.html) | Call a Simulink function  
[Level-2 MATLAB S-Function](https://uk.mathworks.com/help/simulink/slref/level2matlabsfunction.html) | Use Level-2 MATLAB S-function in model  
[MATLAB Function](https://uk.mathworks.com/help/simulink/slref/matlabfunction.html) | Include MATLAB code in Simulink models  
[MATLAB System](https://uk.mathworks.com/help/simulink/slref/matlabsystem.html) | Include System object in model  
[S-Function](https://uk.mathworks.com/help/simulink/slref/sfunction.html) | Include S-function in model  
[S-Function Builder](https://uk.mathworks.com/help/simulink/slref/sfunctionbuilder.html) | Integrate C or C++ code to create S-functions  
[Simulink Function](https://uk.mathworks.com/help/simulink/slref/simulinkfunction.html) | Define a function using Simulink blocks  
#### Author Blocks Using MATLAB
Name|Description
---|---
[MATLAB Function](https://uk.mathworks.com/help/simulink/slref/matlabfunction.html) | Include MATLAB code in Simulink models  
[MATLAB System](https://uk.mathworks.com/help/simulink/slref/matlabsystem.html) | Include System object in model  
[S-Function](https://uk.mathworks.com/help/simulink/slref/sfunction.html) | Include S-function in model  
#### Author Blocks Using C/C++
Name|Description
---|---
[S-Function](https://uk.mathworks.com/help/simulink/slref/sfunction.html) | Include S-function in model  
[S-Function Builder](https://uk.mathworks.com/help/simulink/slref/sfunctionbuilder.html) | Integrate C or C++ code to create S-functions  
## Simulation Integration
### Create Large-Scale Model Components
#### Integrate Components from External Tools
Name|Description
---|---
[FMU](https://uk.mathworks.com/help/simulink/ref_extras/fmu.html) | Include Functional Mockup Unit (FMU) in model  
[S-Function](https://uk.mathworks.com/help/simulink/slref/sfunction.html) | Include S-function in model  
#### Integrate External Code into Simulink
Name|Description
---|---
[C Caller](https://uk.mathworks.com/help/simulink/slref/ccaller.html) | Integrate C code in Simulink  
[C Function](https://uk.mathworks.com/help/simulink/slref/cfunction.html) | Integrate and call external C/C++ code from a Simulink model  
[MATLAB Function](https://uk.mathworks.com/help/simulink/slref/matlabfunction.html) | Include MATLAB code in Simulink models  
[MATLAB System](https://uk.mathworks.com/help/simulink/slref/matlabsystem.html) | Include System object in model  
[Python Code](https://uk.mathworks.com/help/simulink/ref_extras/pythoncode.html) | Integrate native Python code into a Simulink model _(Since R2025a)_  
[S-Function](https://uk.mathworks.com/help/simulink/slref/sfunction.html) | Include S-function in model  
[S-Function Builder](https://uk.mathworks.com/help/simulink/slref/sfunctionbuilder.html) | Integrate C or C++ code to create S-functions  
## References
* [Simulink Blocks](https://uk.mathworks.com/help/simulink/referencelist.html?type=block&listtype=cat&category=index&blocktype=all&capability=&startrelease=&endrelease=)