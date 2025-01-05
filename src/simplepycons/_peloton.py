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


class PelotonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "peloton"

    @property
    def original_file_name(self) -> "str":
        return "peloton.svg"

    @property
    def title(self) -> "str":
        return "Peloton"

    @property
    def primary_color(self) -> "str":
        return "#181A1D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Peloton</title>
     <path d="M17.7283
 5.7642l1.7307-3.0066c.5045-.8803.2077-2.0077-.6725-2.5121-.8802-.5044-2.0077-.2077-2.5121.6725l-1.7407
 3.0066c-3.699-1.167-7.843.3462-9.8606 3.8473-1.2857 2.2253-1.444
 4.7869-.6626 7.032l3.2044-5.5583c.732-1.2759 1.9286-2.1858
 3.3528-2.5715 1.4242-.3857 2.9078-.188 4.1836.5539 2.6308 1.523
 3.5407 4.9055 2.0176 7.5363-1.523 2.6308-4.8957 3.5407-7.5364
 2.0176l1.8396-3.1846c.8803.5044 2.0077.2077
 2.5122-.6726.5044-.8802.2076-2.0077-.6726-2.512-.8802-.5045-2.0077-.2078-2.5121.6725l-5.855
 10.1572c-.5044.8803-.2077 2.0077.6725 2.5121.8802.5044 2.0077.2077
 2.5121-.6725L9.47 20.0754c3.699 1.167 7.843-.3462 9.8606-3.8473
 2.0176-3.4913 1.256-7.833-1.6022-10.4639z" />
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
