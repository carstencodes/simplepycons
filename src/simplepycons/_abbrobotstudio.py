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


class AbbRobotstudioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "abbrobotstudio"

    @property
    def original_file_name(self) -> "str":
        return "abbrobotstudio.svg"

    @property
    def title(self) -> "str":
        return "ABB RobotStudio"

    @property
    def primary_color(self) -> "str":
        return "#FF9E0F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ABB RobotStudio</title>
     <path d="M23.999 12.465a9.601 9.601 0 01-19.203 0h1.07a8.53 8.53
 0 108.533-8.53v-1.07A9.6 9.6 0 0124 12.463zm-9.6-3.2a3.2 3.2 0 103.2
 3.2 3.2 3.2 0 00-3.2-3.2zm-2 0l-.6-6.672-2.462 1.92-1.46-1.44a4.67
 4.67 0 00-5.62-.37l-2.02 1.3a.54.54 0 00-.15.74.54.54 0
 00.74.15l2-1.31a3.64 3.64 0 014.29.22l1.37 1.38-2.29 1.821z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://new.abb.com/products/robotics/en/robo'''

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
