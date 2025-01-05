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


class KitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kit"

    @property
    def original_file_name(self) -> "str":
        return "kit.svg"

    @property
    def title(self) -> "str":
        return "Kit"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kit</title>
     <path d="m3.5 11.633-2.434 2.408V8.687a.53.53 0 0
 0-.533-.527.53.53 0 0 0-.533.527v6.624a.528.528 0 0 0
 .532.526.533.533 0 0 0 .377-.153l2.974-2.939 2.974 2.94a.535.535 0 0
 0 .754 0 .522.522 0 0 0 0-.746l-2.974-2.938L7.61 9.06a.522.522 0 0 0
 0-.745.538.538 0 0 0-.753 0l-3.344 3.307c-.003
 0-.005.003-.007.005l-.007.006v-.001zm8.826 4.206a.53.53 0 0
 1-.533-.526V8.688a.53.53 0 0 1 .533-.528.53.53 0 0 1
 .533.528v6.624a.53.53 0 0 1-.533.526v.001zm7.257-6.624v6.098c0
 .29.238.526.532.526a.53.53 0 0 0 .533-.526V9.215h2.818A.53.53 0 0 0
 24 8.688a.53.53 0 0 0-.533-.527h-6.702a.53.53 0 0 0-.533.527.53.53 0
 0 0 .533.527h2.819-.001z" />
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
