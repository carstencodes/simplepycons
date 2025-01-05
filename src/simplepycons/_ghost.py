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


class GhostIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ghost"

    @property
    def original_file_name(self) -> "str":
        return "ghost.svg"

    @property
    def title(self) -> "str":
        return "Ghost"

    @property
    def primary_color(self) -> "str":
        return "#15171A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ghost</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm.256 2.313c2.47.005 5.116 2.008 5.898
 2.962l.244.3c1.64 1.994 3.569 4.34 3.569 6.966 0 3.719-2.98
 5.808-6.158 7.508-1.433.766-2.98 1.508-4.748 1.508-4.543
 0-8.366-3.569-8.366-8.112
 0-.706.17-1.425.342-2.15.122-.515.244-1.033.307-1.549.548-4.539
 2.967-6.795 8.422-7.408a4.29 4.29 0 01.49-.026Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/TryGhost/Admin/blob/e3e1fa'''

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
