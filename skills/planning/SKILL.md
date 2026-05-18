# Planning Skill

## Description
This skill enables planning and strategy generation for discovery operations.

## Capabilities

### Execution Plan Generation
Generates comprehensive execution plan for discovery.

**Parameters:**
- intake_data: Data from intake phase
- discovery_scope: Workloads to discover

**Output:**
- Execution plan with phases
- Estimated duration
- Resource requirements
- Dependencies

### Discovery Pattern Generation
Generates discovery patterns based on scope.

**Parameters:**
- discovery_scope: Workloads to discover

**Output:**
- List of discovery patterns
- Pattern dependencies
- API call optimization

### Dependency Graph Generation
Generates dependency graph from discovery patterns.

**Parameters:**
- patterns: List of discovery patterns

**Output:**
- Dependency graph structure
- Execution order

## Tool Dependencies
- file_write: For writing execution plans
- file_read: For reading intake data

## Examples
```python
# Generate execution plan
execution_plan = await skills.generate_execution_plan(intake_data, discovery_scope)
```

## Notes
- Optimizes API calls to reduce duplicates
- Generates at least 10 discovery patterns
- Creates detailed runbooks for each pattern
