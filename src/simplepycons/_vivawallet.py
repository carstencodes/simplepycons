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


class VivaWalletIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vivawallet"

    @property
    def original_file_name(self) -> "str":
        return "vivawallet.svg"

    @property
    def title(self) -> "str":
        return "Viva Wallet"

    @property
    def primary_color(self) -> "str":
        return "#1F263A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Viva Wallet</title>
     <path d="M7.275 17.428c.376.777.949 1.223 1.572 1.228h.01c.619 0
 1.191-.435 1.575-1.194l.504-1.08-4.9-10.387-3.388
 1.58zm6.367.033c.382.76.957 1.195 1.575 1.195h.006c.625-.004 1.2-.45
 1.574-1.226l4.567-9.852-3.389-1.581-4.844 10.381zm-1.605 1.206c-.74
 1.245-1.905 1.977-3.18
 1.977h-.022c-1.391-.01-2.643-.89-3.353-2.355C3.657 14.397 1.828
 10.507 0 6.617l6.99-3.259 5.039 10.683 4.985-10.685L24 6.613 18.592
 18.29c-.709 1.465-1.962 2.345-3.353 2.355h-.022c-1.275
 0-2.442-.732-3.18-1.977Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.vivawallet.com/gb_en/press-center'''

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
