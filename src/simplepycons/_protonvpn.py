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


class ProtonVpnIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "protonvpn"

    @property
    def original_file_name(self) -> "str":
        return "protonvpn.svg"

    @property
    def title(self) -> "str":
        return "Proton VPN"

    @property
    def primary_color(self) -> "str":
        return "#66DEB1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Proton VPN</title>
     <path d="m10.176 20.058.858-1.28
 6.513-9.838c.57-.86.026-2.014-1.005-2.131L.378 4.95l8.373
 15.055a.84.84 0 0 0 1.424.052h.001zM23.586 7.14l-9.662 14.61c-1.036
 1.567-3.38 1.478-4.293-.162l-.093-.168c.3-.01.594-.086.855-.235a1.85
 1.85 0 0 0 .612-.57l.86-1.28
 6.516-9.844c.46-.694.525-1.56.173-2.314a2.375 2.375 0 0
 0-1.899-1.364L.493 3.956l-.476-.054C-.163 2.392 1.101.95 2.784
 1.143l18.991 2.16c1.856.21 2.835 2.289 1.812 3.838z" />
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
