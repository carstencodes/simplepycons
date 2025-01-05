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


class UbisoftIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ubisoft"

    @property
    def original_file_name(self) -> "str":
        return "ubisoft.svg"

    @property
    def title(self) -> "str":
        return "Ubisoft"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ubisoft</title>
     <path d="M23.561 11.988C23.301-.304 6.954-4.89.656
 6.634c.282.206.661.477.943.672a11.747 11.747 0 00-.976 3.067 11.885
 11.885 0 00-.184 2.071C.439 18.818 5.621 24 12.005 24c6.385 0
 11.556-5.17 11.556-11.556v-.455zm-20.27 2.06c-.152 1.246-.054
 1.636-.054 1.788l-.282.098c-.108-.206-.37-.932-.488-1.908C2.163
 10.308 4.7 6.96 8.57 6.33c3.544-.52 6.937 1.68 7.728
 4.758l-.282.098c-.087-.087-.228-.336-.77-.878-4.281-4.281-11.002-2.32-11.956
 3.74zm11.002 2.081a3.145 3.145 0 01-2.59 1.355 3.15 3.15 0
 01-3.155-3.155 3.159 3.159 0 012.927-3.144c1.018-.043 1.972.51 2.416
 1.398a2.58 2.58 0 01-.455 2.95c.293.205.575.4.856.595zm6.58.12c-1.669
 3.782-5.106 5.766-8.77
 5.712-7.034-.347-9.083-8.466-4.38-11.393l.207.206c-.076.108-.358.325-.791
 1.182-.51 1.041-.672 2.081-.607 2.732.369 5.67 8.314 6.83 11.045
 1.214C21.057 8.217 11.822.401 3.626 6.374l-.184-.184C5.599 2.808
 9.816 1.3 13.837 2.309c6.147 1.55 9.453 7.956 7.035 13.94z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.ubisoft.com/en-US/company/overvie'''

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
