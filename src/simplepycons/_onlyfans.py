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


class OnlyfansIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "onlyfans"

    @property
    def original_file_name(self) -> "str":
        return "onlyfans.svg"

    @property
    def title(self) -> "str":
        return "OnlyFans"

    @property
    def primary_color(self) -> "str":
        return "#00AFF0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OnlyFans</title>
     <path d="M24 4.003h-4.015c-3.45 0-5.3.197-6.748 1.957a7.996 7.996
 0 1 0 2.103 9.211c3.182-.231 5.39-2.134 6.085-5.173 0
 0-2.399.585-4.43 0 4.018-.777 6.333-3.037 7.005-5.995zM5.61
 11.999A2.391 2.391 0 0 1 9.28 9.97a2.966 2.966 0 0 1
 2.998-2.528h.008c-.92 1.778-1.407 3.352-1.998 5.263A2.392 2.392 0 0 1
 5.61 12Zm2.386-7.996a7.996 7.996 0 1 0 7.996 7.996 7.996 7.996 0 0
 0-7.996-7.996Zm0 10.394A2.399 2.399 0 1 1 10.395 12a2.396 2.396 0 0
 1-2.399 2.398Z" />
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
