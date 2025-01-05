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


class HackClubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hackclub"

    @property
    def original_file_name(self) -> "str":
        return "hackclub.svg"

    @property
    def title(self) -> "str":
        return "Hack Club"

    @property
    def primary_color(self) -> "str":
        return "#EC3750"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hack Club</title>
     <path d="M12 0C2.4 0 0 2.4 0 12s2.4 12 12 12 12-2.4 12-12S21.6 0
 12 0zm4.5
 19.5094h-3.3094V13.003c0-.975-.1875-1.6218-.8343-1.6218-.7125 0-1.575
 1.003-1.575 2.625v5.503H7.5V4.9689l3.2906-.5625v5.428c.7125-.6468
 1.7063-.928 2.7188-.928 2.1562 0 2.9906 1.4156 2.9906 3.628z" />
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
