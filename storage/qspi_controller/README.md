# qspi_controller

## Description

The **qspi_controller** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — Quad-SPI Controller with Execute-in-Place (XIP)
 Iteration 3: Supports AXI4 Master (for XIP fetching) and APB (for config).
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
| wire | 1 | – |
| wire | 1 | – |

### Outputs

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

## Functionality

*qspi_controller provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    Master[AXI4 Master]:::sub --> qspi_controller
```

## Full Signal‑Level Diagram (Mermaid)

```mermaid
graph LR
    classDef sig fill:#eef,stroke:#555,stroke-width:1px;
    classDef port fill:#cfe,stroke:#333,stroke-width:1px;
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(inout, 1)"]:::port
    ctrl_reg["ctrl_reg\n(reg, 32)"]:::sig
    cmd_reg["cmd_reg\n(reg, 32)"]:::sig
    tx_data["tx_data\n(reg, 32)"]:::sig
    rx_data["rx_data\n(reg, 32)"]:::sig
    stat_reg["stat_reg\n(reg, 32)"]:::sig
    state["state\n(reg, 3)"]:::sig
    xip_data["xip_data\n(reg, 32)"]:::sig
    counter["counter\n(reg, 8)"]:::sig
    s_arready_reg["s_arready_reg\n(reg, 1)"]:::sig
    s_rvalid_reg["s_rvalid_reg\n(reg, 1)"]:::sig
```
