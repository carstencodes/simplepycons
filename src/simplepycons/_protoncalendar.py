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


class ProtonCalendarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "protoncalendar"

    @property
    def original_file_name(self) -> "str":
        return "protoncalendar.svg"

    @property
    def title(self) -> "str":
        return "Proton Calendar"

    @property
    def primary_color(self) -> "str":
        return "#50B0E9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Proton Calendar</title>
     <path d="M15.172
 14.818V21.85h-4.276v-1.147c0-.584.21-1.151.592-1.596l3.684-4.288zm-4.93
 5.884c0-.741.266-1.46.75-2.022l4.673-5.32c.522-.591 1.524-.92
 2.262-.92h.967V7.007a1.919 1.919 0 0 0-1.928-1.914H0v14.295c0 1.36
 1.11 2.462 2.482 2.462h7.76v-1.147zM18.8 5.197c.483.485.749 1.128.747
 1.81v5.434H24V4.613c0-1.36-1.11-2.462-2.482-2.462H2.482A2.473 2.473 0
 0 0 .006 4.438h16.96c.694 0 1.345.27 1.834.76zm.34 14.742c.817 0
 1.45-.451 1.45-1.136a.953.953 0 0 0-.79-.971v-.013a.962.962 0 0 0
 .485-.346.944.944 0 0 0 .185-.565c0-.632-.549-1.081-1.343-1.081-.99
 0-1.384.712-1.415 1.21h.843a.54.54 0 0 1 .577-.495c.318 0
 .549.196.549.48 0 .283-.213.473-.732.473h-.3v.713h.346c.536 0
 .807.176.807.492s-.26.532-.655.532a.673.673 0 0
 1-.686-.51h-.873c.063.733.683 1.222 1.551
 1.217zm2-3.39v.806l.79-.532v3.06h.82v-3.988h-.635l-.974.655z" />
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
