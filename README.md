# Quaternion Blacklist Handling

This repository addresses the issue of handling operations between SymPy's `Quaternion` class and other unknown types by introducing a blacklist mechanism. This allows operations like addition, subtraction, multiplication, and division to gracefully handle cases where the operand type is not supported.This repository officially clears the patch #26355 of Sympy's issue list. 

## Overview

The main goal is to modify the behavior of the `Quaternion` class without changing its core logic. This is achieved by introducing a blacklist that checks the type of the operand before performing any operations. If the type is in the blacklist, the operation returns `NotImplemented`, allowing the other operand's right-hand operation (`__radd__`, `__rsub__`, etc.) to handle it.

## Features

- **Blacklist Handling:** Introduces a blacklist to handle unsupported operand types.
- **Seamless Integration:** Modifies the existing `Quaternion` class with minimal changes.
- **Flexible:** Allows easy addition of new types to the blacklist.

## Implementation

The modifications are done through a patch file (`dieter.py`) that redefines the core arithmetic operations for the `Quaternion` class.

### Files

- `dieter.py`: Contains the modified arithmetic operations for the `Quaternion` class.
- `example_usage.py`: Provides examples of how to use the modified `Quaternion` class with the blacklist mechanism.

## Usage

### Prerequisites

Ensure you have SymPy installed:

```bash
pip install sympy
