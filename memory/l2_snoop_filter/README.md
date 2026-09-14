# l2_snoop_filter

## Description

The **l2_snoop_filter** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — L2 Snoop Filter (MESI Directory)
 Iteration 3: Tracks L1 D-Cache coherence state for 4 application cores.
 Coherence Protocol: MESI
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

### Outputs

| Name | Width | Description |
|------|-------|-------------|
| to | 1 | – |
| reg | 1 | – |
| reg | 1 | – |
| reg | 1 | – |
| reg | 1 | – |
| reg | 1 | – |
| reg | 1 | – |
| reg | 1 | – |

## Functionality

*l2_snoop_filter provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    Filter[Snoop Filter]:::sub --> l2_snoop_filter
    array[associative array]:::sub --> l2_snoop_filter
    if[else if]:::sub --> l2_snoop_filter
    if[Inv if]:::sub --> l2_snoop_filter
    if[state if]:::sub --> l2_snoop_filter
    sharers[other sharers]:::sub --> l2_snoop_filter
    if[else if]:::sub --> l2_snoop_filter
    if[else if]:::sub --> l2_snoop_filter
    if[else if]:::sub --> l2_snoop_filter
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
    to["to\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    reg["reg\n(output, 1)"]:::port
    state["state\n(reg, 3)"]:::sig
    hit_mask["hit_mask\n(reg, 4)"]:::sig
    hit_way["hit_way\n(reg, 5)"]:::sig
    line_hit["line_hit\n(reg, 1)"]:::sig
    line_state["line_state\n(reg, 2)"]:::sig
    req_core_saved["req_core_saved\n(reg, 2)"]:::sig
    req_type_saved["req_type_saved\n(reg, 2)"]:::sig
```
