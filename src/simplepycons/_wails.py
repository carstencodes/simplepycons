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


class WailsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wails"

    @property
    def original_file_name(self) -> "str":
        return "wails.svg"

    @property
    def title(self) -> "str":
        return "Wails"

    @property
    def primary_color(self) -> "str":
        return "#DF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wails</title>
     <path d="m19.67 5.252-7.856 5.039-.369-.459-8.69-.283 1.891 1.904
 5.221.106 1.63 1.656-5.878.662 1.77 1.783 5.34-1.185.003-.006.993
 1.168-3.079 3.11 7.399.001-1.582-5.002 2.209
 3.14H24l-5.385-2.415h4.121l-5.384-2.418h4.117L16.297 9.73l1.088-1.443
 4.09-1.076-3.467.248 1.662-2.207zm-3.635 2.322-6.039.43 1.455 1.826
 1.813-.476 2.771-1.78zm-.252 2.84-.86
 1.145-.001-.002.154-.205.707-.938zM0 12.2l5.615 1.033-1.017-1.027L0
 12.2z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
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
