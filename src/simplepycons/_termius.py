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


class TermiusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "termius"

    @property
    def original_file_name(self) -> "str":
        return "termius.svg"

    @property
    def title(self) -> "str":
        return "Termius"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Termius</title>
     <path d="M17.812 19.381A6.194 6.194 0 0 0 24
 13.193c0-1.7-.723-3.352-1.958-4.515a6.01 6.01 0 0 0-6.005-5.955 5.98
 5.98 0 0 0-2.731.656 5.985 5.985 0 0 0-4.12-1.635 6.011 6.011 0 0 0-6
 5.743A6.224 6.224 0 0 0 0 12.917a6.225 6.225 0 0 0 6.706 6.2 6.426
 6.426 0 0 0 5.508 3.14 6.395 6.395 0 0 0
 5.347-2.881c.084.003.167.005.25.005zm-5.598 1.242A4.792 4.792 0 0 1
 7.9 17.888l-.267-.562-.613.108a4.592 4.592 0 0 1-5.387-4.516A4.59
 4.59 0 0 1 4.34 8.734l.506-.228-.026-.555a4.377 4.377 0 0 1
 4.367-4.574c1.297 0 2.512.566 3.347 1.56l.47.56.609-.407a4.349 4.349
 0 0 1 2.425-.734 4.378 4.378 0 0 1 4.364
 4.632l-.025.416.322.265a4.612 4.612 0 0 1 1.669 3.524 4.561 4.561 0 0
 1-5.14 4.518l-.554-.071-.267.49a4.764 4.764 0 0 1-4.192
 2.493zm3.102-6.533.016-.007c.212-.091.288-.171.288-.393v-.278c0-.244-.14-.401-.37-.401h-.013l-.046.01a4.534
 4.534 0 0 1-1.502.272c-.48
 0-.954-.09-1.409-.27l-.013-.005-.052-.007c-.23
 0-.37.157-.37.401v.278c0 .209.078.303.261.382l.02.009.02.008a3.91
 3.91 0 0 0 1.544.32c.525 0 1.071-.107
 1.626-.319zm-7.081-2.285c0-.224.116-.348.272-.38l1.501-.394-1.505-.395c-.156-.041-.268-.164-.268-.38v-.473c0-.207.124-.296.266-.296.046
 0 .094.01.141.028l2.68.867c.203.068.315.231.315.455v.387c0
 .224-.112.388-.316.456l-2.685.868a.437.437 0 0 1-.125.02c-.168
 0-.276-.12-.276-.297v-.466z" />
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
