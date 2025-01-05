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


class BitwardenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bitwarden"

    @property
    def original_file_name(self) -> "str":
        return "bitwarden.svg"

    @property
    def title(self) -> "str":
        return "Bitwarden"

    @property
    def primary_color(self) -> "str":
        return "#175DDC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bitwarden</title>
     <path d="M21.722.296A.964.964 0 0 0 21.018 0H2.982a.959.959 0 0
 0-.703.296.96.96 0 0 0-.297.702v12c0 .895.174 1.783.523
 2.665.349.88.783 1.66 1.3 2.345.517.68 1.132 1.346 1.848 1.993a21.807
 21.807 0 0 0 1.98 1.609c.605.427 1.235.83 1.893 1.212.657.381
 1.125.638 1.4.772.276.134.5.241.664.311a.916.916 0 0 0 .814
 0c.168-.073.389-.177.667-.311.275-.134.743-.394 1.401-.772a25.305
 25.305 0 0 0 1.894-1.212A21.891 21.891 0 0 0 18.348 20c.716-.647
 1.33-1.31 1.847-1.993s.949-1.463
 1.3-2.345c.35-.879.524-1.767.524-2.665V1.001a.95.95 0 0
 0-.297-.705zm-2.325 12.815c0 4.344-7.397 8.087-7.397
 8.087V2.57h7.397v10.54z" />
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
