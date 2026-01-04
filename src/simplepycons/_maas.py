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


class MaasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "maas"

    @property
    def original_file_name(self) -> "str":
        return "maas.svg"

    @property
    def title(self) -> "str":
        return "MAAS"

    @property
    def primary_color(self) -> "str":
        return "#E95420"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MAAS</title>
     <path d="M4.426 0v24h15.148V0Zm3.357 10.385c.474 0
 .858.381.858.852 0 .47-.384.852-.858.852a.855.855 0 0
 1-.858-.852c0-.47.384-.852.858-.852m1.044.212h7.928c.218 0
 .39.173.397.384v.512a.395.395 0 0
 1-.391.384H8.827c.006-.013.012-.02.019-.032a1.22 1.22 0 0
 0-.02-1.248m-1.121 2.83c.474 0 .858.381.858.852 0
 .47-.384.852-.858.852a.855.855 0 0
 1-.858-.852c0-.47.384-.852.858-.852m1.037.198h8.012c.218 0
 .39.173.39.378v.513a.395.395 0 0
 1-.39.384h-8q.012-.001.013-.013c.16-.275.206-.608.122-.922a1.1 1.1 0
 0 0-.147-.34M7.706 16.47c.474 0
 .858.382.858.852s-.384.852-.858.852a.855.855 0 0
 1-.858-.852c0-.47.384-.852.858-.852m1.037.212h8.012c.218 0
 .39.172.39.384v.512a.395.395 0 0 1-.39.384H8.743l.02-.032a1.22 1.22 0
 0 0-.02-1.248m-1.037 2.83c.474 0
 .858.382.858.852s-.384.852-.858.852a.855.855 0 0
 1-.858-.852c0-.47.384-.852.858-.852m1.037.212h8.012a.38.38 0 0 1
 .39.384v.513a.395.395 0 0 1-.39.384H8.743l.02-.032a1.22 1.22 0 0
 0-.02-1.249" />
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
