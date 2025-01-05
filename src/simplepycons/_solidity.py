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


class SolidityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "solidity"

    @property
    def original_file_name(self) -> "str":
        return "solidity.svg"

    @property
    def title(self) -> "str":
        return "Solidity"

    @property
    def primary_color(self) -> "str":
        return "#363636"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Solidity</title>
     <path d="M4.409 6.608L7.981.255l3.572 6.353H4.409zM8.411 0l3.569
 6.348L15.552 0H8.411zm4.036 17.392l3.572 6.354
 3.575-6.354h-7.147zm-.608-10.284h-7.43l3.715 6.605
 3.715-6.605zm.428-.25h7.428L15.982.255l-3.715 6.603zM15.589
 24l-3.569-6.349L8.448 24h7.141zm-3.856-6.858H4.306l3.712 6.603
 3.715-6.603zm.428-.25h7.433l-3.718-6.605-3.715 6.605z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://docs.soliditylang.org/en/v0.8.6/brand'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://docs.soliditylang.org/en/v0.8.6/brand'''

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
