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


class WixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wix"

    @property
    def original_file_name(self) -> "str":
        return "wix.svg"

    @property
    def title(self) -> "str":
        return "Wix"

    @property
    def primary_color(self) -> "str":
        return "#0C6EFC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wix</title>
     <path d="m0 7.354 2.113 9.292h.801a1.54 1.54 0 0 0
 1.506-1.218l1.351-6.34a.171.171 0 0 1 .167-.137c.08 0
 .15.058.167.137l1.352 6.34a1.54 1.54 0 0 0 1.506
 1.218h.805l2.113-9.292h-.565c-.62 0-1.159.43-1.296 1.035l-1.26
 5.545-1.106-5.176a1.76 1.76 0 0
 0-2.19-1.324c-.639.176-1.113.716-1.251 1.365l-1.094
 5.127-1.26-5.537A1.33 1.33 0 0 0 .563 7.354H0zm13.992 0a.951.951 0 0
 0-.951.95v8.342h.635a.952.952 0 0 0 .951-.95V7.353h-.635zm1.778 0
 3.158 4.66-3.14 4.632h1.325c.368 0
 .712-.181.918-.486l1.756-2.59a.12.12 0 0 1 .197 0l1.754
 2.59c.206.305.55.486.918.486h1.326l-3.14-4.632L24 7.354h-1.326c-.368
 0-.712.181-.918.486l-1.772 2.617a.12.12 0 0 1-.197 0L18.014
 7.84a1.108 1.108 0 0 0-.918-.486H15.77z" />
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
