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


class TraktIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trakt"

    @property
    def original_file_name(self) -> "str":
        return "trakt.svg"

    @property
    def title(self) -> "str":
        return "Trakt"

    @property
    def primary_color(self) -> "str":
        return "#9F42C6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trakt</title>
     <path d="m15.082 15.107-.73-.73 9.578-9.583a4.499 4.499 0 0
 0-.115-.575L13.662 14.382l1.08 1.08-.73.73-1.81-1.81L23.422
 3.144c-.075-.15-.155-.3-.25-.44L11.508 14.377l2.154
 2.155-.73.73-7.193-7.199.73-.73 4.309 4.31L22.546 1.86A5.618 5.618 0
 0 0 18.362 0H5.635A5.637 5.637 0 0 0 0 5.634V18.37A5.632 5.632 0 0 0
 5.635 24h12.732C21.477 24 24 21.48 24 18.37V6.19l-8.913
 8.918zm-4.314-2.155L6.814 8.988l.73-.73 3.954
 3.96zm1.075-1.084-3.954-3.96.73-.73 3.959 3.96zm9.853 5.688a4.141
 4.141 0 0 1-4.14 4.14H6.438a4.144 4.144 0 0 1-4.139-4.14V6.438A4.141
 4.141 0 0 1 6.44 2.3h10.387v1.04H6.438c-1.71 0-3.099 1.39-3.099
 3.1V17.55c0 1.71 1.39 3.105 3.1 3.105h11.117c1.71 0 3.1-1.395
 3.1-3.105v-1.754h1.04v1.754z" />
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
