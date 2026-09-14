# BUFX4

## Description

The **BUFX4** module Standard cell stub library for 180nm verification
 Canonical home of cell stubs. Guarded so it may be listed on any compile
 line regardless of ../common/* also being present.
`ifndef TITANX_STDCELL_STUBS
`define TITANX_STDCELL_STUBS

 BUFX4: 4X drive strength buffer

## Interface

### Inputs

| Name | Width | Description |
|------|-------|-------------|
| wire | 1 | – |

### Outputs

| Name | Width | Description |
|------|-------|-------------|
| wire | 1 | – |

## Functionality

*BUFX4 provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    BUFX4[module BUFX4]:::sub --> BUFX4
```

## Full Signal‑Level Diagram (Mermaid)

```mermaid
graph LR
    classDef sig fill:#eef,stroke:#555,stroke-width:1px;
    classDef port fill:#cfe,stroke:#333,stroke-width:1px;
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
```
