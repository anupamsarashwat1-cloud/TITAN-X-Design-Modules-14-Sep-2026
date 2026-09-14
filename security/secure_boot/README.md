# secure_boot

## Description

The **secure_boot** module SPDX-License-Identifier: Apache-2.0
 SMVDU-TITAN-X SoC — Secure Boot Engine
 Iteration 3: Hardware root-of-trust enforcing ECDSA P-256 signature verification of boot image.
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

## Functionality

*secure_boot provides the hardware implementation for its designated function within the SoC.*

## Hierarchical Block Diagram (Mermaid)

```mermaid
graph LR
    classDef sub fill:#f9f,stroke:#333,stroke-width:1px;
    secure_boot[module secure_boot]:::sub --> secure_boot
    if[begin if]:::sub --> secure_boot
    if[begin if]:::sub --> secure_boot
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
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(input, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    wire["wire\n(output, 1)"]:::port
    state["state\n(reg, 3)"]:::sig
    next_state["next_state\n(reg, 3)"]:::sig
    word_count["word_count\n(reg, 32)"]:::sig
    sha_done["sha_done\n(reg, 1)"]:::sig
    ecdsa_done["ecdsa_done\n(reg, 1)"]:::sig
    ecdsa_valid["ecdsa_valid\n(reg, 1)"]:::sig
```
