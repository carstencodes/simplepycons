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


class AffinityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "affinity"

    @property
    def original_file_name(self) -> "str":
        return "affinity.svg"

    @property
    def title(self) -> "str":
        return "Affinity"

    @property
    def primary_color(self) -> "str":
        return "#222324"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Affinity</title>
     <path d="M9.368 1.08h3.778l.318.55h1.082L24 18.004v.001l-2.036
 3.47H13.69l.84 1.445h-.365l-.84-1.446H3.057l-.526-.923h-.652L0
 17.298l.002-.001 2.41-4.176 2.23-1.288 3.69-6.39-.742-1.285L9.368
 1.08zm2.224 5.652L5.066 18.008h6.25l-.723-1.246
 6.808.006-5.809-10.036Z" />
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
