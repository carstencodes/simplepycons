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


class MacysIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "macys"

    @property
    def original_file_name(self) -> "str":
        return "macys.svg"

    @property
    def title(self) -> "str":
        return "Macy's"

    @property
    def primary_color(self) -> "str":
        return "#E21A2C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Macy's</title>
     <path d="M12.015.624L9.19 9.293H0l7.445 5.384-2.819 8.673L12
 17.986l7.422 5.393-2.835-8.713L24 9.292h-9.162L12.015.622v.002z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.macysinc.com/news-media/media-ass'''

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
