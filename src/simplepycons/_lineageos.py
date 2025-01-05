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


class LineageosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lineageos"

    @property
    def original_file_name(self) -> "str":
        return "lineageos.svg"

    @property
    def title(self) -> "str":
        return "LineageOS"

    @property
    def primary_color(self) -> "str":
        return "#167C80"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LineageOS</title>
     <path d="M21.64526 12.05735a2.40391 2.40391 0 0
 0-1.80293.7993l-.13823-.0541a17.80096 17.80096 0 0 0-2.86666-.8594
 4.80782 4.80782 0 0 0-9.61565 0h-.13221a17.74687 17.74687 0 0
 0-2.7645.83537l-.13822.05409a2.40391 2.40391 0 1 0 .5589 1.06974
 16.599 16.599 0 0 1 2.5782-.77526 4.80782 4.80782 0 0 0 9.35722 0
 16.55693 16.55693 0 0 1 2.5782.76925 2.40391 2.40391 0 1 0
 2.38588-1.839zM2.41397 15.6632a1.20196 1.20196 0 1 1 1.20196-1.20195
 1.20196 1.20196 0 0 1-1.20196 1.20195zm9.61565 0a3.60587 3.60587 0 1
 1 3.60586-3.60586 3.60587 3.60587 0 0 1-3.60586 3.60586zm9.61564
 0a1.20196 1.20196 0 1 1 1.20196-1.20195 1.20196 1.20196 0 0 1-1.20196
 1.20195zm-7.81271-3.60586a1.80293 1.80293 0 1 1-1.80293-1.80294
 1.80293 1.80293 0 0 1 1.80293 1.80294z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://docs.google.com/presentation/d/1VmxFr'''
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
