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


class StorybookIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "storybook"

    @property
    def original_file_name(self) -> "str":
        return "storybook.svg"

    @property
    def title(self) -> "str":
        return "Storybook"

    @property
    def primary_color(self) -> "str":
        return "#FF4785"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Storybook</title>
     <path d="M16.71.243l-.12 2.71a.18.18 0
 00.29.15l1.06-.8.9.7a.18.18 0 00.28-.14l-.1-2.76 1.33-.1a1.2 1.2 0
 011.279 1.2v21.596a1.2 1.2 0 01-1.26 1.2l-16.096-.72a1.2 1.2 0
 01-1.15-1.16l-.75-19.797a1.2 1.2 0 011.13-1.27L16.7.222zM13.64 9.3c0
 .47 3.16.24 3.59-.08 0-3.2-1.72-4.89-4.859-4.89-3.15 0-4.899
 1.72-4.899 4.29 0 4.45 5.999 4.53 5.999 6.959 0 .7-.32 1.1-1.05
 1.1-.96 0-1.35-.49-1.3-2.16 0-.36-3.649-.48-3.769 0-.27 4.03 2.23 5.2
 5.099 5.2 2.79 0 4.969-1.49 4.969-4.18 0-4.77-6.099-4.64-6.099-6.999
 0-.97.72-1.1 1.13-1.1.45 0 1.25.07 1.19 1.87z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/storybookjs/brand/tree/6f4'''

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
