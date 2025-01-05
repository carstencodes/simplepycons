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


class GoogleChronicleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlechronicle"

    @property
    def original_file_name(self) -> "str":
        return "googlechronicle.svg"

    @property
    def title(self) -> "str":
        return "Google Chronicle"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Chronicle</title>
     <path d="m2.719 4.812 4.812 3v4l-4.812 3Zm0 10
 4.812-3v9.375l-3.914-2.389a1.875 1.875 0 0 1-.898-1.6ZM2.719
 0h18.562v4.812H2.719Zm4.812 21.188 13.75-8.594v4.618c0 .626-.323
 1.208-.854 1.539L12 24Z" />
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
