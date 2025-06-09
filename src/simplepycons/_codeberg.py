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


class CodebergIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codeberg"

    @property
    def original_file_name(self) -> "str":
        return "codeberg.svg"

    @property
    def title(self) -> "str":
        return "Codeberg"

    @property
    def primary_color(self) -> "str":
        return "#2185D0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Codeberg</title>
     <path d="M11.999.747A11.974 11.974 0 0 0 0 12.75c0 2.254.635
 4.465 1.833 6.376L11.837 6.19c.072-.092.251-.092.323 0l4.178
 5.402h-2.992l.065.239h3.113l.882 1.138h-3.674l.103.374h3.86l.777
 1.003h-4.358l.135.483h4.593l.695.894h-5.038l.165.589h5.326l.609.785h-5.717l.182.65h6.038l.562.727h-6.397l.183.65h6.717A12.003
 12.003 0 0 0 24 12.75 11.977 11.977 0 0 0 11.999.747zm3.654
 19.104.182.65h5.326c.173-.204.353-.433.513-.65zm.385
 1.377.18.65h3.563c.233-.198.485-.428.712-.65zm.383
 1.377.182.648h1.203c.356-.204.685-.412 1.042-.648zz" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://codeberg.org/Codeberg/Design/src/comm
it/ac514aa9aaa2457d4af3c3e13df3ab136d22a49a/logo/special/codeberg-logo'''

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
