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


class QwiklabsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qwiklabs"

    @property
    def original_file_name(self) -> "str":
        return "qwiklabs.svg"

    @property
    def title(self) -> "str":
        return "Qwiklabs"

    @property
    def primary_color(self) -> "str":
        return "#F5CD0E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qwiklabs</title>
     <path d="M14.346 18.205A6.464 6.464 0 0 0 12 5.72a6.462 6.462 0 0
 0-2.346 12.485.69.69 0 0 0 .961-.623v-5.4a1.385 1.385 0 1 1 2.77
 0v5.4a.692.692 0 0 0 .961.623zm.809 5.558C20.252 22.378 24 17.718 24
 12.182c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.536 3.748 10.196
 8.845 11.581a.7.7 0 0 0 .049.013l.059.016.001-.002a1.385 1.385 0 0 0
 .635-2.695 9.231 9.231 0 1 1 4.824-.001 1.385 1.385 0 0 0 .635
 2.695l.001.002.059-.016.049-.013z" />
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
