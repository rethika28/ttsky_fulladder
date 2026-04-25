<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This project implements a 1-bit full adder using combinational logic.

The inputs a, b, and cin are taken from ui_in[0], ui_in[1], and ui_in[2]. These three bits are added together using Verilog arithmetic:

{carry, sum} = a + b + cin;

The result of the addition is a 2-bit value:

The least significant bit (LSB) is assigned to sum
The most significant bit (MSB) is assigned to carry

Outputs are mapped as:

uo_out[0] → sum
uo_out[1] → carry

All other outputs are set to 0. The design is purely combinational, so outputs update immediately when inputs change.

## How to test

To test the design:

Provide input values using ui_in:
ui_in[0] = a
ui_in[1] = b
ui_in[2] = cin
Apply all 8 input combinations (000 to 111)
Observe outputs:
uo_out[0] → sum
uo_out[1] → carry

Example:

Input: a=1, b=1, cin=0
Output: sum=0, carry=1

The included cocotb testbench automatically verifies all combinations.

## External hardware

No external hardware is used in this project.
