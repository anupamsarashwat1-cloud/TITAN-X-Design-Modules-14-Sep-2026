# gpio_ctrl

## Description

The **gpio_ctrl** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — GPIO Controller (32-bit bidirectional)
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

### Outputs

| Name | Width | Description |
|------|-------|-------------|
| reg | 1 | – |
| wire | 1 | – |
| wire | 1 | – |

## Functionality

*gpio_ctrl provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    Controller[GPIO Controller]:::sub --> gpio_ctrl
    polarity[interrupt polarity]:::sub --> gpio_ctrl
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
    reg["reg\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(inout, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    dir_reg["dir_reg\n(reg, 32)"]:::sig
    out_reg["out_reg\n(reg, 32)"]:::sig
    int_en["int_en\n(reg, 32)"]:::sig
    int_pol["int_pol\n(reg, 32)"]:::sig
    int_stat["int_stat\n(reg, 32)"]:::sig
    in_sync["in_sync\n(reg, 32)"]:::sig
    gpio_sync1["gpio_sync1\n(reg, 32)"]:::sig
    gpio_sync2["gpio_sync2\n(reg, 32)"]:::sig
    int_raw["int_raw\n(reg, 32)"]:::sig
```
