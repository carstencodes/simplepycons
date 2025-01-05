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


class SlashdotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "slashdot"

    @property
    def original_file_name(self) -> "str":
        return "slashdot.svg"

    @property
    def title(self) -> "str":
        return "Slashdot"

    @property
    def primary_color(self) -> "str":
        return "#026664"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Slashdot</title>
     <path d="M19.777 0L7.037 24H1.868L14.605 0h5.172zm2.354 19.801c0
 2.268-1.841 4.105-4.109 4.105s-4.107-1.838-4.107-4.105 1.839-4.107
 4.107-4.107 4.109 1.839 4.109 4.107z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Slash'''

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
