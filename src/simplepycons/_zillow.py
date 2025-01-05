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


class ZillowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zillow"

    @property
    def original_file_name(self) -> "str":
        return "zillow.svg"

    @property
    def title(self) -> "str":
        return "Zillow"

    @property
    def primary_color(self) -> "str":
        return "#006AFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zillow</title>
     <path d="M12.006 0L1.086 8.627v3.868c3.386-2.013 11.219-5.13
 14.763-6.015.11-.024.16.005.227.078.372.427 1.586 1.899 1.916
 2.301a.128.128 0 0 1-.03.195 43.607 43.607 0 0 0-6.67
 6.527c-.03.037-.006.043.012.03 2.642-1.134 8.828-2.94
 11.622-3.452V8.627zm-.48 11.177c-2.136.708-8.195 3.307-10.452
 4.576V24h21.852v-7.936c-2.99.506-11.902 3.16-15.959 5.246a.183.183 0
 0 1-.23-.036l-2.044-2.429c-.055-.061-.062-.098.011-.208 1.574-2.3
 4.789-5.899 6.833-7.418.042-.03.031-.06-.012-.042Z" />
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
