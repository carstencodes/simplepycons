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


class BluetoothIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bluetooth"

    @property
    def original_file_name(self) -> "str":
        return "bluetooth.svg"

    @property
    def title(self) -> "str":
        return "Bluetooth"

    @property
    def primary_color(self) -> "str":
        return "#0082FC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bluetooth</title>
     <path d="M12 0C6.76 0 3.1484 2.4895 3.1484 12S6.76 24 12 24c5.24
 0 8.8516-2.4895 8.8516-12S17.24 0 12 0zm-.7773 1.6816l6.2148
 6.2149L13.334 12l4.1035 4.1035-6.2148 6.2149V14.125l-3.418
 3.42-1.2422-1.2442L10.8515 12l-4.289-4.3008 1.2422-1.2441 3.418
 3.4199V1.6816zm1.748 4.2442v3.9687l1.9844-1.9843-1.9844-1.9844zm0
 8.1816v3.9668l1.9844-1.9844-1.9844-1.9824Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.bluetooth.com/develop-with-blueto'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.bluetooth.com/develop-with-blueto'''

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
