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


class NodemonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nodemon"

    @property
    def original_file_name(self) -> "str":
        return "nodemon.svg"

    @property
    def title(self) -> "str":
        return "Nodemon"

    @property
    def primary_color(self) -> "str":
        return "#76D04B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nodemon</title>
     <path d="M22.33 7.851l-.716-.398c1.101-1.569
 1.758-3.927.934-7.453 0 0-1.857 5.029-5.59 4.863l-4.37-2.431a1.171
 1.171 0 0 0-.536-.15h-.101a1.183 1.183 0 0 0-.538.15L7.042
 4.863C3.309 5.03 1.452 0 1.452 0c-.825 3.526-.166 5.884.934
 7.453l-.716.398a1.133 1.133 0 0 0-.589.988l.022 14.591c0
 .203.109.392.294.491a.58.58 0 0 0 .584
 0l5.79-3.204c.366-.211.589-.582.589-.987v-6.817c0-.406.223-.783.588-.984l2.465-1.372a1.19
 1.19 0 0 1 .59-.154c.2 0 .407.05.585.154l2.465
 1.372c.365.201.588.578.588.984v6.817c0 .405.226.779.59.987l5.788
 3.204a.59.59 0 0 0 .589 0 .564.564 0 0 0 .292-.491l.019-14.591a1.129
 1.129 0 0 0-.589-.988z" />
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
