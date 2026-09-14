# gem_sgmii_pcs

## Description

The **gem_sgmii_pcs** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — Gigabit Ethernet SGMII PCS Sublayer
 Iteration 3: SGMII Physical Coding Sublayer (8b/10b encode/decode, auto-negotiation)
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

*gem_sgmii_pcs provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    Sublayer[Coding Sublayer]:::sub --> gem_sgmii_pcs
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
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    tx_data_reg["tx_data_reg\n(reg, 8)"]:::sig
    tx_en_reg["tx_en_reg\n(reg, 1)"]:::sig
    tx_er_reg["tx_er_reg\n(reg, 1)"]:::sig
    tbi_tx_out["tbi_tx_out\n(reg, 10)"]:::sig
    rx_data_reg["rx_data_reg\n(reg, 10)"]:::sig
    rxd_out["rxd_out\n(reg, 8)"]:::sig
    rx_dv_out["rx_dv_out\n(reg, 1)"]:::sig
    rx_er_out["rx_er_out\n(reg, 1)"]:::sig
```
