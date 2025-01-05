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


class DoiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "doi"

    @property
    def original_file_name(self) -> "str":
        return "doi.svg"

    @property
    def title(self) -> "str":
        return "DOI"

    @property
    def primary_color(self) -> "str":
        return "#FAB70C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DOI</title>
     <path d="M24 12c0 6.633-5.367 12-12 12S0 18.633 0 12 5.367 0 12
 0s12 5.367 12 12ZM7.588
 6.097v4.471c-.663-.925-1.403-1.373-2.406-1.373-2.046 0-3.244
 1.441-3.244 3.847 0 2.357 1.325 3.848 3.166 3.848 1.12 0 1.88-.4
 2.445-1.325l-.039 1.042h2.045V6.097Zm-1.763 8.942c-1.12
 0-1.802-.76-1.802-2.045 0-1.325.682-2.085 1.802-2.085 1.081 0
 1.802.76 1.802 2.085 0 1.285-.672 2.045-1.802
 2.045Zm12.253-1.948c0-2.172-1.578-3.789-3.906-3.789-2.328 0-3.945
 1.695-3.945 3.789 0 2.133 1.578 3.789 3.945 3.789 2.289 0 3.906-1.656
 3.906-3.789Zm-2.094-.01c0 1.14-.711 1.89-1.851 1.89-1.139
 0-1.851-.75-1.851-1.89 0-1.139.712-1.89 1.851-1.89 1.149 0 1.861.751
 1.851 1.89Zm2.6-5.795c0 .633.517 1.227 1.189 1.227.633 0 1.188-.555
 1.188-1.227a1.17 1.17 0 0 0-1.188-1.189c-.672 0-1.179.556-1.189
 1.189Zm.166 9.341h2.055V9.604H18.75Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.doi.org/resources/130718-trademar'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.doi.org/images/logos/header_logo_'''

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
