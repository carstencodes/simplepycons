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


class OpenminedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openmined"

    @property
    def original_file_name(self) -> "str":
        return "openmined.svg"

    @property
    def title(self) -> "str":
        return "OpenMined"

    @property
    def primary_color(self) -> "str":
        return "#ED986C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenMined</title>
     <path d="M12 0c-.486 0-.972.242-1.25.725L7.082 7.082.725
 10.75a1.44 1.44 0 000 2.5l6.357 3.668 3.668 6.357a1.44 1.44 0 002.5
 0l3.668-6.357 6.357-3.668c.967-.544.967-1.945
 0-2.5l-6.357-3.668L13.25.725A1.429 1.429 0 0012 0zm.006 4.237l7.757
 7.769-7.769 7.757-7.757-7.757zm-.012 3.112l-4.656 4.657 4.656 4.656
 4.657-4.656z" />
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
