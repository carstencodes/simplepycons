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


class PolymerProjectIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "polymerproject"

    @property
    def original_file_name(self) -> "str":
        return "polymerproject.svg"

    @property
    def title(self) -> "str":
        return "Polymer Project"

    @property
    def primary_color(self) -> "str":
        return "#FF4470"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Polymer Project</title>
     <path d="M14.4 3.686L7.2 16.16 4.8 12l4.8-8.314H4.8L0 12l2.4
 4.159 2.4 4.155h4.8l7.2-12.469L19.2 12l-4.8 8.314h4.8l2.4-4.155L24
 12l-2.4-4.155-2.4-4.159Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Polymer/polymer-project.or
g/blob/3d3e967446858b49a7796676714865ac9b2a5275/app/images/logos/p-log'''

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
