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


class PerforceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "perforce"

    @property
    def original_file_name(self) -> "str":
        return "perforce.svg"

    @property
    def title(self) -> "str":
        return "Perforce"

    @property
    def primary_color(self) -> "str":
        return "#404040"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Perforce</title>
     <path d="M3.741
 8.755c.164-.425.352-.834.573-1.219-.213-.196-.745-.613-.712-.646
 2.774-3.322 6.391-4.32 9.59-3.74.655.09 1.31.246 1.956.483 4.583
 1.702 6.898 6.75 5.18 11.284a9.33 9.33 0 0 1-.614
 1.285c.254.22.81.63.778.663-3.077 3.641-7.177 4.484-10.589 3.47a11.18
 11.18 0 0
 1-.982-.295c-4.574-1.702-6.898-6.751-5.18-11.285zM19.371.982c-.581.556-1.277
 1.227-1.62 1.53a11.886 11.886 0 0 0-1.727-.802C10.819-.221 5.337
 1.964 2.317 6.03.738 8.364-.195 11.236.034 14.19c0 0 .009 5.556 5.14
 8.83.417-.574.948-1.31 1.3-1.785a12.36 12.36 0 0 0 1.817.86c5.892
 2.184 12.422-.606 14.557-6.228 0 0 1.563-3.428 1.048-7.176 0
 0-.401-5.057-4.525-7.708z" />
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
