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


class RakutenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rakuten"

    @property
    def original_file_name(self) -> "str":
        return "rakuten.svg"

    @property
    def title(self) -> "str":
        return "Rakuten"

    @property
    def primary_color(self) -> "str":
        return "#BF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rakuten</title>
     <path d="M23.277 21.3L3.939 24 .722 21.3h22.555zM7.6
 19.276H3.939V0h6.052a6.653 6.653 0 0 1 6.65 6.646c0 2.234-1.108
 4.204-2.799 5.418l5.418
 7.211h-4.585l-4.486-5.979H7.6v5.98zm0-9.64h2.392a2.992 2.992 0 0 0
 2.989-2.989 2.994 2.994 0 0 0-2.989-2.986H7.6v5.975z" />
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
