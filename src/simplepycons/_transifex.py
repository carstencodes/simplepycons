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


class TransifexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "transifex"

    @property
    def original_file_name(self) -> "str":
        return "transifex.svg"

    @property
    def title(self) -> "str":
        return "Transifex"

    @property
    def primary_color(self) -> "str":
        return "#0064AB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Transifex</title>
     <path d="m20.073 12.851-2.758-2.757 3.722-3.659a.33.33 0 0 1
 .467.003l2.27 2.309a.33.33 0 0 1-.004.468zm0 0h-.001zm-9.04-6.433
 12.87 12.869c.129.13.129.34 0 .469l-2.289 2.289a.331.331 0 0 1-.468
 0l-5.168-5.168-2.863 2.815c-.604.593-1.244 1.159-1.975 1.591a7.037
 7.037 0 0 1-2.248.83c-2.191.42-4.557-.047-6.303-1.468A7.065 7.065 0 0
 1 0 15.207V2.069a.33.33 0 0 1 .331-.33h3.237a.33.33 0 0 1
 .331.33v4.125H6.65c.178 0 .323.145.323.323v3.617a.323.323 0 0
 1-.323.323H3.899v4.75c0 1.272.808 2.429 1.988 2.893.753.295 1.617.321
 2.397.131.852-.206 1.484-.717
 2.097-1.319l2.839-2.792-4.945-4.945a.331.331 0 0 1
 0-.468l2.289-2.289a.333.333 0 0 1 .469 0" />
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
