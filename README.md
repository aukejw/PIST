PIST
====

Project Intelligent Systems Track, MSc AI 2013.

An implementation for automatic optimization of the walking parameters for the Berlin United walking engine.

## Planning

### Preparation
 1. Explore parameters
 2. Read relevant literature
 3. WEBOTS (license)
 
### Implementation
 1. ???
 2. Profit
 
### Evaluation
 1. ???
 2. Profit 
 
## Used methods and parameters

### Fitness function
Evaluation through multiple runs:
- Straight walking
- Quick turns
- Diagonal walking
- Quick direction changes

### Online learning
Because of the nature of the evaluation process, it may be impossible to learn online in a sufficiently short period of time. COM error may therefore be useful for immediate evaluation of walking parameters.


### Genetic algorithms
- How and when do mutations take place?
- How and when do crossovers take place?
- Which section of population to keep/discard?

### Gradient ascent/descent algorithms
- Some learning rate (for winning/losing a la Wolf?)
- Neural net settings?
