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


class GlovoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "glovo"

    @property
    def original_file_name(self) -> "str":
        return "glovo.svg"

    @property
    def title(self) -> "str":
        return "Glovo"

    @property
    def primary_color(self) -> "str":
        return "#F2CC38"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Glovo</title>
     <path d="M12.012 0C7.847 0 4.459 3.388 4.459 7.553c0 1.576.494
 3.106 1.412 4.4l.211.281 3.93 5.555s.47.775 1.529.775h.941c1.036 0
 1.53-.775 1.53-.775l3.93-5.555.187-.28a7.43 7.43 0 0 0
 1.412-4.401C19.564 3.388 16.176 0 12.011 0Zm0 3.693a3.837 3.837 0 0 1
 3.836 3.836c0 .824-.26 1.578-.73 2.237l-.212.28-2.894
 4.095-2.895-4.07-.21-.305a3.848 3.848 0 0 1-.731-2.237 3.837 3.837 0
 0 1 3.836-3.836zm-2.117 18.26c0 1.106.893 2.023 2.07 2.047 1.223 0
 2.117-.917 2.117-2.059 0-1.14-.894-2.058-2.094-2.058-1.2
 0-2.093.917-2.093 2.07z" />
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
