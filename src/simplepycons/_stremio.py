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


class StremioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stremio"

    @property
    def original_file_name(self) -> "str":
        return "stremio.svg"

    @property
    def title(self) -> "str":
        return "Stremio"

    @property
    def primary_color(self) -> "str":
        return "#685CEE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stremio</title>
     <path d="M12 0a1.2 1.2 0 0 0-.85.354L.353 11.15c-.47.47-.47 1.227
 0 1.697L11.15 23.647a1.2 1.2 0 0 0 1.7 0l10.797-10.8c.47-.47.47-1.226
 0-1.696L12.85.354A1.2 1.2 0 0 0 12 0zm-1.674 7.586a.2.2 0 0 1 .002 0
 .2.2 0 0 1 .129.04l5.729 4.214a.2.2 0 0 1 0 .323l-5.73 4.213a.2.2 0 0
 1-.317-.16v-8.43a.2.2 0 0 1 .187-.2z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Stremio/stremio-brand/blob
/3f3743087b11e81374cf943aaf1e041af1c97ee3/logos/SVG/stremio-logo-icon-'''

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
