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


class RainmeterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rainmeter"

    @property
    def original_file_name(self) -> "str":
        return "rainmeter.svg"

    @property
    def title(self) -> "str":
        return "Rainmeter"

    @property
    def primary_color(self) -> "str":
        return "#19519B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rainmeter</title>
     <path d="M12.7 1.088L12 0l-.7 1.088c-.751 1.168-7.342
 11.525-7.342 15.366C3.958 20.615 7.565 24 12 24s8.042-3.385
 8.042-7.546c0-3.84-6.591-14.197-7.342-15.366zM12 22.335c-3.516
 0-6.377-2.638-6.377-5.881C5.623 13.908 9.732 6.756 12 3.1c2.268 3.656
 6.377 10.809 6.377 13.355 0 3.242-2.861 5.88-6.377
 5.88zm4.957-6.017c0 2.548-2.22 4.615-4.957 4.615-2.737
 0-4.957-2.067-4.957-4.615 0-.163.021-.347.058-.549 0 0 1.306-2.616
 4.847 0 2.999 2.215 4.95 0 4.95 0 .038.202.059.386.059.549z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/rainmeter/rainmeter-www/bl'''

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
