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


class NordvpnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nordvpn"

    @property
    def original_file_name(self) -> "str":
        return "nordvpn.svg"

    @property
    def title(self) -> "str":
        return "NordVPN"

    @property
    def primary_color(self) -> "str":
        return "#4687FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NordVPN</title>
     <path d="M2.2838 21.5414A11.9866 11.9866 0 010 14.4832C0 7.8418
 5.3727 2.4586 12 2.4586c6.6279 0 12 5.3832 12 12.0246a11.9853 11.9853
 0 01-2.2838 7.0582l-5.7636-9.3783-.5565.9419.5645 2.6186L12
 8.9338l-2.45 4.1447.5707 2.6451-2.0764-3.5555-5.7605 9.3733z" />
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
