#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class RiscvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "riscv"

    @property
    def original_file_name(self) -> "str":
        return "riscv.svg"

    @property
    def title(self) -> "str":
        return "RISC-V"

    @property
    def primary_color(self) -> "str":
        return "#283272"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RISC-V</title>
     <path d="M6.94945.05132h16.9479v6.2099l-10.42482
 14.7424-.52374.73429-5.7888-6.84154c4.10309-.73955 6.2099-3.89648
 6.2099-7.37054 0-3.47539-2.10681-7.0534-6.42044-7.4745zM1.47516
 13.42121l8.73912 10.52747H0V3.4188h5.47428c2.94506 0 4.42154 1.9989
 4.42154 4.10703 0 2.1068-1.47648 4.20967-4.42154
 4.20967H1.47516v1.6857zm14.0693 10.52747H24V12.1566l-7.68505
 10.73802-.77048 1.05406z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://riscv.org/about/risc-v-branding-guide'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
