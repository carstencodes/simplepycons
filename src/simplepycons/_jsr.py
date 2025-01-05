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


class JsrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jsr"

    @property
    def original_file_name(self) -> "str":
        return "jsr.svg"

    @property
    def title(self) -> "str":
        return "JSR"

    @property
    def primary_color(self) -> "str":
        return "#F7DF1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>JSR</title>
     <path d="M3.692
 5.538v3.693H0v7.384h7.385v1.847h12.923v-3.693H24V7.385h-7.385V5.538Zm1.846
 1.847h1.847v7.384H1.846v-3.692h1.846v1.846h1.846zm3.693
 0h5.538V9.23h-3.692v1.846h3.692v5.538H9.231V14.77h3.692v-1.846H9.231Zm7.384
 1.846h5.539v3.692h-1.846v-1.846h-1.846v5.538h-1.847z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/jsr-io/jsr/blob/98c4448c64'''

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
