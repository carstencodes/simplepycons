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


class PaypalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paypal"

    @property
    def original_file_name(self) -> "str":
        return "paypal.svg"

    @property
    def title(self) -> "str":
        return "PayPal"

    @property
    def primary_color(self) -> "str":
        return "#003087"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PayPal</title>
     <path d="M7.016 19.198h-4.2a.562.562 0 0
 1-.555-.65L5.093.584A.692.692 0 0 1 5.776 0h7.222c3.417 0 5.904 2.488
 5.846 5.5-.006.25-.027.5-.066.747A6.794 6.794 0 0 1 12.071
 12H8.743a.69.69 0 0 0-.682.583l-.325 2.056-.013.083-.692
 4.39-.015.087zM19.79 6.142c-.01.087-.01.175-.023.261a7.76 7.76 0 0
 1-7.695 6.598H9.007l-.283 1.795-.013.083-.692
 4.39-.134.843-.014.088H6.86l-.497 3.15a.562.562 0 0 0
 .555.65h3.612c.34 0 .63-.249.683-.585l.952-6.031a.692.692 0 0 1
 .683-.584h2.126a6.793 6.793 0 0 0
 6.707-5.752c.306-1.95-.466-3.744-1.89-4.906z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://newsroom.paypal-corp.com/media-resour'''
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
