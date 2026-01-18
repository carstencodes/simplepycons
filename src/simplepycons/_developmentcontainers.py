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


class DevelopmentContainersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "developmentcontainers"

    @property
    def original_file_name(self) -> "str":
        return "developmentcontainers.svg"

    @property
    def title(self) -> "str":
        return "Development Containers"

    @property
    def primary_color(self) -> "str":
        return "#2753E3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Development Containers</title>
     <path d="M10.31.615a4.5 4.5 0 0 1 3.382 0l8.998 3.648A2.1 2.1 0 0
 1 24 6.208v11.584a2.1 2.1 0 0 1-1.311 1.946l-8.998 3.648a4.5 4.5 0 0
 1-3.382 0l-8.998-3.648A2.1 2.1 0 0 1 0 17.792V6.208a2.1 2.1 0 0 1
 1.311-1.946Zm2.705 1.668a2.7 2.7 0 0 0-2.028 0l-9 3.647a.3.3 0 0
 0-.187.278v11.584a.3.3 0 0 0 .187.278l8.999 3.648a2.7 2.7 0 0 0 2.028
 0l8.999-3.648a.3.3 0 0 0 .187-.278V6.208a.3.3 0 0 0-.187-.278ZM6.019
 6.658 12 8.928l5.98-2.27c1.122-.427 1.762 1.256.64 1.683l-5.72
 2.17V17.1c0 1.2-1.8 1.2-1.8 0v-6.59L5.38
 8.34c-1.122-.426-.482-2.109.64-1.683" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/microsoft/fluentui-system-
icons/blob/3e1e525f4499a22d46039ef54e9b9a86b809bc66/assets/Cube/SVG/ic'''

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
        yield from [
            "devcontainers",
        ]
