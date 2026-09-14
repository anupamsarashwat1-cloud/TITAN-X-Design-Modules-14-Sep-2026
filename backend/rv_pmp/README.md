# rv_pmp

## Description

The **rv_pmp** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — Physical Memory Protection (PMP)
 Iteration 3: 8 PMP entries per hart, placed after MMU output
 RISC-V Privileged Spec v1.12: TOR, NA4, NAPOT, and OFF modes
 Placement: between MMU PA output and L1 cache AXI master
`timescale 1ns/1ps
`include "params.vh"
`include "isa_pkg.vh"

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
| wire | 1 | – |

### Outputs

| Name | Width | Description |
|------|-------|-------------|
| wire | 1 | – |

## Functionality

*rv_pmp provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    Protection[Memory Protection]:::sub --> rv_pmp
    for[generate for]:::sub --> rv_pmp
    if[begin if]:::sub --> rv_pmp
    RWX[check RWX]:::sub --> rv_pmp
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
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    addr_prev["addr_prev\n(wire, 38)"]:::sig
    napot_mask["napot_mask\n(wire, 38)"]:::sig
    match_cfg["match_cfg\n(reg, 8)"]:::sig
    any_match["any_match\n(reg, 1)"]:::sig
```
