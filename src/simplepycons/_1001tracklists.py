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


class OneThousandAndOneTracklistsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "1001tracklists"

    @property
    def original_file_name(self) -> "str":
        return "1001tracklists.svg"

    @property
    def title(self) -> "str":
        return "1001Tracklists"

    @property
    def primary_color(self) -> "str":
        return "#40AEF0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>1001Tracklists</title>
     <path d="M8.0957
 1.334v1.3457H6.7461v1.3457H5.3984V5.371H4.0488v1.3457H2.6992v6.6816H1.3496v1.3477H0v2.4512h1.3496v1.3457h1.3496v1.3457h2.457v-7.836H3.8067V7.8223h1.3497V6.4766h1.3496V5.1309h1.3496V3.7852h8.289v1.3457h1.3496v1.3457h1.3496v1.3457h1.3497v4.2304h-1.3497v7.836h2.457V18.543h1.3497v-1.3457H24V14.746h-1.3496v-1.3477h-1.3496V6.7168h-1.3496V5.3711h-1.3496V4.0254h-1.3477V2.6797h-1.3496V1.334Zm1.3711
 8v1.3515H8.1113v3.8165h2.4688v-4.0567h2.9512v4.3477h-1.3555v1.3515h-1.3535v2.4649h2.4668v-2.7051H16v-5.2188h-1.3555V9.334Zm1.3555
 10.8691v2.463h2.4668v-2.463z" />
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
