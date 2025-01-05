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


class MpvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mpv"

    @property
    def original_file_name(self) -> "str":
        return "mpv.svg"

    @property
    def title(self) -> "str":
        return "mpv"

    @property
    def primary_color(self) -> "str":
        return "#691F69"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>mpv</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm.312 22.775c-6.153
 0-11.142-4.988-11.142-11.142S6.16.491 12.312.491c6.154 0 11.142 4.989
 11.142 11.142s-4.988 11.142-11.142 11.142zm.643-20.464a8.587 8.587 0
 1 0 0 17.174 8.587 8.587 0 0 0 0-17.174zm-1.113 15.257a5.517 5.517 0
 1 1 0-11.034 5.517 5.517 0 0 1 0 11.034zm-1.399-7.995L14.4
 11.97l-3.957 2.518V9.573z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/mpv-player/mpv/blob/da400e'''

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
