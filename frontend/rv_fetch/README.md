# rv_fetch

## Description

The **rv_fetch** module SPDX-License-Identifier: Apache-2.0
 SMVDU-Titan-X SoC — RISC-V Instruction Fetch Stage (RV64I)

 Single-outstanding AXI-Lite fetch FSM with redirect-safe teardown:
 on a redirect the unit first drains any orphaned transaction belonging
 to the abandoned stream (an unaccepted AR, or an R beat already owed)
 before issuing the redirected fetch. Without that drain the stale
 instruction would be paired with the NEW pc_out — silent execution of
 the wrong instruction at the wrong architectural address.
`timescale 1ns/1ps
`include "params.vh"

## Interface

### Inputs

| Name | Width | Description |
|------|-------|-------------|
| wire | 1 | – |
| wire | 1 | – |
| wire | 1 | – |
| wire | 1 | – |
| wire | 1 | – |
| wire | 1 | – |
| wire | 1 | – |
| wire | 1 | – |
| wire | 1 | – |
| wire | 1 | – |

### Outputs

| Name | Width | Description |
|------|-------|-------------|
| reg | 1 | – |
| reg | 1 | – |
| wire | 1 | – |
| reg | 1 | – |
| reg | 1 | – |
| reg | 1 | – |

## Functionality

*rv_fetch provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    Stage[Fetch Stage]:::sub --> rv_fetch
    stall[global stall]:::sub --> rv_fetch
```

## Full Signal‑Level Diagram (Mermaid)

```mermaid
graph LR
    classDef sig fill:#eef,stroke:#555,stroke-width:1px;
    classDef port fill:#cfe,stroke:#333,stroke-width:1px;
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    pc["pc\n(reg, 64)"]:::sig
    fstate["fstate\n(reg, 2)"]:::sig
    pending_r["pending_r\n(reg, 1)"]:::sig
```
