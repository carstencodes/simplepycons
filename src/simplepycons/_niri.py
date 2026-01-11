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


class NiriIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "niri"

    @property
    def original_file_name(self) -> "str":
        return "niri.svg"

    @property
    def title(self) -> "str":
        return "niri"

    @property
    def primary_color(self) -> "str":
        return "#D55C44"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>niri</title>
     <path d="M16.23881 21.91267c0 1.04353-.5217 2.08705-4.17383
 2.08705-3.65226 0-4.17395-1.04365-4.17395-2.08705 0-1.56521
 1.04352-2.6086 4.17395-2.6086s4.17383 1.04339 4.17383
 2.6086zM7.89103-.00038c2.08691 0 10.43483 6.26087 10.43483 11.47835 0
 3.52136-1.65048 5.06209-3.09492
 5.73623-1.09417.5108-1.39726-.17027-.78877-1.21866.409-.7044.75325-1.55688.75325-2.43065
 0-1.56522-.52182-2.60874-1.56522-3.65214-1.04352-1.04352-2.38385-1.56521-3.13043-1.56521-1.04353
 0-1.56522 3.06697-1.56522 4.69565 0 1.29764.3872 2.4663.77658
 3.31301.3672.79877.05988 1.34726-.76363
 1.04442-.89954-.33079-1.97832-.98377-2.6217-2.27064-1.04351-2.08679-.52182-5.09017-.52182-7.82597
 0-4.17395 0-7.30426 2.08705-7.30426z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://yalter.github.io/niri/Name-and-Logo.h'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://yalter.github.io/niri/logo/niri-icon-'''

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
