# SPDX-FileCopyrightText: 2024 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: Apache-2.0
def test_app(dut):
    dut.expect_unity_test_output(timeout=240)