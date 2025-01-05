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


class PaloAltoNetworksIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paloaltonetworks"

    @property
    def original_file_name(self) -> "str":
        return "paloaltonetworks.svg"

    @property
    def title(self) -> "str":
        return "Palo Alto Networks"

    @property
    def primary_color(self) -> "str":
        return "#F04E23"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Palo Alto Networks</title>
     <path d="m10.278 15.443 1.705 1.705-3.426 3.426-3.427-3.426
 8.592-8.591-1.705-1.705 3.426-3.426 3.427 3.426-8.592 8.591zM0
 12.017l3.426 3.426 8.591-8.59-3.426-3.427L0 12.017zm11.983 5.13 3.426
 3.427L24 11.983l-3.426-3.426-8.591 8.59z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.paloaltonetworks.com/company/bran'''
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
