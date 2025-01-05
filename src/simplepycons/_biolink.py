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


class BioLinkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "biolink"

    @property
    def original_file_name(self) -> "str":
        return "biolink.svg"

    @property
    def title(self) -> "str":
        return "Bio Link"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bio Link</title>
     <path d="M3.95192
 4.6371V2.75605c0-.26354-.14223-.39521-.42679-.39521H2.2289V5.0323h1.29624c.28456
 0 .4268-.13168.4268-.3952zm0
 4.2839V6.96087c0-.13696-.03158-.23187-.09482-.28456-.06324-.06324-.1739-.09482-.33197-.09482H2.2289V9.3162h1.29624c.28456
 0 .4268-.13168.4268-.39521zM0 .81166h4.17323c1.33842 0 2.00763.57962
 2.00763 1.73882v1.77049c0 .77986-.23714 1.2699-.71143
 1.4701.47429.17917.71143.63235.71143 1.35953v1.96013c0 1.1698-.6692
 1.75466-2.00763 1.75466H0Zm7.56538
 0h2.24468v10.05373H7.56538zm5.66357 0h2.11829c1.32777 0 1.9917.57962
 1.9917 1.73882v6.56025c0 1.1698-.66393 1.75466-1.9917
 1.75466h-2.1183c-1.33832
 0-2.00753-.58486-2.00753-1.75466V2.55048c0-1.1592.6692-1.73882
 2.00754-1.73882zm1.84948
 7.99868V2.8667c0-.26353-.13696-.3952-.41096-.3952h-.75876c-.28455
 0-.42678.13167-.42678.3952v5.94364c0
 .26354.14223.39521.42678.39521h.75876c.274 0
 .41096-.13167.41096-.3952zm5.03262 2.02892c-.75304
 0-1.3634-.61045-1.3634-1.3634V9.3879c0-.75304.61036-1.3634
 1.3634-1.3634.75295 0 1.3634.61036 1.3634 1.3634v.08796c0
 .75295-.61045 1.3634-1.3634 1.3634zM2.25329
 21.52851h2.8928v1.65983H.00859V13.13461h2.2447zm3.66888-8.3939h2.24469v10.05373h-2.2447zm7.9241
 0h2.07078v10.05373h-2.02338l-2.19727-6.02272v6.02272H9.64144V13.13461h2.03921l2.16561
 6.00698zm10.15373 0-2.02338 4.96367L24
 23.18834h-2.43433l-1.94439-5.09006 1.94439-4.96367zm-6.67082
 10.05373V13.13461h2.24469v10.05373Z" />
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
