# watchdog_timer

## Description

The **watchdog_timer** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — Watchdog Timer
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
| reg | 1 | – |
| wire | 1 | – |

## Functionality

*watchdog_timer provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    watchdog_timer[module watchdog_timer]:::sub --> watchdog_timer
    if[begin if]:::sub --> watchdog_timer
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
    reg["reg\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    load_val["load_val\n(reg, 32)"]:::sig
    count["count\n(reg, 32)"]:::sig
    wdt_en["wdt_en\n(reg, 1)"]:::sig
    int_en["int_en\n(reg, 1)"]:::sig
    int_stat["int_stat\n(reg, 1)"]:::sig
    unlock["unlock\n(reg, 1)"]:::sig
```
