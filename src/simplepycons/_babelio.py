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


class BabelioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "babelio"

    @property
    def original_file_name(self) -> "str":
        return "babelio.svg"

    @property
    def title(self) -> "str":
        return "Babelio"

    @property
    def primary_color(self) -> "str":
        return "#FBB91E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Babelio</title>
     <path d="M15.283 0a13.994 13.994 0 0 1-6.566 7.588v4.691a20.538
 20.538 0 0 0 6.566-3.676zm3.283 7.7a22.121 22.121 0 0 1-13.132
 7.03v4.213a35.545 35.545 0 0 0 3.836-.564 35.118 35.118 0 0 0
 9.296-3.322zm3.282 7.331a36.747 36.747 0 0 1-19.696 5.686V24h19.696Z"
 />
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
