#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class MyanimelistIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "myanimelist"

    @property
    def original_file_name(self) -> "str":
        return "myanimelist.svg"

    @property
    def title(self) -> "str":
        return "MyAnimeList"

    @property
    def primary_color(self) -> "str":
        return "#2E51A2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MyAnimeList</title>
     <path d="M14.921 6.479c-.82 0-3.683 0-4.947 3.156-.662 1.652-.986
 4.812.876 7.886l1.934-1.41s-.767-1.095-1.083-3.191h2.897l.022
 3.19h2.604V8.835h-2.581v2.043l-2.46-.023s.413-2.408
 2.877-2.336h2.454l-.572-2.04ZM0 6.528v9.624h2.348v-5.84l2.031 2.664
 2.047-2.652v5.828h2.336V6.528H6.437L4.368 9.474 2.31
 6.528Zm18.447.022v9.583h5.022L24 14.09h-3.232V6.55Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://myanimelist.net/wrap-up/anime-logo-mo'''

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
        yield from [
            "MAL",
        ]
