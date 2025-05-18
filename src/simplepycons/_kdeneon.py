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


class KdeNeonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kdeneon"

    @property
    def original_file_name(self) -> "str":
        return "kdeneon.svg"

    @property
    def title(self) -> "str":
        return "KDE neon"

    @property
    def primary_color(self) -> "str":
        return "#3DC08D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KDE neon</title>
     <path d="M15.832 12.017a3.85 3.96 0 0 1-3.85 3.96 3.85 3.96 0 0
 1-3.848-3.96 3.85 3.96 0 0 1 3.849-3.96 3.85 3.96 0 0 1 3.849
 3.96zM11.999 3.47a.723.723 0 0 0-.675.467A8.096 8.096 0 0 0 3.904
 12a8.096 8.096 0 0 0 7.42 8.063.723.723 0 0 0 .676.467.723.723 0 0 0
 .676-.468A8.096 8.096 0 0 0 20.096 12a8.096 8.096 0 0
 0-7.421-8.064.723.723 0 0 0-.675-.467zm.648 1.044A7.518 7.518 0 0 1
 19.517 12a7.518 7.518 0 0 1-6.871 7.485.723.723 0 0
 0-.647-.401.723.723 0 0 0-.647.401A7.518 7.518 0 0 1 4.482 12a7.518
 7.518 0 0 1 6.871-7.486.723.723 0 0 0 .646.401.723.723 0 0 0
 .648-.401zM12 0a.723.723 0 0 0-.676.467A11.566 11.566 0 0 0 4.33
 3.384a.723.723 0 0 0-.283-.06.723.723 0 0 0-.723.724.723.723 0 0 0
 .056.28 11.566 11.566 0 0 0-2.913 6.996A.723.723 0 0 0 0 12a.723.723
 0 0 0 .468.676 11.566 11.566 0 0 0 2.907 7.012.723.723 0 0
 0-.05.263.723.723 0 0 0 .723.723.723.723 0 0 0 .265-.05 11.566 11.566
 0 0 0 7.015 2.918.723.723 0 0 0 .672.457.723.723 0 0 0 .676-.467
 11.566 11.566 0 0 0 7.012-2.907.723.723 0 0 0 .263.05.723.723 0 0 0
 .723-.724.723.723 0 0 0-.05-.265 11.566 11.566 0 0 0
 2.918-7.015A.723.723 0 0 0 24 12a.723.723 0 0 0-.468-.676 11.566
 11.566 0 0 0-2.907-7.012.723.723 0 0 0 .05-.263.723.723 0 0
 0-.724-.723.723.723 0 0 0-.265.05A11.566 11.566 0 0 0
 12.671.458.723.723 0 0 0 12-.001zm-.652 1.035a.723.723 0 0 0
 .652.41.723.723 0 0 0 .647-.401 10.988 10.988 0 0 1 6.632
 2.739.723.723 0 0 0-.05.265.723.723 0 0 0 .722.723.723.723 0 0 0
 .262-.05 10.988 10.988 0 0 1 2.751 6.628.723.723 0 0 0-.41.65.723.723
 0 0 0 .401.648 10.988 10.988 0 0 1-2.738 6.632.723.723 0 0
 0-.266-.05.723.723 0 0 0-.723.722.723.723 0 0 0 .05.262 10.988 10.988
 0 0 1-6.627 2.752.723.723 0 0 0-.651-.411.723.723 0 0 0-.648.401
 10.988 10.988 0 0 1-6.632-2.738.723.723 0 0 0 .05-.265.723.723 0 0
 0-.722-.723.723.723 0 0 0-.262.05 10.988 10.988 0 0
 1-2.742-6.633.723.723 0 0 0 .401-.646.723.723 0 0 0-.4-.647 10.988
 10.988 0 0 1 2.752-6.628.723.723 0 0 0 .25.046.723.723 0 0 0
 .724-.723.723.723 0 0 0-.049-.257 10.988 10.988 0 0 1 6.626-2.756z"
 />
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
