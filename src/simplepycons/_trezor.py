#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class TrezorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trezor"

    @property
    def original_file_name(self) -> "str":
        return "trezor.svg"

    @property
    def title(self) -> "str":
        return "Trezor"

    @property
    def primary_color(self) -> "str":
        return "#141609"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trezor</title>
     <path d="M17.858 5.569c0-3.044-2.643-5.569-5.86-5.569-3.216
 0-5.856 2.525-5.856 5.569v1.78H3.731V20.15L11.998
 24l8.271-3.849V7.403h-2.411zm-8.73 0c0-1.434 1.264-2.584 2.87-2.584
 1.61 0 2.87 1.15 2.87 2.584v1.78h-5.74Zm7.81 12.516-4.94
 2.298-4.937-2.298v-7.693h9.878z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://satoshilabs.visualbook.pro/content/2_'''

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
