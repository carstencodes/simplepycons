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


class HackerrankIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hackerrank"

    @property
    def original_file_name(self) -> "str":
        return "hackerrank.svg"

    @property
    def title(self) -> "str":
        return "HackerRank"

    @property
    def primary_color(self) -> "str":
        return "#00EA64"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HackerRank</title>
     <path d="M0 0v24h24V0zm9.95 8.002h1.805c.061 0
 .111.05.111.111v7.767c0 .061-.05.111-.11.111H9.95c-.061
 0-.111-.05-.111-.11v-2.87H7.894v2.87c0 .06-.05.11-.11.11H5.976a.11.11
 0 01-.11-.11V8.112c0-.06.05-.11.11-.11h1.806c.061 0
 .11.05.11.11v2.869H9.84v-2.87c0-.06.05-.11.11-.11zm2.999 0h5.778c.061
 0 .111.05.111.11v7.767a.11.11 0 01-.11.112h-5.78a.11.11 0
 01-.11-.11V8.111c0-.06.05-.11.11-.11z" />
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
