---
topic:
harness:
date: 2026-10-13
addedBy: Jonathan St-Onge
tags:
---
## Current loop

Here's what grant discovery at UVM look like right now, as a loop

```mermaid
%%{init: {'flowchart': {'nodeSpacing': 20, 'rankSpacing': 30, 'padding': 8}}}%%
flowchart LR
    F([Faculty request]) -->|intake| D[Discovery]
    P[(Pivot-RP)] --> D
    D --> E[Eligibility and competitiveness]
    E -->|refine search| D
    K@{ shape: cloud, label: "R&D knowledge: pipeline, limited submissions" }
    K -.-> D
    K -.-> E
    E --> G{Worth pursuing?}
    G -->|yes| A([Proposal])
    G -->|no or not yet| F

    classDef manual fill:#fde8d0,stroke:#d9822b,color:#222
    classDef tool fill:#e3eef9,stroke:#4a7fb5,color:#222

    class D,E,G,K manual
    class P tool
```

A couple of notes about that loop:
- First it is a loop insofar as we are talking about discovery before moving forward the grant into the hands of the Sponsored Administration Office (SPA).


## Agent loop

Now, what would a fully automated agent loop might look like?


