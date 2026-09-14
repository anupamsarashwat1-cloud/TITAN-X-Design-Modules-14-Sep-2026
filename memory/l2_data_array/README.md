# l2_data_array

## Description

The **l2_data_array** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — L2 Data Array
 Wraps TWO sram_32x64_180nm macros (2 banks).
 CRITICAL FIX: dout0[31:0] from both SRAM macros is properly read and driven
 to dout — this resolves the LVS floating-net issue reported by the PD team.
`timescale 1ns/1ps

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

### Outputs

| Name | Width | Description |
|------|-------|-------------|
| reg | 1 | – |
| reg | 1 | – |

## Functionality

*l2_data_array provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    macros[sram_32x64_180nm macros]:::sub --> l2_data_array
    connected[be connected]:::sub --> l2_data_array
    u_sram_bank1[sram_32x64_180nm u_sram_bank1]:::sub --> l2_data_array
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
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    sram_dout_bank0["sram_dout_bank0\n(wire, 32)"]:::sig
    sram_dout_bank1["sram_dout_bank1\n(wire, 32)"]:::sig
    bank_sel_r["bank_sel_r\n(reg, 1)"]:::sig
```
