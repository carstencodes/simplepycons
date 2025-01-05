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


class SefariaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sefaria"

    @property
    def original_file_name(self) -> "str":
        return "sefaria.svg"

    @property
    def title(self) -> "str":
        return "Sefaria"

    @property
    def primary_color(self) -> "str":
        return "#212E50"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sefaria</title>
     <path d="M19.615 15.412c-.62 2.915-2.733 4.152-7.425 4.152-11.54
 0-7.45-9.28-5.84-11.186.678-.85 1.152-1.553 2.874-1.553h3.273c4.567 0
 5.437.217 6.582 2.55.617 1.258.975 3.971.536
 6.036m1.238-5.79c-.385-2.492-.889-5.202-3.052-6.706-1.31-.911-2.663-.981-4.177-.981-1.026
 0-4.666-.041-6.257-.041C5.833 1.893 4.779.618 4.779 0 3.777 1.234
 3.001 2.597 3.272 4.245c.244 1.484 1.261 2.433 2.75 2.622C4.338 9.25
 2.81 11.994 2.881 14.9c.046 1.83.467 9.1 8.686 9.1h1.497c3.507 0
 5.632-2.606 6.25-3.614 1.822-2.963 2.122-7.548 1.537-10.764Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Sefaria/Sefaria-Project/bl'''

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
