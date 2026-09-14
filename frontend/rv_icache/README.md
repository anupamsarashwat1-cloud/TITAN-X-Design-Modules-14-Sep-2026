# rv_icache

## Description

The **rv_icache** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — 32KB, 8-Way Set-Associative I-Cache with SECDED ECC
 Iteration 3: VIPT, PLRU replacement, AXI4 refill master (8-beat burst)
 Target: SCL 180nm, 125-200 MHz
 Geometry: 64-set × 8-way × 64B cacheline = 32KB
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
| reg | 1 | – |
| reg | 1 | – |
| reg | 1 | – |
| reg | 1 | – |
| reg | 1 | – |

## Functionality

*rv_icache provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    master[refill master]:::sub --> rv_icache
    Arrays[SRAM Arrays]:::sub --> rv_icache
    for[generate for]:::sub --> rv_icache
    cacheline[from cacheline]:::sub --> rv_icache
    tree[PLRU tree]:::sub --> rv_icache
    if[begin if]:::sub --> rv_icache
    if[begin if]:::sub --> rv_icache
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
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    p["p\n(reg, 7)"]:::sig
    state["state\n(reg, 2)"]:::sig
    fill_beat["fill_beat\n(reg, 3)"]:::sig
    fill_way["fill_way\n(reg, 3)"]:::sig
```
