import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_full_adder(dut):

    dut._log.info("Starting Full Adder Test")

    dut.ui_in.value = 0
    dut.uio_in.value = 0

    for a in range(2):
        for b in range(2):
            for cin in range(2):

                dut.ui_in.value = (cin << 2) | (b << 1) | a

                await Timer(1, units="ns")

                out = dut.uo_out.value & 0xFF
                sum_out = out & 0x1
                carry_out = (out >> 1) & 0x1

                expected_sum = a ^ b ^ cin
                expected_carry = (a & b) | (b & cin) | (a & cin)

                assert sum_out == expected_sum, f"SUM FAIL {a}{b}{cin}"
                assert carry_out == expected_carry, f"CARRY FAIL {a}{b}{cin}"

    dut._log.info("All tests passed ✅")
