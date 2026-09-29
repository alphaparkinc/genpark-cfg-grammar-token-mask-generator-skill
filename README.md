# genpark-cfg-grammar-token-mask-generator-skill

Finite-state token masking engine enforcing Context-Free Grammar (CFG) constraints to ensure 100% syntactically valid model generation.

## Architecture

```mermaid
flowchart LR
    State[Current Grammar State] --> Masker[CFG Token Mask Generator]
    Masker --> AllowedSet[Allowed Character/Token Mask]
    AllowedSet --> Sampler[Constrained LLM Sampler]
```

## Features
- **Deterministic Next-Token Sets**: Guarantees syntax compliance.
- **Zero Dependencies**: 100% Python standard library.
