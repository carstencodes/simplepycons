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


class OpenvpnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openvpn"

    @property
    def original_file_name(self) -> "str":
        return "openvpn.svg"

    @property
    def title(self) -> "str":
        return "OpenVPN"

    @property
    def primary_color(self) -> "str":
        return "#EA7E20"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenVPN</title>
     <path d="M12 .357C5.385.357 0 5.69 0 12.254c0 4.36 2.358 8.153
 5.896 10.204l.77-5.076a7.046 7.046 0 01-1.846-4.719c0-3.897
 3.18-7.076 7.13-7.076 3.948 0 7.126 3.18 7.126 7.076 0 1.847-.717
 3.488-1.846 4.77L18 22.51c3.59-2.05 6-5.899 6-10.258C24 5.69
 18.615.357 12 .357zm-.05 8.157a3.786 3.786 0 00-3.796 3.795 3.738
 3.738 0 002.461 3.54L9.13 23.643h5.64l-1.435-7.795c1.385-.564
 2.41-1.898 2.41-3.54a3.786 3.786 0 00-3.795-3.794z" />
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
