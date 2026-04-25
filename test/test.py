import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_full_adder(dut):
    """Test TinyTapeout Full Adder"""

    dut._log.info("Starting Full Adder Test")

    # Initialize inputs
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    # Loop through all input combinations (a, b, cin)
    for a in range(2):
        for b in range(2):
            for cin in range(2):

                # Apply inputs
                value = (cin << 2) | (b << 1) | a
                dut.ui_in.value = value

                # Wait for combinational logic to settle
                await Timer(1, units="ns")

                # Read outputs
                sum_out = dut.uo_out.value & 0x1
                carry_out = (dut.uo_out.value >> 1) & 0x1

                # Expected results
                expected_sum = (a ^ b ^ cin)
                expected_carry = (a & b) | (b & cin) | (a & cin)

                dut._log.info(
                    f"a={a}, b={b}, cin={cin} -> sum={sum_out}, carry={carry_out}"
                )

                # Check results
                assert sum_out == expected_sum, f"SUM mismatch for {a},{b},{cin}"
                assert carry_out == expected_carry, f"CARRY mismatch for {a},{b},{cin}"

    dut._log.info("All test cases passed!")
