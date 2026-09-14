# spi_master

## Description

The **spi_master** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — SPI Master Controller
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
| wire | 1 | – |
| wire | 1 | – |
| wire | 1 | – |
| reg | 1 | – |
| wire | 1 | – |

## Functionality

*spi_master provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    spi_master[module spi_master]:::sub --> spi_master
    if[begin if]:::sub --> spi_master
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
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    clk_div["clk_div\n(reg, 16)"]:::sig
    tx_data["tx_data\n(reg, 8)"]:::sig
    rx_data["rx_data\n(reg, 8)"]:::sig
    start["start\n(reg, 1)"]:::sig
    busy["busy\n(reg, 1)"]:::sig
    cs_select["cs_select\n(reg, 4)"]:::sig
    cpol["cpol\n(reg, 1)"]:::sig
    cpha["cpha\n(reg, 1)"]:::sig
    clk_cnt["clk_cnt\n(reg, 16)"]:::sig
    sclk_r["sclk_r\n(reg, 1)"]:::sig
    shift_out["shift_out\n(reg, 8)"]:::sig
    shift_in["shift_in\n(reg, 8)"]:::sig
    bit_cnt["bit_cnt\n(reg, 3)"]:::sig
    mosi_r["mosi_r\n(reg, 1)"]:::sig
```
