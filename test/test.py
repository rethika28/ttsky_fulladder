import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_full_adder(dut):

    # ✅ Initialize all inputs
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1
    dut.clk.value = 0
    dut.rst_n.value = 1

    await Timer(1, units="ns")

    for a in range(2):
        for b in range(2):
            for cin in range(2):

                dut.ui_in.value = (cin << 2) | (b << 1) | a

                await Timer(1, units="ns")

                out = dut.uo_out.value.integer
                sum_out = out & 1
                carry_out = (out >> 1) & 1

                expected_sum = a ^ b ^ cin
                expected_carry = (a & b) | (b & cin) | (a & cin)

                assert sum_out == expected_sum, f"SUM FAIL {a}{b}{cin}"
                assert carry_out == expected_carry, f"CARRY FAIL {a}{b}{cin}"
